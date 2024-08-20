# Python In-built packages
from ultralytics import YOLO
import streamlit as st
import cv2
import numpy as np

# Initialize the YOLO model
model = YOLO('../weights/best.pt')

# Dictionary to store information about detected objects
prediction_dict = {}

# Set page configuration
st.set_page_config(
    page_title="Object Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.header("Object Detection")

# Sidebar
st.sidebar.header("Model Config")

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 25, 100, 50)) / 100
st.sidebar.header("Image Config")

# Image selection
source_img = st.sidebar.file_uploader(
    "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
col1, col2 = st.columns(2)

if source_img is not None:
    # Read the image using OpenCV
    file_bytes = np.asarray(bytearray(source_img.read()), dtype=np.uint8)
    uploaded_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Resize the image
    short_side = 1200
    height, width, _ = uploaded_image.shape
    if height < width:
        new_width = short_side
        new_height = int(height * (short_side / width))
    else:
        new_height = short_side
        new_width = int(width * (short_side / height))
    resized_image = cv2.resize(uploaded_image, (new_width, new_height))

    # Convert color space to RGB
    resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    # Display uploaded image in column 1
    col1.image(resized_image_rgb, caption="Uploaded Image", use_column_width=True)

    if st.sidebar.button('Detect Objects'):
        # Detect objects in the uploaded image
        results = model.predict(resized_image, iou=0.8, conf=confidence)

        # Process the results and add to prediction_dict
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

                # Draw bounding box on the original image
                cv2.rectangle(resized_image_rgb, (x1, y1), (x2, y2), (0, 0, 0), 2)  # Black color for bounding box

                label = f'{prediction_dict[i]["class_name"]}'

                t_size = cv2.getTextSize(label, 0, fontScale=0.6, thickness=2)[0]

                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(resized_image_rgb, (x1, y1), c2, (0, 0, 0), -1, cv2.LINE_AA)
                cv2.putText(resized_image_rgb, label, (x1, y1 - 2), 0, 0.6, [255, 255, 255], thickness=1,
                            lineType=cv2.LINE_AA)

        # Display detected image in column 2
        col2.image(resized_image_rgb, caption='Detected Image', use_column_width=True)

        # Display detection results in an expander
        try:
            with st.expander("Detection Results", expanded=True):
                # Dictionary to store product counts
                product_counts = {}

                # Loop through items in prediction_dict
                for _, product_info in prediction_dict.items():
                    class_name = product_info["class_name"]
                    if class_name in product_counts:
                        product_counts[class_name]["Quantity"] += 1
                    else:
                        product_counts[class_name] = {
                            "Class Name": class_name,
                            "Quantity": 1
                        }

                # Display information about products and their quantities
                for product_info in product_counts.values():
                    st.write("Class Name:", product_info["Class Name"])
                    st.write("Quantity:", product_info["Quantity"])
                    st.write()

        except Exception as ex:
            st.write("No image is uploaded yet!")

# Hide Streamlit style
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
