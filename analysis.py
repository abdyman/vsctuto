import pandas as pd
dat = pd.read_csv('data/data.csv')

# Analyze cure rates for each drug and placebo
cure_rates = dat.groupby('Treatment')['Outcome'].apply(lambda x: (x == 'Cured').mean())
placebo_rate = cure_rates.get('Placebo', 0)
drugs = ['Drug A', 'Drug B', 'Drug C']
best_drug = 'None'
best_improvement = 0
for drug in drugs:
    improvement = cure_rates.get(drug, 0) - placebo_rate
    if improvement > best_improvement and improvement > 0:
        best_improvement = improvement
        best_drug = drug
with open('solution.txt', 'w') as f:
    f.write(best_drug)
