'''
@version: 1.0.0
@author: 1chooo
@date: 2023/05/01

`main.py`
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import utils
import unit_test

def main():

    file_path = './ncu10m/160124.obs'
    lines, data = utils.load_data(file_path)

    unit_test.check_merge_result(lines, data)
    utils.observe_merged_data(data)

    modified_data = utils.data_type_checking(data)
    unit_test.check_modified_data(modified_data)

if __name__ == '__main__':
    main()