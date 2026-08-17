# Dry Bean Species Classification

Multi-class ML classification on the UCI Dry Bean dataset — ML Assignment 2.

---

## a. Problem Statement

Dry bean growers face a labour-intensive manual process to identify and sort bean varieties. This project automates that process by training machine learning classifiers on morphological features extracted from seed images, enabling accurate and fast identification of seven dry bean species.

---

## b. Dataset Description

| Property | Value |
|----------|-------|
| Source | [UCI ML Repository — Dry Bean Dataset](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset) |
| Instances | 13,611 |
| Features | 16 morphological (area, perimeter, axis lengths, shape factors, etc.) |
| Target | `Class` — 7 bean varieties |
| Task | Multi-class classification |
| Missing values | None |

**Bean Classes:** BARBUNYA, BOMBAY, CALI, DERMASON, HOROZ, SEKER, SIRA

**Features:** Area, Perimeter, MajorAxisLength, MinorAxisLength, AspectRation, Eccentricity, ConvexArea, EquivDiameter, Extent, Solidity, roundness, Compactness, ShapeFactor1, ShapeFactor2, ShapeFactor3, ShapeFactor4

---

## c. GitHub Repository Link

[https://github.com/2025da04185/dry-bean-ml](https://github.com/2025da04185/dry-bean-ml)

---

## d. Models Used

Train-test split: 80% train / 20% test (stratified), `random_state=42`  
Metrics use weighted averaging across all 7 classes.

| ML Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|----------|----------|-----|-----------|--------|----------|-----|
| Logistic Regression | 0.9214 | 0.9934 | 0.9222 | 0.9214 | 0.9216 | 0.9050 |
| Decision Tree | 0.8957 | 0.9464 | 0.8961 | 0.8957 | 0.8956 | 0.8739 |
| K-Nearest Neighbors | 0.9166 | 0.9839 | 0.9173 | 0.9166 | 0.9168 | 0.8992 |
| Gaussian Naive Bayes | 0.8979 | 0.9902 | 0.9007 | 0.8979 | 0.8981 | 0.8773 |
| Random Forest | 0.9188 | 0.9925 | 0.9190 | 0.9188 | 0.9188 | 0.9018 |

---

## Model Performance Observations

| ML Model | Observation |
|----------|-------------|
| Logistic Regression | Best overall performer (F1 = 0.9216). The 16 morphological features are well-separated in linear space after standardisation, allowing the model to learn clear decision boundaries. High AUC (0.9934) confirms strong probabilistic separation across all 7 classes. |
| Decision Tree | Weakest accuracy (0.8957) and notably lower AUC (0.9464) compared to others. A single tree tends to over-fit locally and struggles with the feature overlap between similar bean varieties (e.g., SEKER vs CALI). Pruning via `max_depth=15` limits but does not eliminate this. |
| K-Nearest Neighbors | Competitive accuracy (0.9166) but moderately lower AUC (0.9839). Sensitive to class-boundary ambiguity since bean morphology can be gradual across varieties. Distance-weighted voting (`weights='distance'`) improves performance over plain majority vote. |
| Gaussian Naive Bayes | Reasonable accuracy (0.8979) and very high AUC (0.9902) because it models class-conditional probabilities well at the distribution level. However, the Gaussian independence assumption between correlated shape features (e.g., Area and ConvexArea) limits discriminative accuracy. |
| Random Forest | Strong and stable performer (Accuracy 0.9188, MCC 0.9018). The ensemble of 150 trees reduces variance compared to a single tree, giving consistent results across all metrics. Marginally behind Logistic Regression, suggesting linear relationships dominate in this feature space. |
| **Overall Winner** | **Logistic Regression** — highest F1 (0.9216), highest AUC (0.9934), and highest MCC (0.9050). The standardised morphological features form linearly separable clusters, favouring a linear model over tree and distance-based approaches. |

---

## Project Structure

```
dry-bean-ml/
├── app.py                    # Streamlit web application
├── requirements.txt
├── README.md
├── test_data.csv             # 20% held-out test set (2,723 samples)
├── DryBeanDataset/
│   └── Dry_Bean_Dataset.csv
└── model/
    ├── prepare_data.py       # xlsx → csv conversion
    ├── train_models.ipynb    # Model training notebook
    ├── scaler.pkl
    ├── label_encoder.pkl
    ├── logistic_regression.pkl
    ├── decision_tree.pkl
    ├── knn.pkl
    ├── naive_bayes.pkl
    └── random_forest.pkl
```

---

## Streamlit App

**Live App:** [https://dry-bean-ml-f3uyihfuegiongpqprbnu8.streamlit.app/](https://dry-bean-ml-f3uyihfuegiongpqprbnu8.streamlit.app/)

### Features
- Upload `test_data.csv` for evaluation
- Select from 5 trained models
- View 6 evaluation metrics (Accuracy, AUC, Precision, Recall, F1, MCC)
- All-models comparison table with best-value highlighting
- Confusion matrix heatmap
- Per-class classification report

---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/2025da04185/dry-bean-ml.git
cd dry-bean-ml

# 2. Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. (Optional) Re-train models — pkl files are already committed
jupyter notebook model/train_models.ipynb

# 4. Launch the Streamlit app
streamlit run app.py
```

Then open http://localhost:8501, upload `test_data.csv`, select a model, and click **Run Analysis**.
