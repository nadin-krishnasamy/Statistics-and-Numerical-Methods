import scipy.stats as stats
import math

# --- 1. Data Input ---
sample_mean = 17.85 # Mean of the 14 rods (x-bar)
pop_mean = 18.5 # Specified strength (mu)
sample_std = 1.955 # Standard deviaƟon (s)
n = 14 # Sample size
alpha = 0.05 # Significance Level (5%)

# --- 2. CalculaƟons ---
# Formula: t = (x_bar - mu) / (s / sqrt(n))
t_staƟsƟc = (sample_mean - pop_mean) / (sample_std / math.sqrt(n))
# Degrees of freedom: df = n - 1
df = n - 1
# Calculate p-value (two-tailed test)
p_value = stats.t.sf(abs(t_staƟsƟc), df) * 2
# Find criƟcal t-value for alpha = 0.05
t_criƟcal = stats.t.ppf(1 - alpha/2, df)

# --- 3. Output Results ---
print(f"Calculated t-staƟsƟc: {t_staƟsƟc:.4f}")
print(f"CriƟcal t-value: {t_criƟcal:.4f}")
print(f"P-value: {p_value:.4f}")
if abs(t_staƟsƟc) > t_criƟcal:
 print("Decision: Reject the Null Hypothesis.")
 print("Conclusion: The result IS significant. The rods do not meet the 18.5 specificaƟon.")
else:
 print("Decision: Fail to Reject the Null Hypothesis.")
 print("Conclusion: The result is NOT significant. The rods meet the 18.5 specificaƟon.")
