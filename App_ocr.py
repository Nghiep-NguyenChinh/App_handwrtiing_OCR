import streamlit as st
from requests import *
import json
import uuid
import threading
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO
import time

URL = "http://2703-34-90-220-141.ngrok.io"

st.markdown("<h1 style='text-align: center;'>HAND WRITTING OCR </h1>", unsafe_allow_html=True)


def display_app_header(main_txt, sub_txt, is_sidebar=False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#2596be; text_align:center; font-weight: bold;"> {main_txt} </h2>
    <p style = "color:#00ff6f; text_align:center;"> {sub_txt} </p>
    </div>
    """
    st.balloons()
    if is_sidebar:

        st.sidebar.markdown(html_temp, unsafe_allow_html=True)
    else:
        st.markdown(html_temp, unsafe_allow_html=True)


main_txt = "NHÓM THỰC HIỆN  "
sub_txt = "Aicamp batch 5"
display_app_header(main_txt, sub_txt, is_sidebar=True)


add_selectbox = st.sidebar.markdown(
    """
|Mentor   | Huỳnh Trung Nghĩa  |
|:-------:|:------------------:|
| Mentees |Huỳnh Việt Cường       |
|         |Nguyễn Thị Tình |
|         |Nguyễn Chính Nghiệp |
"""
            
            , unsafe_allow_html=True)

################################################################
###  FUNTION 
################################################################

def convertImgToBase64(img_path):
    with open(img_path, 'rb') as f:
        data = base64.b64encode(f.read())
    # print(",<<<<<<<<<<", data)
    return data
        



################################################################
# Text Input

# name = st.text_input("Create a handwritten image from a text", "Type here")
# if st.button("Send "):
#     result = name
#     st.success(result)
#     r = post(url=f"{URL}/", data={ 'data':f"{result}"})
#     a = json.loads(r.text)
#     imgdata = base64.b64decode(a["image"])
#     filename = BytesIO(imgdata)
#     img = Image.open(filename)
#     # st.image(img, width=400, caption="Image")
#     st.image(img, caption="Image")
#     st.write("\n ok ")

# Text area
message = st.text_area("Create a handwritten image from a text", "Type here")
if st.button("Send"):
    result = message
    # st.success(result)
    # st.info('This is a purely informational message')y
    # my_bar = st.progress(0)
    # for percent_complete in range(1000):
    #      time.sleep(0.1)
    #      my_bar.progress(percent_complete + 1)

    r = post(url=f"{URL}/", data={ 'data':f"{result}"})
    a = json.loads(r.text)
    imgdata = base64.b64decode(a["image"])
    filename = BytesIO(imgdata)
    img = Image.open(filename)
    # st.image(img, width=400, caption="Image")
    st.image(img, caption="Image")
    st.write("\n  ")

 # upload file image for OCR
st.write("\n ")
image_file = st.file_uploader("Upload image OCR",type=['jpg','png','JPEG'])

try:
    image_file_ = Image.open(image_file)
    st.image(image_file_, "Ảnh tải lên")
except: pass

option = st.selectbox(
     'Do you use the OCR model for handwriting or typewriter?',
     ('Typewriter','Handwriting'))

st.write('You selected:', option)

search_image_btn = st.button("Send image")
if search_image_btn:

    if option =='Typewriter':
        r = post(url=f'{URL}/ocr_type/', data={'data':convertImgToBase64(image_file.name)})
        result_image = json.loads(r.text)
        st.success(result_image['text'])

    elif option == 'Handwriting':
        r = post(url=f'{URL}/ocr_hw/', data={'data':convertImgToBase64(image_file.name)})
        result_image = json.loads(r.text)
        st.success(result_image['text'])

    # elif image_file== None: st.error("Something is wrong!!!!!")



