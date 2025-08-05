# 🎬 Sentiment Analysis Web Application

A deep learning-powered web app that classifies movie reviews as **Positive** or **Negative** using an RNN model trained on the IMDB dataset.

---

## 📌 Project Overview

This project demonstrates a complete **NLP pipeline** using deep learning to perform sentiment classification on textual movie reviews. It includes:

- Data preprocessing and embedding
- Model training using Simple RNN
- Live sentiment prediction via a web interface
- Deployment on **Streamlit Cloud**

---

## 🧠 Tech Stack

- **Programming Language:** Python  
- **Deep Learning Framework:** TensorFlow / Keras  
- **Frontend/UI:** Streamlit  
- **NLP Libraries:** NumPy, Pandas  
- **Dataset:** IMDB Movie Review Dataset (Keras built-in)  
- **Version Control & Deployment:** Git, GitHub, Streamlit Cloud  

---

## ⚙️ Key Features

- 🔍 **Real-time Sentiment Analysis**: Enter a custom movie review and get an instant sentiment prediction.
- 📈 **Sentiment Scoring**: Displays a confidence score (0–1) for model output.
- 💬 **Example Testing**: Try pre-written test inputs like “I loved it” or “Boring plot”.
- ⚠️ **Error Identification**: Highlights misclassifications (e.g., “Great acting” being predicted as negative).
- 🌐 **Hosted Online**: Access the live demo from anywhere.

---

## 🧪 Model Details

- Model Type: `SimpleRNN`
- Input: Preprocessed and padded text sequences
- Embedding: Keras `Embedding` layer
- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Evaluation Metric: Accuracy

> 🔐 Saved model in `.keras` format (`best_model.keras`) using `ModelCheckpoint`.

---

## 🚀 Planned Enhancements

- ✅ Add support for **Out-of-Vocabulary (OOV)** words  
- ✅ Upgrade to **GRU** or **LSTM** for better long-range sequence understanding  
- 🔍 Improve model **accuracy on borderline inputs**  
- 🧠 Add **explainability tools** like word importance or attention  

---

## 🧾 Sample Predictions

| Input Review       | Predicted Sentiment | Confidence Score |
|--------------------|----------------------|------------------|
| I loved it         | ✅ Positive           | 0.7723           |
| Boring plot        | ✅ Negative           | 0.0529           |
| Great acting       | ❌ **Negative**       | 0.2005 (Wrong)   |

---

## 🔗 Live Demo and Code

- 🚀 **Live App**: [Streamlit Cloud Demo](https://your-live-app-link.streamlit.app)
- 📂 **Source Code**: [GitHub Repository](https://github.com/Prashilkumar/movie_review_analysis.git)

---

## 💻 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Prashilkumar/movie_review_analysis.git
   cd movie_review_analysis
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Run the app**
   ```bash
   streamlit run app.py
