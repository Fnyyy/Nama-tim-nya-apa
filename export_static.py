import pandas as pd
import json
import os

# Ensure directory exists
os.makedirs('static/data', exist_ok=True)

# Load data
df = pd.read_csv('data/processed/clean_data.csv')
trend_df = pd.read_csv('data/processed/trend_data.csv')

# Stats
stats = {
    "total_provinces": int(len(df)),
    "avg_resilience": round(float(df['Economic_Resilience_Index'].mean()), 2),
    "total_qris": round(float(df['Volume_QRIS_Juta'].sum()), 0),
    "top_resilient": str(df.loc[df['Economic_Resilience_Index'].idxmax()]['Provinsi']),
    "top_resilient_score": round(float(df['Economic_Resilience_Index'].max()), 2),
    "avg_digital_adoption": round(float(df['Digital_Adoption_Score'].mean()), 1),
    "cluster_counts": {
        "tangguh": int((df['Status'] == 'Tangguh').sum()),
        "transisi": int((df['Status'] == 'Transisi').sum()),
        "rentan": int((df['Status'] == 'Rentan').sum()),
    }
}

# Save
with open('static/data/stats.json', 'w') as f:
    json.dump(stats, f)

with open('static/data/provinces.json', 'w') as f:
    json.dump(df.to_dict('records'), f)

with open('static/data/trends.json', 'w') as f:
    json.dump(trend_df.to_dict('records'), f)

print("Static data exported to static/data/")
