# Paulean Marguerette F. Parrish
# BSCPE 1-4
# Problem 2 of Assignment 2
# The purpose of this program is to decrypt a string that has been encrypted

import pyfiglet

# Header for the activity
print("Decryption".center(70, "="))

# Request the user to input a string to be decrypted
encrypted_str = input("\033[95mEnter a string to decrypt: ")

# Replace the encrypted symbol with its vowel equivalent
decrypted_str  = encrypted_str.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')