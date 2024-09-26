#!/usr/bin/env python3

# Reads file file_name and returns contents in 8-bit chunks
def read_binary_file(file_name):
	chunks = [1110100] # FIXME
	return chunks

# Split the 12-bit main key into three 4-bit sub_keys
def key_scheduler(main_key):
	key = str(main_key)
	sub_keys = [key[i:i+4] for i in range(0, len(key), 4)]
	return sub_keys

# XOR encryption
def encrypt_block(contents, sub_key):
	encrypted_contents = []
	
	for i, content in enumerate(contents):
		# Convert binary strings to integers
		content_int = int(content, 2)
		sub_key_int = int(sub_key[i % len(sub_key)], 2)
		
		# Perform bitwise XOR
		encrypted_value = content_int ^ sub_key_int
		
		# Convert back to binary string, ensuring it's 8 bits long
		encrypted_binary = format(encrypted_value, '08b')
		
		encrypted_contents.append(encrypted_binary)
		
	return encrypted_contents

def main():
	# User inputs data
	print("Input name of file to read: ")
	file_name = input()
	print("\nReading file \"" + file_name + "\"...")
	
	# 12-bit key 'ACF' = 101011001111
	# Potentially add custom key function
	main_key = 101011001111
	print(f"\nMain Key: \n{main_key}")
	
	# Sub keys
	# Potentially add custom number of sub keys
	sub_keys = key_scheduler(main_key)
	print(f"\nSub Keys: \n{sub_keys}")
	
	# Data block
	contents = read_binary_file(file_name)
	print("\nData Block: ") 
	print(contents)
	
	# Encrypts data using simple XOR encryption
	encrypted_blocks = []
	encrypted_block = encrypt_block(contents, sub_keys)
	encrypted_blocks.append(encrypted_block)
	print("\nEncrypted Data Block: ")
	print(encrypted_block)
	
	# Potentially add a decryption function
	
	return
	
# Calls main function
if __name__ == "__main__":
	main()
