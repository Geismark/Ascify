from pathlib import Path
from PIL import Image
import logging


ascii_surf_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # issue with "\\"?
# ('#','#','@','@','%','%',';',';','*','*',',',',','.','.',' ',' ')
# ["B","S","#","&","@","$","%","*","!",":","."]
ascii_length = len(ascii_surf_chars)

def program():
	file_dir = inputFile()
	if not file_dir:
		print("Exiting program")
		return

	image = Image.open(file_dir)
	ascii_lst = getImageAscii(image)
	
	# out_dir = "image.txt" <- could add user designated output
	writeImageFile(ascii_lst)

def getAsciiChar(pixel):
	(r, g, b) = pixel
	return ascii_surf_chars[round((r + g + b) / (255*3) * (ascii_length - 1))]

def inputFile():
	file = input("Input your file's full path:") # could add easy PySimpleGUI for this
	directory = None

	try:
		if Path(file).is_file():
			directory = Path(file)
			logging.debug("File found")
	except:
		logging.warning("Could not find file")
	return directory

def getImageAscii(image):
	(i_w, i_h) = image.size
	imageAscii = []
	for y in range(0, i_h - 1):
		row = []
		rowStr = ""
		
		row = [getAsciiChar(image.getpixel((x,y))) for x in range(0, i_w-1)]
		
		rowStr = "".join(row) + "\n"

		imageAscii.append(rowStr)

	return imageAscii

def writeImageFile(ascii_lst):
	file_dir = Path(str(Path(__file__).parent.resolve()) + "\\image.txt")
	try:
		with open(file_dir, "w", newline="") as out_file:
				for row in ascii_lst:
					out_file.write(row)
	except:
		logging.error("Export image error")


if __name__ == "__main__":
	program()