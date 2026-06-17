# An electricity provider charges consumers according to the following tariff:
# First 49 units: ₹7 per unit
# Next 51 units (50–100): ₹11 per unit
# Above 100 units: ₹15 per unit
# Additionally, a fixed charge of ₹1000 is added to every bill.
# Given the number of electricity units consumed, calculate and print the total bill amount.



# unit = int(input())
# if unit<50:
#   print(7*unit+1000)
# if unit>=50 and  unit<=100:
#   ans = 49*7
#   unit-=49
#   ans+=(unit*11+1000)
#   print(ans)
# else:
#    ans = 49*7 + 51*11 
#    unit-=100
#    ans+=15*unit+1000
#    print(ans)

# num="dbvbjd" 
# for i in range(len(num)):
#   print(i) 
  
  
#  n = int(input())

# nonzero = 0
# zero = 0

# while n > 0:
#     lastdigit = n % 10

#     if lastdigit == 0:
#         zero += 1
#     else:
#         nonzero += 1

#     n //= 10

# print(zero, nonzero) 


# weight=int(input(""))
# if weight%2==0 and weight>2:
#    print("yes")
# else:
#   print("No")


# n=int(input("enter your number"))
# for i in range(1,n+1,1):
#    if i%3==0 and i%5==0:
#       print(i)
# sum=0  
# n=int(input("enter your no"))
# for i in range(1,n+1,1):
#    if i%2==0:
#     sum+=i
# print(sum)
     
# sum=0  
# for i in range(1,6):
#   sum+=i
# print(sum)
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        steps=0
    while num1>0 and num2>0:
        if num1>num2:
            num1==num2-num1
            newvalue==num1
            steps+=1
        else:
            num2==num1-num2
            newvalue==num2  
        if newvalue==0:
         steps+=1

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=2
        product=1
        sum=0
        while n>0:
            ld=n//10
            sum+=ld
            product*=ld
            return product-sum