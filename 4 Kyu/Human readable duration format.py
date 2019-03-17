"""Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
"""
def format_duration(seconds):
    #your code here
    print(seconds)
    if seconds == 0:
        return 'now'
    year = 0
    day = 0
    hour = 0
    minute = 0
    if seconds >= 31536000:
        year = seconds // 31536000
        seconds -= (year * 31536000)
    if seconds >= 86400:
        day = seconds // 86400
        seconds -= (day * 86400)
    if seconds >= 3600:
        hour = seconds // 3600
        seconds -= hour*3600
    if seconds >= 60:
        minute = seconds // 60
        seconds -= (minute * 60)
    statement0 = '' if year == 0 else '{} year{}'.format(year, 's' if year!= 1 else '')
    statement1 = '' if day == 0 else '{} day{}'.format(day, 's' if day!= 1 else '')
    statement2 = '' if hour == 0 else '{} hour{}'.format(hour, 's' if hour!= 1 else '')
    statement3 = '' if minute == 0 else '{} minute{}'.format(minute, 's' if minute!= 1 else '')
    statement4 = '' if seconds == 0 else '{} second{}'.format(seconds, 's' if seconds!= 1 else '')

    result = []
    if statement0:
        result.append(statement0)
    if statement1:
        result.append(statement1)
    if statement2:
        result.append(statement2)
    if statement3:
        result.append(statement3)
    if statement4:
        result.append(statement4)

    if len(result) == 1:
        return result[0]
    elif len(result) == 2:
        return '{} and {}'.format(result[0],result[1])
    else:
        return ' and '.join([', '.join(result[:-1]), result[-1]])
