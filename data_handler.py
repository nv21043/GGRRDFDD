# data_handler.py


def get_students():
    students = {
        'NV21039': {
            'Name': 'Sayed Ahmed Mohmed Ahmed Marhoom',
            'Classes': {
                'Mathematics': 'B1',
                'English': 'A2',
                'Science': 'B4',
                'History': 'A5',
                'Geography': 'B2',
                'Art': 'A8',
                'Physical Education': 'B7',
                'Music': 'A3',
                'Computer Science': 'B9',
                'Arabic': 'A6'
            },
            'Timetable': {
                'Monday': [
                    {'time': '9:00 AM', 'subject': 'Mathematics'},
                    {'time': '11:00 AM', 'subject': 'English'},
                    # Add more entries for Monday as needed
                ],
                'Tuesday': [
                    {'time': '10:00 AM', 'subject': 'Science'},
                    {'time': '1:00 PM', 'subject': 'History'},
                    # Add more entries for Tuesday as needed
                ],
                # Add entries for other days of the week similarly
            }
        },
        'NV21040': {
            'Name': 'Turki Khaled Ali Aljashari',
            'Classes': {
                'Mathematics': 'A1',
                'English': 'B4',
                'Science': 'A3',
                'History': 'B7',
                'Geography': 'A6',
                'Art': 'B2',
                'Physical Education': 'A5',
                'Music': 'B9',
                'Computer Science': 'A8',
                'Arabic': 'B3'
            },
            'Timetable': {
                # Define timetable for NV21040 similarly as above
            }
        },
        'NV21041': {
            'Name': 'Humood Rashed Ali Alkaabi',
            'Classes': {
                'Mathematics': 'B1',
                'English': 'A2',
                'Science': 'B4',
                'History': 'A5',
                'Geography': 'B2',
                'Art': 'A8',
                'Physical Education': 'B7',
                'Music': 'A3',
                'Computer Science': 'B9',
                'Arabic': 'A6'
            },
            'Timetable': {
                # Define timetable for NV21041 similarly as above
            }
        }
        # Add other students' data here
    }
    return students

def save_students(students):
    # You can implement saving students data to a database or file here
    # For example, you can use SQLAlchemy to save it to a database
    pass
# data_handler.py

# data_handler.py


def update_student_data(nv_number, updated_data):
    students = get_students()
    if nv_number in students:
        students[nv_number] = updated_data
        save_students(students)
        return True  # Return True to indicate successful update
    else:
        return False  # Return False if the student does not