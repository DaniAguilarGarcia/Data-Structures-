from stack import Stack
def reverse_string(stack, input_str):
    #iterates over input_str and pushes each character on to stack.
    for i in range(len(input_str)):
        stack.push(input_str[i])
        #as an empty string.
    rev_str = ""
    while not stack.is_empty():
        #We pop off all the elements from the stack and append them to rev_str one by one
        rev_str += stack.pop()
        # until the stack becomes empty
    return rev_str
stack = Stack()
input_str = "daniela"
print(reverse_string(stack, input_str))