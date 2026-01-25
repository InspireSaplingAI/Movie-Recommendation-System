# Movie-Recommendation-System
build a small-scale recommendation system from scratch

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-orange) ![FastAPI](https://img.shields.io/badge/FastAPI-Deployment-green) ![Status](https://img.shields.io/badge/Status-Educational-yellow)

## 1. Project Introduction
This project is a comprehensive guide to building a **Machine Learning Engineering (MLE)** focused recommendation system. Students will build a small-scale recommendation system from scratch, moving beyond simple notebooks to production-ready code.

The curriculum covers the full lifecycle: data preprocessing, feature engineering, model training (from statistical rules to Deep Learning), evaluation, and system deployment. The final goal is to deliver a personalized recommendation engine and showcase results via a REST API and a web-based demo application.

## 2. Project Architecture
Unlike standard data science courses, this project enforces an **engineering-first** directory structure to promote modularity and scalability.

```text
recsys_project/
├── config/                 # Configuration files (YAML) for paths & hyperparameters
├── data/                   # Dataset storage (Raw, Processed, Models)
├── notebooks/              # Jupyter notebooks for exploration & reporting
├── src/                    # Source code modules
│   ├── data_loader.py      # Data ingestion & preprocessing pipelines
│   ├── models/             # Abstract base classes & model implementations
│   ├── trainer.py          # Training loops & experiment tracking
│   └── inference.py        # Inference logic & cold-start handling
├── app/                    # Deployment layer
│   ├── main.py             # FastAPI backend
│   └── frontend.py         # Streamlit dashboard
└── requirements.txt        # Project dependencies
```

## 3. Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-org/recsys-bootcamp.git](https://github.com/your-org/recsys-bootcamp.git)
   cd recsys-bootcamp
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Course Schedule & Roadmap

### 🏁 Session 1: Project Kickoff & Data Exploration
**Focus:** Establishing the engineering framework and statistical baselines.

| Component | Details |
| :--- | :--- |
| **Topics** | • RecSys Applications (Movies, E-commerce, News)<br>• Data Exploration (User-Item Matrix, Long-tail distribution)<br>• Cold Start Strategy: Popularity-based & Rule-based methods |
| **Skills** | • Pandas/Numpy/Matplotlib<br>• Data Cleaning Pipelines<br>• Object-Oriented Design (Abstract Base Classes) |
| **Deliverable** | 📊 EDA Report (Notebook) & Top-N Popularity Recommender Module |

### 🤝 Session 2: Collaborative Filtering & Matrix Factorization
**Focus:** Transitioning to machine learning models and mathematical representations.

| Component | Details |
| :--- | :--- |
| **Topics** | • User/Item-based Collaborative Filtering<br>• Matrix Factorization theory (SVD/ALS)<br>• Hyperparameter Tuning |
| **Skills** | • `Scikit-learn` / `Surprise` libraries<br>• Metrics: Precision@K, Recall@K<br>• Model Serialization (`.pkl`) |
| **Deliverable** | 🧩 Trained MF Models & Evaluation Report comparing against baseline |

### 🧠 Session 3: Deep Learning for Recommendation
**Focus:** Implementing neural architectures using deep learning frameworks.

| Component | Details |
| :--- | :--- |
| **Topics** | • Neural Collaborative Filtering (NCF)<br>• Embedding Layers for Users/Items<br>• Wide & Deep Architectures |
| **Skills** | • **PyTorch/TensorFlow**<br>• Embedding + MLP Architecture<br>• Custom Dataset & DataLoader creation |
| **Deliverable** | 🕸️ Trained NCF Model & Performance comparison with traditional MF |

### 🚀 Session 4: Systemization & Deployment
**Focus:** Serving the model as a product.

| Component | Details |
| :--- | :--- |
| **Topics** | • Architecture: Retrieval vs. Ranking<br>• API Development (Latency & Throughput)<br>• Future directions: Contextual Recs & RL |
| **Skills** | • **FastAPI** for Backend API<br>• **Streamlit** for Frontend UI<br>• Docker (Optional) |
| **Deliverable** | 💻 Functional REST API & Web Demo Dashboard |

---

## 5. Usage

### Training Models
To train a specific model (defined in `config/config.yaml`):
```bash
python src/trainer.py --model ncf
```

### Running the API
To start the recommendation backend service:
```bash
uvicorn app.main:app --reload
```

### Running the Demo UI
To visualize recommendations in a browser:
```bash
streamlit run app/frontend.py
```

---

## 6. Learning Outcomes
By the end of this project, students will be able to:
- ✅ **Understand** the fundamental principles and architecture of modern recommendation systems.
- ✅ **Gain Hands-on Experience** with Collaborative Filtering, Matrix Factorization, and Neural Networks.
- ✅ **Master** the end-to-end MLE pipeline: Data Preprocessing → Training → Evaluation.
- ✅ **Deploy** machine learning models as scalable APIs.

## 7. Final Deliverables
1. **Code Repository:** A structured Git repo containing modular code, not just notebooks.
2. **Technical Report:** Documentation summarizing the EDA, model selection process, and evaluation metrics.
3. **Live Demo:** A functional API and Web App that takes a User ID and returns personalized item recommendations.

---
*Created for the MLE Recommendation System Course.*
