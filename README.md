# Term Deposit Subscription Predictor

This project uses a machine learning model to predict whether a client will subscribe to a term deposit, based on data from a bank's direct marketing campaign. The solution includes a trained model and a Streamlit web application for real-time predictions.

## 🔍 Project Structure

- `term_deposit_modeling_updated.ipynb`: Jupyter notebook with full analysis, EDA, modeling, and export.
- `streamlit_app.py`: Streamlit app to collect input and display predictions.
- `term_deposit_model.pkl`: Trained Random Forest model saved with joblib.
- `Term_Deposit_Report.docx`: Project report with findings and approach.
- `README.md`: This setup and usage guide.

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Evaluation**: Accuracy, ROC AUC, Classification Report
- **Class Balance Handling**: SMOTE (Synthetic Minority Oversampling Technique)

## 🚀 Running the Streamlit App

### 1. Clone the repository

```bash
git clone https://github.com/your-username/term-deposit-predictor.git
cd term-deposit-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install pandas scikit-learn imbalanced-learn matplotlib seaborn streamlit joblib
```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

This will open the app in your default web browser at `http://localhost:8501`.

## 🧪 Using the App

- Input client attributes using the form
- Click "Predict"
- The app will show the prediction and the probability of subscription

## 📄 Dataset Source

- `bank-additional-full.csv` from the UCI Machine Learning Repository
- The dataset contains 41,188 records and 20 features related to marketing interactions

## 📬 Contact

For questions or collaborations, feel free to reach out at your-email@example.com
