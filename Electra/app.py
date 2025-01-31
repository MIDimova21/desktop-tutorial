import random
import threading
from flask import Flask, render_template, request, redirect, url_for, session

from Electra.BusinessLayer.user_model import UserModel
from Electra.BusinessLayer.user_service import UserService

from Electra.BusinessLayer.profiles_service import ProfilesService
from Electra.BusinessLayer.profiles_model import ProfileModel

from Electra.BusinessLayer.addresses_service import AddressesService
from Electra.BusinessLayer.addresses_model import AddressModel

from Electra.DataAccessLayer.electricity_usage import ElectricityUsage

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        profile = ProfilesService()
        exist_email = profile.check_profile(email, 1)
        exist_password = profile.check_profile(password, 2)
        if exist_email and exist_password:
            return render_template('home.html')
        else:
            error = "Invalid email or password!"
    return render_template('login.html', error=error)



@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    error = None
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['repeat_password']
        region = request.form['region']
        city = request.form['city']

        if len(password) < 8:
            error = "Weak password! (Must to be over 8 symbols)"
        elif password == confirm_password:
            user_id = random.randint(10, 100)
            user = UserModel(user_id, first_name, last_name, age)
            user_service = UserService()
            user_service.add_user(user)

            profile_id = user_id
            profile = ProfileModel(profile_id, email, password, user_id)
            profile_service = ProfilesService()
            profile_service.add_profile(profile)

            address_id = user_id
            address = AddressModel(address_id, region, city, user_id)
            address_service = AddressesService()
            address_service.add_address(address)
            return redirect(url_for('login'))
        else:
            error = "Invalid password!"
    return render_template('registration.html', error=error)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/consumption')
def consumption():
    electricity_usage = ElectricityUsage()
    data = electricity_usage.read_all_electricity_usages()
    return render_template('consumption.html', data=data)



def send_contact_email(name, email, message):
    import time
    time.sleep(5)
    print(f"Email sent from: {name} ({email}) says '{message}'")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')


        thread = threading.Thread(target=send_contact_email, args=(name, email, message))
        thread.start()

        return render_template('contact.html', message="Thank you for contacting us. We will get back to you soon!")

    return render_template('contact.html')


if __name__ == '__main__':
    app.run()