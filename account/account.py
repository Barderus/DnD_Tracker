class Account:
    def __init__(self, username, password_hash, fname, lname, account_id=None):
        self.account_id = account_id
        self.username = username
        self.password_hash = password_hash
        self.fname = fname
        self.lname = lname

