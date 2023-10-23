# Job Portal

Job Portal is a web application built with Flask and MongoDB that allows users to view open job positions, apply for job roles, and submit their job applications.

## Features

- Display a list of open job positions.
- Allow users to apply for specific job roles.
- Collect and store job applications in a MongoDB database.

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


 
