class Time():
    def __init__(self,n):
        self.n=n
    def convert_to_minutes(self):
        m=int(self.n/60)
        s=self.n%60
        print(f'{m}:{s}')
    def convert_to_hours(self):
        h=int(self.n/3600)
        m=int((self.n%3600)/60)
        s=(self.n%3600)%60
        print(f'{h}:{m}:{s}')
n=int(input())
t=Time(n)
t.convert_to_minutes()
t.convert_to_hours()
