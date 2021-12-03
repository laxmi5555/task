from pymongo import MongoClient


mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['house_data']

collection_user = db['user_details']
collection_prediction = db['prediction_details']

def register_user(user_data):
    
    name = user_data['name']
    password = user_data['password']
    emailid = user_data['emailid']
    phone_num = user_data['phone']
    dob = user_data['dob']

    print('name,password,emailid,phone_num,dob',name,password,emailid,phone_num,dob)
    collection_user.insert_one({"Name":name,"Password":password,"Email ID":emailid,
                                "Phone Number": phone_num, 'Date of Birth':dob})
                
    return 'Success'

def login_user(user_data):
    
    emailid = user_data['emailid']
    password = user_data['password']
    
    print(f'emailid == {emailid} \n password == {password}')
    response = collection_user.find_one({"Password":password,"Email ID":emailid})
    print('response',response) 
    if not response:
        return 0

    return 1

def save_house_data(total_sqft,availability,bhk,bath,balcony,location,price):

    location,total_sqft,bhk,bath
    collection_prediction.insert_one({"location":location,
                                        "total_sqft":total_sqft,
                                        "availability":availability,
                                        "balcony":balcony,
                                        "bhk":bhk,
                                        "bath": bath,
                                        "Predicted Price":price})


    return 'Data Saved Successfully'