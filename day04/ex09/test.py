import numpy as np
import pandas as pd
from ridge import Ridge as MyLR

#DataFrame
data = pd.read_csv("spacecraft_data.csv")
X = np.array(data[['Age','Thrust_power','Terameters']])
Y = np.array(data[['Sell_price']])
lr1 = MyLR([1.0,1.0,1.0,1.0])
lr2 = MyLR([1.0,1.0,1.0,1.0,1.0,1.0,1.0])


X = lr1.zscore_(X)
x_train, x_test, y_train, y_test = lr1.data_spliter_(X, Y, 0.5)
x_train2 =lr2.add_polynomial_features_(x_train, 2)

print(lr1.fit_(x_train, y_train))
print(lr1.cost_(x_train, y_train))
print(lr1.cost_.__doc__)

lr2.lambda_ = 0.0
print(lr2.fit_(x_train2, y_train))
while lr2.lambda_ <= 1:
    #print(lr2.fit_(x_train2, y_train))
    print(lr2.cost_(x_train2, y_train))
    print('')
    lr2.lambda_ += 0.1
