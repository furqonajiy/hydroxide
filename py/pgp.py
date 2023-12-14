import gnupg


def pgp_encrypt_file(file_path, recipient_key):
    # Initialize GPG object
    gpg = gnupg.GPG()

    # Read the file content
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file using the recipient's public key
    encrypted_data = gpg.encrypt_file(
        file_data,
        recipients=recipient_key,
        output=file_path + '.pgp'
    )

    # Save the encrypted file
    with open(file_path + '.pgp', 'wb') as encrypted_file:
        encrypted_file.write(str(encrypted_data))

    print('Encryption successful. Encrypted file saved as', file_path + '.pgp')
