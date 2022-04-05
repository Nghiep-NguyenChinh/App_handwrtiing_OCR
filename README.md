# App_handwrtiing_OCR
[Web_app](https://share.streamlit.io/nghiep-nguyenchinh/app_handwrtiing_ocr/main/App_ocr.py)

Đây là giao diện deploy của hệ thống tạo chữ viết tay tiếng Việt. Giao diện được viết 
bằng [Streamlit](https://streamlit.io/) một thư viện mở hỗ trợ deploy các model AI và biểu diễn trực quan phân tích số liệu cho Data Analyst, Data Scientist

Giao diện của hệ thống:
<img src="https://..." alt="..." width="250" />


## Một vài kết quả hệ thống
1. Vietnames handwriting generator

2. Phần OCR cho hệ thống


#  Deploy Vietnamese handwriting generator

Hệ thóng được giao tiếp truyền nhận theo cơ chế server client:

+ Server colab được được xây đựng trên tunnel ngrok và flask api để truyền nhận dữ liệu. Khởi động server bằng cách chạy file [api_diffusion.ipynb]  (teammates_aNghia_OCR_backup/api/diffusion/api_diffusion.ipynb) 

+ client:Sử dụng Stremlit Library để thiết kế 1 giao diện đơn giản [https://share.streamlit.io/nghiep-nguyenchinh/app_handwrtiing_ocr/main/App_ocr.py]

Link github deploy: https://github.com/Nghiep-NguyenChinh/App_handwrtiing_OCR
