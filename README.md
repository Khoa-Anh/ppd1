# [AI] PPD1 - Tài liệu hướng dẫn

# I. Giới thiệu

- API này cho phép các nhà phát triển tích hợp khả năng nhận diện các sản phẩm khuyến mãi của Listerine (Johnson & Johnson).

# II. Các dạng sản phẩm khuyến mãi

### ListerineCoolMint750x2

- Hai chai ListerineCoolMint750 có gắn nhãn đỏ
    
    ![Untitled](images/Untitled.png)
    

### Sản phẩm khuyến mãi chai lớn kèm chai nhỏ

- Hầu hết các trường hợp chai lớn đặt phía sau chai nhỏ ở trên kệ đều là các sản phẩm khuyến mãi (mô hình sẽ phân biệt nhóm chai được xếp như vậy).
    
    ![Untitled](images/Untitled%201.png)
    

### Sản phẩm khuyến mãi có đính kèm nhãn khuyến mãi:

- Để nhận diện chính xác, với mỗi trường hợp cụ thể cần có dữ liệu tương ứng
    
    ![Untitled](images/Untitled%202.png)
    
    ![Untitled](images/Untitled%203.png)
    

### Sản phẩm khuyến mãi kèm quà tặng

- Để nhận diện chính xác, với mỗi trường hợp cụ thể cần có dữ liệu tương ứng
    
    ![Untitled](images/Untitled%204.png)
    

# III. Các khuyến nghị cho hình ảnh đầu vào để cho kết quả dự đoán tốt

- **Độ phân giải tối thiểu**: Để nhận diện dãy sản phẩm trên kệ một cách chính xác, độ phân giải tối thiểu nên đủ lớn để hiển thị chi tiết của sản phẩm và kệ. Điều này bao gồm đặc điểm quan trọng như vị trí và hình dạng của sản phẩm, các nhãn, và các chi tiết quan trọng khác. Không có một con số cụ thể cho độ phân giải tối thiểu của hình ảnh, tuy nhiên dựa vào kinh nghiệm thực tế, đề xuất hình ảnh đầu vào (dạng .jpg hoặc .png) nên có kích thước cạnh ngắn tối thiểu >800px.
- **Khoảng cách và góc nhìn**: Nếu sản phẩm nằm ở khoảng cách xa và nghiêng đối với máy ảnh, bạn có thể cần kích thước lớn hơn để đảm bảo nhận diện chính xác. Để đảm bảo chất lượng nhận diện, khuyến nghị khi chụp hình sản phẩm, mặt phẳng camera phải song song với mặt phẳng dãy kệ.

![Góc chụp không được khuyến nghị](images/SOS_14.jpg)

Góc chụp không được khuyến nghị

![Góc chụp khuyến nghị](images/SOS_250_-_Copy.jpg)

Góc chụp khuyến nghị

- **Ánh sáng đầy đủ**: Hãy đảm bảo rằng khu vực bạn chụp ảnh có đủ ánh sáng. Ánh sáng tốt giúp tạo ra hình ảnh sắc nét và giảm thiểu sự mờ hoặc nhiễu.

![Hình chụp không được khuyến nghị: chất lượng ánh sáng không tốt](images/Untitled.jpeg)

Hình chụp không được khuyến nghị: chất lượng ánh sáng không tốt

![Untitled](images/Untitled%201.jpeg)

Hình chụp được khuyến nghị: ánh sáng đầy đủ

- **Chất lượng ổn định**: Đảm bảo rằng máy ảnh ổn định và không rung lắc trong quá trình chụp.

![Hình chụp không được khuyến nghị: ảnh mờ nhòe](images/Untitled%202.jpeg)

Hình chụp không được khuyến nghị: ảnh mờ nhòe

![Hình chụp khuyến nghị: ảnh đủ rõ nét](images/Untitled%203.jpeg)

Hình chụp khuyến nghị: ảnh đủ rõ nét

- **Tránh bóng đổ hoặc ánh sáng chói**: Hạn chế bóng đổ hoặc ánh sáng chói trực tiếp lên sản phẩm hoặc kệ. Bóng đổ có thể làm mất thông tin quan trọng trên sản phẩm.

![Hình chụp không được khuyến nghị: sản phẩm bị chói làm mất thông tin](images/Untitled%204.jpeg)

Hình chụp không được khuyến nghị: sản phẩm bị chói làm mất thông tin

![Hình chụp khuyến nghị: sản phẩm bị chói nhưng vẫn giữ được thông tin](images/Untitled%205.jpeg)

Hình chụp khuyến nghị: sản phẩm bị chói nhưng vẫn giữ được thông tin

