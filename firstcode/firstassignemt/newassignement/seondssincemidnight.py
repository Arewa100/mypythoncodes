def seconds_since_midnight(hours, minutes, seconds):
	hour_in_seconds = (60 * 60 * hours)
	minute_in_seconds = (60 * minutes)
	result = (hour_in_seconds + minute_in_seconds + seconds)
	return result

time = seconds_since_midnight(13, 30, 45)

print(time, "PM")