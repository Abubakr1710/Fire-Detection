import streamlit as st
import cv2

st.title('Webcam Application')
run = st.checkbox('Run')
Frame_window = st.image([])
cam = cv2.VideoCapture(1)

while run:
    ret, frame = cam.read()
    Frame_window.image(frame)
else:
    st.write('Stopped')
