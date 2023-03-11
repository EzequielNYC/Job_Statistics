Data Analyst Job Postings Analysis

This project analyzed a dataset of data analyst job postings to identify trends and statistics related to job location, required skills, and salary. The dataset contains information of over 2,000 job postings, including job title, company name, location, salary, required skills, and more.

Packages Used
python
import pandas as pd
import numpy as np
from scipy.stats import kstest, norm, ks_2samp
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


Methodolog
The analysis began with testing the distribution of standard salaries in the dataset using the Kolmogorov-Smirnov normality test, which indicated that the data is normally distributed (p-value > 0.05). A histogram was plotted to visualize the distribution of standard_salaries, which showed that most salaries are between $50,000 and $150,000.

The distribution of standard_salaries was also tested and visualized separately for positions that allow remote work (work_from_home == TRUE) and those that don't (work_from_home == FALSE). The Kolmogorov-Smirnov normality test indicated that remote work had a bimodal distribution and non-remote had a non-normal distribution using histograms to see the visualizations and its p score < .05.

The frequency of skill occurrence in the dataset was calculated and visualized using a bar chart. The top 5 most-requested skills are SQL, Python, Excel, Tableau, and Power_Bi. The distribution of standard_salaries was also visualized separately for positions that require SQL, Python, and Tableau skills using boxplots.

The frequency of city occurrence in the dataset was calculated and visualized using a bar chart. The top 5 cities for data analyst positions are Anywhere(Remote), Wichita, Maize, and Tulsa.

The frequency of company occurrence in the dataset was calculated and visualized using a bar chart. The top 5 companies for data analyst positions are UpWork, Cox Communications, Edward Jones, and Insight Global.

Visuals
The analysis used various visualizations to represent the data and findings. A histogram was used to visualize the distribution of standard_salaries, while boxplots were used to visualize the distribution of standard_salaries for positions that require specific skills. Bar, histograms, and other charts were used to represent the frequency of skill, city, and company occurrences.

Below are the image paths for the visualizations used in this analysis:

/Users/ezequielesparza/Job_Statistics/images/non_remote.png
/Users/ezequielesparza/Job_Statistics/images/python_salary.png
/Users/ezequielesparza/Job_Statistics/images/remote_salary.png
/Users/ezequielesparza/Job_Statistics/images/SQL_Salary.png
/Users/ezequielesparza/Job_Statistics/images/top_companies.png
/Users/ezequielesparza/Job_Statistics/images/top5_skills.png
Results
The analysis showed that most salaries for data analyst positions are between $50,000 and $150,000. Positions that allow remote work generally have a wider range of salaries than those that don't. The top 5 most-requested skills are SQL, Python, Excel, Tableau, and Power_Bi. The top 5 cities for data analyst positions are Anywhere(Remote), Wichita, Maize, and Tulsa, while the top 5 companies for data analyst positions are UpWork, Cox Communications, Edward Jones, and Insight Global.

Next Actions
Based on the findings, organizations looking to hire data analysts should focus on recruiting individuals with skills in SQL, Python, Excel, Tableau, and Power_Bi. Additionally, remote work opportunities should be considered to attract a wider pool of candidates. Further analysis could be done on the relationship between skills and salary, as well as the job requirements and responsibilities of the top companies.