import os

class FileOp:
    
    def __init__(self):
        print("File Operations")
        
    def get_types(self,dirpath):
        return os.listdir(dirpath)
    
    def get_contents(self,filepath):
        var = ""
        if os.path.isfile(filepath):
            f = open(filepath, "r")
            var = f.read()
            f.close()
        
        return var