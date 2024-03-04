from flask import Flask, render_template, request, redirect, url_for, send_file
from data_handler import get_students, update_student_data
import yagmail
import qrcode
from io import BytesIO
import os
import base64
from PIL import Image
from pyzbar.pyzbar import decode



SENDER_EMAIL = "nvtcbookingsystem@gmail.com"
SENDER_APP_PASSWORD = "Nvtc@1234"# Replace with your sender app password

def generate_qr_code(username, password):
    # Combine username and password into a single string
    data = f"username:{username},password:{password}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    return img

# Define Flask app instance
app = Flask(__name__)

students = get_students()  # Retrieve students data

# Modify the route function for /qr_generator

@app.route('/login_with_qr', methods=['GET', 'POST'])
def login_with_qr():
    if request.method == 'POST':
        # Get the QR code image from the form
        qr_code_data = request.files['qr_code_image']
        # Decode the QR code image
        qr_code_image = Image.open(qr_code_data)
        decoded_qr_code = decode(qr_code_image)
        if decoded_qr_code:
            # Extract the username and password from the QR code
            qr_code_info = decoded_qr_code[0].data.decode('utf-8')
            username, password = qr_code_info.split(',')
            # Render the login page with the QR code data
            return render_template('login_with_qr.html', qr_code=base64.b64encode(qr_code_image.read()).decode('utf-8'))
    # Render the login page without QR code data
    return render_template('login_with_qr.html', qr_code=None)

@app.route('/qr_generator', methods=['GET', 'POST'])
def qr_generator():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        qr_code_img = generate_qr_code(username, password)
        
        # Save the image to a BytesIO buffer
        img_buffer = BytesIO()
        qr_code_img.save(img_buffer, format='PNG')
        
        # Encode the image buffer to base64
        qr_code_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        
        return render_template('qr_generator.html', qr_code=qr_code_base64)
    return render_template('qr_generator.html')

# Main route
@app.route('/')
def index():
    return render_template('nv_number_form.html')

# Route to access the sending email page
@app.route('/send_email_page')
def send_email_page():
    return render_template('send_email_page.html', specialties=TEAM_MEMBERS.keys())

# Display student's classes route
@app.route('/display_classes', methods=['POST'])
def display_classes():
    nv_number = preprocess_nv_number(request.form['nv_number'])
    student_data = students.get(nv_number)
    if student_data:
        return render_template('class_selection.html', student_name=student_data['Name'], classes=student_data['Classes'])
    else:
        return render_template('nv_number_not_found.html', nv_number=nv_number)
# Add route for displaying student timetable
    
@app.route('/timetable/<nv_number>')
def timetable(nv_number):
    student_data = students.get(nv_number)
    if student_data:
        return render_template('timetable.html', student_name=student_data['Name'], timetable=student_data['Timetable'])
    else:
        return render_template('nv_number_not_found.html', nv_number=nv_number)

# Check class route
@app.route('/check_class', methods=['POST'])
def check_class():
    subject = request.form['subject']
    class_name = get_class_name(subject)
    # You can add logic here to fetch the image based on the subject if needed
    image_filename = f"{subject.lower()}.jpg"  # Example filename
    return render_template('class_result.html', subject=subject, class_name=class_name, image_filename=image_filename)

@app.route('/admin_panel')
def admin_panel():
    students = get_students()  # Retrieve students data
    return render_template('admin_panel.html', students=students)

# Route to update student data
@app.route('/update_student', methods=['POST'])
def update_student():
    nv_number = request.form['nv_number']
    updated_data = {
        'Name': request.form['name'],
        # Add other updated fields here
    }
    update_student_data(nv_number, updated_data)
    # Redirect to admin panel after updating
    return redirect(url_for('admin_panel'))

@app.route('/login')
def login():
    return render_template('login.html')

# Route to render the FAQ page
@app.route('/faq')
def faq():
    return render_template('faq.html')

