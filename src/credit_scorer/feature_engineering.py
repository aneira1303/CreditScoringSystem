from collections import defaultdict
import numpy as np
import pandas as pd

def wei_to_eth(wei):
    return float(wei) / 1e18

def feature_engineer(data):
    features = defaultdict(lambda: defaultdict(float))
    timestamps = defaultdict(list)

    for tx in data:
        wallet = tx.get("userWallet", "")
        action = tx.get("action", "").lower()
        ts = int(tx.get("timestamp", 0))

        try:
            amt = float(tx["actionData"].get("amount", 0))
            price = float(tx["actionData"].get("assetPriceUSD", 0))
        except (KeyError, ValueError):
            amt = 0
            price = 0

        usd_value = wei_to_eth(amt) * price
        features[wallet][f"n_{action}"] += 1
        features[wallet][f"usd_{action}"] += usd_value
        features[wallet]["total_tx"] += 1
        timestamps[wallet].append(ts)

    results = []
    for wallet, feat in features.items():
        ts_list = sorted(timestamps[wallet])
        feat["avg_days_between_txs"] = 0
        feat["wallet_age_days"] = 0
        if len(ts_list) > 1:
            intervals = [ts_list[i] - ts_list[i-1] for i in range(1, len(ts_list))]
            feat["avg_days_between_txs"] = np.mean(intervals) / 86400
            feat["wallet_age_days"] = (max(ts_list) - min(ts_list)) / 86400

        feat["borrow_repay_ratio"] = (
            feat.get("usd_repay", 0) / feat.get("usd_borrow", 1)
        )
        feat["wallet"] = wallet
        results.append(feat)

    return pd.DataFrame(results)
