# 🚀 Media Converter Pro

A blazing-fast, modern, and locally hosted media converter application built with Python (Flask) and FFmpeg. Featuring a beautiful Apple iOS-style glassmorphism UI, real-time progress tracking, and hardware acceleration support for both macOS and Windows.

---

screenshort.png
---


## ✨ Features

- **Format Conversion:** Convert MKV, AVI, MOV, and WEBM to standard MP4, or extract audio directly to MP3.
- **Smart Compression:** Resize videos to 1080p, 720p, or 480p to optimize file size without losing significant quality.
- **Real-Time Progress:** Live percentage tracking using FFmpeg background polling.
- **Hardware Acceleration:** Supports macOS `h264_videotoolbox` and Windows encoders (NVENC/AMF).
- **Batch Processing:** Drag & Drop multiple files and convert them seamlessly.
- **Premium UI:** Clean, responsive, modern Glassmorphism design built with Tailwind CSS.

---

# 🛠️ Prerequisites

Before you begin, ensure you have **Python** and **FFmpeg** installed on your machine.

---

# 🪟 For Windows Users

## 1️⃣ Install Python (3.x or higher)

Download from:
https://www.python.org/downloads/

⚠️ During installation, make sure to check:
**"Add Python to PATH"**

Verify installation:

```bash
python --version
```

---

## 2️⃣ Install FFmpeg

### Option A (Recommended – Using Winget)

Open Command Prompt or PowerShell as Administrator:

```bash
winget install ffmpeg
```

### Option B (Manual Installation)

1. Download FFmpeg from:
   https://ffmpeg.org/download.html
2. Extract the files.
3. Add the `bin` folder to Windows Environment Variables (PATH).

Verify installation:

```bash
ffmpeg -version
```

---

# 🍎 For macOS Users

## 1️⃣ Install Python (Latest Recommended)

Using Homebrew:

```bash
brew install python
```

Or download from:
https://www.python.org/downloads/

---

## 2️⃣ Install FFmpeg

Using Homebrew:

```bash
brew install ffmpeg
```

Verify installation:

```bash
ffmpeg -version
```

---

# 🚀 Installation & Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/IqraSarwar/Media-Converter-Pro.git
cd Media-Converter-Pro
```

---

## Step 2: Install Required Dependencies

This application uses Flask for the backend server.

```bash
pip install flask
```

---

# 💻 How to Run

Inside the project directory, start the Flask server:

```bash
python app.py
```

Open your browser and go to:

http://127.0.0.1:5000

Drag and drop your media files, select format/quality, and click **Start Processing**.

---

# ⚙️ Hardware Acceleration Setup (Very Important)

To achieve 5x–10x faster conversion speeds, configure your encoder inside `app.py`.

Open `app.py` and locate the encoder configuration (around line 55).

---

## 🍎 For macOS (Apple Silicon / Intel)

```python
command.extend(['-c:v', 'h264_videotoolbox', '-b:v', '2500k'])
```

---

## 🪟 For Windows (CPU Only)

```python
command.extend(['-c:v', 'libx264', '-preset', 'fast', '-crf', '23'])
```

---

## 🪟 For Windows (NVIDIA GPU - NVENC)

```python
command.extend(['-c:v', 'h264_nvenc', '-preset', 'fast', '-b:v', '2500k'])
```

---

# 📁 Project Structure

```
Media-Converter-Pro/
│
├── app.py                  # Main Flask backend and FFmpeg logic
├── templates/
│   └── index.html          # Frontend UI (HTML, JS, Tailwind CSS)
│
├── uploads/                # Auto-generated temporary input files
├── downloads/              # Auto-generated converted files
└── progress/               # Real-time progress log files
```

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome!

To contribute:
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is open-source and available under the **MIT License**.

---

# 🌟 Support

If you find this project useful, consider giving it a ⭐ on GitHub!

---

**Made with ❤️ using Python, Flask & FFmpeg**
