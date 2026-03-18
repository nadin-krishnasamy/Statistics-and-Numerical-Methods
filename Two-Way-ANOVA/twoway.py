import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats 

# 1. Create the Dataset
data = {
 'Value': [12, 14, 20, 22, 17, 27, 19, 15, 15, 14, 17, 12, 18, 16, 22, 12, 19, 15, 20, 14],
 'Treatments': ['T1', 'T2', 'T3', 'T4'] * 5,
 'Blocks': ['B1']*4 + ['B2']*4 + ['B3']*4 + ['B4']*4 + ['B5']*4
}
df = pd.DataFrame(data) 

# 2. Fit the Two-Way ANOVA Model
model = ols('Value ~ C(Treatments) + C(Blocks)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# 3. Find CriƟcal Values
alpha = 0.05
f_crit_tr = stats.f.ppf(1 - alpha, 3, 12)
f_crit_bl = stats.f.ppf(1 - alpha, 4, 12)

# 4. Extract Results
f_tr = anova_table['F']['C(Treatments)']
f_bl = anova_table['F']['C(Blocks)'] 

# 5. Output Results
print(f"Treatment F-stat: {f_tr:.4f} (CriƟcal: {f_crit_tr:.4f})")
print(f"Block F-stat: {f_bl:.4f} (CriƟcal: {f_crit_bl:.4f})")

# Decisions
if f_tr > f_crit_tr:
 print("Decision (Treatments): Reject H0. Treatments are significantly different.")
else:
 print("Decision (Treatments): Fail to Reject H0. No significant treatment effect.")
if f_bl > f_crit_bl:
 print("Decision (Blocks): Reject H0. Blocks are significantly different.")
else:
 print("Decision (Blocks): Fail to Reject H0. No significant block effect.")