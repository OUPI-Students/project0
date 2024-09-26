#!/usr/bin/env python3

# Reads file file_name and returns contents in 8-bit chunks
def read_binary_file(file_name):
	chunks = []
	with open(file_name, 'rb') as file:
		while True:
			byte = file.read(1)
			if not byte:
				break
			chunks.append(format(ord(byte), '08b'))
	return chunks

# Generates 3 sub keys
def key_scheduler(main_key):
	# Split the 12-bit main key into three 4-bit sub_keys
	sub_keys = [main_key[i:i+4] for i in range(0, len(main_key), 4)]
	return sub_keys
	
def xor_lists(contents, sub_key):
    # Ensure both lists are of the same length
    if len(contents) != len(sub_key):
        raise ValueError("Both lists must be of the same length")

    # Perform XOR operation
    result = [int(a) ^ int(b) for a, b in zip(contents, sub_key)]
    return result

# XOR encryption
def encrypt_block(contents, sub_key):
	# Ensure both lists are of the same length
	if len(contents) != len(sub_key):
		raise ValueError("Both lists must be of the same length")
	
	# Perform XOR operation
	result = [int(a) ^ int(b) for a, b in zip(contents, sub_key)]
	return result

# Feistel rounds
# TESTME
def feistel_round(left, right, sub_key):
	new_left = right
	new_right = left ^ encrypt_block(right, sub_key) # IDK if this works
	return new_left, new_right

def main():
	# User inputs data
	print("Input name of file to read: ")
	file_name = input()
	print("\nReading file \"" + file_name + "\"...")
	
	# 12-bit key 'ACF' = 101011001111
	main_key = 101011001111
	print(f"\nMain Key: \n{main_key}")
	
	# Sub keys
	sub_keys = key_scheduler(main_key)
	print(f"\nSub keys: \n{sub_keys}")
	# Sub keys appearing as [3863, 2289, 2447]
	# Should be [1010, 1100, 1111]
	
	# Data block
	contents = read_binary_file(file_name)
	print("\nData Block: ") 
	print(contents)
	
	# Encrypts data using simple XOR encryption
	encrypted_blocks = []
	encrypted_block = encrypt_block(contents, sub_keys) # FIXME
	encrypted_blocks.append(encrypted_block)
	print(f"\nEncrypted Block with Sub-Key {bin(sub_key)}: \n{bin(encrypted_block)}")
	# FIXME
	
	# 3 rounds of Feistel network; move me to own function
	for i in range(3):
		left, right = feistel_round(left, right, sub_keys[i])
		print(f"\nAfter Round {i+1} \n- Left: {bin(left)}, \n- Right: {bin(right)}")
	return

# Calls main function
if __name__ == "__main__":
	main()
