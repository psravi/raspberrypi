# import required module
import os
import pandas as pd
#import openpyxl as ox

# Source files directory
src_dir = r'C:\Users\TESTUSR\Documents\src_folder'

# Target files directory
trg_dir = r'C:\Users\TESTUSR\Documents\trg_folder\\'

# iterate over files in above directory
for filename in os.listdir(src_dir):
    f = os.path.join(src_dir, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print("Source :" + f)
        read_file = pd.read_excel (r''+f)
        newfn = filename.replace(".xlsx",".csv")
        print("Target :" + trg_dir + newfn)
        read_file.to_csv (r''+trg_dir+newfn, index=None, header=True)
