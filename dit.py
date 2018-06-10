# -*- coding: UTF-8 -*-
from PIL import Image
import numpy as np
## @package ICN_ImageLib_Darkgeem
#  Cette librairie sert à effectuer différentes modifications sur des images, en utilisant les librairies PIL et numpy.

## Permet de charger une image sans devoir importer PIL dans l'interpréteur
def loadimage(path):
	outimage = Image.open(path)
	return outimage

## Fonction qui convertit une image en niveaux de gris
#  @param inpimage **Objet image** qui sera converti
def gray(inpimage):
	width, height = inpimage.size	#Obtention de la largeur et de la hauteur de l'image en entrée
	outimage = Image.new("L", (width, height), "white")	#Création d'une image de sortie vide (blanche, donc pas vraiment vide, mais remplie de 255), en niveaux de gris uniquement (d'où le "L")
	pixels = outimage.load()	#Création d'une variable contenant la carte des pixels de l'image de sortie 

	for i in range(width):	#Double boucle pour obtenir la moyenne des couleurs primaires de chaque pixel
		for j in range(height):
			pixel = inpimage.getpixel((i, j))	#Définition d'une variable en tant qu'objet pixel, basé sur le pixel en cours
			r = pixel[0]	#
			g = pixel[1]	###Définitions des variable de rouge, vert et bleu en fonction de la quantité de chaque couleur pour le pixel en cours
			b = pixel[2]	#
			gpix = int((r+g+b)/3)	#Définition d'une variable contenant la moyenne des couleurs du pixel en cours qui sera le niveau de gris du même pixel sur l'image de sortie

			pixels[i, j] = gpix	#Ecriture du niveau de gris du pixel en cours sur l'image de sortie

	return outimage	#Retourne l'image de sortie en tant qu'objet image

## Fonction qui convertit une image en noir et blanc "pûr", si le seuil n'est pas précisé, le définit automatiquement sur la médiane.
# @param image **Objet image** qui sera converti
# @param threshold *Optionnel,* le seuil de conversion. Tous les pixels ayant un niveau de gris inférieur à ce seuil seront noirs, sinon, ils seront blancs.
def black(image, threshold=0):
	inpimage = gray(image)	#Conversion de l'image en niveaux de gris
	width, height = inpimage.size	#Obtention de la largeur et de la hauteur de l'image en entrée
	outimage = Image.new("1", (width, height), "white")	#Création d'une image de sortie vide (blanche, donc pas vraiment vide, mais remplie de 255), en noir et blanc "pûr" uniquement (d'où le "1")
	pixels = outimage.load()	#Création d'une variable contenant la carte des pixels de l'image de sortie 
	pmap = (width*height)*[0]	#Création d'une liste vide, de taille égale au nombre de pixels dans l'image
	k = 0	#Initialisation de l'index de liste(pmap) courant à zéro

	for i in range(width):	#Double boucle pour ranger chaque pixel dans la liste pmap
		for j in range(height):
			pixel = inpimage.getpixel((i, j))	#Définition d'une variable en tant qu'objet pixel, basé sur le pixel en cours
			pmap[k] = pixel	#Stocke l'objet pixel dans la liste pmap
			k = k+1	#Incrémentation de l'index de liste pmap

	if threshold <= 0:	#Si le seuil n'est pas défini lors de l'appel de la fonction (ou s'il est défini à 0 ou moins), utilise la médiane des nuances de gris des pixels de l'image
		threshold = int(np.median(pmap))

	for i in range(width):	#Double boucle pour écrire chaque pixel en noir ou blanc en fonction du seuil
		for j in range(height):
			pixel = inpimage.getpixel((i, j))	#Définition d'une variable en tant qu'objet pixel, basé sur le pixel en cours
			if (pixel < treshold):	#Si la nuance de gris du pixel est en dessous du seuil, le rend noir
				pixels[i, j] = 0
			else:					#Sinon, le rend blanc
				pixels[i, j] = 255

	return outimage	#Renvoie l'image en noir et blanc
