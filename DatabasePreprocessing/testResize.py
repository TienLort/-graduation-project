from PIL import Image
import os


def resize_images_in_folder(folder_path, new_width, new_height):
    video_num = 0
    for filename in os.listdir(folder_path):
        video_num += 1
        print('Video {} is running ...'.format(video_num))
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_path = os.path.join(folder_path, filename)
            img = Image.open(file_path)
            resized_img = img.resize((new_width, new_height))
            resized_img.save(file_path)


# Thay đổi kích thước tất cả ảnh trong thư mục "my_folder" thành kích thước mới 300x300
folder_path = "E:\AI-PBL\PBL\ViT\dataset\dataset_final\\training_set\\REAL"
folder_path1 = "E:\AI-PBL\PBL\ViT\dataset\dataset_final\\training_set\\FAKE"
new_width = 224
new_height = 224
resize_images_in_folder(folder_path, new_width, new_height)
resize_images_in_folder(folder_path1, new_width, new_height)
