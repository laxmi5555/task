from flask import Flask,request,jsonify,render_template
from model import get_predicted_price
import house_db

app = Flask(__name__)

#################### Default API ##############################
@app.route('/')
def start():
    return render_template('login.html')


#################### Default API ##############################
@app.route('/reg')
def call_register_page():
    return render_template('register.html')


#################### Registration API ##############################
@app.route('/register',methods = ['POST'])
def user_registration():
    if request.method == 'POST':
        data = request.form
        print(data)
        response = house_db.register_user(data)
        print("Response :",response)

    return jsonify({"Message":"Successfully Registered"})

#################### Login API ##############################
@app.route('/login',methods = ['POST'])
def user_login():
    if request.method == 'POST':
        data = request.form
        response1 = house_db.login_user(data) 
        print('response1',response1)   
    if response1 == 0:
        return jsonify({"Message":"Invalid user id or Password"})
    else:
        return render_template('Request_form.html')

################## Prediction of House Price ######################
@app.route('/prediction', methods = ['POST'])
def prediction():
    if request.method == 'POST':

        user_data = request.form

        if not user_data:
            return jsonify({'Message': 'Enter the required fields'})

        total_sqft = int(user_data['total_sqft'])
        bhk = user_data['bhk']
        bath = float(user_data['bath'])
        location = user_data['location']
        availability = user_data['availability']
        balcony = float(user_data['balcony'])

        price = get_predicted_price(total_sqft,availability,bhk,bath,balcony,location)

        response = house_db.save_house_data(total_sqft,availability,bhk,bath,balcony,location,price)
        return jsonify({'Message':response})

        #return jsonify({"Message" : f"Predicted house price is : {price}" })

    else:
        return jsonify({"Message" : "Not Successful"})


#################### Main app run ##############################
if __name__ == "__main__":
    app.run()