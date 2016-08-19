
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





def extract_videos_clips(input_list_videos,
                         out_video_clip_filename):
    count_i = 0
    out_videos_clips_filenames = []

    for input_video_slot in input_list_videos:
        video_name = input_video_slot[0]
        video_start = input_video_slot[1]
        video_end = input_video_slot[2]

        count_s = str(count_i)
        while len(count_s) < 3:
            count_s = "0" + count_s

        count_s = count_s + "0"

        out_this_clip_filename = out_video_clip_filename
        out_this_clip_filename = out_this_clip_filename.replace("%NUMERATION%", count_s)
        out_this_clip_filename = out_this_clip_filename.replace("%INPUT_FILENAME%",
                                                                video_name.replace("videos/", ""))
        extract_video_clip(video_name,
                           video_start,
                           video_end,
                           out_this_clip_filename)
        out_videos_clips_filenames += [out_this_clip_filename]
        count_i += 1
    return out_videos_clips_filenames





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

    print ("concatenate_videos --> joining " + str(len(input_list_videos_filenames)) + " videos.\n")

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
