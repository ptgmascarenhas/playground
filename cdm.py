def string_to_bin(string_s):
    bin_list = ' '.join(format(ord(x), 'b') for x in string_s).split()
    bin_list_list = []
    for item in bin_list:
        if len(item) == 7:
            item = "0" + item
        bin_list_list.append([int(x) for x in item])
    return bin_list_list, len(string_s)

def bin_to_string(bin_word):
    word = ""
    for item in bin_word:
        chars = [str(int(x)) for x in item]
        chars = ' '.join(chars).replace(" ", "")
        an_integer = int(chars, 2)
        ascii_character = chr(an_integer)
        word += ascii_character
    return word

def multiply(msg, code):
    sig = []
    for item in msg:    
        sig.append([ item[x]*code[x] for x in range(0, len(code)) ])
    return sig

def sum(sig1, sig2):
    sum_list = []
    for index in range(0,len(sig1)):
        sum_list.append([x + y for x, y in zip(sig1[index], sig2[index])])
    return sum_list

def sum_dc(msg, dc):
    sig = []
    for item in msg:    
        sig.append([ item[x]+dc[x] for x in range(0, len(dc)) ])
    return sig

###############################################################################

# Codes
cod1 = [-1,  1, -1,  1, -1,  1, -1,  1]
cod2 = [-1, -1, -1, -1,  1,  1,  1,  1]
dc_p = [ 0.5,  0.5,  0.5,  0.5,  0.5,  0.5,  0.5,  0.5]
dc_n = [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5]

# cod1 = [-2,  2, -2,  2, -2,  2, -2,  2]
# cod2 = [-2, -2, -2, -2,  2,  2,  2,  2]
# dc_p = [ 1,  1,  1,  1,  1,  1,  1,  1]
# dc_n = [-1, -1, -1, -1, -1, -1, -1, -1]

# Words
word1 = "isso_eh_um_teste_____"
word2 = "vamos_ver_se_funciona"

# Get binary from word
bin_word1, lng = string_to_bin(word1)
bin_word2, lng = string_to_bin(word2)

print(f"Binary word: {bin_word1}\n")

# Add DC to remove the 0s
bin_word1 = sum_dc(bin_word1, dc_n)
bin_word2 = sum_dc(bin_word2, dc_n)

print(f"Binary word (+DC): {bin_word1}\n")

# Get product code*chars
sig1 = multiply(bin_word1, cod1)
sig2 = multiply(bin_word2, cod2)

print(f"Multip: {sig1}\n")

# Sum the signals
sig = sum(sig1, sig2)

print(f"Sum: {sig}\n")

# Multiply again
bin_rec1 = multiply(sig, cod1)
bin_rec2 = multiply(sig, cod2)

print(f"Mult Inv.: {sig}\n")

# Remove DC to remove the 0s
bin_word1 = sum_dc(bin_word1, dc_p)
bin_word2 = sum_dc(bin_word2, dc_p)

print(f"Binary word (-DC): {bin_word1}\n")

result1 = bin_to_string(bin_word1)
result2 = bin_to_string(bin_word2)

print(f"Words: {result1} / {result2}\n")