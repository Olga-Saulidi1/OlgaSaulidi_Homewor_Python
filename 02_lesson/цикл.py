for x in range (1,5):
   print("x=",x, "x2=", x*x)

students = ["Ольга", "Алексей", "Нина", "Анна", "Ульяна", "мама", "папа", "Женя"]

for i in range (0, len (students)):     
    print(students [i])

word ="Test"    

for s in word:
    print(s)

for i in range (0, len(students)):     
    print(students [i])

for student in students:
    print(student)


nums = (1,2,3,4,5,6,7,8,9,10)

for n in nums:
    if (n % 2 == 1):
        print(n)
