from hashlib import pbkdf2_hmac


## FUNCTION TO GENERATE HASH PASSWORDS
def hash_passwd(passw):
    salt=b'\x19G\xaf\x8d!\x82P\xac\x7f\xdc\xfc\xfbtRA\xa2OS\x9a\xc2\xd6\x0c\x91I\x8a2y\x1dM\x99\xf6\xbc'
    passw = bytes(passw,"utf-8")
    passw = pbkdf2_hmac('sha256',passw,salt,10).hex()
    return passw