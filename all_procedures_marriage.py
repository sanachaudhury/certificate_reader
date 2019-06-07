#!/usr/bin/env python

from overfiles import create_file_list
from iter import extractTextList, pdf_to_list
from marriage import combined_m
from excel_2 import append_df_to_excel
import numpy as np
import pandas as pd

def everything(directory, first, last):
    a = create_file_list(directory)
    b = a[first:last]
    x = 0
    for file in b:
        text_elements = pdf_to_list(directory + '/' + file)
        list = combined_m(text_elements)
        data = np.array([['Column 0', 'Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7', 'Column 8', 'Column 9'], list])
        df = pd.DataFrame(data=data[1:,0:])
        append_df_to_excel('marr.xlsx', df)
