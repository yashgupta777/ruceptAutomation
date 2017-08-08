import cv2
import numpy as np

import csv

import pandas as pd
df = pd.read_csv("images/prices_ref.csv")
saved_column = df['Phone Price'] #you can also use df['column_name']

print df
print saved_column