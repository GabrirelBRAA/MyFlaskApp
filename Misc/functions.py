import os
from hashlib import pbkdf2_hmac
#import hashlib, binascii
import timeago, datetime

#salt = b'$#0x--.\'/\\98'
our_app_iters = 500_000

#def hash(string):
#    dk = hashlib.pbkdf2_hmac("sha256", bin(int(binascii.hexlify(string), 16)), salt, 1000)
#    return binascii.hexlify(dk).decode("utf-8") 

#def b_hash(string):
#    dk = hashlib.pbkdf2_hmac("sha256", bin(int(binascii.hexlify(string), 16)), salt, 1000)
#   return binascii.hexlify(dk)

def get_salt():
    return os.urandom(12)

def hash(string, salt):
    dk = pbkdf2_hmac('sha256', str.encode(string), salt, our_app_iters)
    return dk

def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

#def ago(date):
#    now = datetime.datetieme.now() + datetime.timedelta(seconds = 60 * 3.4)
#    return (timeago.format(date, now)) #vai printar x secs/horas/minutos atras
