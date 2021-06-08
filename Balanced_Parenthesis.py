# The given string-->
given_string = '[{()()}]'
# Now we will use this string and find is it balanced or not.
# Creating the function/method that will check whether a list of strings are balanced or not-->
# in terms of parenthesis.

def pair_checker(opening_bracket, closing_bracket) :
    if opening_bracket == '(' and closing_bracket == ')':
        return True
    if opening_bracket == '{' and closing_bracket == '}':
        return True
    if opening_bracket == '[' and closing_bracket == ']':
        return True
    return False

# Taking a STACK named 'stack'. STACK--> 'Last in First out'

stack = []
for item in given_string:
    if item == '(' or item == '{' or item == '[':
        stack.append(item)
    elif item == ')' or item == '}' or item == ']':
        last_item_in_stack = stack[-1]

        if pair_checker(last_item_in_stack, item):
            print(stack[-1] , item , '---> Pair matches')
            pop_out_last_item_from_stack = stack.pop()
        else:
            print(stack[-1] , item , '---> Pair does not match')


print()

if len(stack) == 0:
    print('Every pair of bracket matches so-->')
    print('The given string satisfies balanced parenthesis')
else:
    print('Every pair of bracket does bot match so-->')
    print('The given string does not satisfy balanced parenthesis')

#  RIFAT