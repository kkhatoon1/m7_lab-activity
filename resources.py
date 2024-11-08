#khateejakhatoon
#nov 07 2024
#problem 2,5 
# this file contains functions for determining if a number is in a specific range and a function that runs only when the file is executed directly.
 
#problem 2: lets_see

def lets_see(number):
#check if the number is in range to (5 to 15)
    bottom =5
    top = 5+10
    if bottom <= number<= top:
        print(f"{number} is in the range of {bottom}to{top}.")
        return True #return true if the number is in range 
    else:
        print(f"{number} is not in the range of {bottom}to {top}.")
        return False #return false if the number is not in range 
    
#test the function 
lets_see(10)

#problem 5: main function
def main():
    # funtion that prints a message when the file is run directly.
        print("this only runs when i run the file directly") # message for direct execution 
# this print function will always execute of how file is run
        print("i will always get printed.")

#test the funtion 
if __name__ == "__main__":
     main()