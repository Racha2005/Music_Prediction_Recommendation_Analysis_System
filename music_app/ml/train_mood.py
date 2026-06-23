import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

from music_app.config import DATA_LOCAL, MODEL_MOOD

def load_df():
    print("Loading dataset:", DATA_LOCAL)
    return pd.read_csv(DATA_LOCAL)

def generate_mood_label(df):
    # Normalize thresholds
    high_valence = df["valence"] >= 0.5
    high_energy = df["energy"] >= 0.5

    conditions = [
        (high_valence & high_energy),
        (high_valence & ~high_energy),
        (~high_valence & high_energy),
        (~high_valence & ~high_energy)
    ]

    moods = ["Happy", "Calm", "Energetic", "Sad"]
    df["Mood"] = pd.Series(pd.Categorical(pd.cut(range(len(df)), 4, labels=moods)))

    df.loc[conditions[0], "Mood"] = "Happy"
    df.loc[conditions[1], "Mood"] = "Calm"
    df.loc[conditions[2], "Mood"] = "Energetic"
    df.loc[conditions[3], "Mood"] = "Sad"

    return df

def train_and_save():
    df = load_df()
    df = generate_mood_label(df)

    X = df[["danceability", "energy", "acousticness", "valence", "tempo"]]
    y = df["Mood"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    print(classification_report(y_test, preds))

    # Confusion Matrix
    cm = confusion_matrix(y_test, preds)
    plt.figure(figsize=(8, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap="Purples",
                xticklabels=model.classes_,
                yticklabels=model.classes_)
    plt.title("Mood Prediction Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    os.makedirs(os.path.dirname(MODEL_MOOD), exist_ok=True)
    joblib.dump(model, MODEL_MOOD)

    print("🎯 Saved mood model:", MODEL_MOOD)

if __name__ == "__main__":
    train_and_save()