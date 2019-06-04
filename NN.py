data=pd.read_csv('Dataset2.csv', low_memory=False)

def preprocessing(data)
    data['Date']=pd.to_datetime(data['Date'])
    data['day_of_week']=data['Date'].dt.dayofweek
    data['Weekend']=round(data['day_of_week']9,0)
    data['one_day_mean']=data['System_Load'].rolling(window=24).mean()
    data['shift_day']=data['System_Load'].shift(24)
    data['shift_week']=data['System_Load'].shift(168)
    data['relative']=(data['Date']-data['Date'][0])pd.Timedelta('1 day')
    data.fillna(0,inplace=True)
    return data

preprocessing(data)
X=data.drop(['Date','System_Load'],axis=1)
Y=data['System_Load'].ravel()

split_test_size=0.3

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest= train_test_split(X,Y, test_size=split_test_size, random_state=5,shuffle=False)

from sklearn.neural_network import MLPRegressor
mlp=MLPRegressor(random_state=1,hidden_layer_sizes=(10,))
mlp.fit(X,Y)

# save the model to disk
import pickle
pickle.dump(mlp, open('model.pkl','wb'))