import cv2
import sys

#cascPath = sys.argv[1]
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    smile = smileCascade.detectMultiScale(gray,1.1,4)

    for (x, y, w, h) in smile:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()