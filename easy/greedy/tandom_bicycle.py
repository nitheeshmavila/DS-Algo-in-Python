#  O(NLOGN) time, were N is the no of riders in one shirt

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
	if fastest:
		blueShirtSpeeds.sort(reverse=True)
	else:
		blueShirtSpeeds.sort()
		
	tandom_speed_sum = 0
	for idx, red_speed in enumerate(redShirtSpeeds):
		blue_speed = blueShirtSpeeds[idx]
		tandom_speed_sum += max(red_speed, blue_speed)
	return tandom_speed_sum