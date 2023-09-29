import hashlib, binascii
import timeago, datetime

salt = b'$#0x--.\'/\\98'

#Esse algoritmo de hash é bem estranho, talvez devesse ver um pouco disso depois
def hash(string):
    dk = hashlib.pbkdf2_hmac("sha256", bin(int(binascii.hexlify(string), 16)), salt, 1000)
    return binascii.hexlify(dk).decode("utf-8") 

def b_hash(string):
    dk = hashlib.pbkdf2_hmac("sha256", bin(int(binascii.hexlify(string), 16)), salt, 1000)
    return binascii.hexlify(dk)

def ago(date):
    now = datetime.datetieme.now() + datetime.timedelta(seconds = 60 * 3.4)
    return (timeago.format(date, now)) #vai printar x secs/horas/minutos atras
