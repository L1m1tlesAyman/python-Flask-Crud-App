from flask import Flask,request,render_template,redirect,url_for,Response
import json
import re
from model.Student import Student

app = Flask(__name__)
student = Student()
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    limit = 5
    offset = (page - 1) * limit
    students = student.GetAll(limit, offset)
    total = student.CountAll()
    total_pages = (total // limit) + (1 if total % limit > 0 else 0)
    return render_template(
        'index.html',
        Students=students,
        page=page,
        total_pages=total_pages
    )

@app.route('/create', methods=['GET', 'POST'])
def create():
    errors = {}
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        gender = request.form['gender']
        # validation
        if not re.match(r'^[A-Za-z]{2,30}$', firstname):
            errors['firstname'] = "Invalid firstname"
        if not re.match(r'^[A-Za-z]{2,30}$', lastname):
            errors['lastname'] = "Invalid lastname"
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            errors['email'] = "Invalid email"
        if not re.match(r'^(Male|Female)$', gender):
            errors['gender'] = "Select Male or Female"
        if not errors:
            student.Create(firstname, lastname, email, gender)
            return redirect(url_for('index'))
    return render_template('auth/add.html', errors=errors)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    StudentFind = student.Find(id)
    errors = {}
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        gender = request.form['gender']
        # Validation
        if not re.match(r'^[A-Za-z]{2,30}$', firstname):
            errors['firstname'] = "Invalid firstname"
        if not re.match(r'^[A-Za-z]{2,30}$', lastname):
            errors['lastname'] = "Invalid lastname"
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            errors['email'] = "Invalid email"
        if not re.match(r'^(Male|Female)$', gender):
            errors['gender'] = "Invalid gender"
        if not errors:
            student.Update(id, firstname, lastname, email, gender)
            return redirect(url_for('index'))
        return render_template('auth/update.html',student=StudentFind,errors=errors)
    return render_template('auth/update.html',student=StudentFind,errors={})

@app.route('/delete/<id>')
def delete(id):
    student.Remove(id)
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('search')
    results = student.Finds(query)
    return render_template(
    'index.html',
    Students=results,
    page=1,
    total_pages=1
)

@app.route('/export/json')
def export_json():
    data = student.GetALL()
    with open("students.json","w") as f:
        json.dump(data,f,indent=4,default=str)
        return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)