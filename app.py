import streamlit as st
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# -------------------------------
# Load Dataset
# -------------------------------
iris = load_iris()
X = iris.data
y = iris.target

# Train Model (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Iris Classifier", page_icon="🌸")

st.title("🌸 Iris Flower Classification App")
st.write("Predict the species of Iris flower using Machine Learning 🤖")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("Input Features")

def user_input():
    sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
    sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
    petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
    petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

    data = {
        "sepal length (cm)": sepal_length,
        "sepal width (cm)": sepal_width,
        "petal length (cm)": petal_length,
        "petal width (cm)": petal_width
    }

    return pd.DataFrame(data, index=[0])

input_df = user_input()

# -------------------------------
# Show Input
# -------------------------------
st.subheader("📊 User Input Features")
st.write(input_df)

# -------------------------------
# Prediction
# -------------------------------
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

species = iris.target_names[prediction][0]

# -------------------------------
# Output
# -------------------------------
st.subheader("🌼 Prediction Result")
st.success(f"Predicted Flower: {species}")

st.subheader("📈 Prediction Probability")
prob_df = pd.DataFrame(prediction_proba, columns=iris.target_names)
st.write(prob_df)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Built by **Ashraf Shikalgar** 🚀")