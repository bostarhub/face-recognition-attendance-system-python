import os
import pickle
import face_recognition
import numpy as np
from sklearn import neighbors
import tkinter as tk
from tkinter import messagebox

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
    encodings = []
    labels = []

    # Employee data dictionary to store encoded images with employee ID and first name
    employee_data = {}

    # Training directory
    train_dir = os.listdir('dataset/')

    for person in train_dir:
        pix = os.listdir("dataset/" + person)

        for person_img in pix:
            face = face_recognition.load_image_file("dataset/" + person + "/" + person_img)
            height, width, _ = face.shape
            face_location = (0, width, height, 0)
            face_enc = face_recognition.face_encodings(face, known_face_locations=[face_location])

            if len(face_enc) != 1:
                print(f"Image {person_img} does not contain exactly one face. Skipping.")
                continue

            face_enc = np.array(face_enc[0])
            face_enc = face_enc.flatten()

            # Get the first name (you can modify this to fetch the first name from your data source)
            first_name = "employeefirstname"  # Replace with the actual first name

            # Add face encoding for the current image with corresponding label (ID) to the training data
            encodings.append(face_enc)
            labels.append(person)

            # Store the encoded image data along with employee ID and first name
            employee_data[person] = {
                "employee_id": person,
                "first_name": first_name,
                "encoded_image": face_enc
            }

    # Save the employee data to a file using pickle
    with open("employee_data.pkl", 'wb') as f:
        pickle.dump(employee_data, f)

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(encodings, labels)

    # Save the trained KNN classifier
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf

if __name__ == "__main__":
    print("Training KNN classifier...")
    classifier = train("dataset", model_save_path="trained_knn_model.clf", n_neighbors=2)
    print("Training complete!")

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Success", "KNN classifier training completed successfully.")
    root.after(3000, root.destroy)



