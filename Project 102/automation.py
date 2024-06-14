import cv2
import dropbox

access_token = "Enter access token"
dbx = dropbox

def __captureImage__ ():
    videoCapture = cv2.VideoCapture (0)
    rate, frame = videoCapture.read ()

    imageName = "Img.jpg"

    cv2.imwrite (imageName, frame)

    return (imageName)

__captureImage__ ()