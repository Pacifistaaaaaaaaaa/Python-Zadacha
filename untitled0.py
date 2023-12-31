# -*- coding: utf-8 -*-


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


unique_values = data["whoAmI"].unique()
one_hot_data = pd.DataFrame()

for value in unique_values:
    one_hot_data[value] = (data["whoAmI"] == value).astype(int)

one_hot_data.head()


#попытка сделать pull