from src.credit_scorer.feature_engineering import feature_engineer

def test_feature_engineer_minimal():
    test_data = [{
        "userWallet": "0xabc",
        "action": "deposit",
        "timestamp": 1620000000,
        "actionData": {
            "amount": "1000000000000000000",
            "assetPriceUSD": "1.00"
        }
    }]
    df = feature_engineer(test_data)
    assert df.loc[0, "usd_deposit"] > 0
