## INTRO

import os
import pandas as pd
"""
with open('test.txt','w') as file:
    file.write("Data succesfully scraped!") # random name test.txt, allow to write with 'w'. and file is random name.
"""

"""
states = ['California','Texas','Florida','New York']
population = [39613493,29730311,21944577,19299981]

dict_states = {'States':states,'Population':population}

df_states = pd.DataFrame.from_dict(dict_states)
print(df_states)
df_states.to_csv('states.csv',index=False)
"""

# Handling exception errors: try-except
new_list = [2,4,6,'California']
"""kod blogu hata verir düzeltilmis halini aşağıda yaptık
for element in new_list:
    print(element/2)
"""

"""
for element in new_list:
    try:
        print(element/2)
    except:
        print("the element is not a number!")
"""

# while-break
n = 4
while n > 0:
    print(n)
    n = n-1
    if n==2:
        break

print('Loop ended')










