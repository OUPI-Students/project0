### Broken - Gives nonsense output. The issue seems to be with the feistel process. Any ideas? ###
# read EncryptedMessage.txt and convert to list
f = open("EncryptedMessage.txt", 'r')
message = f.read()
list_message = eval(message)

# Function to split message into four-bit segments
def split_byte(byte):
    left_bits = (byte & 0xF0) >> 4  # Left 4-bit 
    right_bits = byte & 0x0F  # Right 4-bit 
    return left_bits, right_bits

# request key as input and convert to binary
key = input("Please enter your key: ")
bin_key = ' '.join(format(ord(x), '012b') for x in key)
#print(bin_key)

# Divide the key into three 4-bit groups
group1 = bin_key[:4]
group2 = bin_key[4:8]
group3 = bin_key[8:12]

# Create subkeys using XOR
int_group1 = int(group1, 2)
int_group2 = int(group2, 2)
int_group3 = int(group3, 2)

k1 = int_group1^int_group2
k2 = int_group2^int_group3
k3 = int_group3^int_group1
    
k = [
	k1,
	k2,
	k3
    ]

print(f"{k1},{k2},{k3}")

# Split bytes for each character in secret and perform feistel process
z = []

for i in list_message:
    right, left = split_byte(i)
 
        # 3-round Feistel process
    for j in range(2,-1,-1):
        prev_left = left
        left = right
        right = prev_left ^ (right ^ k[j])
        
    z.append((right << 4) + left)
print(z)

#join list and convert to ascii characters
decrypted_message = ''.join(chr(num) for num in z)
print(decrypted_message)




