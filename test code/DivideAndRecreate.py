# Brenna Blackwell
# DivideAndRecreate.py
# University of Arkansas 
# CSCE Capstone II - Spring 2004

import sys
from PIL import Image, ImageFilter

def main():

	try:
		original = Image.open("images/TestImage.jpg")
		
  		width, height = original.size
  		oneThird = width / 3
  		first = 0 + oneThird
  		second = first + oneThird
  		
  		firstThird = original.crop((0, 0, first, height))
  		firstThird.save("images/FirstThird.jpg")
  		firstThirdFilter = firstThird.filter(ImageFilter.BLUR)
  		firstThirdFilter.save("images/FirstThirdFilter.jpg")
  		
  		secondThird = original.crop((first, 0, second, height))
  		secondThird.save("images/SecondThird.jpg")
  		secondThirdFilter = secondThird.filter(ImageFilter.EMBOSS)
  		secondThirdFilter.save("images/SecondThirdFilter.jpg")
  		  		
  		thirdThird = original.crop((second, 0, width, height))
  		thirdThird.save("images/ThirdThird.jpg")
  		thirdThirdFilter = thirdThird.filter(ImageFilter.EDGE_ENHANCE)
  		thirdThirdFilter.save("images/ThirdThirdFilter.jpg")
  		
  		finalImage = Image.new("RGB", (width, height))
  		finalImage.paste(firstThirdFilter, (0, 0))
  		finalImage.paste(secondThirdFilter, (first, 0))
  		finalImage.paste(thirdThirdFilter, (second, 0))
  		finalImage.save("images/FinalImage.jpg")
  		
	
	except:
		print "Unable to complete an operation"



if __name__ == '__main__':
  main()