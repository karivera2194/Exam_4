# python3 string_script.py py.test

# We are using multiple tests to create errors for bad data inputs

from string_script import *

import pandas as pd 

# first starting with inputs for obs function
# test obs kmer function 1
def test_obs_kmers_1():
  k = 1
  string = 'ATTTGGATT'
  actual_result = obs_kmers(k, string)
  expected_result = 3
  assert actual_result == expected_result
  
  # test obs kmer function 2
  # k should not run, need it to fail (NA)
def test_obs_kmers_1():
  k = 0
  string = 'ATTTGGATT'
  actual_result = obs_kmers(k, string)
  expected_result = NA
  assert actual_result == expected_result
  
  # test obs kmer function 3
  # k should not run, need it to fail (NA)
def test_obs_kmers_1():
  k = 100
  string = 'ATTTGGATT'
  actual_result = obs_kmers(k, string)
  expected_result = NA
  assert actual_result == expected_result

# look at obs/poss for letters 
def test_obs_kmers_1():
  k = 100
  string = 'ATTTGGAKX'
  actual_result = obs_kmers(k, string)
  expected_result = NA
  assert actual_result == expected_result
  
# then testing possible inputs 
# test poss kmer function
def test_poss_kmer():
  k = 1
  actual_result = poss_kmers(k, string)
  expected_result = 4
  assert actual_result == expected_result


# test the making of the dataframe (df_output)
# cant ref variables from not function 
def test_df_output1():
  string = 'ATT'
  df_output_exp = {'observed kmers': [2,2,1,5], 
            'possible kmers': [3,2,1,6]
            }
  df_actual = make_df(string)
  test = pd.DataFrame(df_output)
  final =  df_output_exp.equals(df_actual) #also try compare (this is an output, its a dataframe)
  assert final == True


