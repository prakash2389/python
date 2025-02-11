
## Import packages
import os
import pandas as pd
import numpy as np
import random

## Create Dataframe
df = pd.DataFrame({
    "year" : np.arange(1900,2025),
    "sales" : [random.randint(100000, 200000) for _ in range(125)]
})

## Print Meand and standard deviation
print(df["sales"].mean())
print(df["sales"].std())
