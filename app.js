function submitSickLeave() {
    const form = document.getElementById('sickLeaveForm');
    const studentName = form.elements['studentName'].value;
    const reason = form.elements['reason'].value;

    // Perform actions with the submitted data
    console.log(`Sick Leave Submitted: Student Name - ${studentName}, Reason - ${reason}`);

    // You can send this data to the server in the future
}
// app.js
const nvtcFAQ = [
    {
        question: 'What programs does NVTC offer?',
        answer: 'NVTC offers courses in mechanical, electrical, and technical engineering.',
    },
    {
        question: 'Is NVTC recognized by the Bahraini government?',
        answer: 'Yes, NVTC is an entity of the Bahraini government and is under the umbrella of the Royal Charity Organization.',
    },
    {
        question: 'Does NVTC provide student support services?',
        answer: 'Yes, NVTC is committed to supporting its students through a range of services and facilities, including student stipends, transportation, student council, student activities, and a clinic.',
    },
    {
        question: 'Does NVTC provide a safe learning environment?',
        answer: 'Yes, NVTC is responsible for providing a healthy and safe environment for its students. They meet occupational health and safety standards, train staff in accident prevention and evacuation procedures, and provide 24x7 security services.',
    },
    {
        question: 'Does NVTC offer any rewards or incentives for high-achieving students?',
        answer: 'Yes, NVTC rewards its top-achieving students by providing them with the opportunity to travel abroad, which helps in gaining more knowledge, developing their personality, and building their career skills.',
    },
];

function generateRandomQuestion() {
    const randomIndex = Math.floor(Math.random() * nvtcFAQ.length);
    const randomQA = nvtcFAQ[randomIndex];

    // Display the random question and answer
    const resultElement = document.getElementById('randomQuestionResult');
    resultElement.innerHTML = `<strong>Question:</strong> ${randomQA.question}<br><strong>Answer:</strong> ${randomQA.answer}`;
}
// Add the function to handle feedback submission
function submitFeedback() {
    const form = document.getElementById('userFeedbackForm');
    const feedbackType = form.elements['feedbackType'].value;
    const feedbackMessage = form.elements['feedbackMessage'].value;

    // You can perform actions with the submitted feedback (e.g., send it to the server)
    console.log(`Feedback Submitted: Type - ${feedbackType}, Message - ${feedbackMessage}`);

    // Optionally, you can reset the form after submission
    form.reset();
}
// Sample child's details
const childDetails = {
    name: 'John Doe',
    grade: '5th Grade',
    attendance: '95%',
    upcomingEvents: ['Science Fair', 'Parent-Teacher Meeting'],
    academicProgress: {
        subjects: ['Math', 'Science', 'English'],
        grades: ['A', 'B', 'A-'],
    },
};

// Update the loginParent function to display child's details
function loginParent() {
    const username = document.getElementById('parentUsername').value;
    const password = document.getElementById('parentPassword').value;

    // Simple validation (you can implement a more secure authentication mechanism in a real application)
    if (username === 'Ali' && password === '123') {
        // Display the parent dashboard and information
        document.getElementById('parentDashboard').style.display = 'block';
        document.getElementById('parentInfo').innerText = `Welcome, ${username}!`;

        // Display child's details
        displayChildDetails(childDetails);

        // Optionally, you can reset the login form after successful login
        document.getElementById('parentLoginForm').reset();
    } else {
        alert('Invalid credentials. Please try again.');
    }
}

// Function to display child's details
function displayChildDetails(child) {
    const childDetailsElement = document.getElementById('childDetails');
    childDetailsElement.innerHTML = `
        <p><strong>Child's Name:</strong> ${child.name}</p>
        <p><strong>Grade:</strong> ${child.grade}</p>
        <p><strong>Attendance:</strong> ${child.attendance}</p>
        <p><strong>Upcoming Events:</strong> ${child.upcomingEvents.join(', ')}</p>
        <h3>Academic Progress</h3>
        <ul>
            ${child.academicProgress.subjects.map((subject, index) => `
                <li><strong>${subject}:</strong> ${child.academicProgress.grades[index]}</li>
            `).join('')}
        </ul>
    `;
}


// ... (previous code)

// Function to handle parent login
function loginParent() {
    const username = document.getElementById('parentUsername').value;
    const password = document.getElementById('parentPassword').value;
    const parentLoginSection = document.getElementById('parentLogin');
    const parentDashboardSection = document.getElementById('parentDashboard');
    const parentInfo = document.getElementById('parentInfo');
    const logoutButton = document.getElementById('logoutButton');

    // Simple validation (you can implement a more secure authentication mechanism in a real application)
    if (username === 'Ali' && password === '123') {
        // Display the parent dashboard and information
        parentDashboardSection.style.display = 'block';
        parentInfo.innerText = `Welcome, ${username}!`;

        // Hide the parent login section
        parentLoginSection.style.display = 'none';

        // Display child's details
        displayChildDetails(childDetails);

        // Show the logout button
        logoutButton.style.display = 'block';

        // Optionally, you can reset the login form after successful login
        document.getElementById('parentLoginForm').reset();
    } else {
        alert('Invalid credentials. Please try again.');
    }
}

// Function to handle parent logout
function logoutParent() {
    const parentLoginSection = document.getElementById('parentLogin');
    const parentDashboardSection = document.getElementById('parentDashboard');
    const logoutButton = document.getElementById('logoutButton');

    // Hide the parent dashboard and logout button
    parentDashboardSection.style.display = 'none';
    logoutButton.style.display = 'none';

    // Display the parent login section
    parentLoginSection.style.display = 'block';
}

// ... (other functions)

