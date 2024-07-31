def hour_converter_seconds(hours):
    return hours * 3600


def minute_converter_seconds(minutes):
    return minutes * 60


def add_hours_minutes():
    hours = float(input("Enter Hours: "))
    minutes = float(input("Enter Minutes: "))
    sum = hour_converter_seconds(hours) + minute_converter_seconds(minutes)
    return int(round(sum))


print(add_hours_minutes())
