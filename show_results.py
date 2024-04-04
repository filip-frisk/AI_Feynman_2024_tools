import pickle 
import os
import pandas as pd
import regex as re
import string
import matplotlib.pyplot as plt

#with open('../units.pkl', 'rb') as f:
#        dic_units = pickle.load(f)

TYPE = 'demo3'
DIR_PATH = 'demo3/'
files = os.listdir(DIR_PATH)

files = [file for file in files if not file.startswith('.')] # delete hidden files 

def round_and_latex_expression(df):
    df['Raw Expression'] = df['Raw Expression'].apply(lambda x: "$"+x+"$") # add latex formatting    
    df['Cleaned Expression'] = df['Raw Expression'].apply(lambda x: re.sub(r'([0-9]+\.[0-9]+)', lambda y: str(round(float(y.group(1)),1)), x))
    return df


for file in files:
    print(f"Processing file {file}\n")
    names= [ 'Average_error',  'Cummulative_error', 'Complexity', 'Error', 'Raw Expression' ]
    df = pd.read_csv(DIR_PATH+file,sep=' ', names=names )

    df = df.reset_index(drop=True)
    df = round_and_latex_expression(df)
    
    df = df[['Average_error', 'Complexity', 'Raw Expression','Cleaned Expression']] # select only the columns we want

    df = df.rename(columns={'Average_error': 'Error'})
    
    df.insert(0,'Labels',list(string.ascii_uppercase[:df.shape[0]]))

    
    
    # Save reults in latex format
    save_path = f'{TYPE}_latex/'
    
    os.makedirs(save_path , exist_ok=True)
    
    with open(save_path+file +'.tex', 'w') as f:
        f.write(df.to_latex(index=False))


    # Save reults in latex format
    save_path = f'{TYPE}_plots/'

    os.makedirs(save_path , exist_ok=True)

    plt.plot(df['Complexity'], df['Error'], color='b')
    plt.scatter(df['Complexity'], df['Error'], color='r')
    plt.xlabel('Complexity [bits]')
    plt.ylabel('Inaccuracy [bits/data point]')
    for i in range(df.shape[0]):
        plt.text(df['Complexity'][i], df['Error'][i], df['Labels'][i], color = 'red', fontsize=14, ha='right',va = 'bottom')

    plt.savefig(save_path+file +'.png', dpi=300) 

    plt.close()

    #plt.show()

# using https://wolframalpha.readthedocs.io/en/latest/?badge=latest

 
""" Using wolframalpha API to get the results of the equations, I did it manually 
import wolframalpha

appId = 'JR3AT2-LVHPJHA755'
client = wolframalpha.Client(appId)

res = client.query('Test') # <class 'wolframalpha.Result'>
dict_res = {}
for pod in res.pods:
    for sub in pod.subpods:
        #print(sub.plaintext)
        dict_res[pod.title] = sub.plaintext
print(dict_res)
""" 
