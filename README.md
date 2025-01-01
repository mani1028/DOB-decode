# DOB Decode

A Python-based web application built with Flask that decodes the user's date of birth and displays personalized information.

## Live Demo

You can view the live demo of the application here: [Live Demo](https://dob-nine.vercel.app/)

## Features

- Enter your Date of Birth (DOB) and decode the details.
- Displays your age and other personalized information.
- Beautiful UI with responsive design.
- Interactive features to enhance the user experience.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **HTML/CSS**: For frontend design and layout.
- **JavaScript**: For dynamic and interactive components.
- **Vercel**: Deployed on Vercel for serverless deployment.


## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Flask library
- A code editor (like VSCode or PyCharm)

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
https://github.com/mani1028/DOB-decode.git
```

### 2. Install Dependencies

Navigate into your project directory:

```bash
cd dob-decode
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. Running Locally

To run the application locally, use the following command:

```bash
python app.py
```

By default, the app will run on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### 4. Deploying on Vercel

This project is deployed using Vercel for serverless hosting. Follow these steps to deploy:

- Sign up or log in to [Vercel](https://vercel.com).
- Install Vercel CLI:

  ```bash
  npm install -g vercel
  ```

- Deploy your app:

  ```bash
  vercel --prod
  ```

Your app will be live on a Vercel URL, which you can share with others.

## Folder Structure

```plaintext
dob-decode/
├── app.py                 # Flask main application file
├── templates/             # HTML files for Flask
│   ├── index.html
│   ├── results.html
│   ├── decode.html
│   └── about.html
├── static/                # CSS, JavaScript, images
│   ├── style.css
│   └── images
├── requirements.txt       # Python dependencies
├── vercel.json            # Vercel configuration
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)

## Contributing

Feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!
