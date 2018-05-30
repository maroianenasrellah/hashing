h=hashlib.sha256().hexdigest()
print("SHA256",h)


hash=0
mystring ="Nobody inspects the spammish repetition"
if hash == 1:
    m=hashlib.md5(mystring.encode())
    m.digest()
    m.hexdigest()
    
    print("digest",m.digest())
    print("hexdigest",m.hexdigest())
    print("digest size",m.digest_size)
    print("Block size ",m.block_size)
    
    #hashing...
h=hashlib.sha512().hexdigest()
print("SHA512",h)

h=hashlib.sha224().hexdigest()
print("SHA224",h)
