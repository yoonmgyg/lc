class MyCalendar(object):
    def __init__(self):
        self.register = [] 
    def book(self, startTime, endTime):
        for s, e in self.register:
            if max(s, startTime) < min(e, endTime):
                return False
        self.register.append((startTime, endTime))
        return True
