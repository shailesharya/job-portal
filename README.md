# Job Portal

Job Portal is a web application built with Flask and MongoDB that allows users to view open job positions, apply for job roles, and submit their job applications.

## Features

- Display a list of open job positions.
- Allow users to apply for specific job roles.
- Collect and store job applications in a MongoDB database.

## Output
https://github.com/shailesharya/job-portal/assets/41483772/85c29ecb-ec2d-4d53-b927-4b3facaf78f7



## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- MongoDB Atlas account (for database storage)

### Installation

1. Clone the repository:
   git clone https://github.com/shailesharya/job-portal.git
   cd job-portal
   
2. Create a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   
3. Install the project dependencies:
   pip install -r requirements.txt
   
4. Set up MongoDB Atlas:
  - Create a MongoDB Atlas account if you don't have one.
  - Set up a MongoDB cluster and configure your connection string.
    
5. Configure the application:
   Update the connection_string variable in app.py:
   connection_string = "mongodb+srv://<user>:<password>@cluster0.u0pmbr0.mongodb.net/"

7. Start the Flask application:
   flask run

8. Access the application in your web browser at http://localhost:5000.

## Usage
- Visit the home page to view open job positions.
- Click on a job role to apply for it.
- Fill out the application form, upload a resume, and submit the application.

## Screenshot
1. HomePage:
   ![1](https://github.com/shailesharya/job-portal/assets/41483772/60d47a99-468f-46d9-bf99-3db393d0f901)
2. Job Details
   ![2](https://github.com/shailesharya/job-portal/assets/41483772/d48a6b98-a7f2-4dd2-8d04-41b5e12b4659)
3. Job Application Form
   ![3](https://github.com/shailesharya/job-portal/assets/41483772/9ca0efcc-1ffc-471e-a4ed-be815dffb79c)
4. Job Application Form Filled with Details
   ![4](https://github.com/shailesharya/job-portal/assets/41483772/ed0c12d0-183e-4122-a187-18120d16feaa)
5. Application Submitted Success!!!
   ![5](https://github.com/shailesharya/job-portal/assets/41483772/b8f385bf-73ae-4413-a1cd-923df43d2f88)
6. Mongo DB Database for Job Listing
   ![6](https://github.com/shailesharya/job-portal/assets/41483772/4384f623-a7ab-4923-820b-66cd991181d3)
7. Mongo DB Database for Storying Applicant Information with CV
   ![7](https://github.com/shailesharya/job-portal/assets/41483772/eca7a85d-b982-42fc-bc19-137515466b72)







 
