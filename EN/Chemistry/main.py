import numpy as np
import torch
import torch.nn as nn
from scipy.spatial.distance import pdist, squareform

# [EN] Dummy molecular feature matrix representing 5 chemical compounds with 10 features each
# [PL] Sztuczna macierz cech cząsteczkowych reprezentujące 5 związków chemicznych po 10 cech każdy
molecular_features = np.random.rand(5, 10)

# [EN] Calculating pairwise Euclidean distance between molecular