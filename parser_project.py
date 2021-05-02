#I built this for work. We had a very large spreadsheet to navigate on how offers would be distributed via guest concern. 
#I read the spreadsheet into a dataframe so that we could parse the spreadsheet only finding rows related to our search.

#STEP ONE: PLEASE MAKE SURE 'spreadsheet' is loaded
#PLEASE REMEMBER TO PRESS <------ PLAY BUTTON -- using google co-lab
import pandas as pd
def enter_category(cat_colab):
  
  file = 'enter spread sheet file here' 
  df = pd.read_excel(file, sheet_name='spread sheet to read')
  df1 = df.dropna() #drop null values
  
  if cat_colab == 'Oos' or cat_colab=='oos' or cat_colab =='OOS':
    cat_colab = cat_colab.upper()
    df_search = df1[(df1['Colab'] == cat_colab)]
    return df_search
  else:
    x = cat_colab.title()
    df_search = df1[(df1['Colab'] == x)]
    return df_search
#file variable above may skip the trial block since the function isn't called
  try:
  with open("FILE NAME", "rb") as f:
    print("You are ready to search!")
except:
  print("PLEASE LOAD What Ever File that's loaded")
  
#This code will list the key search words that you can use above
file = 'enter spread sheet file here' 
df = pd.read_excel(file, sheet_name='spread sheet to read')
df1 = df.dropna()
num = 0 
l_nm = []
for i in df1['Colab']:
  if i not in l_nm:
    l_nm.append(i)
for x in l_nm:
  num += 1
  print(num, x)
