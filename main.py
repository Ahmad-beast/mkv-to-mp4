from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'
PROGRESS_FOLDER = 'progress' # Naya folder live status ke liye
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
os.makedirs(PROGRESS_FOLDER, exist_ok=True)

# Memory mein video durations save karne ke liye
video_durations = {}

def get_video_duration(file_path):
    # FFprobe se video ki total length (seconds mein) nikalna
    try:
        cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return float(result.stdout.strip())
    except Exception:
        return 0.1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files.get('file')
    file_id = request.form.get('file_id')
    target_format = request.form.get('format', 'mp4')
    resolution = request.form.get('resolution', 'original')
    
    if not file or file.filename == '':
        return jsonify({'status': 'error', 'message': 'No file'})
        
    original_ext = os.path.splitext(file.filename)[1].lower()
    base_name = os.path.splitext(file.filename)[0]
    
    input_path = os.path.join(UPLOAD_FOLDER, f"{file_id}{original_ext}")
    output_filename = f"{base_name}_{resolution}.{target_format}"
    output_path = os.path.join(DOWNLOAD_FOLDER, f"{file_id}_{output_filename}")
    progress_file = os.path.join(PROGRESS_FOLDER, f"{file_id}.txt")
    
    file.save(input_path)
    
    # Video ki total length calculate kar ke microseconds mein save karein
    duration_sec = get_video_duration(input_path)
    video_durations[file_id] = duration_sec * 1000000  
    
    # FFmpeg command base
    command = ['ffmpeg', '-y', '-i', input_path, '-progress', progress_file]
    
    # Logic for audio vs video
    if target_format == 'mp3':
        command.extend(['-q:a', '0', '-map', 'a', output_path])
    else:
        if resolution == 'original' and target_format == 'mp4' and original_ext == '.mkv':
            command.extend(['-codec', 'copy', output_path])
        else:
            # Apple Mac Hardware Acceleration for SUPER FAST SPEED 🚀
            command.extend(['-c:v', 'h264_videotoolbox', '-b:v', '2500k'])
            if resolution == '1080p': command.extend(['-vf', 'scale=-2:1080'])
            elif resolution == '720p': command.extend(['-vf', 'scale=-2:720'])
            elif resolution == '480p': command.extend(['-vf', 'scale=-2:480'])
            command.append(output_path)
            
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return jsonify({
            'status': 'success',
            'converted': output_filename,
            'download_id': f"{file_id}_{output_filename}"
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/progress/<file_id>')
def get_progress(file_id):
    # Frontend yahan se live percentage puchega
    progress_file = os.path.join(PROGRESS_FOLDER, f"{file_id}.txt")
    if not os.path.exists(progress_file):
        return jsonify({'percentage': 0})
    
    try:
        with open(progress_file, 'r') as f:
            lines = f.readlines()
            
        out_time_us = 0
        is_end = False
        
        # Log file ko neechay se upar read karein taake latest time mile
        for line in reversed(lines):
            if line.startswith('out_time_ms='):
                val = line.split('=')[1].strip()
                if val.isdigit():
                    out_time_us = int(val)
                break
            if line.startswith('progress=end'):
                is_end = True
                
        if is_end:
            return jsonify({'percentage': 100})
            
        total_us = video_durations.get(file_id, 1)
        percentage = min(99, int((out_time_us / total_us) * 100))
        
        return jsonify({'percentage': max(0, percentage)})
    except Exception:
        return jsonify({'percentage': 0})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)