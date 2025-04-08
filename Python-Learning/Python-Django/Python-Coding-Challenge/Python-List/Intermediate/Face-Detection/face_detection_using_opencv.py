import cv2
import matplotlib.pyplot as plt

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start the webcam feed
cap = cv2.VideoCapture(0)

# Set up a plot to display images in real-time
plt.ion()  # Turn on interactive mode for real-time plotting
fig, ax = plt.subplots()

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Convert the frame to RGB for displaying with Matplotlib
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the output frame using Matplotlib
    ax.imshow(frame_rgb)
    ax.axis('off')
    plt.draw()  # Update the plot with the new frame
    plt.pause(0.001)  # Pause briefly to allow for UI updates

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
plt.ioff()  # Turn off interactive mode
plt.show()  # Make sure the final frame is shown
