#!/usr/bin/env python3

# Reads file file_name and returns contents in binary
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
	# Extracts 4 bits of data from main_key per subkey
	sub_keys = []
	for i in range(3):
		subkey = (main_key >> (i * 4)) & 0xFFF # FIXME
		# TypeError: unsupported operand type(s) for >>: 'str' and 'int'
		sub_keys.append(subkey)
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
	print("\nReading file ~" +file_name + "~...")
	
	# Prints contents of the file as written
	contents = read_binary_file(file_name)
	# print("Contents of ~{file_name}~:" + contents)
	# TypeError: can only concatenate str (not "list") to str
	
	# 12-bit key 'ACF' = 101011001111
	main_key = 101011001111
	print(f"\nMain Key: \n{main_key}")
	
	# Sub keys
	sub_keys = key_scheduler(main_key) # I am a list
	print(f"\nSub keys: \n{sub_keys}")
	# Sub keys appearing as [3863, 2289, 2447]
	# Should be [1010, 1100, 1111]
	
	# Data block
	print("\nData Block: ") 
	print(contents)
	# TypeError: 'str' object cannot be interpreted as an integer
	
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
