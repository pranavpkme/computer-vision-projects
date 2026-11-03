import cv2
import matplotlib.pyplot as plt

photo = cv2.imread("../images/sample.jpg")

if photo is None:
    print("Image not found.")
    exit()

height, width, channels = photo.shape

pixel_count = height * width

print(f"\nImage Information")
print("-" * 20)
print(f"Height: {height}")
print(f"Width: {width}")
print(f"Channels: {channels}")
print(f"Pixel Count: {pixel_count}")

photo_rgb = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
photo_gray = cv2.cvtColor( photo, cv2.COLOR_BGR2GRAY)
photo_blur = cv2.GaussianBlur(photo_gray, (5,5),0)
photo_edge = cv2.Canny(photo_blur, 50, 150)

cv2.imwrite("../images/outputs/gray_dog.jpg", photo_gray)
cv2.imwrite("../images/outputs/blur_dog.jpg", photo_blur)
cv2.imwrite("../images/outputs/edge_dog.jpg", photo_edge)

plt.figure(figsize=(12,10))

plt.subplot(2,2,1)
plt.imshow(photo_rgb)
plt.title("Original Photo")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(photo_gray, cmap="gray")
plt.title("Grayscale Photo")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(photo_blur, cmap="gray")
plt.title("Blurred Photo")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(photo_edge, cmap="gray")
plt.title("Canny Edge Detection")
plt.axis("off")

plt.savefig("../images/outputs/final_comparision.png", bbox_inches="tight")
plt.show()

print("\nProcessing Complete.")
print("Images saved to results folder.")