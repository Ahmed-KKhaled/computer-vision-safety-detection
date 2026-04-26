import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

model = YOLO("best.pt")

st.title("Construction Site Safety 🏗️🪖")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    img_array = np.array(image)

    results = model(img_array)

    annotated_img = None

    no_helmet_count = 0
    helmet_count = 0

    for r in results:
        annotated_img = r.plot()

        for box in r.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id].lower()

            if class_name == "no_helmet":
                no_helmet_count += 1

            if class_name == "helmet":
                helmet_count += 1

    st.image(annotated_img, caption="Detected Image", use_column_width=True)

    
    if no_helmet_count > 0:
        st.markdown(
            """
            <div style="
                background-color:#ffdddd;
                padding:20px;
                border-radius:10px;
                border:2px solid red;
                text-align:center;
            ">
            <h1 style="color:red;">❌ UNSAFE</h1>
            <h3>At least one person without helmet</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="
                background-color:#ddffdd;
                padding:20px;
                border-radius:10px;
                border:2px solid green;
                text-align:center;
            ">
            <h1 style="color:green;">✅ SAFE</h1>
            <h3>All detected persons have helmets</h3>
            </div>
            """,
            unsafe_allow_html=True
        )