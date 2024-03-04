import yagmail
import os
# Set your sender email and app password
SENDER_EMAIL = "nvtcbookingsystem@gmail.com"
SENDER_APP_PASSWORD = "Nvtc@1234"  # Replace with your actual app password

# ... (other parts of your code)

def send_email(recipient, subject, body):
    try:
        with yagmail.SMTP(SENDER_EMAIL, SENDER_APP_PASSWORD) as yag:
            yag.send(recipient, subject, body)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# ... (rest of your code)


# Define team members
TEAM_MEMBERS = {
    "Academic": {
        1: {"name": "Nabih Aziz", "email": "nabih.aziz@example.com"},
        2: {"name": "Dr. Mussab Z. Aswad", "email": "mussab.aswad@example.com"},
        3: {"name": "Basma Mohamed Al Balooshi", "email": "basma.balooshi@example.com"},
        4: {"name": "Sana Abdulrahman", "email": "nv21043@nvtc.edu.bh"}
    },
    "Vocational": {
        1: {"name": "Franklin F. Narag Bosi", "email": "franklin.bosi@example.com"},
        2: {"name": "Raghavendra Shenoy", "email": "raghavendra.shenoy@example.com"}
    }
}

def send_email(recipient, subject, body):
    try:
        with yagmail.SMTP(SENDER_EMAIL, SENDER_APP_PASSWORD) as yag:
            yag.send(recipient, subject, body)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

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

# Call this function to demonstrate the process
display_specialties()
chosen_specialty = choose_specialty()
choose_team_member(chosen_specialty)
