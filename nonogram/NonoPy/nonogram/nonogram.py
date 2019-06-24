try:
	import numpy as np
except:
	print('NumPy not found.')
	print('Please install NumPy by:\n\npip install numpy')
try:
	from PIL import Image, ImageDraw, ImageFont
except:
	print('Pillow not found.')
	print('Please install Pillow by:\n\npip install Pillow')

import os

class Nonogram:
	def __init__(self, imagename):
		self.image = Image.open(imagename)
	
	def convert(self, width, height, threshold, outputname):
		tmp_image = self.image.resize((width, height), Image.BILINEAR)
		tmp_arr = np.ndarray((height, width), dtype=int)

		try:
			tmp = sum(tmp_image.getpixel((0, 0)))
			mode = 0
		except:
			mode = 1

		if mode == 0:
			for i in range(width):
				for j in range(height):
					tmp_arr[j][i] = 1 if sum(tmp_image.getpixel((i, j))) < threshold else 0
		else:
			for i in range(width):
				for j in range(height):
					tmp_arr[j][i] = 1 if tmp_image.getpixel((i, j)) < threshold else 0

		hor = []
		ver = []

		for i in range(width):
			tmp = 0
			col = []
			for j in range(height):
				if tmp_arr[j][i] == 0:
					if tmp > 0:
						col.append(tmp)
						tmp = 0
					continue
				else:
					tmp += 1
			if tmp > 0:
				col.append(tmp)
			hor.append(col)

		for i in range(height):
			tmp = 0
			row = []
			for j in range(width):
				if tmp_arr[i][j] == 0:
					if tmp > 0:
						row.append(tmp)
						tmp = 0
					continue
				else:
					tmp += 1
			if tmp > 0:
				row.append(tmp)
			ver.append(row)
		
		hor_len = list(map(lambda x: len(x), hor))
		ver_len = list(map(lambda x: len(x), ver))
		
		black = (0, 0, 0)
		white = (255, 255, 255)

		offset_x = max(ver_len)*40+20
		offset_y = max(hor_len)*35+20
		size_grid = 40

		size_x = offset_x+width*size_grid
		size_y = offset_y+height*size_grid
		
		output = Image.new("RGB", (size_x, size_y), white)

		draw = ImageDraw.Draw(output)
		font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'OpenSans-Regular.ttf'), 25)

		pos = 0
		for i in range(offset_x, offset_x+width*size_grid, size_grid):
			if not pos % 5:
				linewidth = 3
			else:
				linewidth = 1
			draw.line((i, 0, i, size_y), width=linewidth, fill=black)
			for j in range(len(hor[pos]), 0, -1):
				draw.text((i+8, offset_y-j*35), str(hor[pos][len(hor[pos])-j]), font=font, fill=black)
			pos += 1
		
		pos = 0
		for i in range(offset_y, offset_y+height*size_grid, size_grid):
			if not pos % 5:
				linewidth = 3
			else:
				linewidth = 1
			draw.line((0, i, size_x, i), width=linewidth, fill=black)
			for j in range(len(ver[pos]), 0, -1):
				draw.text((offset_x-j*40, i+3), str(ver[pos][len(ver[pos])-j]), font=font, fill=black)
			pos += 1

		output.save(outputname + "_output.png", "PNG")
		
		for i in range(height):
			for j in range(width):
				if tmp_arr[i][j] == 1:
					draw.rectangle((offset_x+j*size_grid+2, offset_y+i*size_grid+2, offset_x+(j+1)*size_grid-2, offset_y+(i+1)*size_grid-2), fill=black)
		
		output.save(outputname + "_answer.png", "PNG")

		print('Conversion done!')
		print(tmp_arr)
