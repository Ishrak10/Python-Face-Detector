Python-Face-Detector
A python application that detects human faces in front of the web cam.

Libraries used :
- OpenCV

Classifier : haarCascade_frontalFace classifier from openCV

Working:
1. Webcam clicks an image.
2. Image is converted to greyscale image
3. Classifier is applied onto the image which gives 4 rectangular coordinates.
4. Using those coordinates, a rectangle is made around the faces.
5, Finally, the image is shown with highlighted faces.
