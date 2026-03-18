TWO WAY ANOVA

QUESTION:

Treatments T1 T2 T3 T4
Blocks B1 12 14 20 22
B2 17 27 19 15
B3 15 14 17 12
B4 18 16 22 12
B5 19 15 20 14

AIM:

To determine if there are significant differences between the means of the four treatments (T1–T4) and the
five blocks (B1–B5) at a 5% level of significance.

ALGORITHM:

1. Start
2. Define Hypotheses:
 $H_{01}$ (Treatments): There is no significant difference between treatment means.
 $H_{02}$ (Blocks): There is no significant difference between block means.
3. Input Data: Organize the data into a 2D array or matrix.
4. Perform Two-Way ANOVA:
 Calculate the Sum of Squares for Treatments ($SST$), Blocks ($SSB$), and Error ($SSE$).
 Calculate Mean Squares ($MST$, $MSB$, $MSE$).
 Compute F-staƟsƟcs for both Treatments ($F_T$) and Blocks ($F_B$).
5. Determine CriƟcal Values:
 Find $F_{crit}$ for Treatments with $df(3, 12)$.
Find $F_{crit}$ for Blocks with $df(4, 12)$.
6. Comparison and Decision: If $F_{calculated} > F_{critical}$, reject the
corresponding null hypothesis.
7. Stop

OUTPUT:

Treatment F-stat: 0.5401 (CriƟcal: 3.4903)
Block F-stat: 1.3418 (CriƟcal: 3.2592)
Decision (Treatments): Fail to Reject H0. No significant treatment effect.
Decision (Blocks): Fail to Reject H0. No significant block effect. 