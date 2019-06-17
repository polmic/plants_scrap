import os
from os import walk

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


def clean_file(infile, outfile, to_remove_list):
    fin = open(infile, encoding='utf-8')
    fout = open(outfile, "w+", encoding='utf-8')
    for line in fin:
        for word in to_remove_list:
            line = line.replace(word, "")
        fout.write(line)
    fin.close()
    fout.close()
    return


root_dir = './html_files'
category_dirs = parse_directory(root_dir)[1]
print('- - - - - - DIRECTORIES - - - - - - ')
print_array(category_dirs)

for directory in category_dirs:
    path_to_parse = "./html_files/" + directory
    path_to_save = "./cleaned_html_files/4/"
    dir_to_save = path_to_save + directory
    try:
        os.mkdir(path_to_save)
    except FileExistsError:
        pass
    os.mkdir(dir_to_save)
    directory_content = parse_directory(path_to_parse)
    html_files = directory_content[2]
    to_remove_list = ['<strong>', '</strong>', '<em>', '</em>', '<i>', '</i>']
    print('- - - - - - DIRECTORY ' + directory + ' FILES - - - - - - ')
    for file in html_files:
        infilepath = path_to_parse + "/" + file
        outfilepath = dir_to_save + "/" + file
        clean_file(infilepath, outfilepath, to_remove_list)

