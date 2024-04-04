How have state-level policy responses influenced vaccination uptake of the COVID-19 pandemic in the United States


Description: 

This study assesses the influence of state-level policies on COVID-19 vaccination rates in the US, 
focusing on California, New York, Texas, and Florida from 2020 to 2022. Initial findings
show a positive correlation between policy intensity and vaccination rates, highlighting the
effectiveness of early measures. However, in 2021, this trend reversed due to vaccine hesitancy
and availability, indicating the complex nature of policy impact over time. The analysis also
reveals that mandatory vaccination policies correlate with higher uptake. Overall, the research
suggests that adaptable, equity-focused public health policies are crucial for successful
vaccination campaigns in the face of evolving public health challenges.


Data: 

Our study uses data from the Oxford COVID-19 Government Response Tracker (OxCGRT), which tracks how governments worldwide have responded to the pandemic, focusing especially on vaccination policies from 2020 to 2022.
https://github.com/OxCGRT/covid-policy-dataset/tree/main


Method:

We aim to analyze the correlation between government policy intensity and changes in vaccination rates using Spearman's rho (ρ) and Kendall's tau (τ).

Correlation_Multiple_State_to_File.py Caculate the Spearman and Kendall correlation.


Data Visualization:


State_Population_plotly.py: Plot the trend of the population vaccinated over time.

Spearman2021.py: Plot the Spearman correlation coefficients in 2021.

SpearmanWhole.py: Plot the Spearman correlation coefficients from 2020 to 2022.

Kendall2021.py: Plot the Kendall correlation coefficients in 2021.

KendallWhole.py: Plot the Kendall correlation coefficients from 2020 to 2022.


