#  create a sample flask app
from flask import Flask, render_template, jsonify, request, g, session
# cors flask app
from flask_cors import CORS
import pymongo
from gridfs import GridFS

# Create a GridFS object to work with file storage

app = Flask(__name__, template_folder='templates')
app.secret_key = 'beekinTest'
CORS(app)


connection_string = "mongodb+srv://<user>:<password>@cluster0.u0pmbr0.mongodb.net/"
client = pymongo.MongoClient(connection_string)
db = client['Beekin']
collection = db['applications']
fs = GridFS(db)

'''
    API for the HOME page - Displays all the Open JOb Positions
'''
@app.route('/')
def home():
    """
    Home Page
    ---
    responses:
      200:
        description: Displays all open job positions
    """
    return render_template("home.html")


# Sample Job data
#{
#         "id": "1",
#         "title": "Software Engineer",
#         "company": "Beekin",
#         "location": "Ahmedabad",
#         "division": "IT",
#         "description": "We are seeking a highly skilled and motivated Software Developer to join our dynamic development team. As a Software Developer at [Your Company Name], you will play a crucial role in designing, developing, and maintaining software applications that drive our business and contribute to our clients success.",
#         "responsibilities": [
#                 "Collaborate with cross-functional teams, including project managers, designers, and other developers, to understand project requirements and deliver high-quality software solutions.",
#                 "Develop, test, and deploy software applications using industry-standard coding practices.",
#                 "Write clean, efficient, and maintainable code to meet project requirements.",
#                 "Debug and resolve software defects and issues, ensuring smooth application operation.",
#                 "Contribute to the design and architecture of software systems, taking performance and scalability into consideration.",
#                 "Stay up-to-date with industry trends and emerging technologies to drive innovation and improvement.",
#                 "Assist in the estimation and planning of project development tasks.",
#                 "Provide technical guidance and mentorship to junior developers."
#         ]

#     },


'''
    Retrieving all the available open job position at first from MongoDB Atlas Server 
'''
job_collection = db["jobs"]
job_positions = list(job_collection.find({}))
print(job_positions)
# Convert ObjectId values to strings
for job in job_positions:
    job['_id'] = str(job['_id'])

'''
    API for displaying all the jobposition on the home page
'''
@app.route('/job_positions', methods=['GET'])
def get_job_positions():
    """
    Get All Job Positions
    ---
    responses:
      200:
        description: Returns a list of all open job positions
      404:
        description: No job positions found
    """
    if job_positions:
        return jsonify(job_positions)
    else:
        return "No job positions found", 404
    

@app.route('/apply_job/<role>')
def job_application_form(role):
    """
    Apply for a Job
    ---
    parameters:
      - name: role
        in: path
        type: string
        required: true
        description: The job role to apply for
    responses:
      200:
        description: Displays the job application form
    """
    session['selected_role'] = role
    return render_template('ApplicationForm.html', role=role)


@app.route('/submit', methods=['POST'])
def submit_application():
    """
    Submit Job Application
    ---
    parameters:
      - name: role
        in: formData
        type: string
        required: true
        description: The job role to apply for
      - name: firstName
        in: formData
        type: string
        required: true
        description: First name
      - name: lastName
        in: formData
        type: string
        required: true
        description: Last name
      - name: email
        in: formData
        type: string
        required: true
        description: Email address
      - name: phone
        in: formData
        type: string
        required: true
        description: Phone number
      - name: address
        in: formData
        type: string
        required: true
        description: Address
      - name: city
        in: formData
        type: string
        required: true
        description: City
      - name: state
        in: formData
        type: string
        required: true
        description: State
      - name: zip
        in: formData
        type: string
        required: true
        description: Zip code
      - name: resume
        in: formData
        type: file
        required: true
        description: Resume file (PDF, DOC, DOCX)
      - name: coverLetter
        in: formData
        type: string
        required: true
        description: Cover letter
    responses:
      200:
        description: Application submitted successfully
      400:
        description: Error in form submission
    """
    if request.method == 'POST':
        # role =  g.selected_role
        role = session.get('selected_role')
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip']
        resume = request.files['resume']
        cover_letter = request.form['coverLetter']

        if resume:
            # Save the resume file to MongoDB using GridFS
            resume_id = fs.put(resume.read(), filename=resume.filename, content_type=resume.content_type)

            # Now you can store the `resume_id` in your application_data dictionary
            application_data = {
                'role': role,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'address': address,
                'city': city,
                'state': state,
                'zip_code': zip_code,
                'cover_letter': cover_letter,
                'resume_id': str(resume_id)  # Convert the ObjectId to a string for storing
            }
            collection.insert_one(application_data)
            return render_template('thankyou.html')
        else:
            return render_template('error.html')

       

if __name__ == '__main__':
    app.run(debug=True )

