from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import hashlib 

class Algo:
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def generate_key(self):
        # generate private/public key pair
        self.key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537,key_size=1024)
        return self.key

    def get_public_key(self):
        # get public key in OpenSSH format
        self.public_key = self.key.public_key().public_bytes(serialization.Encoding.OpenSSH,serialization.PublicFormat.OpenSSH)
        return self.public_key

    def get_private_key(self):
        # get private key in PEM container format
        self.pem = self.key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption())
        return self.pem

    def get_public_key_str(self):
        # get public key in OpenSSH format
        self.public_key = self.key.public_key().public_bytes(serialization.Encoding.OpenSSH,serialization.PublicFormat.OpenSSH)
        public_key_str = self.public_key.decode('utf-8')
        return public_key_str

    def get_private_key_str(self):
        # get private key in PEM container format
        self.pem = self.key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption())
        private_key_str = self.pem.decode('utf-8')
        return private_key_str

    def get_hash(self,data):
        result = hashlib.sha1(data) 
        return result.hexdigest() 

    def get_file_blocks(self,filename,chunksize):
        blocks = []
        CHUNKSIZE=chunksize
        file = open(filename, "rb")
        try:
            bytes_read = file.read(CHUNKSIZE)
            while bytes_read:
                blocks.append(bytes_read)
                bytes_read = file.read(CHUNKSIZE)
        finally:
            file.close()
        return blocks

    def write_to_file(self,filename,blocks):
        f = open(filename, 'wb')
        for b in blocks:
            f.write(b)
        f.close()
        print("Done")

    def write_to_file2(self,filename,blocks):
        f = open(filename, 'wb')
        f.write(blocks)
        f.close()
        print("File Saved Done")

