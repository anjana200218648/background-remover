import tkinter as tk
from tkinter import filedialog, Label
from rembg import remove
import cv2
from PIL import Image, ImageTk
import os

def select_image():
    global image, original_file_path
    original_file_path = filedialog.askopenfilename()
    if original_file_path:
        image = cv2.imread(original_file_path)
        display_image(original_file_path)
        remove_btn.pack(pady=10)

def remove_background():
    global output_image_path
    output = remove(image)
    output_image_path = "output_image.png"
    cv2.imwrite(output_image_path, output)
    display_image(output_image_path)
    remove_btn.pack_forget()
    download_btn.pack(pady=10)

def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((150, 150), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

def download_image():
    if output_image_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg"),
                                                            ("All files", "*.*")])
        if save_path:
            cv2.imwrite(save_path, cv2.imread(output_image_path))

# Create the GUI
root = tk.Tk()
root.title("Background Remover")
root.geometry("500x500")
root.configure(bg="#2C3E50")

# Set the window icon using raw string
root.iconbitmap(r"C:\Users\User\Desktop\background remover\Gradient Icon Map Navigation App Logo.ico")

title_label = tk.Label(root, text="Remove Background", font=("Helvetica", 12, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

select_btn = tk.Button(root, text="Select Image", command=select_image, font=("Helvetica", 10), bg="#3498DB", fg="white", relief="flat", padx=10, pady=5)
select_btn.pack(pady=10)

remove_btn = tk.Button(root, text="Remove Background", command=remove_background, font=("Helvetica", 10), bg="#E74C3C", fg="white", relief="flat", padx=10, pady=5)

download_btn = tk.Button(root, text="Download Image", command=download_image, font=("Helvetica", 10), bg="#2ECC71", fg="white", relief="flat", padx=10, pady=5)

panel = Label(root, bg="#2C3E50")
panel.pack(pady=10)

footer_label = tk.Label(root, text="Powered by AnjanaTec © 2024", font=("Helvetica", 8), bg="#2C3E50", fg="white")
footer_label.pack(side="bottom", pady=20)

root.mainloop()
