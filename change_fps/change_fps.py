import os
import ffmpeg


def create_directory(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as error:
        print("Directory can not be created")

if __name__ == '__main__':

    os.chdir('DATASET')

    for s in os.listdir():
        if '.DS_Store' not in s:
            os.chdir(s)

            create_directory('../../25fps/'+s)

            for video in os.listdir():
                stream = ffmpeg.input(video)
                video_stream = stream.video
                audio_stream = stream.audio
                stream = stream.filter('fps', fps=25, round='up')
                stream = ffmpeg.output(audio_stream, video_stream, '../../25fps/'+s+'/'+video)
                ffmpeg.run(stream)
            os.chdir('..')
    os.chdir('..')

