#!/usr/bin/env python3

# Reads file file_name and returns contents in 8-bit chunks
def read_binary_file(file_name):
	chunks = ['1110100'] # FIXME
	return chunks

# Split the 12-bit main key into three 4-bit sub_keys
def key_scheduler(main_key):
	key = str(main_key)
	sub_keys = [key[i:i+4] for i in range(0, len(key), 4)]
	return sub_keys

# XOR encryption
def encrypt_block(contents, sub_keys):
	def feistel_round(left, right, subkey):
		# Ensure subkey is an integer
		subkey = int(subkey, 2) if isinstance(subkey, str) else subkey
		# Simple XOR operation for the Feistel function
		new_right = left ^ subkey
		new_left = right
		return new_left, new_right
	
	encrypted_data = []
	for byte in contents:
		# Ensure byte is an integer
		byte = int(byte, 2) if isinstance(byte, str) else byte
		# Split the byte into left and right 4-bit halves
		left = (byte >> 4) & 0x0F
		right = byte & 0x0F
		
		# Perform 3 Feistel rounds
		for subkey in sub_keys:
			left, right = feistel_round(left, right, subkey)
			
		# Combine the left and right halves back into an 8-bit byte
		encrypted_byte = (left << 4) | right
		encrypted_data.append(encrypted_byte)
		
	return encrypted_data

def main():
	# User inputs data
	file_name = input("Input name of file to read: ")
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
	encrypted_block = encrypt_block(contents, sub_keys)
	print("\nEncrypted Data Block: ")
	print(encrypted_block)
	
	# Potentially add a decryption function
	
	return
	
# Calls main function
if __name__ == "__main__":
	main()
