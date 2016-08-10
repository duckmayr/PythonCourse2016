class Clock(object):
	def __init__(self, hour, minutes):
		self.minutes = minutes
		self.hour = hour
		
	@classmethod
	def at(cls, hour, minutes=0):
		return cls(hour, minutes)
		
	def __str__(self):
		if self.minutes < 10 and self.hour > 9:
			return "%s:0%s" % (str(self.hour), str(self.minutes))
		elif self.minutes < 10 and self.hour < 10:
			return "0%s:0%s" % (str(self.hour), str(self.minutes))
		elif self.minutes > 9 and self.hour < 10:
			return "0%s:%s" % (str(self.hour), str(self.minutes))
		return "%s:%s" % (str(self.hour), str(self.minutes))
	
	def __repr__(self):
		return self.__str__()
	
	def __add__(self, minutes):
		new_minutes = self.minutes + minutes
		result = Clock(self.hour, new_minutes)
		if result.minutes >= 60:
			addHours = result.minutes / 60
			result.minutes = result.minutes % 60
			result.hour += addHours
		if result.hour >= 24:
			result.hour -= 24
		return result
		
	def __sub__(self, minutes):
		new_minutes = self.minutes - minutes
		result = Clock(self.hour, new_minutes)
		if result.minutes < 0:
			subHours = result.minutes / 60
			result.minutes = result.minutes % 60
			result.hour += subHours
		if result.hour < 0:
			result.hour += 24
		return result
		
	def __eq__(self, other):
		if type(other) == Clock and self.minutes == other.minutes and self.hour == other.hour:
			return True
		elif type(other) == str:
			otherC = other.split(":")
			selfC = self.__str__().split(":")
			if otherC == selfC:
				return True
			return False
		else:
			return False
		
	def __ne__(self, other):
		return not(self.__eq__(other))