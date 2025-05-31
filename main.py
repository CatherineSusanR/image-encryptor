import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import random
import os

def get_seeded_random(seed):
    rnd = random.Random()
    rnd.seed(seed)
    return rnd

def encrypt_image(input_image_path, output_image_path, seed):
    try:
        image = Image.open(input_image_path)
        width, height = image.size
        pixels = list(image.getdata())
        random_gen = get_seeded_random(seed)
        indices = list(range(len(pixels)))
        random_gen.shuffle(indices)
        encrypted_pixels = [pixels[i] for i in indices]
        encrypted_image = Image.new(image.mode, (width, height))
        encrypted_image.putdata(encrypted_pixels)
        encrypted_image.save(output_image_path)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")
        return False

def decrypt_image(input_image_path, output_image_path, seed):
    try:
        image = Image.open(input_image_path)
        width, height = image.size
        pixels = list(image.getdata())
        random_gen = get_seeded_random(seed)
        indices = list(range(len(pixels)))
        random_gen.shuffle(indices)
        # Inverse mapping
        decrypted_pixels = [None] * len(pixels)
        for i, idx in enumerate(indices):
            decrypted_pixels[idx] = pixels[i]
        decrypted_image = Image.new(image.mode, (width, height))
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save(output_image_path)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")
        return False

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor & Decryptor")
        self.root.geometry("400x350")
        self.input_image_path = ""
        self.output_image_path = ""

        tk.Label(root, text="Select Image to Encrypt/Decrypt:").pack(pady=5)
        self.input_image_label = tk.Label(root, text="No image selected")
        self.input_image_label.pack(pady=5)
        tk.Button(root, text="Browse", command=self.select_input_image).pack(pady=5)

        tk.Label(root, text="Output Image Path:").pack(pady=5)
        self.output_image_label = tk.Label(root, text="No output path selected")
        self.output_image_label.pack(pady=5)
        tk.Button(root, text="Save As", command=self.select_output_image).pack(pady=5)

        tk.Label(root, text="Enter Seed Key:").pack(pady=5)
        self.seed_entry = tk.Entry(root)
        self.seed_entry.pack(pady=5)

        tk.Button(root, text="Encrypt Image", command=self.encrypt).pack(pady=10)
        tk.Button(root, text="Decrypt Image", command=self.decrypt).pack(pady=5)

    def select_input_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if path:
            self.input_image_path = path
            self.input_image_label.config(text=os.path.basename(path))

    def select_output_image(self):
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            self.output_image_path = path
            self.output_image_label.config(text=os.path.basename(path))

    def encrypt(self):
        seed = self.seed_entry.get()
        if not self.input_image_path or not self.output_image_path or not seed:
            messagebox.showerror("Error", "Please select input/output images and enter a seed key.")
            return
        if encrypt_image(self.input_image_path, self.output_image_path, seed):
            messagebox.showinfo("Success", "Image encrypted successfully!")

    def decrypt(self):
        seed = self.seed_entry.get()
        if not self.input_image_path or not self.output_image_path or not seed:
            messagebox.showerror("Error", "Please select input/output images and enter a seed key.")
            return
        if decrypt_image(self.input_image_path, self.output_image_path, seed):
            messagebox.showinfo("Success", "Image decrypted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
