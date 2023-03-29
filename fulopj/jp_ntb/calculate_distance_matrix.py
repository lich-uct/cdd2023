#!/usr/bin/env python3

import numpy as np
import pandas as pd
from rdkit import DataStructs

df = np.load('../data/df.npy', allow_pickle=True)
df = pd.DataFrame(df)
df.columns = ['Mol', 'Source', 'FP']

n = df.shape[0]
dist_matrix = np.zeros((n,n))    # initialize distance matrix to a square of zeros
for i in range(n):
    print(i)
    for j in range(i, n):
        dist_matrix[i,j] = DataStructs.TanimotoSimilarity(df.FP[i], df.FP[j])
        dist_matrix[j,i] = dist_matrix[i,j]

np.save('dist_matrix.npy', dist_matrix) 