#**methods are functions in classes

class Clock(object):
	def _init_(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

def add_time(t1, t2): #you can pass in objects as parameters of a function
	sum = Clock()
	sum.hours = t1.hours + t2.hours
	sum.minutes = t1.minutes + t2.minutes
	sum.seconds = t1.seconds + t2.seconds
	return sum

def increment(time, seconds):
	time.seconds = time.seconds + seconds
		
	while time.seconds >= 60:
		time.seconds = time.seconds - 60
		time.minutes = time.minutes + 1

	while time.minutes >= 60:
		time.minutes = time.minutes - 60
		time.hours = time.hours + 1

#another way to write increment

def convert_to_seconds(t):
	minutes = t.hours * 60 + t.minutes
	seconds = minutes * 60 + t.seconds
	return seconds

def makeTime(seconds):
	time = Clock()
	time.hours = seconds = 3600
	seconds = seconds - time.hours*3600
	time.minutes = seconds/60
	seconds = seconds - time.minutes*60
	time.seconds = seconds
	return time


time = Clock()
time.hours = 11
time.minutes = 59
time.seconds = 30
