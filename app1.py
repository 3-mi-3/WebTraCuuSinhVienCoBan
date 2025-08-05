import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash

# Khởi tạo Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Kết nối Firebase
cred = credentials.Certificate("qlsinhvien-6204c-firebase-adminsdk-fbsvc-35ea0603be.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Giao diện chính với tìm kiếm
@app.route('/')
def index():
    keyword = request.args.get('q', '').lower()
    students = db.collection('students').stream()
    student_list = []
    for s in students:
        data = s.to_dict()
        data['code'] = s.id
        if keyword in data['code'].lower() or keyword in data['name'].lower():
            student_list.append(data)
        elif not keyword:
            student_list.append(data)
    return render_template('index.html', students=student_list, keyword=keyword)

# Thêm sinh viên
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        birthdate = request.form['birthdate']
        class_name = request.form['class_name']
        hometown = request.form['hometown']

        if not code or not name or not class_name or not birthdate or not hometown:
            flash('Vui lòng nhập đủ thông tin!', 'error')
            return redirect(url_for('add'))

        db.collection('students').document(code).set({
            'name': name,
            'birthdate': birthdate,
            'class_name': class_name,
            'hometown': hometown
        })
        flash('Thêm sinh viên thành công!', 'success')
        return redirect(url_for('index'))

    return render_template('form.html')

# Sửa sinh viên
@app.route('/edit/<code>', methods=['GET', 'POST'])
def edit(code):
    student_doc = db.collection('students').document(code).get()
    if not student_doc.exists:
        flash('Sinh viên không tồn tại!', 'error')
        return redirect(url_for('index'))

    student = student_doc.to_dict()
    student['code'] = code

    if request.method == 'POST':
        name = request.form['name']
        birthdate = request.form['birthdate']
        class_name = request.form['class_name']
        hometown = request.form['hometown']

        db.collection('students').document(code).update({
            'name': name,
            'birthdate': birthdate,
            'class_name': class_name,
            'hometown': hometown
        })
        flash('Cập nhật thành công!', 'success')
        return redirect(url_for('index'))

    return render_template('form.html', student=student)

# Xóa sinh viên
@app.route('/delete/<code>', methods=['POST'])
def delete(code):
    db.collection('students').document(code).delete()
    flash('Xóa thành công!', 'success')
    return redirect(url_for('index'))

# API: Lấy danh sách sinh viên
@app.route('/api/students', methods=['GET'])
def get_all():
    students = db.collection('students').stream()
    result = []
    for s in students:
        data = s.to_dict()
        data['code'] = s.id
        result.append(data)
    return jsonify(result)

# API: Tìm sinh viên theo mã
@app.route('/api/students/<code>', methods=['GET'])
def get_student(code):
    doc = db.collection('students').document(code).get()
    if doc.exists:
        data = doc.to_dict()
        data['code'] = code
        return jsonify(data)
    return jsonify({'error': 'Không tìm thấy sinh viên'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

