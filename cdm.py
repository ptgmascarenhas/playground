def string_to_bin(string_s):
    bin_str = ' '.join(format(ord(x), 'b') for x in string_s)
    bin_list = [ int(x) for x in list(bin_str.replace(" ", ""))]
    return bin_list

def bin_to_string(bin_list):
    bin_word = ''.join(str(x) for x in bin_list)
    word = ""
    bin_char = ""
    for i in bin_word:
        bin_char += str(i)
        if len(bin_char) == 7:
            word += chr(int(f"0b{bin_char}", 2))
            bin_char = ""
    return word

def mux(msg, code):
    sig = []
    for x in msg:
        for y in code:
            sig.append(x*y)
    return sig

def demux(sig, code):
    opr1 = [ sig[x]*code[x%len(code)] for x in range(0, len(sig))]
    opr2 = []
    for i in range(0, len(opr1), len(code)):
        num = 0
        for j in range(0, len(code)):
            num += opr1[i+j]
        opr2.append(int(num/len(code)))
    return opr2

def sum(sig1, sig2):
    return [ sig1[x]+sig2[x] for x in range(0, len(sig1)) ]

def pnrz(bin_list):
    return [ int((x-0.5)*2) for x in bin_list ]

def pnrz_rev(bin_list):
    return [ int(x/2+0.5) for x in bin_list ]

###############################################################################

# Codes
cod1 = [-1,  1]
cod2 = [-1, -1]

# Words
word1 = "ene"
word2 = "unb"

# Get binary from word
bin_word1 = string_to_bin(word1)
bin_word2 = string_to_bin(word2)
print(f"Binary word 1: {bin_word1}")
print(f"Binary word 2: {bin_word2}\n")

# Add NRZ to remove the 0s
# msg1 = pnrz(bin_word1)
# msg2 = pnrz(bin_word2)
# print(f"Msg 1 (P-NRZ): {msg1}")
# print(f"Msg 2 (P-NRZ): {msg2}\n")
msg1 = (bin_word1)
msg2 = (bin_word2)

# Get product code*chars
sig1 = mux(msg1, cod1)
sig2 = mux(msg2, cod2)
print(f"Mux msg 1: {sig1}")
print(f"Mux msg 2: {sig2}\n")

# Sum the signals
sig = sum(sig1, sig2)
print(f"Sum: {sig}\n")

# Multiply again
bin_rec1 = demux(sig, cod1)
bin_rec2 = demux(sig, cod2)
print(f"Demux msg 1: {bin_rec1}")
print(f"Demux msg 2: {bin_rec2}\n")

# Remove DC to remove the 0s
# bin_word1_rec = pnrz_rev(bin_rec1)
# bin_word2_rec = pnrz_rev(bin_rec2)
# print(f"Binary word 1: {bin_word1_rec}")
# print(f"Binary word 2: {bin_word2_rec}\n")
bin_word1_rec = (bin_rec1)
bin_word2_rec = (bin_rec2)

result1 = bin_to_string(bin_word1_rec)
result2 = bin_to_string(bin_word2_rec)
print(f"Words: {result1} / {result2}\n")


print(bin_word1)
print(bin_word1_rec)
print(bin_word2)
print(bin_word2_rec)
