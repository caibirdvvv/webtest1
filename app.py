from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 获取表单数据
    name = request.form['name']
    gender = request.form['gender']
    idNumber = request.form['idNumber']
    address = request.form['address']
    phone = request.form['phone']
    insurance = request.form['insurance']
    insuranceNumber = request.form.get('insuranceNumber', '')

    # 将数据传递给success页面
    return render_template('success.html', name=name, gender=gender, idNumber=idNumber,
                           address=address, phone=phone, insurance=insurance,
                           insuranceNumber=insuranceNumber)

if __name__ == '__main__':
    app.run(debug=True)
