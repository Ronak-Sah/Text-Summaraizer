# Text Summarizer using Pegasus (End-to-End MLOps Project)

This project is a **complete end-to-end NLP MLOps pipeline** for training, evaluating, and **locally deploying** a **Transformer-based Text Summarization model** using **Google Pegasus**.
Due to the **large model size and high cloud hosting cost**, the application is deployed on **localhost using Flask** instead of cloud platforms.

The system automatically processes raw data, trains the model, evaluates it using ROUGE metrics, and serves real-time summarization through a **local web interface**.

---

## 🚀 Key Features

* ✅ End-to-End ML Pipeline (Ingestion → Validation → Transformation → Training → Evaluation)
* ✅ Fine-tuned Pegasus Transformer Model
* ✅ Automated Training & Evaluation
* ✅ ROUGE Score Evaluation
* ✅ Model & Tokenizer Artifact Management
* ✅ **Local Flask Deployment (Cost-Optimized)**
* ✅ Modular & Production-Ready Code Structure
* ✅ Resume-Ready MLOps Project

---

## 🧠 Model Used

* **google/pegasus-xsum**
* Fine-tuned on custom summarization dataset
* Optimized for abstractive text summarization

---

## 🗂️ Project Workflow

1. **Update Configuration Files**

   * `config.yaml`
   * `params.yaml`

2. **Define Entities**

   * Configuration and data validation schemas

3. **Configuration Manager**

   * Centralized configuration loading

4. **Component Implementation**

   * Data Ingestion
   * Data Validation
   * Data Transformation
   * Model Trainer
   * Model Evaluation

5. **Pipeline Execution**

   * Individual pipeline stages
   * Orchestrated using `main.py`

6. **Local Web App Deployment**

   * Flask-based UI using `app.py`
   * Hosted on **localhost**

---

## ⚙️ Pipeline Stages

### 1️⃣ Data Ingestion

* Downloads and extracts the dataset
* Stores raw files in `artifacts/data_ingestion`

### 2️⃣ Data Validation

* Validates schema and file structure
* Stores results in `artifacts/data_validation`

### 3️⃣ Data Transformation

* Tokenization using Pegasus tokenizer
* Dataset mapping and preprocessing
* Saves processed datasets to `artifacts/data_transformation`

### 4️⃣ Model Training

* Fine-tunes Pegasus using HuggingFace Trainer
* Saves trained model and tokenizer to `artifacts/model_trainer`

### 5️⃣ Model Evaluation

* Computes ROUGE-1, ROUGE-2, ROUGE-L
* Stores results in `artifacts/model_evaluation/metrics.csv`

---

## 🌐 Local Web App Deployment (Flask)

This project is **deployed locally using Flask** because:

* ✅ The Pegasus model is **very large**
* ✅ Cloud GPU hosting is **paid**
* ✅ Local deployment avoids **runtime billing**
* ✅ Still demonstrates **full production capability**

Users can input text into the web UI and receive real-time summaries.

![Web App UI](image.png)

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Deep Learning:** PyTorch
* **NLP Framework:** HuggingFace Transformers & Datasets
* **Model:** Google Pegasus
* **Web Framework:** Flask
* **Pipeline Orchestration:** Custom Modular Pipeline
* **Logging:** Python Logging Module
* **Evaluation:** ROUGE Score
* **Version Control:** Git & GitHub

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository

```
git clone <your-repository-url>
cd Text-Summaraizer
```

### 2️⃣ Create Virtual Environment & Install Dependencies

```
conda create -n text python=3.10 -y
conda activate text
pip install -r requirements.txt
```

### 3️⃣ Run the Full Training Pipeline

```
python main.py
```

### 4️⃣ Run the Flask Web App (Local Deployment)

```
python app.py
```

Now open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📊 Output Artifacts

* `artifacts/data_ingestion/` – Raw dataset
* `artifacts/data_transformation/` – Tokenized dataset
* `artifacts/model_trainer/` – Trained Pegasus model
* `artifacts/model_evaluation/metrics.csv` – ROUGE evaluation scores

---

## 🎯 Resume Value

This project demonstrates:

* ✅ Real-world **Transformer Fine-Tuning**
* ✅ **End-to-End MLOps Pipeline Engineering**
* ✅ **NLP Model Evaluation using ROUGE**
* ✅ **Local Production Deployment using Flask**
* ✅ **Clean Modular Architecture**
* ✅ **Industry-Style Training Pipeline**

---

## 👨‍💻 Author

**Ronak Sah**
B.Tech Student


