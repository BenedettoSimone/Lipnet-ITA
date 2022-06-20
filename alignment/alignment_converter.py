import errno
import json
import os

DIR_PATH = 'align_json'
TARGET_PATH = 'align/'

# Iterating through the json list
def write_file(file):
    for i in data['fragments']:
        begin = int((float(i['begin']) * 25) * 1000)
        end = int((float(i['end']) * 25) * 1000)
        if file is not None:
            file.write(str(begin) + " " + str(end) + " " + i['lines'][0] + "\n")

# Recursvive directory creation function - makes all intermediate-level directories needed to contain the leaf directory
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


if __name__ == '__main__':

    mkdir_p(TARGET_PATH)

    os.chdir(DIR_PATH)
    for dir in os.listdir():
        os.chdir(dir)
        mkdir_p('../../'+TARGET_PATH+dir)
        for file in os.listdir():
            # Opening JSON file
            f = open(file)

            # returns JSON object as a dictionary
            data = json.load(f)

            with open("../../"+TARGET_PATH+dir+"/"+file[:-5]+".align", 'w+') as file_name:
                write_file(file_name)

            # Closing file
            f.close()
        os.chdir('..')
    os.chdir('..')