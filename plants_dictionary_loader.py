import requests
import csv

url = 'http://localhost:8080/api/plantsdictionary'

def get_data_from_row(row):
    try:
        data = {
            "category": row[0],
            "commonName": row[1],
            "diseasesPests": row[2],
            "exposure": row[3],
            "family": row[4],
            "flowering": row[5],
            "flowersColor": row[6],
            "foliageType": row[7],
            "height": row[8],
            "latinName": row[9],
            "multiplicationMethods": row[10],
            "origin": row[11],
            "plantType": row[12],
            "plantationRepotting": row[13],
            "relatedSpecies": row[14],
            "rusticity": row[15],
            "soilAcidity": row[16],
            "soilHumidity": row[17],
            "soilType": row[18],
            "synonyms": row[19],
            "toxicity": row[20],
            "trimming": row[21],
            "plantUsage": row[22],
            "vegetationType": row[23],
        }
        return data
    except IndexError:
        return ''

with open('data.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            response = requests.post(url, json=get_data_from_row(row))
            if str(response) != '<Response [201]>':
                print('ERROR ON ROW ' + str(row))
            line_count += 1
    print(f'Processed {line_count} lines.')