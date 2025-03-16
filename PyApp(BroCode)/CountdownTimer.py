import time
timer = int(input("Enter the time in seconds: "))
for x in range(timer, 0, -1):
    sec = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)
    print(f'{hours:02}:{minutes:02}:{sec:02}')
    time.sleep(1)
print("Time's up!")
