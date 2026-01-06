age=18
if (age<18):
    print("Алкоголь запрещен")
else:
    print("Алкоголь разрешен")   

rate_as_str=input ("Оцените работу сотрудника от 1 до 5:")
rate=int (rate_as_str)
if(rate<1):
    rate=1
if(rate>5):
    rate=5 
feedback = ' '
if rate == 1:
    feedback = input("Расскажите, что нам улучшить: ")
elif rate == 2:
     feedback = input("Расскажите, что вас смутило: ")
elif rate == 3:
     feedback = input("Расскажите, как нам стать лучше: ")
elif rate == 4:
     feedback = input("Расскажите, почему не 5: ")     
else:
    feedback = input("За что нам похвалить сотрудников: ")
print(feedback) 
