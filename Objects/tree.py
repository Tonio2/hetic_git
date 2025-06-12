class Tree:
    def setTree(self, sha1, blobsha1):
        self.sha1 = sha1
        self.blobsha1 = list(blobsha1)
    
    def getTreeHash(self):
        return self.sha1