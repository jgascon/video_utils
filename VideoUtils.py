
import os
import glob

CONCAT_LIST_FILENAME = ".TempConcatVideosList.txt"




def extract_video_clip(input_video_filename,
                       start_hhmmss_time,
                       end_hhmmss_time,
                       out_video_clip_filename):

    print ("extract_video_clip --> Input [" + input_video_filename + "]\n" +\
           "                       Start [" + start_hhmmss_time + "]\n" +\
	       "                         End [" + end_hhmmss_time + "]\n" +\
	       "                      Output [" + out_video_clip_filename + "]")

    command = "optirun ffmpeg -loglevel panic " +\
                           " -i " + input_video_filename +\
                           " -ss " + start_hhmmss_time +\
			               " -to " + end_hhmmss_time +\
			               " -vcodec copy -an -y " + out_video_clip_filename
    os.system(command)






def get_list_of_videos_filenames_of(path):
    myPath = path
    if myPath[-1] != "/":
        myPath += "/"

    list_of_video_filenames = []
    # TODO: Put more video file extensions
    for fileName in glob.glob(myPath + '*.mp4'):
        list_of_video_filenames += [fileName]

    list_of_video_filenames.sort()
    #~ for fileName in list_of_video_filenames:
        #~ print("     " + fileName)
    return list_of_video_filenames






def concatenate_videos(input_list_videos_filenames,
                       out_video_filename):

    # Creating a list of videos (needed for the ffmpeg command)
    f = open(CONCAT_LIST_FILENAME, "w")
    for video_filename in input_list_videos_filenames:
        f.write("file '" + video_filename + "'\n");
    f.close()

    command = "optirun ffmpeg -loglevel panic " +\
                            " -f concat -i " + CONCAT_LIST_FILENAME +\
                            " -c copy -y " + out_video_filename
    os.system(command)
    os.remove(CONCAT_LIST_FILENAME)






def insert_audio_to_video(input_no_sound_video_filename,
                          input_audio_filename,
                          out_video_filename):

    command = "optirun ffmpeg -loglevel panic " +\
                            " -i " + input_no_sound_video_filename +\
                            " -i " + input_audio_filename +\
                            " -codec copy -shortest -y " + out_video_filename
    os.system(command)
