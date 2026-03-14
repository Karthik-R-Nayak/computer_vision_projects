# Real-Time Color Detection using OpenCV

##  Project Description
This project uses **Python**, **OpenCV**, and **NumPy** to detect specific colors (**white, blue, and red**) in real-time using a webcam.
The program captures video frames from the camera, converts them to **HSV color space**, and applies **color masks** to isolate the selected colors.
Contours are drawn around detected **white objects**, and separate windows display the detected color regions.

## 🎯 Features

* Real-time webcam video processing
* Detection of:

  * White objects
  * Blue objects
  * Red objects
* Contour detection for white objects
* Multiple output display windows
* Simple and beginner-friendly computer vision implementation

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **NumPy**

Optional library included:

* `face_recognition` (currently not used in the code)

## 📦 Requirements

Install the required libraries before running the project.
pip install opencv-python numpy face-recognition

## ▶️ How to Run

1. Clone the repository
git clone https://github.com/yourusername/color-detection-opencv.git

2. Navigate to the project folder
cd color-detection-opencv

3. Run the script
python color_detection.py

## 🖥️ Output Windows

The program displays four windows:

| Window Name | Description                        |
| ----------- | ---------------------------------- |
| `video`     | Original webcam feed with contours |
| `white`     | Only detected white objects        |
| `b`         | Only detected blue objects         |
| `r`         | Only detected red objects          |


## ⌨️ Controls

Press **`D`** on the keyboard to stop the program.

---

## 📂 Project Structure

```
color-detection-opencv
│
├── color_detection.py
├── README.md
```

---

## ⚙️ How It Works

1. Capture frames from the webcam.
2. Convert the frame from **BGR to HSV color space**.
3. Apply color masks to detect specific colors.
4. Use **bitwise operations** to isolate detected regions.
5. Detect contours for white objects.
6. Display the processed frames.
   
## 🚀 Future Improvements
* Detect more colors
* Use bounding boxes instead of contours

## 👨‍💻 Author
https://github.com/Karthik-R-Nayak
Developed as a **Computer Vision practice project using OpenCV**.

