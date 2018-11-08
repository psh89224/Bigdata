import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# Linear regression model
tips = sns.load_dataset("tips")
print(tips.head(100))
#sns.factorplot(x="time", y="total_bill", hue="smoker", col="day", data=tips, kine="box", size=4, aspect=.5)
# step4_3
# sns.lmplot(x="total_bill", y="tip", data=tips)
# step4_4
sns.lmplot(x="total_bill", y="big_tip", data=tips, logistic=True, y_jitter=.03).set_axis_labels("Total Bill", "Big Tip")
plt.title("Logistic Regression of Big Tip vs. Total Bill")
plt.show()
