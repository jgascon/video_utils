#!/usr/bin/python

import os
import sys
import VideoUtils as vu


PROJECT_NAME = sys.argv[1]
PROJECT_VIDEOS_PATH = sys.argv[2]
PROJECT_VIDEO_TEMPLATE = "_video_project_template.py_"


print("\n---------------- Video Project Generator ----------------\n")

print("  Project Name: [" + PROJECT_NAME + "]")
print("  Videos Path:  [" + PROJECT_VIDEOS_PATH + "]\n")


# Creating the list of video clip files.

videos_filenames = vu.get_list_of_videos_filenames_of(PROJECT_VIDEOS_PATH)
clips_filenames_str = "videos_clips = [\n"

#~ print(" Videos Found: ")

for video_filename in videos_filenames:
    video_filename = video_filename.replace(PROJECT_VIDEOS_PATH, "videos")
    #~ print("    " + video_filename)
    clips_filenames_str += '                ["'+video_filename+'", "00:00:00", "00:00:00"],\n'
    #~ clips_filenames += [[]]

clips_filenames_str += "               ]\n"

#~ print("")


#~ for clip_filename in clips_filenames:
    #~ print("    ", clip_filename)

#~ print("")



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
