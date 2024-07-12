import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import subprocess
import shutil
import argparse
# Define paths
DATABASE_FOLDER = 'database'
VIDEO_FOLDER = 'videos'
CSV_FILE = 'people_2.csv'

# Function to handle missing child image upload
def upload_image():
    file_path = filedialog.askopenfilename(title='Select Image File', filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    if file_path:
        shutil.copy(file_path, os.path.join(DATABASE_FOLDER , os.path.basename(file_path)))
        messagebox.showinfo('Success', 'Image uploaded successfully.')

# Function to train the model and update CSV
def train_model():
    try:
        subprocess.run(['python', 'updating csv db sample code.py'], check=True)
        messagebox.showinfo('Success', 'Model trained and CSV updated successfully.')
    except subprocess.CalledProcessError as e:
        messagebox.showerror('Error', f'Error running training script: {e}')

# Function to handle video upload and facial recognition
def upload_video():  
    file_path = filedialog.askopenfilename(title='Select Video File', filetypes=[('Video Files', '*.mp4;*.avi')])
    if file_path:
        shutil.copy(file_path, os.path.join(VIDEO_FOLDER, os.path.basename(file_path)))
        messagebox.showinfo('Success', 'Video uploaded successfully.')


# Function to browse video file and run face recognition code
def browse_and_run_face_recognition():
    file_path = filedialog.askopenfilename(title='Select Video File', filetypes=[('Video Files', '*.mp4;*.avi')])
    if file_path:
        try:
            subprocess.run(['python', 'Video facial recognition with python dlib.py', '--video', file_path], check=True)
            messagebox.showinfo('Success', 'Facial recognition completed successfully.')
        except subprocess.CalledProcessError as e:
            messagebox.showerror('Error', f'Error running facial recognition script: {e}')

# Main Tkinter application
root = tk.Tk()
root.title('Facial Recognition Application')
root.geometry('500x300')  # Set the window size

# Create and place widgets with colorful interface
title_label = tk.Label(root, text='Facial Recognition', font=('Helvetica', 20), fg='blue')
title_label.pack(pady=10)

upload_image_button = tk.Button(root, text='Upload Missing Child Image', command=upload_image, bg='green', fg='white')
upload_image_button.pack(pady=10)

train_button = tk.Button(root, text='Train Model and Update CSV', command=train_model, bg='orange', fg='white')
train_button.pack(pady=10)

upload_video_button = tk.Button(root, text='Upload Video for Facial Recognition', command=upload_video, bg='purple', fg='white')
upload_video_button.pack(pady=10)

browse_and_run_button = tk.Button(root, text='Browse Video and Run Facial Recognition', command=browse_and_run_face_recognition, bg='red', fg='white')
browse_and_run_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
