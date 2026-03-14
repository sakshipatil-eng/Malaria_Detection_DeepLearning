import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

st.title("🦠 Malaria Detection using Deep Learning")

@st.cache_resource
def load_ml_model():
    return load_model("malaria_model.h5")

model = load_ml_model()

uploaded_file = st.file_uploader("Upload Cell Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    
    img = Image.open(uploaded_file).convert("RGB").resize((224,224))
    st.image(img, caption="Uploaded Image", width=300)

    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    score = prediction[0][0]

    st.write("Prediction Score:", score)

    if score < 0.5:
        st.error("🦠 Parasitized (Malaria Infected)")
    else:
        st.success("✅ Uninfected (Healthy)")
