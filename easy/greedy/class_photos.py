# O(nlogn) where n is the no of elements in a row
def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	

	if blueShirtHeights[0] > redShirtHeights[0]:
		backrow = "blue"
	else:
		backrow = "red"
	
	for idx, red_height in enumerate(redShirtHeights):
		blue_height = blueShirtHeights[idx]
		
		if backrow == "blue":
			if blue_height <= red_height:
				return False
		else:
			if blue_height >= red_height:
				return False
	return True