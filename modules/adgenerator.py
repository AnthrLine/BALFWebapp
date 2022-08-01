import random

def generate():
	ads = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	ads[0] = random.randint(1,18)
	ads[1] = random.randint(1, 18)
	ads[2] = random.randint(1,18)
	ads[3] = random.randint(1, 18)
	ads[4] = random.randint(1, 18)
	ads[5] = random.randint(1, 18)
	ads[6] = random.randint(1, 18)
	ads[7] = random.randint(1, 18)
	ads[8] = ads[3]
	ads[9] = ads[1]
	ads[10] = ads[2]
	ads[11] = ads[0]

	while ads[1] == ads[0]:
		ads[1] = random.randint(1, 18)

	while ads[3] == ads[2]:
		ads[3] = random.randint(1, 18)

	while ads[5] == ads[4]:
		ads[5] = random.randint(1, 18)

	while ads[7] == ads[6]:
		ads[7] = random.randint(1, 18)
	
	return ads
		