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
import gdown

def download_url():
    
    gdown.download(id="1I4UoTQY_ypVlg1zRfihybaIwCdKm-Xvu", output="url.txt")
    with open("url.txt", "r") as bf:
        
        URL = bf.read()
        return URL.strip('/')

URL = str(download_url())



# URL = "http://70b9-35-188-186-113.ngrok.io"


print(URL)

st.markdown("<h1 style='text-align: center;'>HANDWRITING GENERATION </h1>", unsafe_allow_html=True)  


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
    return data
        

# input image from uploadfile
def convertImgToBase64_ascii(image):
    return base64.encodebytes(image.getvalue()).decode('ascii')

def convertImgToBase64_image(image_file):
    data = base64.encodebytes(image_file.getvalue())
    return data

################################################################


# Text area
message = st.text_area("Create a handwritten image from a text", "Type here")
# add style
image_style  = st.file_uploader("Upload image for style ",type=['jpg','png','JPEG'])
try:
    image_style_ = Image.open(image_style)
    st.image(image_style_, "Ảnh tải lên")
except: pass
if st.button("Send"):
    st.balloons()
    result = message
    if  image_style is not None :
        r = post(url=f"{URL}/", data={ 'data':f"{result}", 'imgsource' : convertImgToBase64_ascii(image_style)})
        # r = post(url=f"{URL}/", data={ 'data':f"{result}", 'imgsource' : base64.encodebytes(image_style.getvalue()).decode('ascii')})
    else: r = post(url=f"{URL}/", data={ 'data':f"{result}"})
    a = json.loads(r.text)
    imgdata = base64.b64decode(a["image"])
    filename = BytesIO(imgdata)
    img = Image.open(filename)
    # st.image(img, width=400, caption="Image")
    st.image(img, caption="Image")
    st.write("\n  ")








 # upload file image for OCR
st.write("\n ")
st.write("-------------------------------------------------------")
st.markdown("<h1 style='text-align: center;'> OCR </h1>", unsafe_allow_html=True)
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
    st.balloons()
    if option =='Typewriter':
        # r = post(url=f'{URL}/ocr_type/', data={'data':convertImgToBase64(image_file.name)})
        r = post(url=f'{URL}/ocr_type/', data={'data':convertImgToBase64_image(image_file)})
        result_image = json.loads(r.text)
        st.success(result_image['text'])

    elif option == 'Handwriting':
        r = post(url=f'{URL}/ocr_hw/', data={'data':convertImgToBase64_image(image_file)})
        result_image = json.loads(r.text)
        st.success(result_image['text'])

    # elif image_file== None: st.error("Something is wrong!!!!!")

