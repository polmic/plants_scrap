# -*- coding: utf-8 -*-

from os import walk
from bs4 import BeautifulSoup
import traceback
import unicodedata
import csv


def print_array(array):
    for entry in array:
        print(str(entry))
    return


def parse_directory(path_to_parse):
    files = []
    directories = []
    path = []
    for (dirpath, dirnames, filenames) in walk(path_to_parse):
        files.extend(filenames)
        directories.extend(dirnames)
        path.extend(dirpath)
        break
    return [path, directories, files]


root_dir = './html_files'
category_dirs = parse_directory(root_dir)[1]
print('- - - - - - DIRECTORIES - - - - - - ')
print_array(category_dirs)

row_results = [0] * 25

def log_error(filename, directory, error):
    log_file = open('./error_logs.txt', "a+")
    log_file.write('_______________________________________________________________________________'
                   + '\nERROR - '
                   + filename + ' in ' + directory
                   + '\n\n'
                   + error
                   + '\n\n')
    log_file.close()
    return


def get_latin_name(description):
    global no_latin_name_nb
    latin_name = ''
    try:
        latin_name = description.find(title="Nom scientifique de la plante").findNext('i').findNext('i').getText()
    except Exception:
        no_latin_name_nb += 1
        log_error(file, directory, traceback.format_exc())
    print('Nom latin: ' + str(latin_name))
    return latin_name


def add_value_in_row(key, value, row):
    if key == 'Acidité du sol':
        row[16] = value
        row_results[16] += 1
    elif key == 'Couleur des fleurs':
        row[6] = value
        row_results[6] += 1
    elif key == 'Espèces proches':
        row[14] = value
        row_results[14] += 1
    elif key == 'Exposition':
        row[3] = value
        row_results[3] += 1
    elif key == 'Famille':
        row[4] = value
        row_results[4] += 1
    elif key == 'Hauteur':
        row[8] = value
        row_results[8] += 1
    elif key == 'Humidité du sol':
        row[17] = value
        row_results[17] += 1
    elif key == 'Maladies et ravageurs':
        row[2] = value
        row_results[2] += 1
    elif key == 'Méthode de multiplication':
        row[10] = value
        row_results[10] += 1
    elif key == 'Nom latin':
        row[9] = value
        row_results[9] += 1
    elif key == 'Origine':
        row[11] = value
        row_results[11] += 1
    elif key == 'Période de floraison':
        row[5] = value
        row_results[5] += 1
    elif key == 'Plantation, rempotage':
        row[13] = value
        row_results[13] += 1
    elif key == 'Rusticité':
        row[15] = value
        row_results[15] += 1
    elif key == 'Synonyme':
        row[19] = value
        row_results[19] += 1
    elif key == 'Synonymes':
        row[19] = value
        row_results[19] += 1
    elif key == 'Taille':
        row[20] = value
        row_results[20] += 1
    elif key == 'Toxicité':
        row[21] = value
        row_results[21] += 1
    elif key == 'Type de feuillage':
        row[7] = value
        row_results[7] += 1
    elif key == 'Type de plante':
        row[12] = value
        row_results[12] += 1
    elif key == 'Type de sol':
        row[18] = value
        row_results[18] += 1
    elif key == 'Type de végétation':
        row[23] = value
        row_results[23] += 1
    elif key == 'Utilisation':
        row[22] = value
        row_results[22] += 1
    else:
        print('# # # # # # # # # # # # # # # # KEY UNKNOWN : ' + key)
        row_results[24] += 1
    return row


with open('./data.csv', 'w', encoding="utf8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['category',
                        'common_name',
                        'diseases_pests',
                        'exposure',
                        'family',
                        'flowering',
                        'flowers_color',
                        'foliage_type',
                        'height',
                        'latin_name',
                        'multiplication_methods',
                        'origin',
                        'plant_type',
                        'plantation_repotting',
                        'related_species',
                        'rusticity',
                        'soil_acidity',
                        'soil_humidity',
                        'soil_type',
                        'synonyms',
                        'trimming',
                        'toxicity',
                        'usage',
                        'vegetation_type'])

    for directory in category_dirs:
        path_to_parse = "./html_files/" + directory
        directory_content = parse_directory(path_to_parse)
        html_files = directory_content[2]

        print('- - - - - - DIRECTORY ' + directory + ' FILES - - - - - - ')
        for file in html_files:
            filepath = path_to_parse + "/" + file

            # print('- - - - - - ' + file + ' - - - - - - ')

            soup = BeautifulSoup(open(filepath, encoding="utf8"), "html.parser", from_encoding="utf-8")
            article = soup.find("article")
            plant_name = str(article.h1.getText())
            # print(plant_name)
            description = soup.find("div", {"id": "description3"})

            entries = description.find_all('div')
            new_row = [''] * 24
            new_row[0] = directory
            row_results[0] += 1

            if plant_name:
                new_row[1] = plant_name
                row_results[1] += 1

            for div in entries:
                entry = unicodedata.normalize("NFKD", div.getText()).split(':')
                key = entry[0].strip()
                value = entry[1].strip()
                add_value_in_row(key, value, new_row)

            csvwriter.writerow(new_row)

print(str(row_results))
