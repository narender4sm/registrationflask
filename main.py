from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        fullname = request.form['fullname']
        htnumber = request.form['htnumber']
        branch = request.form['branch']
        section = request.form['section']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        gender = request.form['gender']
        image = request.form['image']
        address = request.form['address']
        return render_template('success.html')
    else:
        return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)