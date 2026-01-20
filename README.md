# ✈️ Flight Price Prediction

This project focuses on building a **machine learning regression model** to predict flight ticket prices based on travel details such as airline, source, destination, duration, and number of stops.

---

## 🔍 Project Workflow

### 1. 📂 Data Preparation
- Loaded the flight price dataset
- Removed unnecessary columns
- Handled missing values
- Converted date and time features into meaningful components

---

### 2. 📊 Exploratory Data Analysis (EDA)
- Analyzed price distribution across airlines and routes
- Studied the impact of:
  - Number of stops
  - Journey duration
  - Airline type
- Visualized relationships using **Matplotlib** and **Seaborn**

---

### 3. 🛠 Feature Engineering
- Extracted:
  - Journey day & month
  - Departure & arrival hours
  - Total journey duration
- Encoded categorical features using:
  - One-Hot Encoding
  - Label Encoding

---

### 4. 🤖 Model Building
- Trained and evaluated multiple regression models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
- Performed train-test split for validation

---

### 5. 📈 Evaluation
- Evaluation metrics used:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
- Compared models to select the best performer

---

### 6. 🔍 Results
- **Random Forest Regressor** achieved the highest performance
- Captured non-linear relationships effectively
- Significantly reduced prediction error compared to linear models

---

## ⚙️ Tech Stack
- **Python**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **Scikit-learn**

---

## 📊 Insights
- Flight prices are strongly influenced by:
  - Airline brand
  - Number of stops
  - Journey duration
- Tree-based models outperform linear approaches for this dataset
- Feature engineering played a key role in improving accuracy

---

## 🚀 Conclusion
This project demonstrates a complete **end-to-end regression pipeline**, from data cleaning and feature engineering to model comparison and evaluation, using a real-world flight pricing dataset.
