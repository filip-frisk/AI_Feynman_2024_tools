
import pickle


with open('units.pkl', 'rb') as f:
        dic_units = pickle.load(f)

### test all equaitons in units ###
# equations_in_units = list(dic_units.keys())
# SELECTED_EQUATIONS = equations_in_units



### test SOME equaitons in units ###
UNITS_OR_NO = 'without' # used to have unique file names 

SELECTED_EQUATIONS = ["I.8.14", "I.10.7", "I.50.26"] # Example equations in parent repo

NUMBER_OF_SAMPLES = 1000

import os 
import random 
path_OG = "Feynman_with_units/"

for equation in SELECTED_EQUATIONS:
    with open(path_OG + equation, "r") as f:
        file_content = f.readlines()
        sample_data = random.sample(file_content, NUMBER_OF_SAMPLES)
    path_new = f"Feynman_with_units_sampled_{NUMBER_OF_SAMPLES}_{UNITS_OR_NO}_units/"
    os.makedirs(path_new, exist_ok=True)
    
    with open(path_new+equation+"_"+str(NUMBER_OF_SAMPLES)+"_"+str(UNITS_OR_NO)+"_units", "w") as f:
        f.writelines(sample_data)
