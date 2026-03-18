One-Sample T-Test

📝 Problem Statement:

A machinist is making engine parts with an axle diameter of 0.700 inch. A random sample of 10 parts shows a mean diameter of 0.742 inch with a standard deviation of 0.40.

🎯 Aim:

To test whether the sample mean diameter (0.742 inch) is significantly different from the specified diameter (0.700 inch) at a 5% Level of Significance (LoS).

⚙️ Algorithm

1. Start.
2. Input sample mean, population mean, standard deviation, and sample size.
3. Set $\alpha = 0.05$.
4. Calculate t-statistic: $t = \frac{\bar{x} - \mu}{s / \sqrt{n}}$.
5. Determine degrees of freedom ($df = n - 1$) and find the critical t-value.
6. Reject the Null Hypothesis if $|t| > [cite_start]t_{critical}$, else accept it.

📊 Result:

* t-statistic: 0.3320  * p-value: 0.7475 
Conclusion: Fail to reject the null hypothesis. The work is meeting the specifications.