import time
import subprocess
reps = 20
while True:
    for i in range(reps):
        print("_"*i, end="")
        print("--", end="")
        print("_"*(reps-i))
        time.sleep(0.05)
        subprocess.run(["clear"])
    for i in range(reps,0,-1):
        print("_"*i, end="")
        print("--", end="")
        print("_"*(reps-i))
        time.sleep(0.05)
        subprocess.run(["clear"])
