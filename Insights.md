## Reflectii asupra solutiei de clasificare a companiilor

### Introducere
Acest document prezinta o analiza detaliata a procesului de creare a solutiei de clasificare a companiilor, inclusiv motivatiile din spatele deciziilor luate, alternativele considerate, punctele forte, punctele slabe si factorii care ar putea influenta functionarea acesteia.

### Procesul de rezolvare a problemei
Pasii Urmariti si Gandirea din Spatele Lor 
intelegerea Problemei (Ce trebuie sa fac?): Primul pas a fost sa inteleg clar ce se cerea. Trebuia sa clasific companii intr-o taxonomie data, folosind informatiile disponibile despre ele. M-am intrebat: "Care sunt datele de intrare? Ce format trebuie sa aiba rezultatul? Cum ma asigur ca clasificarile sunt corecte?"

Analiza Datelor (Ce informatii am?): Am examinat listele de companii (descrieri, tags, etc.) si taxonomia. Am observat ca atat companiile cat si etichetele taxonomiei erau descrise prin text. M-am gandit: "Cum pot compara doua bucati de text si sa determin daca se potrivesc?". Am analizat processed_taxonomy.csv si processed_companies.csv create in dataPreparation.py

Alegerea Abordarii Initiale (Cum rezolv problema simplu?): Am decis sa incep cu o abordare simpla, bazata pe reguli si potrivire de cuvinte cheie. Rationamentul a fost: "Pot obtine rezultate decente cu o metoda usor de inteles si de implementat? Pot reveni la abordari mai complexe daca e nevoie, dar incep cu ceva simplu."

Implementarea Potrivirii de Cuvinte Cheie (Cum transform ideea in cod?): Am scris cod pentru a preprocesa textul (eliminare caractere speciale, etc.) si a numara cuvintele cheie comune intre descrierea companiei si etichetele taxonomiei. M-am confruntat cu intrebari precum: "Cum definesc o 'potrivire'? Cat de mult trebuie sa se suprapuna cuvintele pentru a considera ca exista o potrivire?"

Stabilirea unui Prag si crearea unei formule de calcularea scorului (Cand consider o potrivire suficient de buna?): Am stabilit un prag (threshold) pentru a decide daca o companie ar trebui sa fie clasificata intr-o anumita categorie. M-am intrebat: "Cum gasesc pragul optim? Trebuie sa experimentez si sa validez rezultatele."

Validarea Rezultatelor (Este clasificarea corecta?): Avand in vedere lipsa datelor etichetate, am creat metode de validare alternative (verificarea acoperirii, examinarea esantioanelor). M-am intrebat: "Cum pot evalua daca clasificarile sunt rezonabile fara a avea raspunsurile corecte?"

Refacerea si Optimizarea (Pot imbunatati rezultatele?): Pe baza rezultatelor validarii, am ajustat pragul si regulile de potrivire a cuvintelor cheie.

### Motivatia abordarii rule-based
Am ales abordarea bazata pe reguli (rule-based) si potrivire de cuvinte cheie (keyword matching) deoarece mi s-a parut cea mai directa si accesibila solutie, avand in vedere lipsa cunostintelor mele in machine learning si ai altor facotri descrisi mai jos.

### Alternative considerate si respinse
Modele Machine Learning (ML): Am luat in considerare utilizarea modelelor ML, cum ar fi clasificarea Naive Bayes sau masini cu vectori de suport (SVM). Totusi, acestea necesita date etichetate pentru antrenament, ceea ce nu era disponibil. in plus, modelele ML pot fi "cutii negre", fiind dificil de inteles de ce o companie a fost clasificata intr-un anumit fel.

Embeddings (Word2Vec, GloVe): Desi embeddings ar putea capta similaritati semantice, necesita o cantitate mare de date pentru a fi antrenate eficient. Avand in vedere dimensiunea dataset-ului si lipsa cunostintelor mele in domeniu, am decis sa nu folosesc aceasta abordare.

TF-IDF si Clustering: Aceste tehnici ar putea ajuta la identificarea grupurilor de companii similare, dar nu ofera o clasificare directa in categoriile taxonomiei date. Ar necesita pasi suplimentari pentru a asocia clusterele cu etichetele din taxonomie.

### De ce nu am ales aceste alternative?
Am respins abordarile ML complexe din cauza lipsei datelor etichetate si a necesitatii de a mentine o solutie interpretabila.
Abordarile bazate pe embeddings si clustering ar fi putut adauga complexitate inutila, fara a garanta o acuratete semnificativ mai mare, avand in vedere dimensiunea dataset-ului.

## Analiza punctelor forte si slabe
### Puncte forte
Simplitate si Interpretabilitate: Solutia este usor de inteles si de implementat. Regulile de potrivire a cuvintelor cheie pot fi examinate si ajustate cu usurinta.

Nu necesita date de antrenament: Abordarea rule-based functioneaza direct cu datele disponibile, fara a necesita date etichetate.

Flexibilitate: Taxonomia si pragurile pot fi adaptate si ajustate rapid pentru a imbunatati acuratetea.

Valoarea pragului: Ajustarea pragului poate ajuta la eliminarea rezultatelor false pozitive.

### Puncte slabe
Lipsa intelegerii Semantice: Solutia se bazeaza doar pe potrivirea cuvintelor, nu pe intelegerea contextului sau a sinonimelor.

Sensibilitate la Vocabular: Daca descrierile companiilor folosesc termeni diferiti de cei din taxonomie, clasificarea poate fi inexacta.

Nu e complet automatizata: E nevoie de o calibrare manuala a pragurilor si revizuirea regulilor pentru a imbunatati rezultatele.

Scalabilitate si Performanta pe Dataset-uri Mari
Solutia actuala este potrivita pentru dataset-uri de dimensiuni moderate (e.g., cateva mii de companii). Pentru dataset-uri mai mari (e.g., milioane de companii), ar fi necesare optimizari:

Procesare Paralela: Utilizarea procesarii paralele pentru preprocesarea textelor si potrivirea cuvintelor cheie.

Vectorizare: Transformarea cuvintelor cheie si a descrierilor companiilor in vectori numerici pentru a accelera potrivirea.

Baze de Date: Stocarea datelor preprocesate intr-o baza de date optimizata pentru cautari rapide.

### Asumari si factori necunoscuti
Calitatea Datelor: Se presupune ca descrierile companiilor si taxonomia sunt precise si cuprinzatoare. Informatii incomplete sau eronate pot afecta negativ acuratetea.

Relevanta Taxonomiei: Taxonomia trebuie sa fie relevanta si actualizata pentru a reflecta corect activitatile companiilor.

Distributia Termenilor: Se presupune ca termenii importanti din taxonomie apar si in descrierile companiilor. Daca exista un decalaj in vocabular, acuratetea poate scadea.

Evolutia Afacerilor: Activitatile companiilor se pot schimba in timp, ceea ce ar putea necesita actualizarea regulilor de clasificare.

### Concluzie
Abordarea aleasa reprezinta un compromis intre simplitate si eficienta. Desi are limitari, ofera o baza solida pentru clasificarea companiilor, care poate fi imbunatatita prin optimizari si actualizari periodice. Principala provocare consta in mentinerea acuratetei si relevantei in timp, pe masura ce datele si activitatile companiilor evolueaza.
