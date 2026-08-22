'''
Spoken Duration
Given a number of seconds, return the duration in spoken English.

Break the duration into hours, minutes, and seconds.
Skip any zero values.
Use singular or plural as appropriate ("1 hour", "2 hours").
If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes and 3 seconds").

Testes:
1. get_spoken_duration(3723) should return "1 hour, 2 minutes and 3 seconds".
2. get_spoken_duration(7295) should return "2 hours, 1 minute and 35 seconds".
3. get_spoken_duration(8521) should return "2 hours, 22 minutes and 1 second".
4. get_spoken_duration(435) should return "7 minutes and 15 seconds".
5. get_spoken_duration(14455) should return "4 hours and 55 seconds".
6. get_spoken_duration(72000) should return "20 hours".
7. get_spoken_duration(1) should return "1 second".
'''

def get_spoken_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seg = seconds % 60

    time = [
        ['hour' if hours == 1 else 'hours', hours],
        ['minute' if minutes == 1 else 'minutes', minutes],
        ['second' if seg == 1 else 'seconds', seg]
    ]

    time = [item for item in time if item[1] > 0]

    if len(time) == 1:
        return f'{time[0][1]} {time[0][0]}'
    elif len(time) == 2:
        return f'{time[0][1]} {time[0][0]} and {time[1][1]} {time[1][0]}'
    else:
        return f'{time[0][1]} {time[0][0]}, {time[1][1]} {time[1][0]} and {time[2][1]} {time[2][0]}'

print(get_spoken_duration(3723))
print(get_spoken_duration(7295))
print(get_spoken_duration(8521))
print(get_spoken_duration(435))
print(get_spoken_duration(14455))
print(get_spoken_duration(72000))
print(get_spoken_duration(1))