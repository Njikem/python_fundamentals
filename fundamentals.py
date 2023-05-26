my_num = 10
my_string = 'Welcome back'
my_bool = True

print(my_bool)
print(my_string)
print(my_num) 

if (my_num > 10):
   print('that is larger than 10')

else: 
  print( 'is below 10')

if(my_num < 0 and my_bool == True):
    print('Negative and True')
elif(my_num >=0 and my_bool ==False):
    print('positive and False')
elif(my_num > 100 or my_bool == True):
    print('large or True')
else:
    print("I don't know")


string = ['bright', 'eva', 'mona', 'sonia']
nums = [1, 2, 3, 4, 5]

for string in strings:
    print(string)

for num in nums:
    print(num)


def static_greeting():
    print('Hello! my name is Maureen')

    static_greeting('Hello!', 'Mauby')

    def dynamic_greeting(greetings):
        print('Hello', greetings)

        dynamic_greeting('mum')
        dynamic_greeting('Alice')
        dynamic_greeting('John')


        def find_treasure(to_search):
         for test in to_search:
            if(test == 'treasure'):
                return True
            return False
                
strings_one = ['one', 'treasure', 'three']
contains_treasure = find_treasure(strings_one)
print(contains_treasure)

strings_one = ['one', 'two', 'three']
contains_treasure = find_treasure(strings_one)
print(contains_treasure)

                    





