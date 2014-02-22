import sys
from PIL import Image, ImageFilter

def main():

	try:
		original = Image.open("TestImage.jpg")
		original.show()
		
  		width, height = original.size
  		oneThird = width / 3
  		first = 0 + oneThird
  		second = first + oneThird
  		
  		firstThird = original.crop((0, 0, first, height))
  		firstThird.show()
  		firstThird.save("FirstThird.jpg")
  		
  		secondThird = original.crop((first, 0, second, height))
  		secondThird.show()
  		secondThird.save("SecondThird.jpg")
  		
  		thirdThird = original.crop((second, 0, width, height))
  		thirdThird.show("ThirdThird.jpg")
  		
	
	except:
		print "Unable to load image"



if __name__ == '__main__':
  main()