import tkinter as tk
from tkinter import Message, Text
import cv2
import os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import pyttsx3

newPath = 'EM III'
myList = os.listdir(newPath)

newPath1 = 'DLCOA'
myList1 = os.listdir(newPath1)

newPath2 = 'DS'
myList2 = os.listdir(newPath2)

window = tk.Tk()
window.title("Face Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'

window.configure(background='orange')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="Attendance Management System Using Face Recognition", bg="Blue", fg="white", width=50,
                   height=3, font=('times', 30, 'bold'))

message.place(x=200, y=20)

# ID
lbl = tk.Label(window, text="Enter ID", width=10, height=2, fg="red", bg="yellow", font=('times', 15, ' bold '))
lbl.place(x=10, y=200)

# ID
txt = tk.Entry(window, width=15, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt.place(x=160, y=215)

# Name
lbl2 = tk.Label(window, text="Enter Name", width=10, fg="red", bg="yellow", height=2, font=('times', 15, ' bold '))
lbl2.place(x=10, y=300)

# Name
txt2 = tk.Entry(window, width=15, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt2.place(x=160, y=315)

# Notification
lbl3 = tk.Label(window, text="Notification : ", width=10, fg="red", bg="yellow", height=2,
                font=('times', 15, 'bold'))
lbl3.place(x=10, y=400)

# Notification
message1 = tk.Label(window, text="", bg="yellow", fg="red", width=30, height=2, activebackground="yellow",
                   font=('times', 15, ' bold '))
message1.place(x=160, y=400)

# Attendance
lbl4 = tk.Label(window, text="Attendance : ", width=12, fg="red", bg="yellow", height=2,
                font=('times', 15, 'bold'))
lbl4.place(x=10, y=650)

# Total Lectures
lbl5 = tk.Label(window, text="Total Lectures : ", width=12, fg="red", bg="yellow", height=2,
                font=('times', 15, 'bold'))
lbl5.place(x=10, y=720)

# Attendance
message2 = tk.Label(window, text="", fg="red", bg="yellow", activeforeground="green", width=35, height=2,
                    font=('times', 15, ' bold '))
message2.place(x=180, y=650)

# Total Lectures
message3 = tk.Label(window, text="", fg="red", bg="yellow", activeforeground="green", width=25, height=2,
                    font=('times', 15, ' bold '))
message3.place(x=180, y=720)

# Unknown Faces
lbl6 = tk.Label(window, text="Unknown Faces ", width=20, fg="red", bg="yellow", height=2,
                font=('times', 15, 'bold'))
lbl6.place(x=730, y=470)

# Subjects
lbl7 = tk.Label(window, text="Subjects", width=20, fg="red", bg="yellow", height=2,
                font=('times', 15, 'bold'))
lbl7.place(x=680, y=190)

# Unknown faces
message4 = tk.Label(window, text="", fg="red", bg="yellow", activeforeground="green", width=35, height=2,
                    font=('times', 15, ' bold '))
message4.place(x=650, y=540)

lbl8 = tk.Label(window, text="Total Students", width=20, fg="red", bg="yellow", height=2,
                font=('times', 15, 'bold'))
lbl8.place(x=1200, y=200)

message5 = tk.Label(window, text="", fg="red", bg="yellow", activeforeground="green", width=20, height=2,
                    font=('times', 15, ' bold '))
message5.place(x=1200, y=280)

lbl9 = tk.Label(window, text="Today's (% Attendance)", width=20, fg="red", bg="yellow", height=2,
                font=('times', 15, 'bold'))
lbl9.place(x=1200, y=380)

message6 = tk.Label(window, text="", fg="red", bg="yellow", activeforeground="green", width=20, height=2,
                    font=('times', 15, ' bold '))
message6.place(x=1200, y=460)


def clear():
    txt.delete(0, 'end')
    res = ""
    message.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = ""
    message.configure(text=res)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def TakeImages():
    Id = (txt.get())
    name = (txt2.get())
    if (is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)      # haarcascade - detecting faces
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('frame', img)
            # wait for 100 milliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 60
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)


    else:
        if (is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text=res)
        if (name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text=res)


def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    message1.configure(text=res)


def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # print(imagePaths)

    # create empty face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()   # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time', 'Lecture']
    lecture = "EM III"
    attendance = pd.DataFrame(columns=col_names)
    total = len(myList)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa + "-" + str(int(conf))
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp, lecture]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 90):
                engine = pyttsx3.init()
                engine.say("An Unknown person has entered")
                #print("An Unknown person has entered")
                result = "An Unknown person has entered"
                message4.configure(text=result)
                rate = engine.getProperty('rate')  # getting details of current speaking rate
                #print(rate)
                engine.setProperty('rate', 115)
                engine.runAndWait()
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)

        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "EM III\Attendance_" + date + "-" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)

    a = len(attendance)
    #print(len(attendance))
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    res1 = total
    message2.configure(text=res)
    message3.configure(text=res1)
    f = open('StudentDetails/StudentDetails.csv')

    reader = csv.reader(f)
    people = []
    for row in reader:
        people.append(row)
    r = len(people) / 2
    s = int(r)
    b = (a*100)/s
    message5.configure(text = s)
    message6.configure(text = b)

