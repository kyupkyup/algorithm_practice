from datetime import datetime

def convert_to_seconds(time):
    time = map(int, time.split(":"))
    result = 0
    for t, sec in zip(time, [3600, 60, 1]):
        result = t * sec
    return result

def seconds_to_time(seconds):
    s= seconds % 60
    seconds //= 60
    m = seconds % 60
    seconds //= 60
    h= seconds
    return '{:02d}:{:02d}:{:02d}'.format(h, m ,s)