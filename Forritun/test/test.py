class Clock():
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def str_update(self, string):
        klukkan = string.split(":")
        self.hours=int(klukkan[0])
        self.minutes=int(klukkan[1])
        self.seconds=int(klukkan[2])
    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes,self.seconds)
    
    def min_hours_sec(self,x,y):
        if x//60!=0:
            numerator=x//60
            y=numerator+y
            x=x-(numerator*60)
        return x,y
    def hours_days(self,total_hours):
        if total_hours>=24:
            total_hours=total_hours-24
        return total_hours
    def add_clocks(self, clock):

        total_hours=self.hours + clock.hours
        total_minutes=self.minutes + clock.minutes
        total_seconds=self.seconds + clock.seconds
        total_seconds,total_minutes=self.min_hours_sec(total_seconds, total_minutes)
        total_minutes,total_hours=self.min_hours_sec(total_minutes, total_hours)
        total_hours=self.hours_days(total_hours)
        new_clock = Clock(total_hours, total_minutes, total_seconds)
        return new_clock     
    


clock1 = Clock()
clock2 = Clock()
clock1.str_update("20:10:52")
clock2.str_update("08:49:24")
print(clock1)
assert str(clock1) == "20 hours, 10 minutes and 52 seconds"

print(clock2)
assert str(clock2) == "8 hours, 49 minutes and 24 seconds"

clock3 = clock1.add_clocks(clock2)
print(clock3)
assert str(clock3) == "5 hours, 0 minutes and 16 seconds"