def TrackImages1():
    recognizer = cv2.face.LBPHFaceRecognizer_create()   # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time', 'Lecture']
    lecture = "DLCOA"
    attendance = pd.DataFrame(columns=col_names)
    total1 = (len(myList1) + 1)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa + "-" + str(int(conf))
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp, lecture]


            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 90):
                engine = pyttsx3.init()
                engine.say("An Unknown person has entered")
                print("An Unknown person has entered")
                result = "An Unknown person has entered"
                message4.configure(text=result)
                rate = engine.getProperty('rate')  # getting details of current speaking rate
                print(rate)
                engine.setProperty('rate', 115)
                engine.runAndWait()
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)

        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "DLCOA\Attendance_" + date + "-" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    a = len(attendance)
    res = attendance
    res1 = total1
    message2.configure(text=res)
    message3.configure(text=res1)
    f = open('StudentDetails/StudentDetails.csv')

    reader = csv.reader(f)
    people = []
    for row in reader:
        people.append(row)
    print(len(people)/2)

    r = len(people) / 2
    s = int(r)
    b = (a * 100) / s
    message5.configure(text = s)
    message6.configure(text=b)


def TrackImages2():
    recognizer = cv2.face.LBPHFaceRecognizer_create()   # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time', ' Lecture']
    lecture = "DS"
    attendance = pd.DataFrame(columns=col_names)
    total2 = (len(myList2) + 1)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa + "-" + str(int(conf))
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp, lecture]


            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 90):
                engine = pyttsx3.init()
                engine.say("An Unknown person has entered")
                print("An Unknown person has entered")
                result = "An Unknown person has entered"
                message4.configure(text=result)
                rate = engine.getProperty('rate')  # getting details of current speaking rate
                print(rate)
                engine.setProperty('rate', 115)
                engine.runAndWait()
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)

        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "DS\Attendance_" + date + "-" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    a = len(attendance)
    res = attendance
    res1 = total2
    message2.configure(text=res)
    message3.configure(text=res1)
    f = open('StudentDetails/StudentDetails.csv')

    people = []
    reader = csv.reader(f)
    for row in reader:
        people.append(row)
    print(len(people)/2)

    print(len(people)/2)
    r = len(people) / 2
    s = int(r)
    b = (a * 100) / s
    message5.configure(text = s)
    message6.configure(text=b)


clearButton = tk.Button(window, text="Clear", command=clear, fg="red", bg="yellow", width=10, height=2,
                        activebackground="Red", font=('times', 15, ' bold '))
clearButton.place(x=350, y=200)
clearButton2 = tk.Button(window, text="Clear", command=clear2, fg="red", bg="yellow", width=10, height=2,
                         activebackground="Red", font=('times', 15, ' bold '))
clearButton2.place(x=350, y=300)
takeImg = tk.Button(window, text="Take Images", command=TakeImages, fg="red", bg="yellow", width=15, height=3,
                    activebackground="Red", font=('times', 15, ' bold '))
takeImg.place(x=10, y=500)
trainImg = tk.Button(window, text="Train Images", command=TrainImages, fg="red", bg="yellow", width=15, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
trainImg.place(x=210, y=500)
trackImg = tk.Button(window, text="EM III", command=TrackImages, fg="red", bg="yellow", width=12, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
trackImg.place(x=550, y=260)

trackImg1 = tk.Button(window, text="DLCOA", command=TrackImages1, fg="red", bg="yellow", width=12, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
trackImg1.place(x=730, y=260)

trackImg2 = tk.Button(window, text="DS", command=TrackImages2, fg="red", bg="yellow", width=12, height=3,
                     activebackground="Red", font=('times', 15, ' bold '))
trackImg2.place(x=910, y=260)
quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="red", bg="yellow", width=15, height=3,
                       activebackground="Red", font=('times', 15, ' bold '))
quitWindow.place(x=415, y=500)

window.mainloop()
