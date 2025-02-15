# RSA Decrypter

RSA Decrypter is a web application that allows users to decrypt messages encrypted using the RSA algorithm. The application is built using Flask and provides a simple interface for users to input their encrypted message, public key, and modulus value to obtain the decrypted message.

## Features

- Decrypt messages encrypted using the RSA algorithm
- Simple and user-friendly interface
- Built with Flask

## Project Structure

```
RSA-decrypter/ 
├── app/ 
│ ├── init.py 
│ ├── routes.py 
│ ├── templates/ 
│ │ └── index.html 
│ └── static/ 
│   └── styles.css 
├── venv/ 
├── requirements.txt 
└── README.md'
```

## Setup Instructions

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Local Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/RSA-decrypter.git
    cd RSA-decrypter
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**

    ```bash
    export FLASK_APP=app
    flask run
    ```

    The application will be available at http://127.0.0.1:5000/.


### Usage

- Open the web application in your browser.
- Enter the encrypted message, public key, and modulus value in the provided fields.
- Click the "Decrypt" button to obtain the decrypted message.


### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgements

- Flask
- PythonAnywhere

