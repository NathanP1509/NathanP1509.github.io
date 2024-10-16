from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Fungsi untuk membaca data kursus dari file CSV
def load_courses():
    courses = []
    with open('courses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            courses.append(row)
    return courses

# Rute untuk halaman utama
@app.route('/')
def home():
    return render_template('home.html')

# Rute untuk halaman daftar kursus
@app.route('/courses')
def courses():
    courses = load_courses()
    return render_template('courses.html', courses=courses)

# Rute untuk halaman pendaftaran kursus
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course_id = request.form['course_id']
        
        # Simpan data registrasi ke file CSV (atau database lainnya)
        with open('registrations.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, course_id])
        
        return redirect('/')
    
    courses = load_courses()
    return render_template('register.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
