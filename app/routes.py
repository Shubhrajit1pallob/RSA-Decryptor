from flask import render_template, request, redirect, url_for, flash
from . import create_app
from rsa_decrypter import decrypt_message

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        encrypted_message = request.form['encrypted_message']
        private_key = request.form['private_key']
        n = request.form['n']
        try:
            plain_text = decrypt_message(encrypted_message, private_key, n)
            return render_template('index.html', decrypted_message=plain_text)
        except ValueError:
            flash('Invalid input: Please ensure the encrypted message and private key are integers.')
            return redirect(url_for('index'))
        except Exception as e:
            flash('An error occurred: ' + str(e))
            return redirect(url_for('index'))
    return render_template('index.html')