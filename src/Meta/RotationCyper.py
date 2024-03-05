def rotationalCipher(input_str, rotation_factor):
    # Write your code here
    rotation_factor_digit = rotation_factor % 10
    rotation_factor_alpha = rotation_factor % 26

    output = []

    for i, ch in enumerate(input_str):
        if ch.isalpha():
            if ch.islower():
                output.append(chr((ord(ch) - ord('a') + rotation_factor_alpha) % 26 + ord('a')))
            else:
                output.append(chr((ord(ch) - ord('A') + rotation_factor_alpha) % 26 + ord('A')))
        elif ch.isdigit():
            output.append(chr((ord(ch) - ord('0') + rotation_factor_digit) % 10 + ord('0')))
        else:
            output.append(ch)

    return ''.join(output)