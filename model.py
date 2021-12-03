import numpy as np
import pickle
import json

with open('columns_house.json', 'r') as f1:
    col = json.load(f1)

columns = col['columns']

with open('Pickle_LR_Model.pkl', 'rb') as file:
    pickle_lr_model = pickle.load(file)


def get_predicted_price(sqft, avail, bhk, bath, balc, loc):#values
    x_test = np.zeros(233)

    x_test[0] = (52272 - sqft) / (52272 - 1)  # total_sqft

    for i in range(0, 233):  # availability
        if avail == columns[i]:
            x_test[i] = 1

    for i in range(0, 233):  # bhk
        if bhk == columns[i]:
            x_test[i] = 1

    for i in range(0, 233):  # bath
        if bath == columns[i]:
            x_test[i] = 1

    for i in range(0, 233):  # balcony
        if balc == columns[i]:
            x_test[i] = 1

    for i in range(0, 233):  # location
        if loc == columns[i]:
            x_test[i] = 1

    price = pickle_lr_model.predict([x_test])
    return price[0]