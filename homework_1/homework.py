

#Homework_part 1

# объявлем переменные
SEC_IN_MINUTE = 60
SEC_IN_HOUR = SEC_IN_MINUTE * 60
SEC_IN_DAY = SEC_IN_HOUR * 24

in_sec_str = input("количество секунд: ")
output_msg:str = ""



sec = int(in_sec_str)

    # if sec < 0
num_sign = 1
if sec < 0:
  sec = abs(sec)
  num_sign = -1

if sec >= SEC_IN_DAY:
  output_msg += str(num_sign * (sec // SEC_IN_DAY)) + " дн "
  sec %= SEC_IN_DAY

if sec >= SEC_IN_HOUR:
  output_msg += str(num_sign * (sec // SEC_IN_HOUR)) + " час "
  sec %= SEC_IN_HOUR

if sec >= SEC_IN_MINUTE:
  output_msg += str(num_sign * (sec // SEC_IN_MINUTE)) + " мин "
  sec %= SEC_IN_MINUTE

output_msg += str(num_sign * sec) + " сек"
print(output_msg)



#Homework_part 2

# 1. Сумма чисел из списка, сумма цифр которых делится нацело на 7.
cubes = [x**3 for x in range (100) if  x%2 != 0 ]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list=[]

print()

# итерация по списку
for i in range(len(cubes)):
    #print('---print cubes[i]', cubes[i])
    my_str = str(cubes[i])
    my_list = list(my_str)
    #print('print my_list', my_list)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
 
    # Вычислим сумму чисел 
    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

  
  
    #Сумма чисел делится нацело на 7
    if my_numbers_sum % 7 == 0:
        #print('Cумма чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list.append(my_numbers_sum)

print('Список чисел, делящихся на 7 : ',my_numbers_sum_list)

# 2. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
print()
cubes = [(x**3)+17 for x in range(100) if x%2 == 0]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list=[]

print()

# итерация по списку
for i in range(len(cubes)):
    #print('---print cubes[i]', cubes[i])
    my_str = str(cubes[i])
    my_list = list(my_str)
    #print('print my_list', my_list)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
 
    # Вычислим сумму чисел 
    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

  
    #Сумма чисел делится нацело на 7
    if my_numbers_sum % 7 == 0:
        #print('Cумма чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list.append(my_numbers_sum)

print('Список чисел, делящихся на 7 (с добавлением 17) : ',my_numbers_sum_list)

#Homework_part 3

for i in range(100):
    new_str=str(i+1)
    new_list = list(new_str)
    if int(new_list[-1])==1 and i+1!=11:
        print('{} процент'.format(i + 1))
    elif int(new_list[-1])>1 and int(new_list[-1])<= 4:
        if  i+1> 10 and i+1<= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))


