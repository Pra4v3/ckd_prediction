# Chronic kidney disease (CKD) prediction model

### Purpose
This model aims to predict whether a patient has chronic kidney disease (CKD) based on various data gathered from clinical history, examinations, and laboratory findings.

#### Inspiration
As a doctor working in the Polonnaruwa district of Sri Lanka, I have observed that the prevalence of CKD in this area is alarmingly high, which is often reported in various research studies. [This article](https://doaj.org/article/9e1d2d9528464fcea616fe02c845841b) provides further insights.
I aspire to develop a machine learning model that can be deployed online to accurately predict whether a patient has CKD. This model is designed to identify patients in the early stages of CKD and guide them toward treatment before they progress to end-stage renal failure.

### Data source
The data used for model training is taken from the UC Irvine Machine Learning Repository. The dataset can be found [here](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease)
This data was gathered in Tamil Nadu, India, in 2015 and is available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. The original data was available in ARFF format and was processed with LibreOffice Calc to CSV format for better integration with Python workflows.

<img width="1113" height="819" alt="image" src="https://github.com/user-attachments/assets/5bc11a90-37b1-4027-8f28-7d4182bb09f7" />
*A correlation matrix of the data shows the relationship between various features. In this dataset, Class 1 indicates having CKD, while Class 0 indicates not having CKD.*  
Please refer to the Jupyter Notebook for detailed clarifications.

### Trained model
The best model among the trained models was a Random Forest Classifier. More information regarding the steps of the model training can be found in this Jupyter Notebook.

<img width="840" height="672" alt="image" src="https://github.com/user-attachments/assets/a2611b1a-85ec-483a-89ed-af07880c8a51" />
*The feature importance of the trained model has been assessed to understand which variables contribute most to the prediction of CKD.*

### Deployement
The web app has been deployed on [Streamlit cloud](https://ckd-prediction-model.streamlit.app/). You can enter patient data to receive information about how likely it is for that person to have Chronic Kidney Disease.
