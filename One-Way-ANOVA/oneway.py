import scipy.stats as stats 

# 1. Input Data
feed_2 = [7.0, 7.5, 7.8, 8.3]
feed_4 = [5.8, 4.6, 4.8, 6.2]
feed_6 = [9.2, 9.6, 8.2, 8.5]
alpha = 0.05

# 2. Perform One-Way ANOVA
f_stat, p_value = stats.f_oneway(feed_2, feed_4, feed_6) 

# 3. Calculate CriƟcal Value for Comparison
# df_between = groups - 1 = 2
# df_within = total_samples - groups = 9
f_criƟcal = stats.f.ppf(1 - alpha, 2, 9) 

# 4. Output Results
print(f"Calculated F-staƟsƟc: {f_stat:.4f}")
print(f"CriƟcal F-value: {f_criƟcal:.4f}")
print(f"P-value: {p_value:.6f}")
if f_stat > f_criƟcal:
 print("Decision: Reject the Null Hypothesis.")
 print("Conclusion: Feed rate has a SIGNIFICANT effect on surface finish.")
else:
 print("Decision: Fail to Reject the Null Hypothesis.")
 print("Conclusion: Feed rate has NO significant effect on surface finish.")