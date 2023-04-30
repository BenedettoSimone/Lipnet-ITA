import os

from flask import Flask, jsonify, request, make_response
from mouth_extract import extract_mouth_frames
from predict import predict_main
from predictENG import predictENG_main
import shutil

app = Flask(__name__)


#To use the English model:
    # change the output file
    # disable conversions file
    # use predictENG function
    # in mouth_extract change SOURCE_EXTS = '*.mpg'

@app.route('/main', methods=['GET', 'POST'])
def index11():
    req = request.get_data()

    FILE_OUTPUT = 'DATASET/s99/video.h264'

    #FILE_OUTPUT = 'DATASET/s99/0-sc.mpg'

    # Checks and deletes the output file
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)

    out_file = open(FILE_OUTPUT, "wb")  # open for [w]riting as [b]inary
    out_file.write(req)
    out_file.close()

    # convert video .h264 to .mp4
    os.system("ffmpeg -framerate 25 -i DATASET/s99/video.h264 -c copy DATASET/s99/0-sc.mp4")

    os.remove("DATASET/s99/video.h264")

    print("Conversion done")

    # extract frames
    extract_mouth_frames()

    print("MouthExtract done")

    # remove video
    #os.remove("DATASET/s99/0-sc.mp4")

    for filename in sorted(os.listdir("frames/s99/0-sc"))[100:]:
        filename_relPath = os.path.join("frames/s99/0-sc", filename)
        os.remove(filename_relPath)

    response = predict_main()
    #response = predictENG_main()

    #remove frames
    #shutil.rmtree("frames/s99")

    # set response
    res = make_response(jsonify({"message": response}), 200)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
