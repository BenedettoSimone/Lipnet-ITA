import errno
import os

from PIL import Image, ImageOps


# Recursvive directory creation function - makes all intermediate-level directories needed to contain the leaf directory
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


mkdir_p("augmented")

os.chdir('frames')
for subject in os.listdir():
    if '.DS_Store' not in subject:
        new_folder = subject.replace("s", "a")
        mkdir_p("../augmented/"+new_folder)

        os.chdir(subject)
        print("\n=====================")
        print("Processing folder - " + subject)
        print("=====================")
        for phrase in os.listdir():
            if '.DS_Store' not in phrase:
                os.chdir(phrase)
                print("Processing phrase - " + phrase)
                mkdir_p("../../../augmented/" + new_folder + "/" + phrase)
                for image in os.listdir():
                    if '.DS_Store' not in image:
                        # execute flip
                        img = Image.open(image)

                        img_mirror = ImageOps.mirror(img)
                        img_mirror.save("../../../augmented/" + new_folder + "/" + phrase + "/" + image, quality=100)
                os.chdir('..')
        os.chdir('..')
os.chdir('..')
