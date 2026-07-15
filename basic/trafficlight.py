import time

lights = [("RED", 5), ("YELLOW", 2), ("GREEN", 5)]

while True:
    for color, duration in lights:
        print(f"\n{color}")
        for t in range(duration, 0, -1):
            print(t)
            time.sleep(1)



