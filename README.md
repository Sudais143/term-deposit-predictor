# Term Deposit Subscription Predictor

🎯 **Live App**: [Click here to try it out](https://term-deposit-predictor.streamlit.app/)

This project uses a machine learning model to predict whether a client will subscribe to a term deposit, based on data from a bank's direct marketing campaign. The solution includes a trained model and a Streamlit web application for real-time predictions.

## 🔍 Project Structure

- `term_deposit_modeling.ipynb`: Jupyter notebook with full analysis, EDA, modeling, and export.
- `streamlit_app.py`: Streamlit app to collect input and display predictions.
- `term_deposit_model.pkl`: Trained Random Forest model saved with joblib.
- `Term_Deposit_Report.docx`: Project report with findings and approach.
- `requirements.txt` – Dependencies list for setup
- `bank-additional-full.csv` – Dataset used for training and evaluation
- `screenshot.png` – Visual preview of the deployed Streamlit app
- `README.md`: This setup and usage guide.

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Evaluation**: Accuracy, ROC AUC, Classification Report
- **Class Balance Handling**: SMOTE (Synthetic Minority Oversampling Technique)

## 🧪 Using the App

- Input client attributes using the form
- Click "Predict"
- The app will show the prediction and the probability of subscription

### 🔍 App Screenshot

<img width="816" alt="6e3ae259-16b2-413f-855b-c434941dd2df" src="https://github.com/user-attachments/assets/55f94b3c-3ba4-4f8f-8d8f-d16b6d70d5f3" />

## 📄 Dataset Source

- `bank-additional-full.csv`
- The dataset contains 41,188 records and 20 features related to marketing interactions

## 🚀 🛠️ For Developers : Running the Streamlit App

### 1. Clone the repository

```bash
git clone https://github.com/your-username/term-deposit-predictor.git
cd term-deposit-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

This will open the app in your default web browser at `http://localhost:8501`.

## ✅ How to Run the Streamlit App Locally

You can run the app locally on your computer by following these steps:

### 1. Close Jupyter Notebook (if open)

Make sure no other apps are using the same port (like Jupyter on port 8501).

### 2. Open Your Terminal

Use **Anaconda Prompt**, **Command Prompt**, or **Terminal** (Mac/Linux).

### 3. Navigate to Your Project Folder

```bash
cd path\to\your\project\folder
```

Make sure your folder contains both:
- `streamlit_app.py`
- `term_deposit_model.pkl`

### 4. Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

The app will open automatically in your browser at:

```
http://localhost:8501
```

### 📌 Tips

- Press `Ctrl + C` in the terminal to stop the app
- Ensure your environment has all dependencies from `requirements.txt`


## 📬 Contact

For questions or collaborations, feel free to reach out at hajjsudais143@gmail.com
