class Password_manager():
    def __init__(self, old_passwords):
        self.old_passwords=old_passwords
    def get_password(self):
        return self.old_passwords[len(self.old_passwords)-1)]
    def set_password(self, f):
        self.old_passwords.append(f)
    def is_correct(self,s):
        if Password_manager.get_password(self)==s:
            return True
        else:
            return False
old_passwords=["elnara", "aru", "izzzzu"]
o=Password_manager(old_passwords)
s=str(input("password: "))
print(o.is_correct(s))
f=str(input("change password: "))
