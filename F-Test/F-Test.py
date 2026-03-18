import scipy.stats as stats
import math

# 1. Input Data
method_1 = [20, 16, 26, 27, 23, 22]
method_2 = [27, 33, 42, 35, 34, 38]
alpha = 0.05

# 2. Calculate Variances (Sample Variance using ddof=1)
# Variance = sum((x - mean)^2) / (n - 1)
mean1 = sum(method_1) / len(method_1)
var1 = sum((x - mean1)**2 for x in method_1) / (len(method_1) - 1)
mean2 = sum(method_2) / len(method_2)
var2 = sum((x - mean2)**2 for x in method_2) / (len(method_2) - 1)

# 3. Calculate F-staƟsƟc
# For a two-tailed test, we put the larger variance on top
if var1 > var2:
 f_stat = var1 / var2
 dfn = len(method_1) - 1
 dfd = len(method_2) - 1
else:
 f_stat = var2 / var1
 dfn = len(method_2) - 1
 dfd = len(method_1) - 1

# 4. Find CriƟcal F-value
# alpha/2 is used for a two-tailed test
f_criƟcal = stats.f.ppf(1 - alpha/2, dfn, dfd)

# 5. Output Results
print(f"Variance of Method I: {var1:.4f}")
print(f"Variance of Method II: {var2:.4f}")
print(f"Calculated F-raƟo: {f_stat:.4f}")
print(f"CriƟcal F-value: {f_criƟcal:.4f}")
if f_stat > f_criƟcal:
 print("Decision: Reject the Null Hypothesis.")
 print("Conclusion: There is a significant difference in variances.")
else:
 print("Decision: Fail to Reject the Null Hypothesis.")
 print("Conclusion: There is no significant difference in variances.")
