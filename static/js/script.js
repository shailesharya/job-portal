// Function to fetch job positions data

function btnClicked(event){
    console.log("Button clicked");
    console.log(event);
}

function fetchJobPositions() {
    
    fetch('http://127.0.0.1:5000/job_positions')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Handle the job positions data
            displayJobPositions(data);
        })
        .catch(error => {
            console.error('Error fetching job positions:', error);
        });
}


// Function to display job positions on the page
function displayJobPositions(jobPositions) {
    const jobListings = document.getElementById('jobListings');
    jobPositions.forEach(position => {
        console.log(position);
        
        createJobListingCard(position.id,position.title, 
                            position.company, position.location, 
                            position.division, position.description,
                            position.responsibilities);
    });
}


function createJobListingCard(id ,title, company, location, division, description, responsibilities) {
    const jobListings = document.getElementById('jobListings');

    // Create a new job listing card
    const jobListingCard = document.createElement('div');
    jobListingCard.className = 'col-md-4 mb-4';
    console.log(responsibilities);
    console.log(typeof(responsibilities));
    if(id % 2 == 0){
        jobListingCard.innerHTML = `
        <div class="card border-warning text-bg-warning">
        <div class=" h4 card-header bg-transparent border-warning text-warning">${title}</div>
            <div class="card-body ">
                <p class="card-text">Company: ${company}</p>
                <p class="card-text">Location: ${location}</p>
                <p class="card-text">Division: ${division}</p>
                <button class="btn btn-warning" onclick="openJobDetailsModal('${title}', '${company}', '${location}', '${division}', '${description}',  '${responsibilities}')">View Details</button>
            </div>
        </div>
        `;
    }else{
        jobListingCard.innerHTML = `
        <div class="card border-success text-bg-warning">
            <div class=" h4 card-header bg-transparent border-success text-success">${title}</div>
            <div class="card-body ">
                <p class="card-text">Company: ${company}</p>
                <p class="card-text">Location: ${location}</p>
                <p class="card-text">Division: ${division}</p>
                <button class="btn btn-success" onclick="openJobDetailsModal('${title}', '${company}', '${location}', '${division}', '${description}', '${responsibilities}')">View Details</button>
            </div>
        </div>
        `;
    }

    // Populate the card content
    

    // Append the card to the jobListings row
    jobListings.appendChild(jobListingCard);
}




function openJobDetailsModal(title, company, location, division, description, responsibilities) {
    
    // map responsibilities
    let responsibilitiesArray = responsibilities.split('.').map(item => item.replace(/^[, ]+|[, ]+$/g, ''));
    // remove last element  from responsibilitiesArray
    if (responsibilitiesArray.length > 0) {
        responsibilitiesArray = responsibilitiesArray.slice(0, -1); // Remove the last element
    }

    const responsibilitiesList = responsibilitiesArray.map(item => `<li>${item}</li>`).join('');


    console.log("In open", responsibilitiesArray);

    // Set the modal title
    document.getElementById('jobDetailsModalLabel').textContent = title;

    // Create the HTML structure for the job details
    const modalBody = document.getElementById('modalBody');
    console.log(responsibilities);
    modalBody.innerHTML = `
        <p>Company: ${company}</p>
        <p>Location: ${location}</p>
        <p>Division: ${division}</p>
        <p>Description</p>
        <p> ${description} </p>

        <p>Responsibilities</p> 
        
        <ul>
            ${responsibilitiesList}
         </ul>

        <div class="modal-footer">
            <button type="button" class="btn btn-warning" onClick="apply_job('${title}')">Apply</button>
            <button type="button" class="btn btn-success" data-dismiss="modal">Close</button>
        </div>
        
    `;

    // Open the modal
    $('#jobDetailsModal').modal('show');
}


// Call the function to fetch job positions when the page loads
fetchJobPositions();

function apply_job(role){
    console.log("Role:", role);
    window.location.href = "/apply_job/" + role;
    alert(`You have applied for Job ID : ${role}`);
}


function redirectHome() {
    // Redirect to the home page URL
    window.location.href = '/'; // Replace '/home' with your desired URL
}