- **Vật thể bị che lấp**: Nhận diện các vật thể nằm sau vật thể khác luôn là thách thức với các mô hình thị giác máy tính. Nếu vật thể bị thiếu thông tin và không có các đặc điểm rõ ràng, mô hình sẽ khó phân biệt. Tuy nhiên không có gì cần khuyến nghị ở đây, điều này chỉ ra rằng các mô hình thường sẽ nhận diện tốt với lớp đầu tiên trên dãy kệ, và bỏ qua các lớp đằng sau.

![Vật thể bị che lấp nhưng vẫn đủ thông tin để phân biệt](images/Untitled%206.jpeg)

Vật thể bị che lấp nhưng vẫn đủ thông tin để phân biệt

![Mô hình chỉ nhận diện được các vật thể ở lớp đầu tiên](images/Untitled%207.jpeg)

Mô hình chỉ nhận diện được các vật thể ở lớp đầu tiên

# IV. Hướng dẫn Sử Dụng API Nhận Diện Sản Phẩm

## 1**. Dữ liệu đầu vào**

- Gửi yêu cầu với một hoặc nhiều ảnh đầu vào dưới dạng jpg hoặc png, key là `image`.

## 2 **Cách gửi yêu cầu**

- Để gửi yêu cầu đến API, sử dụng phương thức POST và truy cập endpoint **`http://izmthxfxxc.ap-southeast-1.awsapprunner.com/objectdetection/`**
- Ví dụ:

```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "image=@đường/dẫn/tới/hình/ảnh1.jpg" -F "image=@đường/dẫn/tới/hình/ảnh2.jpg" http://**izmthxfxxc.ap-southeast-1.awsapprunner.com**/objectdetection/
```

- Đảm bảo có các file ảnh thích hợp (**`image1.jpg`** và **`image2.jpg`**).

## 4**. Dữ Liệu Đầu Ra**

Dữ liệu đầu ra sẽ được trả về dưới định dạng JSON và bao gồm thông tin chi tiết về các đối tượng được nhận diện, bao gồm tên lớp, độ chắc chắn, và vị trí bbox.

API sẽ trả về một dictionary chứa thông tin về các đối tượng đã nhận diện. Mỗi đối tượng được đánh số thứ tự và có chứa các thông tin sau:

- "bbox": Tọa độ bounding box của đối tượng.
- "class_name": Tên của đối tượng (sản phẩm), với sản phẩm Listerine, số cuối mã là dung tích sản phẩm tính theo ml.
- "confidence": Độ tin cậy của nhận diện.

```python
{
    "dimension": {
        "height": [
            1500
        ],
        "width": [
            1500
        ]
    },
    "results": {
        "0": {
            "bbox": [
                1003,
                968,
                1392,
                1499
            ],
            "class_name": "0",
            "confidence": 0.97,
        }
	}
}

```

**Coco Format:**

*[x_min, y_min, width, height]*

**Pascal_VOC Format:**

*[x_min, y_min, x_max, y_max]*

---

## Hướng dẫn chạy chương trình trên local

**Cài Virtualenv**

```
pip install virtualenv

```

**Tạo môi trường ảo**

- Mở terminal và di chuyển đến thư mục dự án. Sau đó, sử dụng lệnh sau để tạo một môi trường ảo mới (thay `myenv` bằng tên muốn đặt cho môi trường ảo):

```
python -m venv myenv

```

**Kích hoạt môi trường ảo**

- Trên Linux/macOS:

```
source myenv/bin/activate

```

- Trên Windows (PowerShell)

```
.\\myenv\\Scripts\\Activate.ps1

```

- Trên Windows (Command Prompt):

```
.\\myenv\\Scripts\\activate

```

- **Cài các thư viện trong** requirements.txt

```
pip install -r requirements.txt

```

- Chạy chương trình:

```
streamlit run app.py
```

**Thoát khỏi môi trường ảo**

```
deactivate

```

---

### 1. **Mô hình YOLO (You Only Look Once) để phát hiện đối tượng**

- **YOLO** là một mô hình học sâu dùng để phát hiện đối tượng theo thời gian thực. YOLO dự đoán các hộp giới hạn (bounding boxes) và xác suất phân lớp cho nhiều đối tượng trong một lần xử lý của mạng nơ-ron.
- Mô hình được khởi tạo bằng dòng lệnh:
    
    ```python
    model = YOLO('../weights/best.pt')
    
    ```
    
    Ở đây, `best.pt` là tệp mô hình đã được huấn luyện trước, được dùng để phát hiện đối tượng. YOLO sử dụng một mạng nơ-ron duy nhất để phát hiện, giúp nó nhanh hơn so với các phương pháp dựa trên vùng như Faster R-CNN.
    
