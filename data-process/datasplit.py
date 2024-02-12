import os
import shutil
from os.path import basename


def organizefiles(dataset_dir,correct_dir,incorrect_dir):
    if not os.path.exists(correct_dir):
        os.makedirs(correct_dir)
    if not os.path.exists(incorrect_dir):
        os.makedirs(incorrect_dir)

    for filename in os.listdir(dataset_dir):
        if os.path.isfile(os.path.join(dataset_dir,filename)):
            # file = basename(filename)
            root,ext = os.path.splitext(filename)
            text = root.rsplit('_')
            label = text[-2]
            if label == '1':
                shutil.move(os.path.join(dataset_dir, filename), os.path.join(correct_dir, filename))
                print('correct posture')
            else:
                shutil.move(os.path.join(dataset_dir, filename), os.path.join(incorrect_dir, filename))
                print('incorrect posture')
    
#organizefiles('SkeletonData/Simplified','Correct_postures','incorrect_postures')
lst = os.listdir('incorrect_postures') # your directory path
number_files = len(lst)
print (number_files)

