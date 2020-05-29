def reverse_string(string):
    reversed_string = ''
    i = -1
    for letter in string:
        reversed_string += string[i]
        i -= 1
    return reversed_string


print(reverse_string('Its always about the choice !'))
