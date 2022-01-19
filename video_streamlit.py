import streamlit as st
import numpy as np
import cv2

st.title("""
# Video Display 
""")
st.write("""
- Accesses the user's webcam and displays the video feed in the browser.
- Click the "Capture Frame" button to grab the current video frame and
return it to Streamlit.
""")
captured_image = webcam()
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(captured_image)
# switch = st.select_slider("Video",options=["OFF","ON"],value="OFF")
# position = st.empty()
# if switch=="ON":
#     vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#     while(True):
#         _, frame = vid.read()
#         frame = np.array(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
#         position.image([frame])
