import datetime
import os
import time
import cv2

start_time = time.time()


def remove_img(path,  img_name):
    os.remove(path + '/' + img_name)


file_path = 'E:\AI-PBL\PBL\ViT\dataset\\after\\test_set\\image'
file_lists = os.listdir(file_path)
video_num = 0
new_width = 224
new_height = 224
for file_list in file_lists:
    rename_path = os.path.join(file_path, file_list)
    rename_lists = os.listdir(rename_path)
    video_num += 1
    print('Video {} is running ...'.format(video_num))
    i = 0
    k = 0
    for rename_list in rename_lists:
        namelist = rename_list.split(".")
        if namelist[-1] == "jpg":
            new_filename = str(i) + "_1.jpg"
            old_filename = str(i) + "_0.jpg"
            img = cv2.imread(rename_path + "/" + old_filename)
            img_new = cv2.resize(src=img, dsize=(new_width, new_height))
            os.chdir(rename_path)
            cv2.imwrite(new_filename, img_new)
            i += 1

    for rename_list in rename_lists:
        namelist = rename_list.split(".")
        if namelist[-1] == "jpg":
            new_filename = str(k) + "_1.jpg"
            old_filename = str(k) + "_0.jpg"
            os.chdir(rename_path)
            remove_img(rename_path, old_filename)
            k += 1

end_time = time.time()
delta_time = datetime.timedelta(seconds=(end_time-start_time))
print('Running time : %s ' % (delta_time))
