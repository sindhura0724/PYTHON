import random
import datetime
initialseed=6
currenttime=datetime.datetime.now().timestamp()
updatedseed=initialseed+int(currenttime)
random.seed(updatedseed)
randomnum=[random.randint(10,50)for _ in range(5)]
print(randomnum)