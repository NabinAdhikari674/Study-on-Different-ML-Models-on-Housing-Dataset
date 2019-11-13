#Roll No. : 45,46,47,48
#Project : Compare LR,Plynomial Regression, DT Regressor and RF Regressor
#Housing Prices Dataset : https://www.kaggle.com/apratim87/housingdata


print("\n********Importing to main.py ...**********")
from pre_processor import Xtrain,Xtest,Ytrain,Ytest,np
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
print("\n\n\tRunning main.py\n")


lr=LinearRegression()
pr1=LinearRegression()
pr2=LinearRegression()
quadratic1=PolynomialFeatures(degree=2)
quadratic2=PolynomialFeatures(degree=3)
dtr=DecisionTreeRegressor(max_depth=3)
rfr = RandomForestRegressor(n_estimators=100)



Xquad1=quadratic1.fit_transform(Xtrain)
Xquad2=quadratic2.fit_transform(Xtrain)

lr.fit(Xtrain,Ytrain)
pr1.fit(Xquad1,Ytrain)
pr2.fit(Xquad2,Ytrain)


y_lin_pred=lr.predict(Xtest)
y_quad1_pred=pr1.predict(quadratic1.fit_transform(Xtest))
y_quad2_pred=pr2.predict(quadratic2.fit_transform(Xtest))
print("Training MSE => Linear : %.3f, \n\tQuadratic1(d=2) : %.3f, \n\tQuadratic2(d=3) : %.3f"%(mean_squared_error(Ytest,y_lin_pred),
                                                                                        mean_squared_error(Ytest,y_quad1_pred),
                                                                                        mean_squared_error(Ytest,y_quad2_pred)))
print("Training R2 score => Linear : %.3f, \n\tQuadratic(d=2) : %.3f, \n\tQuadratic2(d=3) : %.3f"%(r2_score(Ytest,y_lin_pred),
                                                                                      r2_score(Ytest,y_quad1_pred),
                                                                                      r2_score(Ytest,y_quad2_pred)))


dtr.fit(Xtrain,Ytrain)
dtr_pred=dtr.predict(Xtest)
print("Training MSE => DTR : %.3f"%(mean_squared_error(Ytest,dtr_pred)))
print("Training R2 score => DTR : %.3f"%(r2_score(Ytest,dtr_pred)))

rfr.fit(Xtrain,Ytrain)
rfr_pred=rfr.predict(Xtest)
print("Training MSE => RFR : %.3f"%(mean_squared_error(Ytest,rfr_pred)))
print("Training R2 score => RFR : %.3f"%(r2_score(Ytest,rfr_pred)))

#plt.scatter(Xtest,Ytest,label='Testing Points')
#plt.plot(Xtest,dtr_pred,label='DT Regression',color='red')
#plt.legend()
#plt.show()


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

print("Done")
