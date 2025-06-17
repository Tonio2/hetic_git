import hashlib

class Tree:
    def setTree(self, blobsha1_list):
        # blobsha1_list : liste des chemins de fichiers blob
        contenu_total = b""
        for blob_path in blobsha1_list:
            with open(blob_path, "rb") as f:
                contenu_total += f.read()
        self.sha1 = hashlib.sha1(contenu_total).hexdigest()
        self.blobsha1 = blobsha1_list
    
    def getTreeHash(self):
        return self.sha1