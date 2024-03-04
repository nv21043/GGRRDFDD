from flask import Flask, render_template, request, redirect, url_for
from data_handler import get_students, save_students

app = Flask(__name__)

students = get_students()
# Route to display the admin panel
@app.route('/admin_panel')
def admin_panel():
    students = get_students()  # Retrieve students data
    return render_template('admin_panel.html', students=students)

@app.route('/admin/view_students')
def view_students():
    return render_template('view_students.html', students=students)

@app.route('/admin/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Add new student to the students dictionary
        # Update students data in the data handler
        save_students(students)
        return redirect(url_for('view_students'))
    return render_template('add_student.html')

@app.route('/admin/edit_student/<nv_number>', methods=['GET', 'POST'])
def edit_student(nv_number):
    if request.method == 'POST':
        # Edit existing student in the students dictionary
        # Update students data in the data handler
        save_students(students)
        return redirect(url_for('view_students'))
    return render_template('edit_student.html', student=students.get(nv_number))

@app.route('/admin/delete_student/<nv_number>')
def delete_student(nv_number):
    # Delete student from the students dictionary
    # Update students data in the data handler
    save_students(students)
    return redirect(url_for('view_students'))

if __name__ == "__main__":
    app.run(debug=True)