# Define team members
TEAM_MEMBERS = {
    "Academic": {
        1: {"name": "Nabih Aziz", "email": "nabih.aziz@example.com"},
        2: {"name": "Dr. Mussab Z. Aswad", "email": "nv21053@nvtc.edu.bh"},
        3: {"name": "Basma Mohamed Al Balooshi", "email": "basma.balooshi@example.com"},
        4: {"name": "Sana Abdulrahman", "email": "nv21043@nvtc.edu.bh"}
    },
    "Vocational": {
        1: {"name": "Franklin F. Narag Bosi", "email": "franklin.bosi@example.com"},
        2: {"name": "Raghavendra Shenoy", "email": "raghavendra.shenoy@example.com"}
    }
}

# Define the send_email function to send meeting requests
def send_email(recipient, subject, body):
    try:
        with yagmail.SMTP(SENDER_EMAIL, SENDER_APP_PASSWORD) as yag:
            yag.send(recipient, subject, body)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def preprocess_nv_number(nv_number):
    # Remove any non-alphanumeric characters and convert to uppercase
    nv_number = ''.join(char for char in nv_number if char.isalnum()).upper()
    # Add "NV" prefix if missing
    if not nv_number.startswith("NV"):
        nv_number = "NV" + nv_number
    return nv_number

# Function to retrieve class name based on subject
def get_class_name(subject):
    for student_data in students.values():
        class_name = student_data['Classes'].get(subject)
        if class_name:
            return class_name
    return None

# Route to select specialty
@app.route('/select_specialty')
def select_specialty():
    display_specialties()
    return render_template('select_specialty.html', specialties=TEAM_MEMBERS.keys())

# Route to select team member
@app.route('/select_team_member', methods=['POST'])
def select_team_member():
    specialty = request.form['specialty']
    team_members = TEAM_MEMBERS.get(specialty, {})
    return render_template('select_team_member.html', specialty=specialty, team_members=team_members)

# Route to send meeting request
@app.route('/send_meeting_request', methods=['POST'])
def send_meeting_request():
    team_member_email = request.form['team_member_email']
    guest_name = request.form['guest_name']
    meeting_time = request.form['meeting_time']
    subject = f"Meeting Request from {guest_name}"
    body = f"Hi,\n\nMr/s {guest_name} would like to meet you at {meeting_time}.\n\nBest regards,\nYour Guest"
    send_email(team_member_email, subject, body)
    return redirect(url_for('index'))

def display_specialties():
    print("Available Specialties:")
    for i, specialty in enumerate(TEAM_MEMBERS, start=1):
        print(f"{i}. {specialty}")

def choose_specialty():
    while True:
        try:
            specialty_choice = int(input("Enter the number of your preferred specialty: "))
            specialties = list(TEAM_MEMBERS.keys())
            if 1 <= specialty_choice <= len(specialties):
                return specialties[specialty_choice - 1]
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_team_member(specialty):
    team_member_list = TEAM_MEMBERS.get(specialty, {})
    if not team_member_list:
        print(f"No team members found for {specialty}.")
        return

    print(f"Team members in {specialty}:")
    for num, member in team_member_list.items():
        print(f"{num}. {member['name']} ({member['email']})")

    while True:
        try:
            team_member_choice = int(input("Enter the number of your preferred team member: "))
            if team_member_choice in team_member_list:
                selected_member = team_member_list[team_member_choice]
                print(f"Selected team member: {selected_member['name']} ({selected_member['email']})")

                # Get guest name and meeting time
                guest_name = input("Enter your name: ")
                meeting_time = input("Enter the meeting time (e.g., 2:00 PM): ")

                # Compose email
                subject = f"Meeting Request from {guest_name}"
                body = f"Hi {selected_member['name']},\n\nMr/s {guest_name} would like to meet you at {meeting_time}.\n\nBest regards,\nYour Guest"

                # Send email
                send_email(selected_member['email'], subject, body)
                break
            else:
                print("Invalid choice. Please enter a valid team member number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    app.run(debug=True)