- YOLO thực hiện **hồi quy hộp giới hạn** và **dự đoán phân lớp** đồng thời cho các đối tượng trong ảnh, dựa trên các đặc trưng được trích xuất từ ảnh.
- Quá trình phát hiện đối tượng được kích hoạt bằng:
    
    ```python
    results = model.predict(resized_image, iou=0.8, conf=confidence)
    ```
    
    Ở đây, phương thức `predict` nhận một hình ảnh và áp dụng phát hiện đối tượng với hai tham số chính:
    
    - **IoU (Intersection over Union):** Ngưỡng để xác định mức độ trùng lặp giữa các hộp giới hạn. Chỉ giữ lại các dự đoán có IoU lớn hơn `0.8`.
    - **Confidence (Độ tin cậy):** Ngưỡng (được điều chỉnh qua thanh trượt trong thanh bên của Streamlit) xác định liệu một đối tượng được phát hiện có đủ tin cậy để giữ lại hay không.

### 2. **Streamlit cho giao diện web**

- **Streamlit** được sử dụng để tạo giao diện web đơn giản và tương tác, nơi người dùng có thể tải lên hình ảnh và cấu hình các thiết lập của mô hình như độ tin cậy.
- Các thành phần chính được Streamlit xử lý:
    - **Tải lên hình ảnh:**
        
        ```python
        source_img = st.sidebar.file_uploader("Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
        ```
        
        Điều này cho phép người dùng tải lên các hình ảnh thuộc nhiều định dạng khác nhau để phát hiện đối tượng.
        
    - **Thanh trượt độ tin cậy (Confidence slider):**
        
        ```python
        confidence = float(st.sidebar.slider("Select Model Confidence", 25, 100, 50)) / 100
        ```
        
        Thanh trượt này cho phép người dùng thiết lập ngưỡng độ tin cậy của mô hình khi phát hiện đối tượng. Ngưỡng thấp phát hiện nhiều đối tượng hơn nhưng ít chính xác hơn, trong khi ngưỡng cao đảm bảo các đối tượng được phát hiện có độ chính xác cao hơn.
        
- **Bố cục cột để hiển thị hình ảnh:** Giao diện sử dụng hai cột:
    - `col1` để hiển thị hình ảnh đã tải lên.
    - `col2` để hiển thị hình ảnh với các hộp giới hạn đã phát hiện.

### 3. **OpenCV để xử lý hình ảnh**

- **OpenCV** (Thư viện Thị giác Máy tính Mã nguồn Mở) được sử dụng cho các tác vụ xử lý hình ảnh khác nhau, chẳng hạn như đọc, thay đổi kích thước và vẽ các hộp giới hạn quanh các đối tượng được phát hiện:
    - **Đọc hình ảnh đã tải lên:**
        
        ```python
        uploaded_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        ```
        
        Điều này giúp giải mã hình ảnh được người dùng tải lên.
        
    - **Thay đổi kích thước hình ảnh:**
        
        ```python
        resized_image = cv2.resize(uploaded_image, (new_width, new_height))
        ```
        
        Hình ảnh được thay đổi kích thước để đảm bảo phù hợp với trang và giữ nguyên tỷ lệ ban đầu.
        
    - **Vẽ hộp giới hạn:** Các đối tượng được phát hiện được đánh dấu bằng hộp giới hạn, và tên lớp đối tượng được hiển thị trên ảnh:
        
        ```python
        cv2.rectangle(resized_image_rgb, (x1, y1), (x2, y2), (0, 0, 0), 2)  # Hộp giới hạn màu đen
        cv2.putText(resized_image_rgb, label, (x1, y1 - 2), 0, 0.6, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
        ```
        
        Tọa độ của hộp giới hạn được lấy từ kết quả dự đoán, và các hàm `rectangle` và `putText` của OpenCV được sử dụng để vẽ chúng trên ảnh.
        

### 4. **Xử lý kết quả phát hiện đối tượng**

- **Dữ liệu hộp giới hạn** được trích xuất từ các dự đoán của mô hình YOLO và được lưu trữ trong dictionary `prediction_dict`:
    
    ```python
    prediction_dict[i] = {
        "class_name": class_name,
        "bbox": [x1, y1, x2, y2]
    }
    ```
    
    Mỗi mục trong dictionary chứa tên lớp đối tượng và tọa độ của hộp giới hạn (`x1`, `y1`, `x2`, `y2`).
    
- **Hiển thị kết quả:** Các đối tượng được phát hiện và số lượng của chúng được hiển thị trong một mục mở rộng bằng tính năng `expander` của Streamlit:
    
    ```python
    with st.expander("Detection Results", expanded=True):
        st.write("Class Name:", product_info["Class Name"])
        st.write("Quantity:", product_info["Quantity"])
    ```
    

### 5. **Tiền xử lý hình ảnh**

- Trước khi đưa ảnh vào mô hình YOLO, ảnh được thay đổi kích thước để đảm bảo kích thước phù hợp và tối ưu cho quá trình phát hiện:Việc thay đổi kích thước này được thực hiện theo tỷ lệ, giúp duy trì tỷ lệ kích thước của các đối tượng trong ảnh.
    
    ```python
    resized_image = cv2.resize(uploaded_image, (new_width, new_height))
    ```
    