
# coding: utf-8

# In[14]:


#Codeforces Round #230 (Div. 1)
#Problem C
n , k = input().split()
n = int(n)
k = int(k)
a = 1
b = 1
i = 1
sum = 0
while(n):
    #print(b)
    c = a + b 
    a = b 
    b = c
    #print(b,i)
    sum = sum + a * (i**k)
    i = i +1
    n = n - 1
print(sum%1000000007)

