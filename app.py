from flask import Flask, render_template, request, send_file
from Crypto.Cipher import AES
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load AES Key
key = open("key.key", "rb").read()


def encrypt_file(file_data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    return cipher.nonce + tag + ciphertext


def decrypt_file(encrypted_data):
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file_data = file.read()

    encrypted_data = encrypt_file(file_data)

    encrypted_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(encrypted_path, "wb") as f:
        f.write(encrypted_data)

    return f"File '{file.filename}' uploaded and encrypted successfully!"


@app.route("/download/<filename>")
def download(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        return "File not found!"

    encrypted_data = open(file_path, "rb").read()
    decrypted_data = decrypt_file(encrypted_data)

    decrypted_path = "decrypted_" + filename
    with open(decrypted_path, "wb") as f:
        f.write(decrypted_data)

    return send_file(decrypted_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
