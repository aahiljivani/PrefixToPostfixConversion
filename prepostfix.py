from .stack_class import stack
def process_inputfile(input_file, output_file):
    """
    Reads each prefix expression from the input_file, strips the line of any whitespace and converts it to postfix.
    The function writes the echoed prefix expression and postfix result to the output_file.
    """
    for liner in input_file:
        # Remove leading,trailing  and 'in between' whitespace
        line = liner.strip().replace(" ", "")
        # Check if the line is not empty
        if line:
            try:
                # Convert line from prefix to postfix expression
                postfix_expression = pre_to_postfix(line)
                # write to the output file: prefix expression : postfix expression
                output_file.write('Prefix Expression is ' + line + ':\n' + 'Postfix Expression is ' + postfix_expression + '\n')
            # Allow ValueErrors and write them to the output file line corresponding to the input.txt
            except ValueError as e:
                output_file.write(str(e) + '\n')


def pre_to_postfix(line):
    """
    Converts a prefix expression to a postfix expression.

    This function utilizes two stacks to facilitate the conversion process: one to reverse the prefix expression
    and another to hold the intermediate postfix results. As the function iterates over the reversed prefix expression,
    operands are pushed to the holding stack, and operators are used to pop operands, form a postfix string, and
    push the result back on the holding stack. The function raises a ValueError if the caret '^' is used,
    prompting the user to replace it with the dollar sign '$' as the exponent operator. If the holding stack ends
    up with exactly one item, it is considered a valid postfix expression and is returned; otherwise, an error message
    is returned indicating an invalid expression.

    Parameters:
        line (str): A string representing a single prefix expression without whitespace.

    Returns:
        str: The converted postfix expression or an error message if the input is invalid.
    """
    operators = set(['$', '*', '/', '+', '-'])
    convert = stack()
    holding = stack()

    for char in line:
        # take all characters from line and push on to stack
        convert.push(char)

    while not convert.is_empty():
        # while loop instead of a for loop to preserve a stack's non-iterable properties
        char = convert.pop()
        if char == '^':
            # Raise a ValueError if the caret '^' is encountered
            raise ValueError(f"Invalid use of exponent, please change '^' character to '$' in the input line: '{line}'")

        else:
            if char not in operators:
                # If char is an operand, push it onto the holding stack
                holding.push(char)

            else:
                # If char is an operator,pop two operands and form a postfix string with operator at the end.
                if holding.GetLength() >= 2:
                    # each pop should be placed in a temp variable and appended to the string
                    first = holding.pop()
                    second = holding.pop()
                    operator = char
                    appended = first + second + operator
                    # the appended string is pushed back on to the holding stack
                    holding.push(appended)
                else:
                    # If there are not enough operands for an operation, return an error message
                    print("Error Invalid Expression")

    # If the holding stack has exactly one item, return it as the result
    if holding.GetLength() == 1:
        return holding.pop()
    else: # raise a ValueError as the number of operators and operands do not follow correct prefix format.
        raise ValueError(f"Error: Invalid Expression. Check the input expression for correctness and ensure it's a valid prefix expression. Input line: '{line}'")

