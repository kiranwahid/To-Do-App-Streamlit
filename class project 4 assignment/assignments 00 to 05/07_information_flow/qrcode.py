# 📦 For generating QR codes
import qrcode
# 📷 For decoding QR codes using computer vision
import cv2
import numpy as np
# 🖼️ For handling images
from PIL import Image
 # 🖥️ To display images in Jupyter
from IPython.display import display

# ✅ Function to generate a QR code and save it as an image
def generate_qr_code(data, filename = "qrcode.png"):
    qr = qrcode.QRCode(
        # QR version (size). 1 is 21x21 matrix
        version = 1 ,
         # Size of each box in pixels
        box_size= 10,
        # Thickness of the border (quiet zone)
        border= 5)
    # ➕ Add your data to QR
    qr.add_data(data)
      # 🔄 Auto fit size based on data
    qr.make(fit=True)
     # 🎨 Colors
    img = qr.make_image(fill_color = "green" , back_color = "white")
     # 💾 Save image file
    img.save(filename)
     # 👀 Display QR code (works in Jupyter)
    display(img)
    print(f"QR code saved as {filename}")

# ✅ Function to decode a QR code image
def decode_qr_code(filename):
    # 📷 Read the image using OpenCV
    img = cv2.imread(filename)
     # 🔍 Initialize QR code detector
    detector = cv2.QRCodeDetector()

    # 🔍 Decode the QR code (returns data, points, and straight_qrcode)
    data, _, _ = detector.detectAndDecode(img)
    
    # ✅ Check and display the decoded data
    if data:

      print(f"✅ Decoded data: {data} 🎉")
    else:
      print("❌ QR code could not be decoded.  🚫")

    # 🧪 Example usage:
    generate_qr_code("Successfully Generated🌍", "my_qr.code")
    decode_qr_code("my_qr.png")
