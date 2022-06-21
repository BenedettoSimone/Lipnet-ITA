import errno
import sys
import subprocess
import os
from zipfile import ZipFile




#print(path)
#sys.argv
#if sys.argv==null:
   # exit(1)
#riga di comando chiedere directory dataset
#ricavare dir padre di dataset e creare align
#creo config file per s1
#result esce nella
#replace manually substitute value with the name of the folders

def create_config():
    with open(main_path + "\config.txt", 'w+') as file_name:
        file_name.write("is_hierarchy_type=flat \n"+
                        "is_hierarchy_prefix=substitute\\\n "+
                        "is_text_file_relative_path=.\n "+
                        "is_text_file_name_regex=.*\.txt\n "+
                        "is_text_type=plain\n "+
                        "is_audio_file_relative_path=.\n "+
                        "is_audio_file_name_regex=.*\.mpg\n "+

                        "os_job_file_name=result\n "+
                        "os_job_file_container=zip\n "+
                        "os_job_file_hierarchy_type=flat\n "+
                        "os_job_file_hierarchy_prefix=.\n "+
                        "os_task_file_name=$PREFIX.json\n "+
                        "os_task_file_format=json\n "+
                        "os_task_file_smil_page_ref=$PREFIX.xhtml\n "+
                        "os_task_file_smil_audio_ref=$PREFIX.mpg\n "+

                        "job_language=en\n "+
                        "job_description=Example 1 (flat hierarchy, parsed text files)"
    )

def replacing_substitute(dir_name):
    with open(main_path+"\config.txt", 'r') as file :
        filedata = file.read()
    print(dir_name)
    # Replace the target string


    filedata = filedata.replace(to_sub, dir_name)



    with open(main_path+"\config.txt", 'w') as file:
        file.write(filedata)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise




if __name__ == '__main__':
    main_path = input("Enter dataset path:")
    print(main_path)
    path = os.path.dirname(main_path)
    to_sub="substitute"
    mkdir_p(str(path) + "/align")
    create_config()
    for dir in os.listdir(main_path):
        if "config" not in dir:
            print(dir)
            replacing_substitute(dir)
            to_sub=dir
            #dir s*
            #python -m aeneas.tools.execute_job D:\GRID\s1prova\dataset D:\GRID\s1prova\align \ --skip-validator
            #print(path)

            os.system("python -m aeneas.tools.execute_job "+main_path+" "+str(path)+"/align --skip-validator")
            print("CANEWEEEEEEEEEEEEE")
            with ZipFile(path+"/align/result.zip",'r') as zipObj:
                print("UNZIPPING")
                zipObj.extractall(path+"/align/"+dir)

            os.remove(path+"/align/result.zip")




    # implement pip as a subprocess:
    #subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'idna==3.3'])