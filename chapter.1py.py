#khateeja khatoon
# nov 07 2024
#problem 1,3,4 
#this file contains functions that demonstrates random greeting, list processiong, andunique element

# problem 1: say_my_name

import random 
def say_my_name(name):
    greeting_type = random.choice([0,1])
    if greeting_type == 0:
        print(f"hey, {name}! you look so bad!") #user greeting angrily
    else:
        print(f"hey, {name}! ypu look so beautiful!") #user greeting friendly
#test the function
say_my_name("kk")

#problem 3:  mutiply_if funtion

def multiply_if():
    #generate a list of 10 random integers between 1 and 20 
    random_numbers = [random.randint(1,20)for _ in range(10)]
    print(f"original list: {random_numbers}")
    updated_numbers = []
    for num in random_numbers:
        updated_numbers.append(num*5)
    else:
        updated_numbers.append(num)
        print(f"updated list: {updated_numbers}")
        return updated_numbers #return the updated list
    
#test the funtion 
multiply_if()

#problem 4: unique_elements function

def unique_elements(input_list):
    unique_list= []
    #iterate through each item in the input_list
    for element in input_list:
         #check if the element is not already in the unique_list
         if element not in unique_list:
            unique_list.append(element)
    unique_list.sort()
    return unique_list #return the sorted unique list

#test the function
print(unique_elements([1,4,4,4,5,3,4,7]))
    

   

