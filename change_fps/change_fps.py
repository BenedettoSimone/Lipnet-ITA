import os


def create_directory(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        print("Directory can not be created")


if __name__ == '__main__':

    os.chdir('../DATASET')

    for s in os.listdir():
        if '.DS_Store' not in s:
            os.chdir(s)

            create_directory('../../25fps/' + s)

            for video in os.listdir():
                os.system("ffmpeg -i " + video + " -filter:v fps=fps=25 " + '../../25fps/' + s + '/' + video)

            os.chdir('..')
    os.chdir('..')
