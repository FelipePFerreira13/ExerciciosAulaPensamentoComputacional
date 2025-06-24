import random
t=''
j=''
date=''
for i in range(16):
    t += str(random.randint(0,9))
for i in range(3):
    j += str(random.randint(0,9))

date += f'{str(random.randint(1,30))} {str(random.randint(1,12))}'
    
print(t, j, date)