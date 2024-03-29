def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def water_jug_problem(x, y, target):
    if target > max(x, y) or target % gcd(x, y) != 0:
        return None  

    visited_states = set()
    stack = [(0, 0)]

    while stack:
        current_state = stack.pop()
        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        if current_state[0] == target or current_state[1] == target:
            return visited_states

       
        stack.append((x, current_state[1])) 
        stack.append((current_state[0], y))  

       
        stack.append((0, current_state[1])) 
        stack.append((current_state[0], 0))  

        
        pour_amount = min(current_state[0], y - current_state[1])  
        stack.append((current_state[0] - pour_amount, current_state[1] + pour_amount))

        pour_amount = min(x - current_state[0], current_state[1])  
        stack.append((current_state[0] + pour_amount, current_state[1] - pour_amount))

    return None 

x = int(input("Enter the capacity of the first jug: "))
y = int(input("Enter the capacity of the second jug: "))
target = int(input("Enter the target amount of water: "))

solution = water_jug_problem(x, y, target)

if solution:
    print("Solution found!")
    for state in solution:
        print(state)
else:
    print("No solution found.")
