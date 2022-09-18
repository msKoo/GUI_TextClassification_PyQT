import time

import pandas as pd
import matplotlib.pyplot as plt

from preprocessing import pre_html
from Visualizing import displayWordCloud, displayWordCount, dataGraph, displayResult

# df = pd.read_csv('./src/training_data.csv')
# test = ['id', 'sentence', 'label']

# for index, row in df.iterrows():
#     for item in test:
#         print(row[item])
#     print('======\n')
#
#     if index == 1:
#         break

# raw_contents = df['sentence'].values.tolist()

# print(raw_contents)
#
# tmp = list(map(lambda x:pre_html(x), raw_contents))

# tmp = []
# for con in raw_contents:
#     tmp.append(pre_html(con))

# print(raw_contents)

# displayWordCloud(' /'.join(raw_contents))
# displayWordCount(raw_contents)
# dataGraph(raw_contents)

displayResult()