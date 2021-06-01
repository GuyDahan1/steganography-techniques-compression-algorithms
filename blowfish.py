from Crypto.Cipher import Blowfish
from secrets import token_hex
import base64
import PIL.Image as Image
import io


def imageToData(imagePath):
    with open(imagePath, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        return str


def encrypt(key, data):
    enc_cipher = Blowfish.new(key, Blowfish.MODE_EAX)
    encrypted_data = enc_cipher.encrypt(data)
    return enc_cipher, encrypted_data


def decrypt(enc_cipher, encrypted_data):
    dec_cipher = Blowfish.new(key, Blowfish.MODE_EAX, enc_cipher.nonce)
    decrypted_data = dec_cipher.decrypt(encrypted_data)

    b = base64.b64decode(decrypted_data)
    img = Image.open(io.BytesIO(b))
    img.show()
    img.save("images/img1.png")

    return decrypted_data