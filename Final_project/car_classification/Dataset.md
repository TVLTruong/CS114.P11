[Truy cập Dataset đã được upload và public trên kaggle](https://www.kaggle.com/datasets/lamtruong1594/car-cs114)

[Access the Dataset that has been uploaded and published on kaggle](https://www.kaggle.com/datasets/lamtruong1594/car-cs114)

The dataset directory tree/Cây thư mục của dataset:

car-cs114  
├── CheckDuplicate                # Folder containing duplicate data / Thư mục chứa dữ liệu trùng lặp  
│   ├── CheckDuplicate_Train_1.csv   # Duplicate images in training set 1 / Thông tin các ảnh bị trùng trong tập train-1  
│   ├── CheckDuplicate_Train_2.csv   # Duplicate images in training set 2 / Thông tin các ảnh bị trùng trong tập train-2  
│   ├── CheckDuplicate_Train_3.csv   # Duplicate images in training set 3 / Thông tin các ảnh bị trùng trong tập train-3  
│   ├── CheckDuplicate_Train_4.csv   # Duplicate images in training set 4 / Thông tin các ảnh bị trùng trong tập train-4  
│   ├── CheckDuplicate_Train_5.csv   # Duplicate images in training set 5 / Thông tin các ảnh bị trùng trong tập train-5  
│   └── DuplicateDetectionResults.csv # Duplicate images across the entire dataset / Thông tin các ảnh bị trùng trong toàn bộ dataset  
├── Stat_dataset                  # Folder containing dataset statistics and analysis / Thư mục chứa thống kê và phân tích dữ liệu  
│   ├── CarDataset-1.csv             # Statistics of all images contributed by each student / Thống kê tất cả ảnh mỗi sinh viên đã đóng góp  
│   ├── CarDataset-2.csv             # Number of images contributed by students per car brand / Thống kê số lượng ảnh sinh viên đã đóng góp theo từng hãng xe  
│   └── InvalidNames.csv             # List of invalid names in the dataset / Danh sách các tên không hợp lệ trong dữ liệu  
├── car_split                    # Folder containing train/test split datasets / Thư mục chứa dữ liệu đã được chia để train và test  
│   └── car_split  
│       ├── CarDataset-Splits-1-Test.csv   # Test set for split 1 / Tập test 1  
│       ├── CarDataset-Splits-1-Train.csv  # Training set for split 1 / Tập train 1  
│       ├── CarDataset-Splits-2-Test.csv   # Test set for split 2 / Tập test 2  
│       ├── CarDataset-Splits-2-Train.csv  # Training set for split 2 / Tập train 2  
│       ├── CarDataset-Splits-3-Test.csv   # Test set for split 3 / Tập test 3  
│       ├── CarDataset-Splits-3-Train.csv  # Training set for split 3 / Tập train 3  
│       ├── CarDataset-Splits-4-Test.csv   # Test set for split 4 / Tập test 4  
│       ├── CarDataset-Splits-4-Train.csv  # Training set for split 4 / Tập train 4  
│       ├── CarDataset-Splits-5-Test.csv   # Test set for split 5 / Tập test 5  
│       ├── CarDataset-Splits-5-Train.csv  # Training set for split 5 / Tập train 5  
│       └── CarDataset.csv                 # Consolidated dataset after splitting / Bộ dữ liệu tổng hợp sau khi chia  
├── dataset                      # Folder containing car images categorized by brand / Thư mục chứa hình ảnh xe hơi theo từng hãng  
│   ├── Honda                        # Images of Honda cars / Hình ảnh xe của hãng Honda  
│   ├── Hyundai                      # Images of Hyundai cars / Hình ảnh xe của hãng Hyundai  
│   ├── KIA                          # Images of KIA cars / Hình ảnh xe của hãng KIA  
│   ├── Mazda                        # Images of Mazda cars / Hình ảnh xe của hãng Mazda  
│   ├── Mitsubishi                   # Images of Mitsubishi cars / Hình ảnh xe của hãng Mitsubishi  
│   ├── Others                       # Images of other car brands / Hình ảnh xe thuộc các hãng khác  
│   ├── Suzuki                       # Images of Suzuki cars / Hình ảnh xe của hãng Suzuki  
│   ├── Toyota                       # Images of Toyota cars / Hình ảnh xe của hãng Toyota  
│   └── VinFast                      # Images of VinFast cars / Hình ảnh xe của hãng VinFast  
└── ImageErrors.csv             # List of images that cannot be read by PIL or OpenCV / Danh sách các hình ảnh không đọc được thông qua thư viện PIL và cv2  

