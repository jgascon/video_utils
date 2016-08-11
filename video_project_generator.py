#!/usr/bin/python

import os
import sys
import VideoUtils as vu


PROJECT_NAME = sys.argv[1]
PROJECT_VIDEOS_PATH = sys.argv[2]


print "---------------- Video Project Generator ----------------\n"

print "  Project Name: [" + PROJECT_NAME + "]"
print "  Videos Path:  [" + PROJECT_VIDEOS_PATH + "]"


# Creating the list of files.
