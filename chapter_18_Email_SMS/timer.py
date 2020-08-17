import time

starttime = time.time()


# Print Tick every 60 seconds. %60 ensures time is always positive
while True:
    print("tick")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
