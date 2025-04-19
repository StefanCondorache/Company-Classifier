import pandas as pd

from A_dataPreparation import companies_df, taxonomy_df

print("Starting feature extraction...")

#companies_df = pd.read_csv('processed_companies.csv')
#taxonomy_df = pd.read_csv('processed_taxonomy.csv')

# Extrage cuvinte cheie din etichetele taxonomiei
taxonomy_keywords = {}
for idx, row in taxonomy_df.iterrows():
    label = row['label']
    processed_text = row['processed_label']
    
    # Extrage cuvinte cheie (excluzând cuvintele comune)
    keywords = [word for word in processed_text.split()] 
    
    # Stochează cuvintele cheie pentru această etichetă
    taxonomy_keywords[label] = keywords
    
# Creează o reprezentare consolidată a fiecărei companii
companies_df['consolidated_info'] = (
    companies_df['processed_description'] + " " + 
    companies_df['processed_tags'] + " " + 
    companies_df['processed_sector'] + " " +
    companies_df['processed_category'] + " " +
    companies_df['processed_niche']
)


#if( eval(input("Test? >> ")) == True ):
#    with open('test.txt', "w") as f:
#        f.write(companies_df['consolidated_info'][0])

print("Feature extraction completed.", end="\n\n")