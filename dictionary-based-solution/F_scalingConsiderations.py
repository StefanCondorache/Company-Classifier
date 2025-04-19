import numpy as np
import pandas as pd

from B_featureExtraction import companies_df, taxonomy_keywords

# Exemplu de potrivire optimizată folosind CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

print("Starting scaling considerations process...")

# Creează un vectorizator pentru cuvintele cheie din taxonomie
taxonomy_texts = {label: ' '.join(keywords) for label, keywords in taxonomy_keywords.items()}
labels = list(taxonomy_texts.keys())
texts = [taxonomy_texts[label] for label in labels]

vectorizer = CountVectorizer(binary=True)
taxonomy_vectors = vectorizer.fit_transform(texts)

# Funcție pentru procesarea în loturi a companiilor
def process_company_batch(company_batch, vectorizer, taxonomy_vectors, labels, threshold=0.15):
    batch_results = []
    
    company_info_texts = company_batch['consolidated_info'].tolist()
    company_vectors = vectorizer.transform(company_info_texts)
    
    similarity_matrix = (company_vectors @ taxonomy_vectors.T).toarray()
    
    for i, company in enumerate(company_batch.iterrows()):
        idx, row = company
        
        scores = similarity_matrix[i]
        
        matching_indices = np.where(scores >= threshold)[0]
        matching_labels = [labels[j] for j in matching_indices]

        label_scores = [(labels[j], scores[j]) for j in matching_indices]
        label_scores.sort(key=lambda x: x[1], reverse=True)
        sorted_labels = [label for label, score in label_scores]
        
        result = {
            'company_index': idx,
            'insurance_label': "; ".join(sorted_labels)
        }
        batch_results.append(result)
    
    return pd.DataFrame(batch_results)

batch_size = 1000
results = []

for i in range(0, len(companies_df), batch_size):
    batch = companies_df.iloc[i:i+batch_size]
    batch_results = process_company_batch(batch, vectorizer, taxonomy_vectors, labels)
    results.append(batch_results)

final_results = pd.concat(results, ignore_index=True)
final_results.to_csv('insurance_labels.csv', index=False)

print("Classification process completed.", end="\n\n")
