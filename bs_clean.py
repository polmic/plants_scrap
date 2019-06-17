from os import walk
import os
from bs4 import BeautifulSoup


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

version_num = 2

for directory in category_dirs:
    path_to_parse = "./html_files/" + directory
    path_to_save = "./cleaned_html_files/" + str(version_num) + "/" + directory

    try:
        os.mkdir("./cleaned_html_files/" + str(version_num))
    except FileExistsError:
        pass
    os.mkdir(path_to_save)
    directory_content = parse_directory(path_to_parse)
    html_files = directory_content[2]

    print('- - - - - - DIRECTORY ' + directory + ' FILES - - - - - - ')
    for file in html_files:
        filepath = path_to_parse + "/" + file
        print('- - - - - - ' + file + ' - - - - - - ')
        soup = BeautifulSoup(open(filepath, encoding="utf8"), "html.parser", from_encoding="utf-8")
        articleXL = soup.find("div", {"id": "articleXL"})
        article = soup.find('article')
        article.find('figure').decompose()

        for div in article.find_all("div", {'class': 'hidden-xlarge'}):
            div.decompose()
        for div in article.find_all("div", {'id': 'mb-1'}):
            div.decompose()
        for div in article.find_all("div", {'class': 'spacer'}):
            div.decompose()
        for div in article.find_all("div", {'class': 'boxrezo'}):
            div.decompose()
        for div in article.find_all("div", {'class': 'hidden-small'}):
            div.decompose()
        for span in article.find_all("span", {'class': 'help'}):
            span.decompose()
        for i in article.find_all('i', {'class': 'fa'}):
            i.decompose()
        for i in article.find_all('i', {'class': 'wi'}):
            i.decompose()
        for ul in article.find_all('ul'):
            ul.decompose()

        article_str = str(article)
        file_to_save = open(path_to_save + "/" + file, "w", encoding='utf-8')
        file_to_save.write(article_str)
        file_to_save.close()