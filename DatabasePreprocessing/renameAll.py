import datetime
import os
import time

start_time = time.time()

file_path = 'E:\AI-PBL\PBL\ViT\dataset\\after\\test_set\\image_test'
file_lists = os.listdir(file_path)
for file_list in file_lists:
    rename_path = os.path.join(file_path, file_list)
    rename_lists = os.listdir(rename_path)
    i = 0
    for rename_list in rename_lists:
        namelist = rename_list.split(".")
        if namelist[-1] == "jpg":
            (filename, extension) = os.path.splitext(rename_list)
            new_filename = str(i) + "_0"
            old_file = rename_path+'/' + rename_list
            new_file = rename_path+'/' + new_filename + extension
            os.rename(old_file, new_file)
            i += 1

end_time = time.time()
delta_time = datetime.timedelta(seconds=(end_time-start_time))
print('Running time : %s ' % (delta_time))

# rename 38970 images output
# Running time : 0:00:39.003402
