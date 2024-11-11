import os
import logging
from cryptography.fernet import Fernet



logging.basicConfig(filename="logs/encryption_tool.log", level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")



# now lets Generate key for encryption:
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key","wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved")


# lets load_key
def load_key():
    with open ("encryption_key.key","rb") as key_file:
        return key_file.read()


# lets define Encryption function
def encrypt_file(file_path):
    try:
        key = load_key()
        fernet = Fernet(key)
        with open(file_path,"rb") as file:
            file_data = file.read()
            encrypt_data =  fernet.encrypt(file_data)
        encrypted_folder = "encrypted_files"
        os.makedirs(encrypted_folder, exist_ok=True)
        new_path  = os.path.join(encrypted_folder,os.path.basename(file_path))
        with open(new_path,"wb") as file:
            file.write(encrypt_data)
        logging.info(f"File{file_path} encrypted successfully and saved to{new_path}.")
        print(f"file encrypt and saved as {new_path}")
    except Exception as e:
        logging.error(f"Failed to encrypt {file_path}:{e}")
        print("An error occured during encryption. check the log file details.")

# generate_key()
# encrypt_file(r"C:\Users\ankit\Desktop\encryption tool project\detail.txt")

# lets create decryption function:
def decrypt_file(file_path):
    try:
        key = load_key()
        fernet = Fernet(key)
        with open(file_path,"rb") as file:
            encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_path,"wb") as file:
            file.write(decrypted_data)
        logging.info(f"File{file_path} decrypted succesfully.")
        print(f"file decrypted and saved as {file_path}")
    except Exception as e:
        logging.error(f"Failed to decrypt {file_path}:{e}")
        print("An error occur during decryption. check the log file for details.")


# decrypt_file(r"C:\Users\ankit\Desktop\encryption tool project\encrypted_files\detail.txt")

# now lets batch processing to enhnce feature
def encrypt_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root,file_name)
            encrypt_file(file_path)
    logging.info(f"All files in {directory_path} encrypted succesfully.")
    print("all files encrypted successfully.")


# now lets create decrypt function for directory
def decrypt_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path)
    logging.info(f"All files in {directory_path} decrypted successfully.")
    print("All files decrypted successfully.")



# Main function with user interface
def main():
    while True:
        choice = input("Choose an option: (g)enerate key, (e)ncrypt file, (d)ecrypt file, (ed) encrypt directory, (dd) decrypt directory, (q)uit: ").lower()
        if choice == 'g':
            generate_key()
        elif choice == 'e':
            file_path = input("Enter file path to encrypt: ")
            encrypt_file(file_path)
        elif choice == 'd':
            file_path = input("Enter file path to decrypt: ")
            decrypt_file(file_path)
        elif choice == 'ed':
            directory_path = input("Enter directory path to encrypt all files: ")
            encrypt_directory(directory_path)
        elif choice == 'dd':
            directory_path = input("Enter directory path to decrypt all files: ")
            decrypt_directory(directory_path)
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 'g', 'e', 'd', 'ed', 'dd', or 'q'.")

if __name__ == "__main__":
    main()
