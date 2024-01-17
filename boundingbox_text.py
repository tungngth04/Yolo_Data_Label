import cv2
from tkinter import Tk, simpledialog
import os

image_folder = r"C:\Users\Administrator\OneDrive\Pictures\anh"

# Iterate over each file in the directory
for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)
    image = cv2.imread(image_path)
    while True:
     # Hiển thị ảnh và chờ người dùng chọn bounding box
        x,y,w,h = cv2.selectROI("Select Bounding Box", image, fromCenter=False, showCrosshair=True)

        # Nếu bounding box được chọn, vẽ nó lên ảnh và thêm vào danh sách
        if w > 0 and h > 0:
            text = simpledialog.askstring("Nhập văn bản", "Nhập nội dung:")

            cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.rectangle(image, (x,y), (x + w, y + h), (0, 255, 0), 2)
        #  'q' để kết thúc
        key = cv2.waitKey(0)
        if key == ord('q'):
            break

    cv2.imshow("Img with Bounding Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()