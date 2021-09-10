import streamlit as st
import numpy as np
import cv2

st.write("""
# Video Display 
""")

switch = st.select_slider("Video",options=["OFF","ON"],value="OFF")
position = st.empty()
if switch=="ON":
    vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while(True):
        _, frame = vid.read()
        position.image(frame)