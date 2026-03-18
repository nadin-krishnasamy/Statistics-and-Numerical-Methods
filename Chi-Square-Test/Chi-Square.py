import scipy.stats as stats

# 1. Observed Data (ConƟngency Table)
# Row 1: AIML [Python, Java, C++]
# Row 2: CSE [Python, Java, C++]
observed = [[50, 30, 20],
 [45, 45, 10]]
alpha = 0.05

# 2. Chi-Square Test
# chi2: StaƟsƟc, p: P-value, dof: Degrees of Freedom, expected: Expected Frequencies
chi2, p, dof, expected = stats.chi2_conƟngency(observed)

# 3. Find CriƟcal Value
criƟcal_value = stats.chi2.ppf(1 - alpha, dof)

# 4. Output Results
print(f"Calculated Chi-Square: {chi2:.4f}")
print(f"CriƟcal Chi-Square: {criƟcal_value:.4f}")
print(f"Degrees of Freedom: {dof}")
print(f"P-value: {p:.4f}")
if chi2 > criƟcal_value:
 print("Decision: Reject the Null Hypothesis.")
 print("Conclusion: Language preference DEPENDS on the department.")
else:
 print("Decision: Fail to Reject the Null Hypothesis.")
 print("Conclusion: Language preference is INDEPENDENT of the department.")
