import errno
import os
from zipfile import ZipFile


# create config file
def create_config():
    with open(main_path + "\config.txt", 'w+') as file_name:
        file_name.write("is_hierarchy_type=flat \n" +
                        "is_hierarchy_prefix=substitute\\\n " +
                        "is_text_file_relative_path=.\n " +
                        "is_text_file_name_regex=.*\.txt\n " +
                        "is_text_type=plain\n " +
                        "is_audio_file_relative_path=.\n " +
                        "is_audio_file_name_regex=.*\.mpg\n " +

                        "os_job_file_name=result\n " +
                        "os_job_file_container=zip\n " +
                        "os_job_file_hierarchy_type=flat\n " +
                        "os_job_file_hierarchy_prefix=.\n " +
                        "os_task_file_name=$PREFIX.json\n " +
                        "os_task_file_format=json\n " +
                        "os_task_file_smil_page_ref=$PREFIX.xhtml\n " +
                        "os_task_file_smil_audio_ref=$PREFIX.mpg\n " +

                        "job_language=ita\n " +
                        "job_description=Example 1 (flat hierarchy, parsed text files)"
                        )


# modify config file
def replacing_substitute(dir_name):
    with open(main_path + "\config.txt", 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(to_sub, dir_name)

    with open(main_path + "\config.txt", 'w') as file:
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

    path = os.path.dirname(main_path)
    to_sub = "substitute"

    # create folder to store aligned folder
    mkdir_p(str(path) + "/align_json")

    # create config file
    create_config()

    for dir in os.listdir(main_path):
        if "config" not in dir:
            print("\nALIGNING: " + dir)

            # modify config file
            replacing_substitute(dir)
            to_sub = dir

            os.system("python -m aeneas.tools.execute_job " + main_path + " " + str(path) + "/align_json --skip-validator")

            print('UNZIPPING: ' + dir)
            with ZipFile(path + "/align_json/result.zip", 'r') as zipObj:
                zipObj.extractall(path + "/align_json/" + dir)

            os.remove(path + "/align_json/result.zip")
