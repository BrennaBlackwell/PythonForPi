# Brenna Blackwell
# DivideAndRecreate.py
# University of Arkansas CSCE Capstone II - Spring 2004

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
  		firstThirdBlur = firstThird.filter(ImageFilter.BLUR)
  		firstThirdBlur.save("images/FirstThirdBlur.jpg")
  		
  		secondThird = original.crop((first, 0, second, height))
  		secondThird.save("images/SecondThird.jpg")
  		secondThirdEdge = secondThird.filter(ImageFilter.EDGE_ENHANCE)
  		secondThirdEdge.save("images/SecondThirdEdge.jpg")
  		  		
  		thirdThird = original.crop((second, 0, width, height))
  		thirdThird.save("images/ThirdThird.jpg")
  		thirdThirdEmboss = thirdThird.filter(ImageFilter.EMBOSS)
  		thirdThirdEmboss.save("images/thirdFilterEmboss.jpg")
  		
	
	except:
		print "Unable to complete an operation"



if __name__ == '__main__':
  main()