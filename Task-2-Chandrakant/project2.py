# Project 2 : Data Classification Using AI 
# Name : Chandrakant Mahto
# Internship : DecodeLabs AI Internship

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Load Iris Dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add Species Column
df["Species"] = iris.target

print("First 5 Rows\n")
print(df.head())

print("\nDataset Information\n")
df.info()

print("\nStatistical Summary\n")
print(df.describe())


# Features and Labels
X = iris.data
y = iris.target


# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Create KNN Model
model = KNeighborsClassifier(n_neighbors=3)

# Train Model
model.fit(X_train, y_train)

# Make Prediction
y_pred = model.predict(X_test)


# Evaluate Model
print("\nAccuracy :", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))


# Scatter Plot
plt.figure(figsize=(8, 5))

plt.scatter(
    df["sepal length (cm)"],
    df["petal length (cm)"],
    c=df["Species"],
    cmap="viridis"
)

plt.title("Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")

plt.show()


# User Prediction
print("\nPredict a Flower\n")

sepal_length = float(input("Sepal Length : "))
sepal_width = float(input("Sepal Width  : "))
petal_length = float(input("Petal Length : "))
petal_width = float(input("Petal Width  : "))

new_flower = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

new_flower = scaler.transform(new_flower)

prediction = model.predict(new_flower)

print("\nPredicted Flower :", iris.target_names[prediction[0]])