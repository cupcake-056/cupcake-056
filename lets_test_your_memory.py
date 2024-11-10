import random
import time

def rand_elem():
    # contains int from 0 to 9 and chr from 'a' to 'j'
    container = [list(range(10)), [chr(i) for i in range(ord('a'), ord('j') + 1)]]
    for elements in container:
        # shuffle both int and chr
        random.shuffle(elements)
    return container   

r_e = rand_elem()
# appends both int and chr
flat_list = r_e[0] + r_e[1]
# select random 10 chr and in combined for series
result = random.choices(flat_list, k=10)
# convert result list into one full string
result_str = ' '.join(map(str, result))
print(result_str, end=' ', flush=True)#flush is used to force print with no delay
# the series vanishes after 15 seconds
time.sleep(15)
print("\033c", end='')
print("LETS TEST YOUR MEMORY")    

chances = 10
while chances > 0:   
    ans = input("Enter the elements you have seen: ").lower().strip().split()  # Split input into a list of elements
    
    # Compare the user's input (ans) with the result (split into a list)
    if ans == [str(x) for x in result]:  # Convert result elements to strings and compare
        print("YOU WON")
        print("The series is:", result_str.capitalize())
        break
    else:
        chances -= 1
        print("Your guess is wrong.")
        print("Chances remaining:", chances)
else:
    print("You ran out of chances. Better luck next time.")
    print("The series is:", result_str.capitalize())
