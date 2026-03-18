F-TEST


QUESTION:
Time taken by workers in performing a job is given below:
 Method I  : 20 16 26 27 23 22
 Method II : 27 33 42 35 34 38
 Test whether there is any significant difference between the variances of the Ɵme
distribuƟon at 5% level of significance.

AIM:

To determine if there is a staƟsƟcally significant difference between the variances of the Ɵme taken by
workers using Method I and Method II at a 5% significance level.

ALGORITHM:

1. Start
2. IniƟalize Data: Define two lists, method_1 and method_2, containing the Ɵme taken by workers. Set
the significance level alpha to 0.05.
3. Calculate Mean: Compute the average value for both datasets.
4. Calculate Sample Variance: * Compute the sum of squared differences from the mean for each
group.
o Divide by $(n - 1)$ to get the sample variance ($s_1^2$ and $s_2^2$).
5. Compute F-StaƟsƟc:
o Compare the two variances.
o Divide the larger variance by the smaller variance to ensure the $F$-raƟo is $\geq 1$.
6. Assign Degrees of Freedom: * Set $dfn$ (numerator) as $n-1$ of the larger variance group.
o Set $dfd$ (denominator) as $n-1$ of the smaller variance group.
7. Find CriƟcal Value: Use the F-distribuƟon funcƟon to find the criƟcal value at $1 - (\alpha/2)$ for
the given degrees of freedom.
8. Compare and Decide:
o If Calculated F > CriƟcal F, Reject the Null Hypothesis.
o Otherwise, Fail to Reject the Null Hypothesis.
9. Output Results: Print the calculated values and the final conclusion.

OUTPUT:

Variance of Method I: 16.2667
Variance of Method II: 25.3667
Calculated F-raƟo: 1.5594
CriƟcal F-value: 7.1464
Decision: Fail to Reject the Null Hypothesis.
Conclusion: There is no significant difference in variances. 