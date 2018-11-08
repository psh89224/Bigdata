import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# 쌍별 이변량 산점도
iris = sns.load_dataset("iris")
#print(iris.head(100)) # 데이터셋 확인하기 step3_1, step3_2
sns.pairplot(iris)
#sns.pairplot(iris, hue="species")  # step3_2
plt.show()


