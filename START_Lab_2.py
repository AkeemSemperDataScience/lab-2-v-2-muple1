def lab2Question1(word:str) -> bool:
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    word = word.replace(" ","")
    return word == word[::-1]



def lab2Question2(number_val: int) -> list:
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    fib_seq = [0,1]

    while True:
        next_val = fib_seq[-1] + fib_seq[-2]
        if next_val > number_val:
            break
        fib_seq.append(next_val)

    return fib_seq if number_val >= 0 else []

def lab2Question3(str1: str, str2: str) -> int:
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    str1 = str1.lower()
    str2 = str2.lower()
    return str1.count(str2)

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    if len(list1) != len(list2):
        return []
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    
    while True:
        password = input("Enter a password: ")
        if isValidPassword(password):
            print("Password is valid.")
            return password
        else:
            print("Invalid password.")

def isValidPassword(password: str) -> bool:
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True



## test
def test_lab2Question1():
    assert lab2Question1("purple") == False, "Test Case 1 Failed"
    print("test passed")
test_lab2Question1()

print(lab2Question2(10))
print(lab2Question3("Superstitious and superfluous", "super"))
print(lab2Question4([1,2,3],[4,5,6]))

password_to_test = 'ABdC1234567'
print(f"Is '{password_to_test}' a valid password? {isValidPassword(password_to_test)}")


