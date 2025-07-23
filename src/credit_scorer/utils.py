import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histogram(df, path):
    plt.figure(figsize=(10,6))
    plt.hist(df["credit_score"], bins=20, color="#4CAF50", edgecolor="black")
    plt.title("Wallet Credit Score Distribution")
    plt.xlabel("Credit Score")
    plt.ylabel("Number of Wallets")
    plt.grid(True, linestyle='--')
    plt.savefig(path)
    plt.close()

def plot_heatmap(df, path, top_n=50):
    top_df = df.sort_values("credit_score", ascending=False).head(top_n)
    plt.figure(figsize=(12, 6))
    sns.heatmap(top_df[['credit_score']].set_index(top_df['wallet']), 
                cmap="YlGnBu", annot=True, fmt='d', cbar=True)
    plt.title("Top Wallets - Credit Score Heatmap")
    plt.savefig(path)
    plt.close()
