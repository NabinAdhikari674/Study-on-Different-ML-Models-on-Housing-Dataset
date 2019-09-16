#Roll No. : 45,46,47,48
#Project : Compare LR,Plynomial Regression, DT Regressor and RF Regressor
#Housing Prices Dataset : https://www.kaggle.com/apratim87/housingdata


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
print("Import Done\n")

df=pd.read_excel("houseData.xls")
df.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(df.head())
print("\n")

cols=['LSTAT','INDUS','NOX','RM','MEDV']

x=df['RM'].values
y=df['MEDV'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
x_train=x_train.reshape(-1,1)
x_test=x_test.reshape(-1,1)

lr=LinearRegression()
pr1=LinearRegression()
pr2=LinearRegression()
quadratic1=PolynomialFeatures(degree=2)
quadratic2=PolynomialFeatures(degree=3)



x_quad1=quadratic1.fit_transform(x_train)
x_quad2=quadratic2.fit_transform(x_train)

lr.fit(x_train,y_train)
pr1.fit(x_quad1,y_train)
pr2.fit(x_quad2,y_train)


'''
y_lin_fit=lr.predict(x_test)
y_quad1_fit=pr1.predict(quadratic1.fit_transform(x_test))
y_quad2_fit=pr2.predict(quadratic2.fit_transform(x_test))

plt.scatter(x_test,y_test,label='Training Points')
plt.plot(x_test,y_lin_fit,label='Linear Fit',linestyle='-')
plt.plot(x_test,y_quad1_fit,label='Quadratic Fit1(d=2)')
plt.plot(x_test,y_quad2_fit,label='Quadratic Fit2(d=3)')
plt.legend(loc='upper left')
plt.show()
#'''

y_lin_pred=lr.predict(x_test)
y_quad1_pred=pr1.predict(quadratic1.fit_transform(x_test))
y_quad2_pred=pr2.predict(quadratic2.fit_transform(x_test))
print("Training MSE => Linear : %.3f, \n\tQuadratic1(d=2) : %.3f, \n\tQuadratic2(d=3) : %.3f"%(mean_squared_error(y_test,y_lin_pred),
                                                                                        mean_squared_error(y_test,y_quad1_pred),
                                                                                        mean_squared_error(y_test,y_quad2_pred)))
print("Training R2 score => Linear : %.3f, \n\tQuadratic(d=2) : %.3f, \n\tQuadratic2(d=3) : %.3f"%(r2_score(y_test,y_lin_pred),
                                                                                      r2_score(y_test,y_quad1_pred),
                                                                                      r2_score(y_test,y_quad2_pred)))

dtr=DecisionTreeRegressor(max_depth=3)
dtr.fit(x_train,y_train)
dtr_pred=dtr.predict(x_test)
print("Training MSE => DTR : %.3f"%(mean_squared_error(y_test,dtr_pred)))
print("Training R2 score => DTR : %.3f"%(r2_score(y_test,dtr_pred)))
plt.scatter(x_test,y_test,label='Testing Points')
plt.plot(x_test,dtr_pred,label='DT Regression',color='red')
plt.legend()
plt.show()

print("Done")
