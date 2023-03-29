import os
from cryptography.fernet import Fernet
from colorama import Fore, Style

# Initialize colorama
Fore.GREEN, Style.RESET_ALL

# ASCII art logo
logo = """
██████╗ ██╗██╗   ██╗███████╗██████╗ ██╗ ██████╗███████╗
██╔══██╗██║██║   ██║██╔════╝██╔══██╗██║██╔════╝██╔════╝
██║  ██║██║██║   ██║█████╗  ██████╔╝██║██║     █████╗  
██║  ██║██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██║     ██╔══╝  
██████╔╝██║ ╚████╔╝ ███████╗██║  ██║██║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝
"""

# Print the logo
print(Fore.GREEN + logo + Style.RESET_ALL)

# Get the file name from the user
filename = input("Enter the name of the file to obfuscate: ")

# Check if the file exists
if not os.path.exists(filename):
    print(f"{Fore.RED}File '{filename}' not found.{Style.RESET_ALL}")
    exit()

# Read the contents of the file
with open(filename, "rb") as f:
    contents = f.read()

# Generate a new Fernet key
key = Fernet.generate_key()

# Create a Fernet object with the key
fernet = Fernet(key)

# Encrypt the contents of the file in blocks of 64 KB
encrypted_contents = b""
for i in range(0, len(contents), 65536):
    block = contents[i:i + 65536]
    encrypted_block = fernet.encrypt(block)
    encrypted_contents += encrypted_block

# Write the encrypted contents to a new file with a '.obf' extension
new_filename = filename + ".obf"
with open(new_filename, "wb") as f:
    f.write(encrypted_contents)

# Print the success message
print(Fore.GREEN + "\nObfuscation process complete:")
print(f" - Input file: '{filename}'")
print(f" - Output file: '{new_filename}'")
print(f" - Key: {key.decode('utf-8')}")
print("\nEncryption process:")
print(f" - Total blocks encrypted: {len(encrypted_contents) // 65536}")
print(f" - Last block size: {len(encrypted_contents) % 65536} bytes")
print("Obfuscation process completed successfully." + Style.RESET_ALL, end='', flush=True)
