import matplotlib.pyplot as plt

from B_featureExtraction import companies_df, taxonomy_keywords
from C_classificationLogic import calculate_label_score

print("Starting threshold determination...")

# Creează un dataframe cu rezultatele
all_scores = []
for idx, company in companies_df.iterrows():
    company_info = company['consolidated_info']
    for label, keywords in taxonomy_keywords.items():
        score, _ = calculate_label_score(company_info, keywords)
        all_scores.append(score)

# Plotează histograma scorurilor
# Această vizualizare ajută la identificarea unei valori rezonabile a pragului care separă potrivirile semnificative de zgomot.
plt.figure(figsize=(10, 6))
plt.hist(all_scores, bins=30)
plt.title('Distribution of Label Matching Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.axvline(x=0.5, color='r', linestyle='--', label='Threshold (0.5)')
plt.xticks(ticks=[i * 0.05 for i in range(int(max(all_scores) / 0.05) + 1)])  
plt.legend()
plt.show()

print("Threshold determination completed.", end="\n\n")

