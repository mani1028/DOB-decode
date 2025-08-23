from flask import Flask, render_template, request,  send_from_directory
from datetime import datetime, timedelta
import math
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ads.txt')
def serve_ads():
    return send_from_directory(os.getcwd(), 'ads.txt', mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.getcwd(), 'sitemap.xml', mimetype='application/xml')
    
@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        dob = request.form['dob']
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            return render_template('decode.html', error="Invalid date format. Please use YYYY-MM-DD.")

        today = datetime.today()
        # Calculate various age-related facts
        age_years = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        age_hours = int((today - dob_date).total_seconds() / 3600)
        age_minutes = int((today - dob_date).total_seconds() / 60)
        age_seconds = int((today - dob_date).total_seconds())
        age_days = (today - dob_date).days

        # Zodiac, moon phase, day of the week
        zodiac_sign = get_zodiac_sign(dob_date.month, dob_date.day)
        moon_phase = get_moon_phase(dob_date)
        day_of_week = dob_date.strftime('%A')

        # Next birthday
        next_birthday = datetime(today.year, dob_date.month, dob_date.day)
        if today > next_birthday:
            next_birthday = datetime(today.year + 1, dob_date.month, dob_date.day)
        days_to_next_birthday = (next_birthday - today).days

        # Life path number, heartbeats, blinks, full moons
        life_path_number = calculate_life_path_number(dob_date)
        heartbeats = math.floor(age_minutes * 80)  # Avg 80 beats/min
        blinks = math.floor(age_minutes * 20)  # Avg 20 blinks/min
        full_moons = math.floor(age_days / 29.53)  # Avg lunar cycle

        # Famous personality with the same birthday
        famous_personality = get_famous_personality(dob_date)
        lucky_number = calculate_lucky_number(dob_date)

        # Zodiac traits for radar chart
        zodiac_traits = get_zodiac_traits(zodiac_sign)

        return render_template('result.html', dob=dob, age_years=age_years, age_hours=age_hours,
                               age_minutes=age_minutes, age_seconds=age_seconds, age_days=age_days,
                               zodiac_sign=zodiac_sign, moon_phase=moon_phase, 
                               day_of_week=day_of_week, days_to_next_birthday=days_to_next_birthday,
                               life_path_number=life_path_number, heartbeats=heartbeats, 
                               blinks=blinks, full_moons=full_moons, 
                               famous_personality=famous_personality, lucky_number=lucky_number,
                               zodiac_traits=zodiac_traits)

    return render_template('decode.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Taurus'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Gemini'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Leo'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Virgo'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Libra'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Scorpio'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Sagittarius'
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 'Capricorn'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Aquarius'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Pisces'
    return "Unknown"

def get_moon_phase(date):
    moon_phases = ['New Moon', 'First Quarter', 'Full Moon', 'Last Quarter']
    return moon_phases[date.day % 4]

def calculate_life_path_number(dob_date):
    digits = [int(x) for x in dob_date.strftime('%Y%m%d')]
    while len(digits) > 1:
        digits = [int(x) for x in str(sum(digits))]
    return digits[0]

def age_days(dob_date, today):
    return (today - dob_date).days

def get_famous_personality(dob_date):
    famous_birthdays = {
        "01-01": "J.D. Salinger",
        "12-25": "Isaac Newton",
        "02-14": "Galileo Galilei",
    }
    key = dob_date.strftime('%m-%d')
    return famous_birthdays.get(key, "No match found")

def calculate_lucky_number(dob_date):
    digits = str(dob_date.day) + str(dob_date.month) + str(dob_date.year)
    total = sum(int(digit) for digit in digits)
    
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    
    return total

def get_zodiac_traits(zodiac_sign):
    traits = {
        "Aries": [8, 7, 6, 7, 8],
        "Taurus": [6, 8, 7, 5, 8],
        "Gemini": [7, 8, 9, 6, 5],
        "Cancer": [8, 6, 7, 8, 7],
        "Leo": [9, 7, 8, 7, 6],
        "Virgo": [7, 8, 6, 9, 8],
        "Libra": [6, 7, 8, 7, 8],
        "Scorpio": [8, 9, 7, 6, 7],
        "Sagittarius": [7, 8, 9, 8, 6],
        "Capricorn": [6, 7, 8, 9, 7],
        "Aquarius": [8, 6, 7, 8, 9],
        "Pisces": [7, 8, 9, 7, 6]
    }
    return traits.get(zodiac_sign, [0, 0, 0, 0, 0])

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
