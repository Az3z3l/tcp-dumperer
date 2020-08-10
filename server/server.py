from flask import Flask, render_template, request, abort, jsonify, send_from_directory
import werkzeug
import os


app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
      os.system('sudo cp '+os.path.join(app.config['UPLOAD_FOLDER'], f.filename)+' '+os.path.join(app.config['UPLOAD_FOLDER'], 'latest.pcap '))
      return 'file uploaded successfully'
		
@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_FOLDER, path, as_attachment=True)



if __name__ == '__main__':
   app.run(host='0.0.0.0', port = 5000)
