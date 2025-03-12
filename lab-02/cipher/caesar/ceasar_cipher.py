from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text : str, key:int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for char in text:
          char_index = self.alphabet.index(char)
          output_index = (char_index + key) % alphabet_len
          output_letter= (self.alphabet[output_index])
          encrypted_text.append(output_letter)
        return "".join(encrypted_text)
       
    def decrypt_text(self, text : str , key : int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for char in text:
          char_index = self.alphabet.index(char)
          output_index = (char_index - key) % alphabet_len
          output_letter= (self.alphabet[output_index])
          decrypted_text.append(output_letter)
        return "".join(decrypted_text)
        
