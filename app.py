from flask import Flask, request, send_from_directory, redirect, url_for, render_template
import subprocess
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'access_logs'
REPORT_FOLDER = 'report_logs'

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        # Generate unique filenames to avoid collisions
        unique_id = str(uuid.uuid4())
        log_filename = os.path.join(UPLOAD_FOLDER, unique_id)
        report_filename = os.path.join(REPORT_FOLDER, unique_id + '.html')

        file.save(log_filename)

        # Process the log file with GoAccess
        subprocess.run([
            'goaccess', log_filename,
            '-o', report_filename,
            '--log-format=%^ %h %^[%d:%t %^] "%r" %s %b "%R" "%u" %^'
        ])

        return redirect(url_for('report', uuid=unique_id))

@app.route('/report/<uuid>')
def report(uuid):
    return send_from_directory(REPORT_FOLDER, uuid + '.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

