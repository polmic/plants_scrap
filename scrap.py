import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# pour une categorie, recuperer toutes les url des plantes
categoriesUrl = [
'xxxxxxx/plantes/arbres-arbustes-ete.php',
'xxxxxxx/plantes/arbres-arbustes-printemps.php',
'xxxxxxx/plantes/aromatiques-condimentaires-officinales.php',
'xxxxxxx/plantes/encyclopedie-balcon.php',
'xxxxxxx/plantes/encyclopedie-bassin.php',
'xxxxxxx/plantes/encyclopedie-cactus.php',
'xxxxxxx/plantes/encyclopedie-jardin-feuillage.php',
'xxxxxxx/plantes/encyclopedie-jardin-ete.php',
'xxxxxxx/plantes/encyclopedie-jardin-printemps.php',
'xxxxxxx/plantes/encyclopedie-jardin-automne.php',
'xxxxxxx/plantes/encyclopedie-jardin-hiver.php',
'xxxxxxx/plantes/fleurs-vivaces-ete.php',
'xxxxxxx/plantes/fleurs-vivaces-printemps.php',
'xxxxxxx/plantes/encyclopedie-jardin-tropical.php',
'xxxxxxx/plantes/encyclopedie-jardin-sud.php',
'xxxxxxx/plantes/encyclopedie-orchidees.php',
'xxxxxxx/plantes/palmiers-bananiers-cycas.php',
'xxxxxxx/plantes/encyclopedie-potager.php',
'xxxxxxx/plantes/sauvages.php',
'xxxxxxx/plantes/encyclopedie-verger.php'
'xxxxxxx/plantes/encyclopedie-haies.php',]

for oneCategoryUrl in categoriesUrl :
	html = requests.get(oneCategoryUrl)
	soup = BeautifulSoup(html.text, "html.parser", from_encoding="utf-8")
	oneCategoryLinks = soup.find_all("a")

	# recuperation de toutes les url des plantes sur la page d'une categorie
	plantsUrls = []
	for link in oneCategoryLinks:
		url  = link['href']
		if "xxxxxxx/plantes/" not in url:
			continue
		else:
			plantsUrls.append(url);
			foldername = oneCategoryUrl.replace('https://', '').replace('http://', '').replace('xxxxxxx/plantes/', '').replace('.php', '')
			try:
				os.mkdir(foldername)
			except OSError :
				continue

	# pour chaque url de plante, recuperer le contenu
	i = 1
	for url in plantsUrls:
		html = requests.get(url)
		soup = BeautifulSoup(html.text, "html.parser", from_encoding="utf-8")
		plantPageContent = soup.find("div", {"id": "centercontentpage"})
		ppcstr = str(plantPageContent)
		filename = url.replace('xxxxxxx/plantes/', '').replace('.php', '') + ".html"
		print(ppcstr)
		Html_file = open(str(foldername)+'/'+filename,"w")
		Html_file.write(ppcstr)
		Html_file.close()
		i += 1

