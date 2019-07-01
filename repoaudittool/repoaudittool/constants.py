WEEKDAYS = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
HOURS = [
    (0, "12am"),
    (1, "1am"),
    (2, "2am"),
    (3, "3am"),
    (4, "4am"),
    (5, "5am"),
    (6, "6am"),
    (7, "7am"),
    (8, "8am"),
    (9, "9am"),
    (10, "10am"),
    (11, "11am"),
    (12, "12pm"),
    (13, "1pm"),
    (14, "2pm"),
    (15, "3pm"),
    (16, "4pm"),
    (17, "5pm"),
    (18, "6pm"),
    (19, "7pm"),
    (20, "8pm"),
    (21, "9pm"),
    (22, "10pm"),
    (23, "11pm"),
]


def generate_hiw():
    HOURS_IN_WEEK = []
    for weekday in WEEKDAYS:
        for hour in HOURS:
            HOURS_IN_WEEK.append((weekday, hour[1]))


HOURS_IN_WEEK = generate_hiw()
