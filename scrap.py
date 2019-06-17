import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# pour une categorie, recuperer toutes les url des plantes
categoriesUrl = [
'http://www.aujardin.info/plantes/arbres-arbustes-ete.php',
'http://www.aujardin.info/plantes/arbres-arbustes-printemps.php',
'http://www.aujardin.info/plantes/aromatiques-condimentaires-officinales.php',
'http://www.aujardin.info/plantes/encyclopedie-balcon.php',
'http://www.aujardin.info/plantes/encyclopedie-bassin.php',
'http://www.aujardin.info/plantes/encyclopedie-cactus.php',
'http://www.aujardin.info/plantes/encyclopedie-jardin-feuillage.php',
'http://www.aujardin.info/plantes/encyclopedie-jardin-ete.php',
'http://www.aujardin.info/plantes/encyclopedie-jardin-printemps.php',
'http://www.aujardin.info/plantes/encyclopedie-jardin-automne.php',
'http://www.aujardin.info/plantes/encyclopedie-jardin-hiver.php',
'http://www.aujardin.info/plantes/fleurs-vivaces-ete.php',
'http://www.aujardin.info/plantes/fleurs-vivaces-printemps.php',
'http://www.aujardin.info/plantes/encyclopedie-jardin-tropical.php',
'http://www.aujardin.info/plantes/encyclopedie-jardin-sud.php',
'http://www.aujardin.info/plantes/encyclopedie-orchidees.php',
'http://www.aujardin.info/plantes/palmiers-bananiers-cycas.php',
'http://www.aujardin.info/plantes/encyclopedie-potager.php',
'http://www.aujardin.info/plantes/sauvages.php',
'http://www.aujardin.info/plantes/encyclopedie-verger.php'
'https://www.aujardin.info/plantes/encyclopedie-haies.php',]

for oneCategoryUrl in categoriesUrl :
	html = requests.get(oneCategoryUrl)
	soup = BeautifulSoup(html.text, "html.parser", from_encoding="utf-8")
	oneCategoryLinks = soup.find_all("a")

	# recuperation de toutes les url des plantes sur la page d'une categorie
	plantsUrls = []
	for link in oneCategoryLinks:
		url  = link['href']
		if "https://www.aujardin.info/plantes/" not in url:
			continue
		else:
			plantsUrls.append(url);
			foldername = oneCategoryUrl.replace('https://', '').replace('http://', '').replace('www.aujardin.info/plantes/', '').replace('.php', '')
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
		filename = url.replace('https://www.aujardin.info/plantes/', '').replace('.php', '') + ".html"
		print(ppcstr)
		Html_file = open(str(foldername)+'/'+filename,"w")
		Html_file.write(ppcstr)
		Html_file.close()
		i += 1

