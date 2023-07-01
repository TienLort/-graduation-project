# graduation-project

Trong thư mục này là quá trình preprocessing dữ liệu.

- Bước 1: Clone repository về máy và di chuyển vào đó:  
  git clone https://github.com/TienLort/-graduation-project.git  
  cd -graduation-project
- Bước 2: Tải dữ liệu dataset.  
  https://www.kaggle.com/search?q=bdfdc
- Bước 3: Xử lý dữ liệu, chạy lần lượt :  
  python framing.py  
  python findfaceFR_folder.py  
  python delLastFile.py  
  python renameAll.py  
  python moveAll.py  
  python Resize.py
- Cấu trúc dataset cần được giống với dataset_sample để có thể sử dụng  
  Dữ liệu sau khi hoàn thành các bước trên có thể sử dụng để làm data đầu vào cho mô hình
- Nếu như không thực hiện các bước trên, bạn có thể sử dụng dataset đã được tôi tạo sẵn tại kaggle.json  
  Các bước sử dụng kaggle.json đã được thực hiện tại vit_deepfake_final.ipynb
  \*Upload vit_deepfake_final.ipynb lên colab và bật chế độ GPU tại colab để chạy mô hình
  các bước chạy mô hình trên colab được thực hiện từ trên xuống dưới
