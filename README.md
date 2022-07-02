# Face-Recognition-Based-Attendance-System

As the name suggests, this project helps in monitoring the attendance for any class, by identifying the face of the students and then automatically updating the data in a file along with the id, name, date and time. The file name will include the date, in order to be specific that for a particular date and class, which all students were present.

## Procedure of marking attendance by detecting face
#
#### 1: Taking Images - Here, 100 images of a particular face will be stored. While training, a user has to provide all possible angles of their face. This will further ease the process of detecting faces while marking attendance.
#
#### 2: Training the Images - The images will be trained in two steps. First we have used haar-cascade to detect the facial features and then used LBPH algorithm provided by cv2 to recognize the images.
#
#### 3: Tracking the images - When the track button is clicked, the camera is turned on and during this period, the camera captures all the iamges and stores the details of the people who are identified i.e people whose images and data are stored. Other people if detected are classified as unknown.
#
#### 4: Usage of a threshold value for identifying a person - We have set a threshold value of 50 to confirm the presence of the correct person.
#
#### 5: Calculating the attendance percentage - after detecting, the system will provide you with the details of no.of students present and how much percentage of them are present for a particular lecture at a given date and time.
#
#### 6: Voice alert system for alerting the presence of an unknown person in front of the camera - If an unknown person is detected in front of the camera, the system will give a voice message "An unknown person has entered" so that one can know that other than the students, someone else has entered.
#
#### 7: Attendance marking for different subjects - Here, attendance can be marked for different subjects.
#
## Screenshots of Output
 
#![](https://user-images.githubusercontent.com/68478902/177007267-0a5ca81d-16e1-4949-9665-19d36055511b.jpeg)


## Demo



https://user-images.githubusercontent.com/68478902/177007530-baea4e48-b5c5-4ef9-802c-f665d6ba1daa.mp4

