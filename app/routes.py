from flask import Blueprint, request, render_template, flash, redirect, url_for
from rsa_decrypter import decrypt_message

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        encrypted_message = request.form['encrypted_text']
        public_key = request.form['public_key']
        n = request.form['n']
        try:
            plain_text = decrypt_message(int(encrypted_message), int(public_key), int(n))
            return render_template('index.html', decrypted_text=plain_text)
        except ValueError:
            flash('Invalid input: Please ensure the encrypted message and public key are integers.')
            return redirect(url_for('index'))
        except Exception as e:
            flash('An error occurred: ' + str(e))
            return redirect(url_for('index'))
    return render_template('index.html')


# if __name__ == '__main__':
#     main.run(debug=True)