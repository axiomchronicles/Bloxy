from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%B %d, %Y')

import math

def calculate_reading_time(content):
    words_per_minute = 200 

    words = content.split()
    num_words = len(words)

    reading_time_minutes = num_words / words_per_minute

    reading_time_seconds = reading_time_minutes * 60

    hours = math.floor(reading_time_seconds / 3600)
    reading_time_seconds %= 3600
    minutes = math.floor(reading_time_seconds / 60)
    seconds = math.ceil(reading_time_seconds % 60)

    parts = []
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0 or (hours == 0 and minutes == 0): 
        parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    reading_time = ", ".join(parts)
    return reading_time
