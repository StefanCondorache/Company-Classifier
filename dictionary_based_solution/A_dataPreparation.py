import pandas as pd
#import nltkst
import re 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 

print("Starting data preprocessing...")

# Încărcarea seturilor de date
companies_df = pd.read_csv('ml_insurance_challenge.csv')
taxonomy_df = pd.read_excel('insurance_taxonomy.xlsx')

# Descărcarea resurselor NLTK dacă este necesar
#nltk.download('punkt_tab') 
#nltk.download('stopwords')

# Definirea funcției de preprocesare
def preprocess_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()

    text = re.sub(r'[^\w\s]', ' ', text)

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

# Aplică preprocesarea datelor companiei
companies_df['processed_description'] = companies_df['description'].apply(preprocess_text)
companies_df['processed_tags'] = companies_df['business_tags'].apply(preprocess_text)
companies_df['processed_sector'] = companies_df['sector'].apply(preprocess_text)
companies_df['processed_category'] = companies_df['category'].apply(preprocess_text)
companies_df['processed_niche'] = companies_df['niche'].apply(preprocess_text)

# Preprocesarea etichetelor din taxonomie
taxonomy_df['processed_label'] = taxonomy_df['label'].apply(preprocess_text)

# Salvarea datelor preprocesate pentru verificare
#companies_df.to_csv('processed_companies.csv', index=False)
#taxonomy_df.to_csv('processed_taxonomy.csv', index=False)

print("Data preprocessing completed.",end="\n\n")