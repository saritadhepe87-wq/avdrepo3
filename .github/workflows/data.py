import pandas as pd
data = {
    'name':['A','B','C'],
    'Age': [30,20,20],
    'address': ['Pune','Mumbai','CSN']
}
print('Student Details')
df= pd.DataFrame(data)
print(data)