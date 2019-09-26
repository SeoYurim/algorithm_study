N  = int(input())

customer = []
for i in range(N):
  age, name = input().split()
  age = int(age)
  customer.append([age, name, i])
customer_list = sorted(customer, key= lambda customer : (customer[0], customer[2]))
customer_sort = list(map(lambda customer: customer[:-1], customer_list))
for j in customer_sort:
  print(*j)