import datetime

class Commit:
    def setCommit(self, sha1, ref, message):
        self.sha1 = sha1
        self.date = datetime.datetime.now()
        self.ref = ref
        self.message = message