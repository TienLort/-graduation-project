import csv
import os

input_path = 'E:\AI-PBL\PBL\ViT\dataset\\before\\test_set'
output_path = 'E:\AI-PBL\PBL\ViT\dataset'
if not os.path.exists(output_path):
    os.mkdir(output_path)
txt_path = output_path+'/dfdc_test_labels.csv'

videos = os.listdir(input_path)
videos.sort(key=lambda x: x[:-4])

with open(txt_path, 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["filename", "label"])
    if len(videos) != 0:
        video_num = 0
        for each_video in videos:
            t = str(each_video[11:15])
            writer = csv.writer(file)
            if(t == "REAL"):
                writer.writerow([each_video, "0"])
            else:
                writer.writerow([each_video, "1"])
    else:
        print('Empty Directory')
