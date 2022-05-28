import shutil
from imutils import face_utils
import dlib
import os
import cv2
import numpy as np
import glob
import re


def lip_extractor(video_path):
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    # create new directory for frame
    dirname = 'frame'
    os.mkdir(dirname)
    while success:

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detect faces in the grayscale image
        rects = detector(gray, 1)
        for (i, rect) in enumerate(rects):
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            print("frame:" + str(count))
            for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
                if name == 'mouth':
                    # h,w modify
                    (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
                    max_value = max(h, w)
                    y = y - max_value // 3
                    roi = image[y:y + max_value, x:x + max_value]
                    roi = cv2.resize(roi, (300, 300))

        cv2.imwrite(os.path.join(dirname, "frame-%d.jpg" % count), roi)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1


if __name__ == '__main__':

    # extract all frames of video
    lip_extractor("2-am.mpg")

    # define property of new video
    frameSize = (300, 300)
    out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*"mp4v"), float(25), frameSize)

    # Get list of all files in a given directory
    list_of_files = glob.glob('frame/*')

    # sort all files numerically
    list_of_files.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])

    # write frames in video and save it
    for filename in list_of_files:
        print(filename)
        img = cv2.imread(filename)
        out.write(img)

    out.release()

    # delete folder frame
    shutil.rmtree('frame')
