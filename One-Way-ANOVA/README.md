ONE-WAY ANOVA


QUESTION:

A mechanical engineer wants to investigate the effect of feed rate (mm/min) on the surface finish of
a milling operation. He has selected three different feed rates (i.e., 2, 4 and 6 mm/min) and decided
to obtain four observations at each feed rate. The study consists of 12 experiments (3 levels X 4
observations) as given below. Test whether the feed rate has significant effect on the surface finish.
Feed Rate (mm/min) Observations
(Surface Roughness)
2 7.0 7.5 7.8 8.3
4 5.8 4.6 4.8 6.2
6 9.2 9.6 8.2 8.5

AIM:

To determine if the different feed rates (2, 4, and 6 mm/min) have a staƟsƟcally significant effect on the
surface finish of a milling operaƟon at a 5% level of significance.

ALGORITHM:

1. Start
2. Define Hypotheses:
 Null Hypothesis ($H_0$): The mean surface roughness is the same for all feed rates ($\mu_1 =
\mu_2 = \mu_3$).
 AlternaƟve Hypothesis ($H_1$): At least one feed rate mean is significantly different.
3. IniƟalize Data: Create three lists or arrays represenƟng the surface roughness observaƟons for each
feed rate level.
4. Calculate ANOVA StaƟsƟcs:
 Compute the Mean Square Between (MSB) groups.
 Compute the Mean Square Within (MSW) groups (Error).
 Calculate the F-staƟsƟc
5. Determine Degrees of Freedom: Find CriƟcal Value: Obtain the criƟcal $F$-value from the $F$-
distribuƟon table for $(2, 9)$ degrees of freedom at $\alpha = 0.05$.
6. Comparison:
 If Calculated F > CriƟcal F (or $P\text{-value} < \alpha$), Reject $H_0$.
 Otherwise, Fail to Reject $H_0$.
7. Output Results and Stop.

OUTPUT:

Calculated F-staƟsƟc: 29.5067
CriƟcal F-value: 4.2565
P-value: 0.000112
Decision: Reject the Null Hypothesis.
Conclusion: Feed rate has a SIGNIFICANT effect on surface finish. 