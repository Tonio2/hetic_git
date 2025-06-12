import datetime

class Commit:
    def setCommit(self, sha1, ref, message):
        self.sha1 = sha1
        self.date = datetime.datetime.now()
        self.ref = ref
        self.message = message

    def getCommitHash(self):
        return self.sha1
    
    def getCommitDate(self):
        return self.date
    
    def getCommitRef(self):
        return self.ref
    
    def getCommitMessage(self):
        return self.message