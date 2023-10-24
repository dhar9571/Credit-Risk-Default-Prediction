# Credit-Risk-Default-Predictions

Link to the live server of my Credit Risk Default Prediction streamlit app

https://credit-risk-default-prediction-dharmendra.streamlit.app/

**Business Objective:**
The primary objective of the Credit Risk Default Prediction project is to assist a financial institution in assessing the creditworthiness of loan applicants. By utilizing machine learning and predictive modeling, the project aims to predict whether a loan applicant is likely to default on their loan. This is crucial for risk management and making informed lending decisions, helping to minimize financial losses and improve overall loan portfolio quality.

**Approach:**
The project leverages historical data on loan applicants and their financial profiles to build a predictive model. The approach involves the following key steps:

Data Collection: Gathered the data from Kaggle.com.

Data Preprocessing: Performed data cleaning, missing and duplicate value imputation, and data transformation. Utilize techniques such as label encoding for categorical variables.

Model Development: Trained machine learning and deep learning models such as XGBoost, RandomForest and Artifical Neural Networks, to predict whether a loan applicant is likely to default. The model learns from historical loan data, including both default and non-default cases.

Model Evaluation: Evaluated all trained model's performance using metrics like accuracy, precision and recall. Employed techniques like cross-validation to assess the model's robustness. Found XGBoost giving highest accuracy, precision and recall scores of 96%, 99% and 91% respectively.

Deployment: Deployed the trained model to Streamlit cloud. This allows real-time credit risk assessment for loan applicants.

**Challenges Faced:**
While developing the Credit Risk Default Prediction project, several challenges may have been encountered:

Imbalanced Data: Imbalanced datasets, where non-default cases significantly outnumber default cases, can lead to model bias. Implemented SMOTE method under Random Over Sampling to handle class imbalance.

Improving performance: Improving Recall score was quite difficult. However, different feature engineering steps were carried out in order to achieve the best performance for the model.

**Future Scope:**
The Credit Risk Default Prediction project has several future scopes:

Advanced Models: Implement more advanced machine learning and deep learning models to improve predictive accuracy and interpretability.

Real-time Monitoring: Develop a system for real-time monitoring of the loan portfolio to promptly identify potential defaults.
