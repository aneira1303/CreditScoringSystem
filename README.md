# 🏦 DeFi Wallet Credit Scorer — Aave V2

Assigns a credit score (0–1000) to each wallet interacting with the Aave V2 protocol based on behavioral insights from DeFi transactions.

## 🔍 How It Works

1. Parses raw Aave V2 transaction data in `.json` format
2. Engineers transaction-level features per wallet
3. Calculates a credit score using a trained model or heuristic logic
4. Outputs scores, visualizations, and reports

## 🔧 Installation

pip install -r requirements.txt


## 🚀 One-Step Scoring

python scripts/score_wallets.py

## 📂 File Outputs

- `reports/wallet_scores.csv` — Main credit score output
- `reports/score_distribution.png` — Histogram of scores
- `reports/top_wallets_heatmap.png` — Heatmap of top 50 wallets

## 📊 Score Explanation

| Score Range | Meaning                          |
|-------------|----------------------------------|
| 900–1000    | Highly trustworthy wallet        |
| 700–899     | Good user                        |
| 500–699     | Mixed behavior                   |
| 300–499     | Risky wallet                     |
| 0–299       | High risk or exploit-like usage  |

## 📦 Extendability

Model-based scoring can be trained with `sklearn`, `LightGBM`, etc.
Re-train with:

