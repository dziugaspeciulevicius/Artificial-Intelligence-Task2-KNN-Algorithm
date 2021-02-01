import pandas as pd
import math
from io import StringIO

# read data file
df = pd.read_csv('data.csv')

# read data_to_classify file
df_no_class = pd.read_csv('data_to_classify.csv')




# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyChaGrm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
