from algo import *


class PDP:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def keygen(self):
        keys=[]
        a = Algo()
        a.generate_key()
        keys.append(a.get_private_key())
        keys.append(a.get_public_key())
        #private_key_str = a.get_private_key_str()
        #public_key_str = a.get_public_key_str()
        #print('Private key = ')
        #print(private_key_str)
        #print('Public key = ')
        #print(public_key_str)
        return keys

    def tagblock(self,pk,sk,m):
        a = Algo()
        result = a.get_hash(pk+sk+m)
        #print(f'Sha=={result}')
        return result

    def genproof(self,filehash,chal):
        proof = {}
        for c in chal:
            proof[c] = filehash[c]
        return proof

    def checkproof(self,sk,chal,proof):
        for c in chal:
            data = proof[c]
            hash2 = self.tagblock(data[0],sk,data[1])
            if hash2 == data[2]:
                print("OK")
            else:
                print("Fail")

def main():
    p = PDP()
    keys = p.keygen()
    a = Algo()
    blocks= a.get_file_blocks("1.txt",11)
    fileHash={}
    i=0
    for b in blocks:
        #print(b)
        hash = p.tagblock(keys[1],keys[0],b)
        fileHash[i] = [keys[1],b,hash]
        i = i+1
    #print(fileHash)    
    chal = [0,1,2]
    proof = p.genproof(fileHash,chal)
    #print(proof)
    p.checkproof(keys[0],chal,proof)


if __name__ == "__main__":
    main()

