# -*- coding: utf-8 -*-

#importing the necessary library for regression 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

"""# **Linear Regression of percentage of students achieving grade a with respect to grade threshold of grade a**"""

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/physics_grades_regression/physics_as_csv_grade_a.csv")
df.head(5)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_a (Physics)")
plt.ylabel("%_achieving_grade_a (Physics)")
plt.scatter(df.grade_threshold_of_grade_a, df.percent_achieving_grade_a, color='red', marker='+')

physics_a_reg = linear_model.LinearRegression()
physics_a_reg.fit(df[['grade_threshold_of_grade_a']], df.percent_achieving_grade_a)

predicted_percent_acheiving_grade_a = physics_a_reg.predict(df[['grade_threshold_of_grade_a']])
predicted_percent_acheiving_grade_a

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_a (Physics)")
plt.ylabel("%_achieving_grade_a (Physics)")
plt.scatter(df.grade_threshold_of_grade_a, df.percent_achieving_grade_a, color='red', marker='+')
plt.plot(df.grade_threshold_of_grade_a, physics_a_reg.predict(df[['grade_threshold_of_grade_a']]), color='blue')

"""# **Linear Regression of percentage of students achieving grade b with respect to grade threshold of grade b**"""

df_b = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/physics_grades_regression/physics_as_csv_grade_b.csv")
df_b.head(5)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_b (Physics)")
plt.ylabel("%_achieving_grade_b (Physics)")
plt.scatter(df_b.grade_threshold_of_grade_b, df_b.percent_achieving_grade_b, color='red', marker='+')

physics_b_reg = linear_model.LinearRegression()
physics_b_reg.fit(df_b[['grade_threshold_of_grade_b']], df_b.percent_achieving_grade_b)

predicted_percent_acheiving_grade_b = physics_b_reg.predict(df_b[['grade_threshold_of_grade_b']])
predicted_percent_acheiving_grade_b

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_b (Physics)")
plt.ylabel("%_achieving_grade_b (Physics)")
plt.scatter(df_b.grade_threshold_of_grade_b, df_b.percent_achieving_grade_b, color='red', marker='+')
plt.plot(df_b.grade_threshold_of_grade_b, physics_b_reg.predict(df_b[['grade_threshold_of_grade_b']]), color='blue')

"""# **Linear Regression of percentage of students achieving grade c with respect to grade threshold of grade c**"""

df_c = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/physics_grades_regression/physics_as_csv_grade_c.csv")
df_c.head(5)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_c (Physics)")
plt.ylabel("%_achieving_grade_c (Physics)")
plt.scatter(df_c.grade_threshold_of_grade_c, df_c.percent_achieving_grade_c, color='red', marker='+')

physics_c_reg = linear_model.LinearRegression()
physics_c_reg.fit(df_c[['grade_threshold_of_grade_c']], df_c.percent_achieving_grade_c)

predicted_percent_acheiving_grade_c = physics_c_reg.predict(df_c[['grade_threshold_of_grade_c']])
predicted_percent_acheiving_grade_c

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_c (Physics)")
plt.ylabel("%_achieving_grade_c (Physics)")
plt.scatter(df_c.grade_threshold_of_grade_c, df_c.percent_achieving_grade_c, color='red', marker='+')
plt.plot(df_c.grade_threshold_of_grade_c, physics_c_reg.predict(df_c[['grade_threshold_of_grade_c']]), color='blue')

"""# **Linear Regression of percentage of students achieving grade d with respect to grade threshold of grade d**"""

df_d = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/physics_grades_regression/physics_as_csv_grade_d.csv")
df_d.head(5)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_d (Physics)")
plt.ylabel("%_achieving_grade_d (Physics)")
plt.scatter(df_d.grade_threshold_of_grade_d, df_d.percent_achieving_grade_d, color='red', marker='+')

physics_d_reg = linear_model.LinearRegression()
physics_d_reg.fit(df_d[['grade_threshold_of_grade_d']], df_d.percent_achieving_grade_d)

predicted_percent_acheiving_grade_d = physics_d_reg.predict(df_d[['grade_threshold_of_grade_d']])
predicted_percent_acheiving_grade_d

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_d (Physics)")
plt.ylabel("%_achieving_grade_d (Physics)")
plt.scatter(df_d.grade_threshold_of_grade_d, df_d.percent_achieving_grade_d, color='red', marker='+')
plt.plot(df_d.grade_threshold_of_grade_d, physics_d_reg.predict(df_d[['grade_threshold_of_grade_d']]), color='blue')

"""# **Linear Regression of percentage of students achieving grade e with respect to grade threshold of grade e**"""

df_e = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/physics_grades_regression/physics_as_csv_grade_e.csv")
df_e.head(5)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_e (Physics)")
plt.ylabel("%_achieving_grade_e (Physics)")
plt.scatter(df_e.grade_threshold_of_grade_e, df_e.percent_achieving_grade_e, color='red', marker='+')

physics_e_reg = linear_model.LinearRegression()
physics_e_reg.fit(df_e[['grade_threshold_of_grade_e']], df_e.percent_achieving_grade_e)

predicted_percent_acheiving_grade_e = physics_e_reg.predict(df_e[['grade_threshold_of_grade_e']])
predicted_percent_acheiving_grade_e

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.xlabel("grade_threshold_of_grade_e (Physics)")
plt.ylabel("%_achieving_grade_e (Physics)")
plt.scatter(df_e.grade_threshold_of_grade_e, df_e.percent_achieving_grade_e, color='red', marker='+')
plt.plot(df_e.grade_threshold_of_grade_e, physics_e_reg.predict(df_e[['grade_threshold_of_grade_e']]), color='blue')



"""#**We Know That:** <br>
x-axis = grade_threshold_of_grade_e_(Physics) <br>
y-axis = %_achieving_of_grade_e_(Physics)<br>
_____________________________________________<br>
1. An upward sloping linear line means that when the grade threshold for a grade increases, percetage of students achieving that particular grade also increases.

2. A downward sloping linear line measn that when the grade threshold for a grade increases, percentage f students achieving that paricular grade decreases.

# **Conclusion:** <br>
For Grade (a) and Grade (b) <br>
1. The downward sloping curve reflects that as the grade threshold for grade (a) and grade (b) increase, the percentage (%) of students achieving grades (a) and (b) decreases.

For Grade (c), (d), and (e)
1. The upward sloping curve reflects that as the grade threshold for grade (a) and grade (b) increase, the percentage (%) of students achieving grades (a) and (b) increases.

2. The gradient of the linear line is deiffernt. This shows that "how much change in grade thresholds" will cause "how much change in % achieving that grade".
"""