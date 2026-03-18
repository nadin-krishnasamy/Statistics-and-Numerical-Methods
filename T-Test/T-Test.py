import scipy.stats as stats
# Given Data
sample_mean = 0.742
pop_mean = 0.700
sample_std = 0.40
n = 10
alpha = 0.05
# Degrees of freedom
df = n - 1
# CalculaƟng the t-staƟsƟc
# Formula: t = (x_bar - mu) / (s / sqrt(n))
t_staƟsƟc = (sample_mean - pop_mean) / (sample_std / (n**0.5))
# CalculaƟng the p-value (two-tailed test)
p_value = stats.t.sf(abs(t_staƟsƟc), df) * 2
# Output Results
print(f"t-staƟsƟc: {t_staƟsƟc:.4f}")
print(f"p-value: {p_value:.4f}")
if p_value < alpha:
 print("Conclusion: Reject the null hypothesis. The parts do NOT meet specificaƟons.")
else:
 print("Conclusion: Fail to reject the null hypothesis. The parts meet specificaƟons.")