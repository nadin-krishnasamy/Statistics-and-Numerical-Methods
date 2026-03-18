One-Sample Z-Test Analysis

📝 Problem Statement

The average breaking strength of steel rods is specified to be 18.5 thousand pounds. To verify this, a sample of 14 rods was tested, yielding a mean breaking strength of 17.85 thousand pounds and a standard deviation of 1.955.

🎯 Aim

To determine if the sample mean breaking strength is significantly different from the specified average of 18.5 thousand pounds at a 5% level of significance ($\alpha = 0.05$).

⚙️ Algorithm

1. Start the process.
2. Input Data: Define the sample mean ($\bar{x}$), population mean ($\mu$), standard deviation ($s$), and sample size ($n$).
3. Set Significance: Define $\alpha = 0.05$.
4. Calculate Statistics: Compute the test statistic using the formula: $$t = \frac{\bar{x} - \mu}{s / \sqrt{n}}$$
5. Determine Critical Value: Find the critical value from the distribution table for $df = n - 1$.
6. Decision Logic:If $|t| > [cite_start]t_{critical}$, Reject the Null Hypothesis.
7. Else, Fail to Reject the Null Hypothesis.Display Result and conclusion.

📊 Results & Conclusion

- Based on the Python implementation :
- Calculated Statistic: -1.2440 
- Critical Value: 2.1604 
- P-value: 0.2355 
- Decision: Fail to Reject the Null Hypothesis.
- Conclusion: The result is NOT significant. The steel rods meet the 18.5 thousand pounds specification.