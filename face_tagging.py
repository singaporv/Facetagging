import face_recognition

# picture_of_me = face_recognition.load_image_file("/home/apoorv/Desktop/known/s.jpg")
# my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

# unknown_picture = face_recognition.load_image_file("/home/apoorv/Desktop/b1.JPG")
# unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# # Now we can see the two face encodings are of the same person with `compare_faces`!

# results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

# if results[0] == True:
#     print("It's a picture of me!")
# else:
#     print("It's not a picture of me!")



# Facial features

from PIL import Image, ImageDraw
# import face_recognition

# Load the jpg file into a numpy array
# image = face_recognition.load_image_file("/home/apoorv/Desktop/a1.jpg")

# # Find all facial features in all the faces in the image
# face_landmarks_list = face_recognition.face_landmarks(image)

# print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# # Create a PIL imagedraw object so we can draw on the picture
# pil_image = Image.fromarray(image)
# d = ImageDraw.Draw(pil_image)

# for face_landmarks in face_landmarks_list:

#     # Print the location of each facial feature in this image
#     for facial_feature in face_landmarks.keys():
#         print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

#     # Let's trace out each facial feature in the image with a line!
#     for facial_feature in face_landmarks.keys():
#         d.line(face_landmarks[facial_feature], width=5)

# # Show the picture
# pil_image.show()


# Find comparison

# import face_recognition

# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("/home/apoorv/Desktop/known/ranveer.jpg")
obama_image = face_recognition.load_image_file("/home/apoorv/Desktop/known/s.jpg")
unknown_image = face_recognition.load_image_file("/home/apoorv/Desktop/a1.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    biden_face_encoding,
    obama_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Biden? {}".format(results[0]))
print("Is the unknown face a picture of Obama? {}".format(results[1]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))