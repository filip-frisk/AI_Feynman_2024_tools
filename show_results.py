
### Create table of equation and result ###

import regex as re
import pandas as pd
import string

EQUATIONNAME = 'I.8.14'
FILENAME = 'test_output.txt'
# Average_error_[bits]  Cummulative_error[bits] Complexity[bits] Error[bits/data_point] Expression
names= [ 'Average_error',  'Cummulative_error', 'Complexity', 'Error', 'Raw Expression' ]
df_raw = pd.read_csv(FILENAME,sep=' ', names=names )
df_rounded = df_raw.round(1)

# write a function that loops through column Expression and rounds the numbers to 1 decimal place
# Here are an example: exp(-23.549133910321+exp(pi)) -> exp(-23.5+exp(pi))
# The function should return a new dataframe with the rounded expressions
def round_expression(df):
    df['Cleaned Expression'] = df['Raw Expression'].apply(lambda x: re.sub(r'([0-9]+\.[0-9]+)', lambda y: str(round(float(y.group(1)),1)), x))
    return df
df_rounded_expressions = round_expression(df_rounded)

# Get the number of rows in the DataFrame
num_rows = df_rounded_expressions.shape[0]

# Generate a list of alphabetic labels
labels = list(string.ascii_uppercase[:num_rows])

# add this first to the dataframe
df_rounded_expressions['Labels'] = labels

# Add column Labels to the left 
df_rounded_expressions = df_rounded_expressions[['Labels'] + [ col for col in df_rounded_expressions.columns if col != 'Labels' ]]


### Create pareto frontier ###
import matplotlib.pyplot as plt

plt.plot(df_rounded['Complexity'], df_rounded['Error'], color='b')
plt.scatter(df_rounded['Complexity'], df_rounded['Error'], color='r')
plt.xlabel('Complexity [bits]')
plt.ylabel('Inaccuracy [bits/data_point]')
plt.title('Pareto frontier for equation: '+EQUATIONNAME, fontsize=10)
for i in range(num_rows):
    plt.text(df_rounded_expressions['Complexity'][i]+2.5, df_rounded_expressions['Error'][i]+0.01, df_rounded_expressions['Labels'][i], color = 'red', fontsize=14, ha='right',va = 'bottom')

# save using FILENAME

plt.savefig(FILENAME.replace('.txt','.png')) 

plt.show()


### Create tex-file  ###

df_rounded_expressions_latex = df_rounded_expressions.copy()

# remove trailing zeros in Average_error & Cummulative_error & Complexity & Error
df_rounded_expressions_latex['Average_error'] = df_rounded_expressions_latex['Average_error'].apply(lambda x: re.sub(r'\.0$', '', str(x)))
df_rounded_expressions_latex['Cummulative_error'] = df_rounded_expressions_latex['Cummulative_error'].apply(lambda x: re.sub(r'\.0$', '', str(x)))
df_rounded_expressions_latex['Complexity'] = df_rounded_expressions_latex['Complexity'].apply(lambda x: re.sub(r'\.0$', '', str(x)))
df_rounded_expressions_latex['Error'] = df_rounded_expressions_latex['Error'].apply(lambda x: re.sub(r'\.0$', '', str(x)))

# Only include labels, complexity and Error,raw expression and cleaned expression
df_rounded_expressions_latex = df_rounded_expressions_latex[['Labels', 'Complexity', 'Error', 'Raw Expression', 'Cleaned Expression']]
df_rounded_expressions_latex.columns = ['Label', 'Complexity', 'Error', 'Raw Expression','Cleaned Expression']


df_rounded_expressions_latex.to_latex(FILENAME.replace('.txt','.tex'), index=False)

# Append the caption, label, and end of the table environment
with open(FILENAME.replace('.txt','.tex'), 'a') as f:
    f.write('\caption{Pareto frontier for equation: ' + EQUATIONNAME + ' with Complexity in bits and Error in bits/data point}\n')
    f.write('\label{tab:pareto_' + EQUATIONNAME + '}\n')
    f.write('\\end{table}\n')


