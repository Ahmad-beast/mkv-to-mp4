# 🚀 Media Converter Pro

A blazing-fast, modern, and locally hosted media converter application built with Python (Flask) and FFmpeg. Featuring a beautiful Apple iOS-style glassmorphism UI, real-time progress tracking, and hardware acceleration for Mac users.

## ✨ Features
* **Format Conversion:** Convert MKV, AVI, MOV, and WEBM to standard MP4, or extract audio directly to MP3.
* **Smart Compression:** Resize videos to 1080p, 720p, or 480p to save space.
* **Real-Time Progress:** Live percentage tracking using FFmpeg background polling.
* **Apple Hardware Acceleration:** Utilizes Mac's native `h264_videotoolbox` for 5x-10x faster encoding speeds.
* **Batch Processing:** Drag & Drop multiple files and convert them simultaneously.
* **Premium UI:** Clean, responsive, and modern Glassmorphism design built with Tailwind CSS.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your machine:

**1. Python (3.x or higher)**
* **Mac/Windows:** Download and install from [python.org](https://www.python.org/downloads/).
* *Note for Windows users:* Make sure to check the box **"Add Python to PATH"** during installation.

**2. FFmpeg (Core Engine)**
* **Mac:** The easiest way to install is via Homebrew. Open your terminal and run:
  ```bash
  brew install ffmpeg
  (If you don't have Homebrew, install it first from brew.sh)

Windows: Download the FFmpeg executable from the official website and add it to your System Environment Variables.

Gemini said
Zabardast! GitHub par apna project push karna ek behtareen aadat hai. Yeh README.md file aapke project ko bilkul ek professional aur open-source enterprise tool jaisi look degi.

Isme maine Python install karne se le kar, FFmpeg setup, cloning, aur app run karne tak ka har ek step detail mein likh diya hai. Aap is code ko copy kar ke apne GitHub repository mein README.md ke naam se save kar lein:

Markdown
# 🚀 Media Converter Pro

A blazing-fast, modern, and locally hosted media converter application built with Python (Flask) and FFmpeg. Featuring a beautiful Apple iOS-style glassmorphism UI, real-time progress tracking, and hardware acceleration for Mac users.

## ✨ Features
* **Format Conversion:** Convert MKV, AVI, MOV, and WEBM to standard MP4, or extract audio directly to MP3.
* **Smart Compression:** Resize videos to 1080p, 720p, or 480p to save space.
* **Real-Time Progress:** Live percentage tracking using FFmpeg background polling.
* **Apple Hardware Acceleration:** Utilizes Mac's native `h264_videotoolbox` for 5x-10x faster encoding speeds.
* **Batch Processing:** Drag & Drop multiple files and convert them simultaneously.
* **Premium UI:** Clean, responsive, and modern Glassmorphism design built with Tailwind CSS.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your machine:

**1. Python (3.x or higher)**
* **Mac/Windows:** Download and install from [python.org](https://www.python.org/downloads/).
* *Note for Windows users:* Make sure to check the box **"Add Python to PATH"** during installation.

**2. FFmpeg (Core Engine)**
* **Mac:** The easiest way to install is via Homebrew. Open your terminal and run:
  ```bash
  brew install ffmpeg
(If you don't have Homebrew, install it first from brew.sh)

Windows: Download the FFmpeg executable from the official website and add it to your System Environment Variables.

🚀 Installation & Setup
Step 1: Clone the Repository
Open your terminal (or command prompt) and run:

Bash
git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
cd YOUR-REPO-NAME
(Note: Replace YOUR-USERNAME and YOUR-REPO-NAME with your actual GitHub details).

Step 2: Install Required Libraries
This application uses Flask for the backend. Install it using pip:

Bash
pip install flask
💻 How to Run
Open your terminal and navigate to the project directory.

Start the Flask server by running:

Bash
python app.py
Open your web browser and go to:
http://127.0.0.1:5000

Drag and drop your media files, select your desired format/quality, and click Start Processing!

⚠️ Important Note for Windows/Linux Users
This application is highly optimized for macOS and uses Apple's hardware acceleration (h264_videotoolbox).

If you are running this on Windows or Linux, you need to make a small change in app.py for it to work:

Open app.py in your code editor.

Find this line (around line 55):

Python
command.extend(['-c:v', 'h264_videotoolbox', '-b:v', '2500k'])
Change it to standard encoding:

Python
command.extend(['-c:v', 'libx264', '-preset', 'fast', '-crf', '23'])
📁 Project Structure
Plaintext
├── app.py                  # Main Python Flask application & logic
├── templates/              
│   └── index.html          # Frontend UI (Tailwind CSS + JS)
├── uploads/                # Temporary folder for input files (Auto-generated)
├── downloads/              # Output folder for converted files (Auto-generated)
└── progress/               # Temporary logs for real-time progress (Auto-generated)
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.


### Isme Aapko Kya Change Karna Hai?
Is file ke andar jahan jahan maine **`YOUR-USERNAME`** aur **`YOUR-REPO-NAME`** likha hai, wahan aapne apne GitHub ka actual username aur repository ka naam likh dena hai (maslan `IqraSarwar/MediaConverterPro`). 

Agar aap is repo ko GitHub par upload kar lengi, toh doosre developers bhi aapka code use kar sakenge aur iski tareef karenge! Kuch aur help chahiye Git ya GitHub ke hawalay se?
