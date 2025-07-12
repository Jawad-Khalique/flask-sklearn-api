import sklearn
from sklearn.ensemble import RandomForestClassifier
import joblib

iris = sklearn.datasets.load_iris()

X,y = iris.data, iris.target

model = RandomForestClassifier()

model.fit(X,y)

joblib.dump(model, 'model.pkl')
print('Model saved as model.pkl')