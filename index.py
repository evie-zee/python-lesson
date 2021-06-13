color=['red' , 'yellow' , 'green' , 'blue' , 'orange']
for i in color:
    print(i.capitalize())
print('\n')

for i in color:
    print(i.upper())
print('\n')

for i in color:
    print(i,len(i), '') 
for i in color:
    for j in i:
        print(j + '=' + str (i.count(j))) 
    print('\n')


