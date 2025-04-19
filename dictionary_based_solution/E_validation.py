import numpy as np
import pandas as pd

from C_classificationLogic import  final_df

print("Starting validation process...")

# Funcție pentru validarea rezultatelor clasificării
def validate_classification(results_df: pd.DataFrame):
    # 1. Verifică acoperirea - ce procentaj de companii a primit cel puțin o etichetă
    companies_with_labels = results_df[results_df['insurance_label'] != ''].shape[0]
    total_companies = results_df.shape[0]
    coverage = companies_with_labels / total_companies
    
    # 2. Verifică numărul mediu de etichete per companie
    label_counts = results_df['insurance_label'].apply(
        lambda x: len(x.split('; ')) if isinstance(x, str) and x else 0
    )
    avg_labels = label_counts.mean()
    
    # 3. Validare prin eșantionare - examinează eșantioane aleatorii pentru verificare manuală
    sample_size = min(10, total_companies)
    sample_indices = np.random.choice(total_companies, sample_size, replace=False)
    samples = results_df.iloc[sample_indices]
    
    # Afișează metricele de validare
    print(f"Classification coverage: {coverage:.2%}")
    print(f"Average labels per company: {avg_labels:.2f}")
    print("\nSample classifications for review:")
    for idx, row in samples.iterrows():
        print(f"\nCompany: {row['index']}")
        print(f"Description: {row['description']}...")
        print(f"Assigned labels: {row['insurance_label']}")
    
    return coverage, avg_labels, samples


coverage, avg_labels, samples = validate_classification(final_df)

print("Validation process completed.", end="\n\n")