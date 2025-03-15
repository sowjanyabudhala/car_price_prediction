# 🚗 Car Price Prediction using Machine Learning  

## 📌 Table of Contents  
- [Demo](#demo)  
- [Overview](#overview)  
- [Motivation](#motivation)  
- [Technical Aspect](#technical-aspect)  
- [Installation, Run & Deployment](#installation-run--deployment)  
- [Directory Structure](#directory-structure)  
- [To-Do & Bug / Feature Request](#to-do--bug--feature-request)  
- [Technologies Used](#technologies-used)  
- [Credits](#credits)  

---

## 🎥 Demo  
🔗 **Live Demo**: [Add your deployment link here]  
![Demo](https://your-demo-link.com/demo.gif)  

---

## 📖 Overview  
This project predicts **used car prices** based on various factors like **car brand, fuel type, transmission type, kilometers driven, owner history, and vehicle age** using machine learning techniques.  

💡 **Models Used**:  
✔ Linear Regression  
✔ Random Forest Regressor  
✔ Gradient Boosting Regressor (**Best Performing Model**)  
✔ XGBoost Regressor  

📊 **Evaluation Metric**: R² Score

---

## 🎯 Motivation  
Car resale prices are influenced by multiple factors such as **mileage, brand, and condition**. This project aims to:  
✔ Provide an **accurate pricing model** for used cars.  
✔ Help **buyers and sellers** make data-driven decisions.  
✔ Reduce **pricing biases** in the used car market.  

---

## ⚙️ Technical Aspect  
1️⃣ **Data Preprocessing**  
- Handling missing values  
- Encoding categorical features (Fuel Type, Seller Type, Transmission)  
- Creating new feature: **Car Age**  
- Removing **outliers**  

2️⃣ **Exploratory Data Analysis (EDA)**  
- **Univariate & Bivariate Analysis** using histograms and scatter plots  
- **Heatmap of correlations**  
- **Pairplot** for relationships  

3️⃣ **Model Training & Evaluation**  
- **Splitting dataset** into train & test sets  
- Training **Linear Regression, Random Forest, Gradient Boosting, and XGBoost**  
- Selecting **Gradient Boosting Regressor** as the best model based on R² Score  

4️⃣ **Model Deployment using Streamlit**  
- **User-friendly UI** for predicting car prices based on input parameters  

---

## ⚡ Installation, Run & Deployment  
```bash
# Install dependencies
pip install -r requirements.txt  

# Run the project
python car_price_prediction.py  

# Install Streamlit for deployment
pip install streamlit  

# Run Streamlit app
streamlit run app.py  


----
###📂 Directory Structure
📦 Car Price Prediction  
 ┣ 📂 data  
 ┃ ┣ 📄 car_data.csv  
 ┣ 📂 models  
 ┃ ┣ 📄 car_price_predictor.pkl  
 ┣ 📂 scripts  
 ┃ ┣ 📄 car_price_prediction.py  
 ┣ 📂 streamlit_app  
 ┃ ┣ 📄 app.py  
 ┣ 📄 requirements.txt  
 ┣ 📄 README.md  
 ┣ 📄 LICENSE
------

✅ To-Do & Bug / Feature Request
# To-Do  
✔ Deploy the model using Flask API  
✔ Enable real-time car price prediction  

# Bug / Feature Request  
If you find a bug or want to request a new feature, open an issus


🛠 Technologies Used
# Libraries Used:  
✔ Scikit-Learn (Machine Learning)  
✔ Streamlit (Web App Framework)  
✔ Pandas (Data Analysis)  
✔ Matplotlib & Seaborn (Data Visualization)  
✔ Joblib (Model Saving)  

🙌 Credits
# Dataset:  
✔ Kaggle Car Price Prediction Dataset  

# Contributor:  
✔ B. Sowjanya  

 



