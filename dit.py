# -*- coding: UTF-8 -*-
from PIL import Image
import numpy as np

# Permet de charger une image sans charger PIL
def loadimage(path):
	outimage = Image.open(path)
	return outimage

# Fonction qui convertit une image en niveaux de gris
def gray(inpimage):
	width, height = inpimage.size
	outimage = Image.new("L", (width, height), "white")
	pixels = outimage.load()

	for i in range(width):
		for j in range(height):
			pixel = inpimage.getpixel((i, j))
			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			gpix = int((r+g+b)/3)

			pixels[i, j] = gpix

	return outimage

# Fonction qui convertit une image en noir et blanc "pûr", si le seuil n'est pas précisé, le définit automatiquement sur la médiane.
def black(image, threshold=0):
	inpimage = gray(image)
	width, height = inpimage.size
	outimage = Image.new("1", (width, height), "white")
	pixels = outimage.load()
	pmap = (width*height)*[0]
	k = 0

	for i in range(width):
		for j in range(height):
			pixel = inpimage.getpixel((i, j))
			pmap[k] = pixel
			k = k+1

	if threshold <= 0:
		threshold = int(np.median(pmap))

	for i in range(width):
		for j in range(height):
			pixel = inpimage.getpixel((i, j))
			if (pixel < treshold):
				pixels[i, j] = 0
			else:
				pixels[i, j] = 255

	return outimage
