# Online-Payment-Fraud-Detection
 
# 💳 Online Payment Fraud Detection

A machine learning-powered web application that detects fraudulent online payment transactions in real time. Built with Python, scikit-learn, and Flask.

---

## 🧠 Overview

Online payment fraud is a growing threat to financial systems worldwide. This project trains a classification model on transaction data to distinguish between legitimate and fraudulent payments, and deploys it as an interactive web interface where users can input transaction details and get an instant fraud prediction.

---

## 🚀 Features

- Predicts whether a transaction is **fraudulent or legitimate**
- Simple and intuitive web interface built with Flask
- Pre-trained machine learning model loaded via `pickle`
- Accepts key transaction features: type, amount, and account balances

---

## 🗂️ Project Structure

```
Online-Payment-Fraud-Detection/
│
├── templates/
│   └── index.html              # Frontend HTML template
│
├── Online Payments Fraud Detection.ipynb   # EDA & model training notebook
├── app.py                      # Flask web application
├── fraud_model.pkl             # Serialized trained ML model
├── requirements.txt            # Python dependencies
└── README.md
```

---

## ⚙️ How It Works

1. The model is trained on a payment transactions dataset (see the Jupyter notebook).
2. Four features are used for prediction:
   - **Transaction Type** (encoded as a number)
   - **Transaction Amount**
   - **Old Balance (Origin Account)**
   - **New Balance (Origin Account)**
3. The Flask app loads the pre-trained model and serves predictions via a web form.

---

## 🛠️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/anilesh-prajapati/Online-Payment-Fraud-Detection.git
cd Online-Payment-Fraud-Detection
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Flask app**
```bash
python app.py
```

**4. Open your browser and visit**
```
http://127.0.0.1:5000
```

---

## 🧪 Model Details

The model is trained and evaluated in the `Online Payments Fraud Detection.ipynb` notebook. It covers:

- Exploratory Data Analysis (EDA)
- Feature engineering and preprocessing
- Model training and evaluation
- Exporting the final model as `fraud_model.pkl`

---

## 📦 Tech Stack

| Layer        | Technology              |
|--------------|-------------------------|
| Language     | Python                  |
| ML Library   | scikit-learn            |
| Web Framework| Flask                   |
| Frontend     | HTML (Jinja2 templates) |
| Notebook     | Jupyter                 |

---

## 📊 Input Features

| Feature          | Description                              |
|------------------|------------------------------------------|
| `type`           | Transaction type (encoded as integer)    |
| `amount`         | Amount of the transaction                |
| `oldbalanceOrg`  | Balance in origin account before transaction |
| `newbalanceOrig` | Balance in origin account after transaction  |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open source. See the repository for details.

---

## 👤 Author

**Anilesh Prajapati**  
[GitHub Profile](https://github.com/anilesh-prajapati)
