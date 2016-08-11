#!/usr/bin/python

import os
import sys
import VideoUtils as vu


#--------------------- Constants and Global variables ------------------------

PROJECT_NAME = sys.argv[1]
PROJECT_VIDEOS_PATH = sys.argv[2]
if PROJECT_VIDEOS_PATH[-1] != "/":
    PROJECT_VIDEOS_PATH += "/"

PROJECT_VIDEO_TEMPLATE = "_video_project_template.py_"



#-------------------------- Auxiliar Functions -------------------------------


def create_symlink(directory, symlink_name):
    if os.path.exists(symlink_name):
        os.remove(symlink_name)
    os.symlink(directory, symlink_name)



def create_folder_and_symlink(symlink_name):
    directory = PROJECT_VIDEOS_PATH + symlink_name
    if not os.path.exists(directory):
        os.makedirs(directory)
    create_symlink(directory, symlink_name)




#---------------------------- Main Program -----------------------------------


print("\n---------------- Video Project Generator ----------------\n")

print("  Project Name: [" + PROJECT_NAME + "]")
print("  Videos Path:  [" + PROJECT_VIDEOS_PATH + "]\n")


# Creating the list of video clip files.

videos_filenames = vu.get_list_of_videos_filenames_of(PROJECT_VIDEOS_PATH)
clips_filenames_str = "videos_clips = [\n"

for video_filename in videos_filenames:
    video_filename = video_filename.replace(PROJECT_VIDEOS_PATH, "videos/")
    clips_filenames_str += '               ["'+video_filename+'", "00:00:00", "00:00:00"],\n'

clips_filenames_str += "               ]\n"



# Creating the project filename template.
f = open(PROJECT_VIDEO_TEMPLATE, "r")
template = f.read()
f.close()

template = template.replace("%PROJECT_NAME%", PROJECT_NAME)
template = template.replace("%LIST_OF_VIDEOS_CLIPS%", clips_filenames_str)


# Saving the project filename.
f = open(PROJECT_NAME+".py", "w")
f.write(template)
f.close()

os.system("chmod a+x " + PROJECT_NAME + ".py")


# Creating the folders and the symbolic links
create_symlink(PROJECT_VIDEOS_PATH, "videos")
create_folder_and_symlink("temp_clips")
create_folder_and_symlink("sounds")
create_folder_and_symlink("finals")
