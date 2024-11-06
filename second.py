from string import ascii_uppercase

message =  "SATELITENITOHSDQNTELESCOPIONUDMTRNFOSSIL"
coder_code = int(input("Coder code: "))

print(f"message: {message}")
print(f"coder code: {coder_code}")

# step 1
coder_code_sum = coder_code
while(coder_code_sum > 26):
    coder_code_sum = sum(  map(int, list(str(coder_code_sum)))   )

coder_code_mapped_letter = ascii_uppercase[coder_code_sum-1]

print(f"sum: {coder_code_sum}")
print(f"letter: {coder_code_mapped_letter}")

message = message.replace(coder_code_mapped_letter, " ")
print(f"new message: {message}")

# step 2
is_odd = lambda x: x%2==1
is_even = lambda x: x%2==0

odd_key = (sum(list(filter(is_odd, list(map(int, list(str(coder_code))))))) % 26)+1

even_key = (sum(list(filter(is_even, list(map(int, list(str(coder_code))))))) % 26)+1


final_message = ""
for i, part in enumerate(message.split(" ")):


    for letter in part:
        
        letter_index = ascii_uppercase.find(letter)

        if(is_odd(i+1)):
            letter_index = (letter_index + odd_key)%26
        else:
            letter_index = (letter_index + even_key)%26
        
        final_message += ascii_uppercase[letter_index]

    final_message += " "

print(f"decoded message: {final_message}")



