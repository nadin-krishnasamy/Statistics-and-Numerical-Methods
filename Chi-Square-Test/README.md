CHI-SQUARE TEST


QUESTION:

A survey was conducted to see if the preference for a Programming Language (Python, Java,
C++) is independent of a student's Department (AIML, CSE). The data collected is as follows:
Department Python Java C++
AIML 50 30 20
CSE  45 45 10

AIM:

To perform a Chi-Square test of independence to determine if there is a significant associaƟon between a
student's Department and their Programming Language preference at alpha = 0.05%.

ALGORITHM:

1) Start.
2) Define Hypotheses:
Null Hypothesis ($H_0$): Programming language preference is independent of the
department.Alternative Hypothesis ($H_1$): Programming language preference depends on the
department.
3) Input Data: Create a 2D array (contingency table) representing the observed frequencies.
4) Calculate Chi-Square Statistic:
5) Find Critical Value:
6) Comparison: Compare the calculated value with the tabulated value.
7) Show results. 

OUTPUT:

Calculated Chi-Square: 5.8673
CriƟcal Chi-Square: 5.9915
Degrees of Freedom: 2
P-value: 0.0532
Decision: Fail to Reject the Null Hypothesis.
Conclusion: Language preference is INDEPENDENT of the department.