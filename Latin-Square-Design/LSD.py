LATIN SQUARE DESIGN

QUESTION:

An oil company wants to test the effect of four different blends of gasoline (A, B, C, D) on fuel
efficiency. The company has used four cars for testing the four types of fuel. To control the
variability due to the cars and the drivers, a Latin square design has been used and the data
collected are given in Table. Analyse the data from the experiment and draw conclusion.
Driver Cars
I II III IV
1 D=15.5 B=33.9 C=13.2 A=29.1
2 B=16.3 C=26.6 A=19.4 D=22.8
3 C=10.8 A=31.1 D=17.1 B=30.3
4 A=14.7 D=34.0 B=19.7 C=21.6

AIM:

To test whether there is a significant difference in fuel efficiency among four different gasoline blends (A, B,
C, D) while controlling for variability between drivers and cars at a 5% level of significance.

ALGORITHM:

1. Start
2. Hypothesis FormulaƟon:
 $H_{01}$ (Blends): There is no significant difference in fuel efficiency between blends.
 $H_{02}$ (Drivers): There is no significant difference between drivers.
 $H_{03}$ (Cars): There is no significant difference between cars.
3. Data Structuring: Organize the data into four columns: Drivers (Rows), Cars (Columns), Blends
(Treatments), and Fuel Efficiency (Values).
4. Compute ANOVA for LSD:
 Calculate Sum of Squares for Rows (Drivers), Columns (Cars), and Treatments (Blends).
 Calculate Error Sum of Squares ($SSE$).
 Calculate Mean Squares by dividing by the respecƟve degrees of freedom ($n-1$ for factors, $(n1)(n-2)$ for error).
5. Calculate F-staƟsƟcs: Divide each Factor Mean Square by the Error Mean Square.
6. Comparison: Compare calculated $F$ values with the criƟcal $F$ value from the table for df(3, 6) at alpha
= 0.05.
7. Conclusion and Stop.

OUTPUT:

 sum_sq df F PR(>F)
C(Driver) 31.3225 3.0 1.238290 0.375836
C(Car) 660.1025 3.0 26.096322 0.000830
C(Blend) 154.2625 3.0 6.100020 0.029606
Residual 50.5900 6.0 NaN NaN

CriƟcal F-value (3, 6): 4.7571
Result: Reject H0 for Blends. Gasoline blends significantly affect efficiency