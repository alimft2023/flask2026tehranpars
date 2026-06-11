from flask import Flask, render_template, redirect, url_for, request
from models import Student

app = Flask(__name__)


@app.route("/")
def index():
    students = Student.select().order_by(Student.id.desc())
    return render_template("index.html", sts=students)


@app.route('/details/<int:id>')
def details(id):
    st = Student.get_by_id(id)
    return render_template('details.html', s=st)


@app.route('/delete/<int:id>')
def delete(id):
    st = Student.get_by_id(id)
    st.delete_instance()
    return redirect(url_for('index'))


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        Student.create(sname=fname, sfamily=lname, age=age)
        return redirect('index')
    return render_template('create.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    st = Student.get_by_id(id)
    if request.method == 'POST':
        st.sname = request.form['name']
        st.sfamily = request.form['family']
        st.age = request.form['age']
        st.save()
        return redirect(url_for('index'))
    return render_template('update.html', s=st)


if __name__ == "__main__":
    app.run(debug=True)
