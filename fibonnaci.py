# # Enter number of terms needed                   #0,1,1,2,3,5....
# a= int(input("Enter the terms"))
# f=0                                         #first element of series
# s=1                                         #second element of series
# if a<=0:
#     print("The requested series is",f)
# else:
#     print(f,s,end, " ")
#     for x in range(2,a):
#         next=f+s                           
#         print(next,end=" ")
#         f=s
#         s=next

# Program to display the Fibonacci sequence up to n-th term

nth_terms = int(input("How many terms will you like to display? "))

# Defining the first two terms
term1, term2 = 0, 1values
count = 0

# checking if the number of terms is a positive integer or above 0
if nth_terms <= 0:
   print("Please enter a positive integer above 0")
elif nth_terms == 1:
   print("Fibonacci sequence upto",nth_terms,":")
   print(term1)
else:
   print("Fibonacci sequence:")
   while count < nth_terms:
       print(term1)
       nth = term1 + term2
       #this section updates values
       term1 = term2
       term2 = nth
       count += 1