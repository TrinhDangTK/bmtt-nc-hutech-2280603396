from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

ceasar_cipher = CaesarCipher()


#CEASAR CIPHER
@app.route("/api/caesar/encrypt", methods=["POST"])

def ceasar_encrypt():
    data = request.json
    P_text = data['P_text']
    key = int(data['key'])
    encrypted_text = ceasar_cipher.encrypt_text(P_text, key)
    return jsonify({'encrypted_mess': encrypted_text})
    data = request.json

@app.route("/api/caesar/decrypt", methods=["POST"])
def ceasar_decrypt():
    data = request.json
    C_text = data['C_text']
    key = int(data['key'])
    decrypted_text = ceasar_cipher.decrypt_text(C_text, key)
    return jsonify({'decrypted_mess': decrypted_text})

#VIGENERE CIPHER


@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    P_text = data['P_text']
    key = data['key']
    vigenere_cipher = VigenereCipher()
    encrypted_text = vigenere_cipher.vigenere_encrypt(P_text, key)
    return jsonify({'encrypted_mess': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    C_text = data['C_text']
    key = data['key']
    vigenere_cipher = VigenereCipher()
    decrypted_text = vigenere_cipher.vigenere_decrypt(C_text, key)
    return jsonify({'decrypted_mess': decrypted_text})

#main function 
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
