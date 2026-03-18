import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats

# 1. Input Data
data = {
 'Driver': ['1','1','1','1', '2','2','2','2', '3','3','3','3', '4','4','4','4'],
 'Car': ['I','II','III','IV', 'I','II','III','IV', 'I','II','III','IV', 'I','II','III','IV'],
 'Blend': ['D','B','C','A', 'B','C','A','D', 'C','A','D','B', 'A','D','B','C'],
 'Efficiency': [15.5, 33.9, 13.2, 29.1, 16.3, 26.6, 19.4, 22.8, 10.8, 31.1, 17.1, 30.3, 14.7, 34.0, 19.7, 21.6]
}
df = pd.DataFrame(data) 

# 2. Fit the LaƟn Square ANOVA Model
# Formula: Efficiency ~ Drivers + Cars + Blends
model = ols('Efficiency ~ C(Driver) + C(Car) + C(Blend)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# 3. CriƟcal Value for alpha = 0.05, dfn=3, dfd=6
f_crit = stats.f.ppf(1 - 0.05, 3, 6)

# 4. Output Results
print(anova_table)
print(f"\nCriƟcal F-value (3, 6): {f_crit:.4f}")

# Conclusion Logic for Blend
f_blend = anova_table['F']['C(Blend)']
if f_blend > f_crit:
 print("Result: Reject H0 for Blends. Gasoline blends significantly affect efficiency.")
else:
 print("Result: Fail to Reject H0 for Blends. No significant difference between blends.") 
