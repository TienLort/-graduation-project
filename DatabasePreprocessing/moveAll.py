import datetime
import os
import time
import shutil
start_time = time.time()

file_path = 'E:\AI-PBL\PBL\ViT\dataset\\after\\validation_set\\image'
file_goal = 'E:\AI-PBL\PBL\ViT\dataset\\after\\validation_set'
file_lists = os.listdir(file_path)
video_num = 0
for file_list in file_lists:
    print('Video {} is running ...'.format(video_num))
    video_num += 1
    rename_path = os.path.join(file_path, file_list)
    rename_lists = os.listdir(rename_path)
    i = 0
    nameLabel = file_list.split("_")
    for rename_list in rename_lists:
        if i == 10:
            break
        namelist = rename_list.split(".")
        if namelist[-1] == "jpg":
            (filename, extension) = os.path.splitext(rename_list)
            new_filename = file_list + "_" + str(i)
            old_file = rename_path+'/' + rename_list
            new_file = file_goal+'/' + \
                nameLabel[-1] + "/" + new_filename + extension
            shutil.copy(old_file, new_file)
            i += 1

end_time = time.time()
delta_time = datetime.timedelta(seconds=(end_time-start_time))
print('Running time : %s ' % (delta_time))

# rename 38970 images output
# Running time : 0:00:39.003402
