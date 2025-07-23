import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import json
import pandas as pd
from credit_scorer.feature_engineering import feature_engineer
from credit_scorer.scoring import compute_scores
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, path):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['credit_score'], bins=30, kde=True, color='teal')
    plt.title('Wallet Credit Score Distribution')
    plt.xlabel('Credit Score')
    plt.ylabel('Count')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def plot_boxplot(df, path):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df['credit_score'].dropna(), color='orange')
    plt.title('Wallet Credit Score Distribution (Boxplot)')
    plt.xlabel('Credit Score')
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def plot_enhanced_heatmap(df, path, top_n=50):
    top_wallets = df.sort_values('credit_score', ascending=False).head(top_n)
    heatmap_data = top_wallets.set_index('wallet')[['credit_score']]
    heatmap_matrix = heatmap_data.values.reshape(-1, 1)

    plt.figure(figsize=(12, 10))
    ax = sns.heatmap(
        heatmap_matrix,
        annot=True,
        fmt='d',
        linewidths=0.8,
        linecolor='gray',
        cmap='YlGnBu',
        cbar=True,
        square=True,
        yticklabels=top_wallets['wallet'],
        xticklabels=False
    )
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=9)
    plt.title(f'Top {top_n} Wallets Credit Score Heatmap', fontsize=16)
    plt.ylabel('Wallet Address')
    plt.xlabel('')
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def main():
    input_file = "data/raw/user-wallet-transactions.json"
    output_file = "reports/wallet_scores.csv"

    with open(input_file, "r") as f:
        tx_data = json.load(f)

    df_features = feature_engineer(tx_data)
    df_features["credit_score"] = compute_scores(df_features)
    df_features[["wallet", "credit_score"]].to_csv(output_file, index=False)

    # Generate visualizations
    plot_histogram(df_features, "reports/score_distribution.png")
    plot_boxplot(df_features, "reports/score_boxplot.png")
    plot_enhanced_heatmap(df_features, "reports/top_wallets_heatmap_enhanced.png")

    print("✅ Credit scoring complete. Check /reports for results.")

if __name__ == "__main__":
    main()
