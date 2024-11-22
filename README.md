Features
Key Management:

Generate a secure encryption key.
Load an existing encryption key for reuse.
File Encryption:

Encrypt individual files to ensure their contents are secure.
Save encrypted files to a designated directory for better organization.
File Decryption:

Decrypt individual encrypted files back to their original form.
Directory Encryption:

Batch encrypt all files within a specified directory.
Directory Decryption:

Batch decrypt all files within a specified directory.
Logging:

Detailed logs of encryption and decryption activities are stored in logs/encryption_tool.log.
Error Handling:

Robust error handling with helpful logs in case of failures





Prerequisites
Before using this tool, ensure you have the following installed:

Python 3.7+
Required Python packages (install with pip):
bash
Copy code
pip install cryptography
How to Use
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/file-encryption-tool.git
cd file-encryption-tool
Run the Tool: Launch the tool by running:

bash
Copy code
python file_encryption_tool.py
Choose an Option: Use the interactive menu to:

Generate an encryption key.
Encrypt or decrypt files.
Batch process directories for encryption or decryption.
Menu Options:

(g) Generate Key
(e) Encrypt a File
(d) Decrypt a File
(ed) Encrypt All Files in a Directory
(dd) Decrypt All Files in a Directory
(q) Quit the Tool
File Structure
bash
Copy code
file-encryption-tool/
├── file_encryption_tool.py   # Main script for the tool
├── encryption_key.key        # Generated encryption key (created upon key generation)
├── logs/
│   └── encryption_tool.log   # Log file for tool activities
├── encrypted_files/          # Directory where encrypted files are saved
Logging
All activities (success or failure) are logged in logs/encryption_tool.log for audit purposes.

