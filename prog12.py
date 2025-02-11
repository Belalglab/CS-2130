# Belal G
#4/18/2024
#Finite State Machines: Cryptoquotes Assigemement
# Main Funcation
def create_mapping(key):
    """Generate mapping dictionaries from the key for encoding and decoding.
    Args:
        key (str): A string of 26 unique uppercase letters.
    Returns:
        tuple: Two dictionaries, one for encoding and one for decoding.
    """
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encode_dict = dict(zip(alpha, key))
    decode_dict = dict(zip(key, alpha))
    return encode_dict, decode_dict

def transform_text(text, mapping):
    """Transform the text using the provided mapping, keeping non-alphabetic characters unchanged.
    Args:
        text (str): The string to encode or decode.
        mapping (dict): A dictionary mapping characters for transformation.
    Returns:
        str: The transformed text.
    """
    transformed = []
    for char in text.upper():
        if char in mapping:
            transformed.append(mapping[char])
        else:
            transformed.append(char)
    return ''.join(transformed)

def main():
    import sys
    
    # Initialize the main variables
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encode_dict, decode_dict = {}, {}
    key_entered = False  # Flag to check if a key has been entered
    
    while True:
        # Display menu options to the user
        print("\nPlease choose from the following options:")
        print("1 - Enter a key")
        print("2 - Display a key")
        print("3 - Encode a quote")
        print("4 - Decode a Cryptoquote")
        print("5 - Exit program")
        
        choice = input("Choice? ")
        
        if choice == '1':
            # Enter a new key
            while True:
                key_input = input("Please enter the key. Characters will be read until 26 unique characters are entered: ")
                filtered_key = ''.join([char.upper() for char in key_input if char.isalpha()])
                unique_chars = ''.join(sorted(set(filtered_key), key=filtered_key.index))
                
                if len(unique_chars) == 26:
                    encode_dict, decode_dict = create_mapping(unique_chars)
                    key_entered = True
                    break
                else:
                    print("Invalid key. Ensure exactly 26 unique alphabetic characters are entered.")
        
        elif choice == '2':
            # Display the current key
            if not key_entered:
                print("No key entered. Please enter a key first.")
            else:
                print("The key value is:")
                print(" ".join(alpha))
                print(" ".join(encode_dict[key] for key in alpha))
        
        elif choice == '3':
            # Encode a quote using the entered key
            if not key_entered:
                print("No key entered. Please enter a key first.")
            else:
                quote = input("Please enter the string to create the Cryptoquote from as one line of text: ")
                encoded_quote = transform_text(quote, encode_dict)
                print("The resulting string is:")
                print(encoded_quote)
        
        elif choice == '4':
            # Decode a cryptoquote using the entered key
            if not key_entered:
                print("No key entered. Please enter a key first.")
            else:
                cryptoquote = input("Please enter the Cryptoquote string to decode as one line of text: ")
                decoded_quote = transform_text(cryptoquote, decode_dict)
                print("The resulting string is:")
                print(decoded_quote)
        
        elif choice == '5':
            # Exit the program
            print("Bye!!! Hope you solved your Cryptoquote!")
            sys.exit()
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
