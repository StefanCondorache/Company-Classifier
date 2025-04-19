import pandas as pd

from B_featureExtraction import companies_df, taxonomy_keywords

print("Starting classification...")

def calculate_score(match_list: dict, label_keywords: list):

    if not match_list:
        return 0
    if len(match_list) == 1:
        word_list = ['services', 'manufacturing', 'service']
        if any(word in list(match_list.keys()) for word in word_list):
            return 0
    
    n = len(label_keywords)
    frac = 2**(n-1) / (2**n -1) 
    max_f = max(list(match_list.values())) if match_list else 100
    list1 = [f/max_f for f in match_list.values()] if match_list else [0]
    sum_label = sum(list1)/len(list1)
    score = frac * sum_label

    return score

def calculate_label_score(company_text: str, label_keywords: list):

    if not label_keywords:
        return 0, {}
    
    score = 0
    
    company_words = set(company_text.split())
    matching_keywords = {kw : company_text.count(kw) for kw in label_keywords if kw in company_words}

    # Calculează scorul (raportul dintre cuvintele cheie potrivite și totalul cuvintelor cheie)
    score = len(matching_keywords) / len(label_keywords)
    if score != 1:
        score = calculate_score(matching_keywords, label_keywords)
    
    return score, matching_keywords



results = []
for idx, company in companies_df.iterrows():

    company_info = company['consolidated_info']

    threshold = 0.5
    result = {
        'company_index' : idx,
        'insurance_label': "",
        'top_score': 0,
        'matching_keywords': {}
    }

    for label, keywords in taxonomy_keywords.items():

        score, match = calculate_label_score(company_info, keywords)

        if score >= threshold:
            result['top_score'] = max(result['top_score'], score)
            result['insurance_label'] += label + "; "
            result['matching_keywords'][label] = match

    results.append(result)
        
#with open('results.txt', "w") as f:
#    for result in results:
#        f.write(f"Company index: {result['company_index']}\n")
#        f.write(f"Insurance label: {result['insurance_label']}\n")
#        f.write(f"Top score: {result['top_score']}\n")
#        f.write(f"Matching keywords: {result['matching_keywords']}\n\n")

results_df = pd.DataFrame(results)
companies_df = companies_df.reset_index()
final_df = pd.merge(companies_df, results_df[['company_index', 'insurance_label']], left_on='index', right_on='company_index')
final_df = final_df.drop(columns=['company_index'])

print("Classification completed.", end="\n\n")
        
       