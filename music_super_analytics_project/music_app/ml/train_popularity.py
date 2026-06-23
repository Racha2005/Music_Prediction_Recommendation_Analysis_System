import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib, os

BASE = os.path.join(os.path.dirname(__file__), "..", "data")
df = pd.read_csv(os.path.join(BASE, "music_dataset_500.csv"))
X = df[['duration_sec','danceability','energy','acousticness','valence','tempo']]
y = df['popularity']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Train R^2:", model.score(X_test, y_test))
joblib.dump(model, os.path.join(os.path.dirname(__file__), "..", "models", "popularity_rf.joblib"))
