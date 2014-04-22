# Brenna Blackwell
# DivideAndRecreate.py
# University of Arkansas 
# CSCE Capstone II - Spring 2004

import sys
from PIL import Image, ImageFilter

def main():
	try:
		original = Image.open("/home/pi/images/" + sys.argv[1])
		
  		width, height = original.size
  		oneThird = width / 3
  		first = 0 + oneThird
  		second = first + oneThird
  		
  		firstThird = original.crop((0, 0, first, height))
  		firstThird.save("/home/pi/algo2/FirstThird.jpg")
  		firstThirdFilter = firstThird.filter(ImageFilter.BLUR)
#  		firstThirdFilter.save("/home/pi/algo2/FirstThird.jpg")
  		
  		secondThird = original.crop((first, 0, second, height))
  		secondThird.save("/home/pi/algo2/SecondThird.jpg")
  		secondThirdFilter = secondThird.filter(ImageFilter.EMBOSS)
#  		secondThirdFilter.save("/home/pi/algo2/SecondThird.jpg")
  		  		
  		thirdThird = original.crop((second, 0, width, height))
  		thirdThird.save("/home/pi/algo2/ThirdThird.jpg")
  		thirdThirdFilter = thirdThird.filter(ImageFilter.EDGE_ENHANCE)
#  		thirdThirdFilter.save("/home/pi/algo2/ThirdThird.jpg")
  		
  		finalImage = Image.new("RGB", (width, height))
  		finalImage.paste(firstThirdFilter, (0, 0))
  		finalImage.paste(secondThirdFilter, (first, 0))
  		finalImage.paste(thirdThirdFilter, (second, 0))
  		finalImage.save("/home/pi/algo2/Results/" + sys.argv[1])
  		
	
	except:
		print "Unable to complete an operation"



if __name__ == '__main__':
  main()