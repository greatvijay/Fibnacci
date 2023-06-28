#Fibnacci numbers between 0 and 50
num_1=0
num_2=1
sum=0
print(num_2)
while num_2<50:
    sum=num_1+num_2
    num_1=num_2
    num_2=sum
    if sum<=50:
        print(sum)


    