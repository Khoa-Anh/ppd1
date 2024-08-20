import cv2
import numpy as np
from flask import Flask, request, jsonify, send_file
from ultralytics import YOLO

app = Flask(__name__)

# Initialize the YOLO model
model = YOLO('../weights/best.pt')

# Dictionary to store information about detected objects
prediction_dict = {}

@app.route("/", methods=["GET"])
def index():
    return "Welcome to Object Detection API"

@app.route("/objectdetection/", methods=["POST"])
def detect_objects():
    try:
        if request.method != "POST":
            return {"error": "Invalid method"}

        if "image" not in request.files:
            return {"error": "No image in request"}

        image_file = request.files["image"]

        # Read the image using OpenCV
        image_bytes = image_file.read()
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        width = img.shape[1]
        height = img.shape[0]

        # Thực hiện nhận diện trên ảnh
        results = model(img, save=False, conf=0.35)

       # Xử lý kết quả và thêm vào prediction_dict
        prediction_dict = {}
        for result in results:
            obj_conf = result.boxes.conf.tolist()
            class_id = result.boxes.cls.tolist()
            bbox = result.boxes.xyxy.tolist()

            for i in range(len(bbox)):
                class_name = str(int(class_id[i]))
                x1, y1, x2, y2 = bbox[i]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Create a new entry in prediction_dict
                prediction_dict[i] = {
                    "class_name": class_name,
                    "bbox": [x1, y1, x2, y2]
                }

        # Trả về thông tin kích thước ảnh đã ghép cùng với kết quả nhận diện
        response = {
            "dimension": {
                "width": width,
                "height": height,
            },
            "results": prediction_dict
        }

        return jsonify(response)

    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)