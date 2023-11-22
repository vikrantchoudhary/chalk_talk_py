from flask import Flask, render_template, jsonify

app = Flask(__name__)

SERVICES = [
  {
    'id': 1,
    'title': 'Data Analyst',
  },
  {
    'id': 2,
    'title': 'Data Scientist'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer'
  },
  {
    'id': 4,
    'title': 'Backend Engineer'
  }
]

# Set the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'
# Allow only images to be uploaded
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('home.html', services= SERVICES, company_name='Chalk Talk Speech And Hearing Clinic')

@app.route('/about')
def about():
    return render_template('about.html',company_name='Chalk Talk Speech And Hearing Clinic')

@app.route('/services')
def services():
    return render_template('services.html',company_name='Chalk Talk Speech And Hearing Clinic')

@app.route('/feedbacks')
def contact():
    return render_template('feedback.html',company_name='Chalk Talk Speech And Hearing Clinic')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    # Get the feedback text
    feedback_text = request.form['feedback_text']

    # Check if the post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return redirect(request.url)

    # If the file is allowed and the file is selected
    if file and allowed_file(file.filename):
        # Save the file to the upload folder
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Add your code here to store the feedback text and image filename in a database or handle it as needed

        return 'Feedback submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
