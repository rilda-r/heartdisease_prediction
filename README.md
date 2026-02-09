Heart Disease Prediction using Machine Learning

# Overview
This project predicts the risk of heart disease using machine learning models trained on medical data.
The best-performing model is deployed as a web application using Flask and provides probability-based risk prediction.

# Technologies Used
- Python
- Scikit-learn
- Flask
- Pandas
- NumPy
- HTML & CSS

# Dataset
- Source: Kaggle Heart Disease Dataset
- Records: ~1025
- Target Variable:
  - 0 → Low risk / No heart disease
  - 1 → High risk / Heart disease

# Models Trained
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest Classifier

# Model Selection
The Random Forest Classifier was selected as the final model based on:
- Higher Accuracy
- Better ROC-AUC score
- Hyperparameter tuning (n_estimators, depth)
- Cross-validation performance

# Features Used
- Age  
- Sex  
- Chest Pain Type  
- Resting Blood Pressure  
- Cholesterol  
- Fasting Blood Sugar  
- Resting ECG  
- Maximum Heart Rate  
- Exercise Induced Angina  
- Oldpeak (ST Depression)  
- Slope  
- Number of Major Vessels  
- Thalassemia  


# Web Application
- Built using Flask
- Clean and responsive UI
- Input validation
- Displays:
  - Risk category (High / Low)

# How to Run the Project

1. Clone the repository
2. Install dependencies
   pip install -r requirements.txt
3. Run the Flask app
4. Open browser


# Project Structure

├── app.py
├── heartdisease_best_model.pkl
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md


# Future Improvements
- Add SHAP-based explainability in UI
- Store patient prediction history
- Deploy on cloud (Render / AWS / Railway)

