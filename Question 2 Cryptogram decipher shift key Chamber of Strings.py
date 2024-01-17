# Define function to decrypt a ciphertext
def decrypt(ciphertext, shift):
     # Initialize decrypted text as empty string
    decrypted_text = ""
    # Iterate through each character in the ciphertext
    for char in ciphertext: 
       # Check if the character is a letter
        if char.isalpha(): 
            # Calculate ASCII offset for uppercase or lowercase letters
            ascii_offset = ord('A') if char.isupper() else ord('a') 
            # Decrypt the character using Caesar cipher formula and ASCII offset
            decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset) 
         # If the character is not a letter
        else:
           # Append the character to the decrypted text without decryption
            decrypted_text += char 
    # Return the decrypted text
    return decrypted_text

def find_shift_key(ciphertext):
    # Iterate through each possible shift key (from 0 to 25)
    for shift in range(26): 
        # Decrypt the ciphertext using the current shift key
        decrypted_text = decrypt(ciphertext, shift) 
        # Print the shift key and the decrypted text
        print(f"Shift {shift}: {decrypted_text}") 

# Example cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Call the function to find the shift key for the example cryptogram
find_shift_key(cryptogram) 