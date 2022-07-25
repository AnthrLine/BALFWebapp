import random

def generate():
	ads = [0, 0, 0, 0]
	ads[0] = random.randint(1,17)
	ads[1] = random.randint(1, 17)
	ads[2] = random.randint(1,17)
	ads[3] = random.randint(1, 17)

	while ads[1] == ads[0]:
		ads[1] = random.randint(1, 17)

	while ads[3] == ads[2]:
		ads[3] = random.randint(1, 17)
	
	return ads
		