from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = 'http://localhost:5000/api/students'

# Trang nhập mã và xem thông tin
@app.route('/', methods=['GET', 'POST'])
def index():
    student = None
    if request.method == 'POST':
        code = request.form['code']
        response = requests.get(f'{API_URL}/{code}')
        if response.status_code == 200:
            student = response.json()
        else:
            student = {'error': 'Không tìm thấy sinh viên'}
    return render_template('search.html', student=student)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
