import cv2 as cv
#from matplotlib import pyplot as plt

directorio = "192.168.1.11:4747/video"
droid_cam = f"http://{directorio}"

video = cv.VideoCapture(droid_cam)
print(video)

while True:
    ret, frame = video.read()
    
    cv.imshow('CAMARA DROIDCAM', frame)
    if ret == True:    
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    
video.release()

cv.destroyAllWindows()