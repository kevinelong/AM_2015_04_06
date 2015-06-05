def ascii(letters):
    output = []
    for c in letters:
        output.append(ord(c))
    return output


def characters(numbers):
    output = ""
    for n in numbers:
        output += chr(n)
    return output


def characters_two(numbers):
    output = []
    for n in numbers:
        output.append(chr(n))
    return ", ".join(output)


numbers = ascii("Kevin Ernest Long (503) 888-6879 \t\talmost\nthe\nend")

original = characters(numbers)  # USE chr
with_commas = characters_two(numbers)  # USE chr

print(numbers)
print(original)
print(with_commas)

