#!/usr/bin/env python3
import random # for random key generation

# Reads file file_name and returns contents in binary
def read_binary_file(file_name):
	with open(file_name, 'r') as file:
		contents = file.read()
	return contents
	
# TESTME
def text_to_binary(main_key)
	binary_list = [format(ord(char), '08b') for char in text
	return ' '.join(binary_list

# Generates 3 sub keys
def key_scheduler(main_key):
	# Extracts 4 bits of data from main_key per subkey
	sub_keys = []
	for i in range(3):
		subkey = (main_key >> (i * 4)) & 0xFFF
		sub_keys.append(subkey)
	return sub_keys

# XOR encryption
def encrypt_block(data_block, sub_key):
	return data_block ^ sub_key # FIXME
	# TypeError: unsupported operand type(s) for ^: 'list' and 'list'
	# https://www.geeksforgeeks.org/python-list-xor/

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
	print("\nReading file <" + file_name + ">...\n")
	
	# Prints contents of the file as written
	contents = read_binary_file(file_name)
	print("Contents of read file:\n" + contents)
	
	# 12-bit key 'ACF' = 101011001111
	# User inputs key
	print("Input encryption key: ")
	main_key = input()
	print(f"Main Key: {bin(main_key)}")
	
	# Sub keys
	sub_keys = key_scheduler(main_key)
	print(f"Sub keys: {sub_keys}")
	
	# Data block
	data_block = contents
	print(f"Data Block: {data_block}") # FIXME?
	# TypeError: 'str' object cannot be interpreted as an integer
	
	# Encrypts data using simple XOR encryption
	encrypted_blocks = []
	encrypted_block = encrypt_block(data_block, sub_keys) # FIXME
	encrypted_blocks.append(encrypted_block)
	print(f"Encrypted Block with Sub-Key {bin(sub_key)}: {bin(encrypted_block)}")
	# FIXME
	
	# 3 rounds of Feistel network; move me to own function
	for i in range(3):
		left, right = feistel_round(left, right, sub_keys[i])
		print(f"After Round {i+1} - Left: {bin(left)}, Right: {bin(right)}")
	return

# Calls main function
if __name__ == "__main__":
	main()
