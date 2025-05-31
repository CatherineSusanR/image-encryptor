
# 🖼️ Image Encryptor & Decryptor

A simple, user-friendly Python application to **encrypt and decrypt images** using pixel shuffling and a secret key. Features a graphical interface built with Tkinter.  
Your images are scrambled beyond recognition and can only be restored with the correct key.

---

## 🚀 Features

- **Encrypt images** using a custom key (pixel shuffling)
- **Decrypt images** with the same key
- **Intuitive GUI** — no command line required
- Supports common image formats: `.png`, `.jpg`, `.jpeg`, `.bmp`
- Lightweight and easy to use

---

## 📦 Requirements

- Python 3.x
- Pillow (`pip install pillow`)

---

## ⚡ Installation

1. **Clone or download this repository**  
   (Or just download `main.py` if you prefer)

2. **Install dependencies**
   ```bash
   pip install pillow
   ```

3. **Run the app**
   ```bash
   python main.py
   ```

---

## 📝 Usage

1. **Open the app**  
   `python main.py`

2. **Encrypt an image**
   - Click **Browse** to select the image you want to encrypt.
   - Click **Save As** to choose where to save the encrypted image.
   - Enter a **seed key** (any word or number, but remember it!).
   - Click **Encrypt Image**.

3. **Decrypt an image**
   - Select the encrypted image as input.
   - Choose where to save the decrypted image.
   - Enter the **same seed key** used for encryption.
   - Click **Decrypt Image**.

> **Note:** The same key must be used for both encryption and decryption. If you lose the key, you cannot recover your image.

---

## 🔒 How It Works

- The app uses a **pixel shuffling algorithm** based on your secret key.
- The image is scrambled so it’s unrecognizable.
- Decryption restores the original image only if the correct key is provided.

---

## 📁 Project Structure

```
image-encryptor/
├── main.py
├── README.md
├── requirements.txt
└── screenshot.png  # (optional, for demo)
```

---

## 🙋 FAQ

**Q:** Is this strong encryption?  
**A:** Pixel shuffling is good for obfuscation and learning, but not for high-security needs. For sensitive data, use proven cryptography libraries.

**Q:** What image formats are supported?  
**A:** PNG, JPG, JPEG, BMP.

**Q:** Can I use this on large images?  
**A:** Yes, but very large images may take longer to process.

---

## 🧑‍💻 Author

- **Catherine Susan**
- [GitHub Profile](https://github.com/CatherineSusanR)

---

