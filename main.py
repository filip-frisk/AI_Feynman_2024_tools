import aifeynman
import pickle
import multiprocessing
import time 

def run_aifeynman_with_timeout(kwargs):
        """
        Wrapper function to run aifeynman.run_aifeynman with the provided arguments and keyword arguments.
        """
        # Assuming aifeynman.run_aifeynman() is the function you want to call
        aifeynman.run_aifeynman(**kwargs)

if __name__ == '__main__':
    # load units 
    with open('units.pkl', 'rb') as f:
        dic_units = pickle.load(f)

    ### run 3 examples ### 
    # Example 1: I.8.14
    # Example 2: I.10.7
    # Example 3 - I.50.26
        
    #SELECTED_EQUATIONS = ["I.8.14", "I.10.7", "I.50.26"]

    ### run all equations ### 
    SELECTED_EQUATIONS = list(dic_units.keys()) 
    
    pathdir = "Feynman_with_units_sampled_1000_without_units/"
    # filename = "example1.txt" (IN LOOP)
    BF_try_time = 30 # From example.py
    BF_ops_file_type = "14ops.txt" # From example.py
    polyfit_deg = 3 # From example.py
    NN_epochs = 100 # From paper 1 
    #vars_name = ["x2","x1","y2","y1","d"] # (IN LOOP)
    test_percentage = 20 # From paper 1

    SOLVER_MAX_TIME = 3000 # in seconds one hour

    for equation in SELECTED_EQUATIONS:

        ### Use dimensional analysis ###
        #vars_name = dic_units[equation][1:] # for all equations else bring your own dictionary ex. my_units = {'E':['m','c','E_n'], 'E_hard':['m','c','gamma','E_n'],....}

        ### DO NOT use dimensional analysis ###
        vars_name = [] # make it a empty list

      
        filename = equation + "_1000_without_units" # needs to be unique otherwise progress from other runs will be written over
      
        print(f"Starting analysing equation {equation} with variables {vars_name}")

        # Setup the arguments for aifeynman.run_aifeynman as keyword arguments
        kwargs = {
            'pathdir': pathdir,
            'filename': filename,
            'BF_try_time': BF_try_time,
            'BF_ops_file_type': BF_ops_file_type,
            'polyfit_deg': polyfit_deg,
            'NN_epochs': NN_epochs,
            'vars_name': vars_name,
            'test_percentage': test_percentage
        }

        # We need multiprocessing to be able to kill the program in SOLVER_MAX_TIME seconds
      
        # Create a Process object
        process = multiprocessing.Process(target=run_aifeynman_with_timeout, args=(kwargs,))
        process.start()
        start_time = time.time()
        # Wait for the process to complete or timeout
        process.join(timeout=SOLVER_MAX_TIME)
        
        end_time = time.time()
        print(f"\nTime taken to analyse equation {equation}: {end_time - start_time} seconds")
        print("\n")
        print("\n")
        print("New analysis.")
        print("\n")
        print("\n")

        if process.is_alive():
            print(f"Stopping the analysis of equation {equation} due to timeout")
            process.terminate()
            process.join()  # Wait for the process to be terminated
        else:
            print(f"Finished analysing equation {equation}")
        if equation != SELECTED_EQUATIONS[-1]:
            print("\n")
            print("sleep for 5 minutes to avoid overloading the system with fortrain code running")
            print("\n")
            time.sleep(300) 
        else:
            print("\n")
            print("Finished analysing all equations")
