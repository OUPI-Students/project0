#!/usr/bin/env python3
import random # for random key generation

# Reads file file_name and returns contents in binary
def read_binary_file(file_name):
	with open(file_name, 'r') as file:
		contents = file.read()
	return contents

# Generates 3 sub keys
# Need to keep this in binary FIXME
def key_scheduler(main_key):
	# Convert the key to a hexadecimal string with 3 characters
	key_hex = f"{main_key:03x}"
	print("key hex: ")
	print(key_hex)
	
	# Convert each character to its decimal value
	key_dec = [int(char, 16) for char in key_hex]
	print("key dec: ")
	print(key_dec)
	
	# Create the 3-round subkeys using bitwise XOR
	k1 = key_dec[0] ^ key_dec[1]
	k2 = key_dec[1] ^ key_dec[2]
	k3 = key_dec[2] ^ key_dec[0]
	return [k1, k2, k3]

# XOR encryption
def encrypt_block(data_block, sub_key):
	return data_block ^ sub_key # FIXME
	# TypeError: unsupported operand type(s) for ^: 'list' and 'list'
	# https://www.geeksforgeeks.org/python-list-xor/

# Feistel rounds
# Test this
def feistel_round(left, right, sub_key):
	new_left = right
	new_right = left ^ encrypt_block(right, sub_key) # IDK if this works
	return new_left, new_right

def main():
	# User inputs data
	print("Input name of file to read: ")
	file_name = input()
	print("\nReading " + file_name + "...\n")
	
	# Prints contents of the file as written
	contents = read_binary_file(file_name)
	print("Contents of read file:\n(contents)")
	
	# Main key
	main_key = 101011001111 # Can use randomly generated key if needed
	print(f"\nMain Key: {bin(main_key)}")
	
	#Sub keys
	sub_keys = key_scheduler(main_key)
	print(f"Sub keys: {sub_keys}")
	
	#Data block
	data_block = contents
	print(f"Data Block: {data_block}") # FIXME?
	# TypeError: 'str' object cannot be interpreted as an integer
	
	# Encrypts data using simple XOR encryption
	encrypted_blocks = []
	encrypted_block = encrypt_block(data_block, sub_keys)
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
