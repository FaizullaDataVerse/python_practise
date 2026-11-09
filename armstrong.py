# armstrong number
num = int(input("enter number"))
temp=num
sum=0
while temp>0:
    digit= temp%10
    sum+=digit**3
    temp=temp//10
if num==sum:
    print("armstrong")
else:
    print("not armstrong")