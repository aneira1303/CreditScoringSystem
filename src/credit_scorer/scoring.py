import joblib
import numpy as np

def compute_scores(df):
    model_path = "credit_model.pkl"
    feature_data = df.drop(columns=["wallet"]).fillna(0)

    try:
        model = joblib.load(model_path)
        score_preds = model.predict(feature_data)
        return np.clip(score_preds * 1000, 0, 1000).astype(int)
    except:
        # Manual logic fallback
        scores = (
            feature_data.get("usd_deposit", 0) * 3 +
            feature_data.get("n_repay", 0) * 100 +
            feature_data.get("borrow_repay_ratio", 0) * 200 -
            feature_data.get("n_liquidationcall", 0) * 300 -
            feature_data.get("usd_borrow", 0) * 0.5
        )
        return np.clip(scores.fillna(0).round(), 0, 1000).astype(int)
