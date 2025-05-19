import cv2

# Đọc ảnh mẫu test.jpg đặt cùng thư mục
img = cv2.imread("test.jpg")
if img is None:
    print("Không tìm thấy file test.jpg")
else:
    print("Kích thước ảnh:", img.shape)
    # Chuyển ảnh về grayscale và hiển thị
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
