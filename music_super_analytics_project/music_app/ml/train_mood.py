import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib, os
BASE = os.path.join(os.path.dirname(__file__), "..", "data")
df = pd.read_csv(os.path.join(BASE, "music_dataset_500.csv"))
# synthetic mood label for demo
df['mood'] = ((df['valence']>0.5) & (df['energy']>0.5)).astype(int)
X = df[['danceability','energy','acousticness','valence']]
y = df['mood']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Test accuracy:", model.score(X_test, y_test))
os.makedirs(os.path.join(os.path.dirname(__file__), "..", "models"), exist_ok=True)
joblib.dump(model, os.path.join(os.path.dirname(__file__), "..", "models", "mood_rf.joblib"))
