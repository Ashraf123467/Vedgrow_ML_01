# Vedgrow_ML_01 - 🌸 Iris Flower Classification using Machine Learning

## 📌 Project Overview

This project focuses on building a machine learning model to classify iris flowers into three species — **Setosa, Versicolor, and Virginica** — based on their physical features.

The project includes:

* Exploratory Data Analysis (EDA)
* Model training using multiple algorithms
* Performance evaluation
* Visualization of results

---

## 📊 Dataset Description

The dataset used is the **Iris dataset**, a classic dataset in machine learning.

### 🔹 Features:

* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)

### 🔹 Target Classes:

* 0 → Setosa
* 1 → Versicolor
* 2 → Virginica

  <img width="419" height="210" alt="image" src="https://github.com/user-attachments/assets/1e672aa0-817a-47bb-8925-bffc1eadf7d1" />



### 🔹 Dataset Info:

* Total samples: **150**
* Each class: **50 samples**
* Type: **Multiclass Classification**

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was performed to understand relationships between features and class separability.

### 📈 Key Insights:

* **Petal length and petal width are the most important features**
* Setosa is clearly separable from other classes
* Versicolor and Virginica show slight overlap

### 📊 Visualizations Used:

* Pairplot (feature relationships)
* Histograms (distribution)
* Boxplots (outliers)
* Heatmap (feature correlation)
* Scatter plots (class separation)
* Violin plots (distribution comparison)

---

## 🤖 Models Used

The following machine learning models were implemented and compared:

* K-Nearest Neighbors (KNN)
* Decision Tree
* Support Vector Machine (SVM)
* Random Forest (Ensemble Model)

---

## 📊 Model Performance

| Model         | Test Accuracy | Cross Validation Accuracy |
| ------------- | ------------- | ------------------------- |
| KNN           | 1.00          | ~0.95–0.96                |
| Decision Tree | 1.00          | ~0.93–0.95                |
| SVM           | 1.00          | ~0.95–0.96                |
| Random Forest | 1.00          | ~0.95–0.96                |

### 🧠 Key Observation:

Although all models achieved **100% accuracy on the test set**, cross-validation revealed a more realistic accuracy of around **95–96%**, indicating strong generalization performance.

---

## 📉 Confusion Matrix

Confusion matrix was used to evaluate classification performance:

* Shows correct vs incorrect predictions
* Helps identify misclassification between classes

---

## 🔥 Feature Importance (Random Forest)

Feature importance analysis revealed:

* **Petal Length and Petal Width** are the most influential features
* Sepal features contribute less to classification

---

## 🔮 Prediction System

A prediction system was built to classify new flower inputs:

Example:

```python
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)
```

---

## 🚀 Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 💡 Conclusion

* The Iris dataset is well-structured and easy to classify
* Multiple models achieved high accuracy due to clear class separation
* Cross-validation ensured reliable performance evaluation
* Ensemble methods like Random Forest provided robust results

---

## ⚠️ Limitations

* Small dataset (150 samples)
* May not generalize well to real-world noisy data
* Limited feature complexity

---

## 🌟 Future Improvements

* Hyperparameter tuning (GridSearchCV)
* Deployment using Streamlit
* Testing on custom datasets
* Model optimization for real-world use

---

## 🙌 Author

**Ashraf Shikalgar**
Machine Learning Enthusiast 🚀

---

## VISUALISATIONS


