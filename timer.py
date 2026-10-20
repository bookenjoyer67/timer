import time

total_minutes = int(input("Enter countdown time in minutes: "))
add_seconds = int(input("Enter how many seconds: "))

total_seconds = (total_minutes * 60) + add_seconds

# total_seconds = int(input("Enter countdown time in minutes: "))

def chime(times=3, beeps=3, interval=0.1):
    import threading

    stop_event = threading.Event()

    def stop():
        input("Press enter to dismiss...")
        stop_event.set()

    t = threading.Thread(target=stop)
    t.daemon = True
    t.start()

    while not stop_event.is_set():
        for _ in range(times):
            for _ in range(beeps):
                print('\a', end='', flush=True)
                time.sleep(interval)
        time.sleep(0.5)

while total_seconds > 0:
    minutes, seconds = divmod(total_seconds, 60)
    print(f"\r{minutes:02d}:{seconds:02d}", end="")
    time.sleep(1)
    total_seconds -=1

print("\r00:00")
print("Time's up!")
chime()
