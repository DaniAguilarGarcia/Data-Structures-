from stack import Stack
def convert_int_to_bin(dec_num)
    s = Stack()
#we calculate the remainder of the division of dec_num by 2 and push it onto the stack
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
# bin_num is declared as an empty string
    bin_num = ""
# loop on the very next line executes if the stack s is not empty.
    while not s.is_empty():
        bin_num += str(s.pop())
#The following code helps us to evaluate whether our implementation is correct or not
    return bin_num
print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))

print(int(convert_int_to_bin(56),2)==56)