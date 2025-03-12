import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])  # Changed from setText to setPlainText

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption Successful")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        } 
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Print response data for debugging
                print("API response:", data)
                
                # Try to get result using different possible key names
                if "decrypted_message" in data:
                    decrypted_text = data["decrypted_message"]
                elif "decryted_message" in data:  # Added this condition to handle the typo
                    decrypted_text = data["decryted_message"]
                elif "plain_text" in data:
                    decrypted_text = data["plain_text"]
                elif "message" in data:
                    decrypted_text = data["message"]
                elif "result" in data:
                    decrypted_text = data["result"]
                else:
                    # If none of the expected keys are found, show available keys
                    keys = list(data.keys())
                    error_msg = f"Unexpected API response format. Available keys: {keys}"
                    print(error_msg)
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Decryption Error")
                    msg.setDetailedText(error_msg)
                    msg.exec_()
                    return
                    
                self.ui.txt_plain_text.setPlainText(decrypted_text)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption Successful")
                msg.exec_()
            else:
                error_msg = f"API Error: {response.status_code}"
                print(error_msg)
                if hasattr(response, 'text'):
                    print(f"Response content: {response.text}")
                    
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(error_msg)
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Connection Error: {str(e)}")
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())