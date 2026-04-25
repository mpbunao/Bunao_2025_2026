# To find the time how long it takes to run a marathon

distance = 42.195
speed = int(input("Input speed (km/h): "))

def Time(distance, speed):
    time = distance / speed
    hours = time // 1
    fractionalpart = time % 1
    minutes = (fractionalpart * 60) // 1

    print("At", speed, "km/h, it will take approximately",
          int(hours), "hours and", int(minutes), "minutes.")

    return time

Time(distance, speed)

# Scope:
# It dictates the region of code where a variable is accessible.
