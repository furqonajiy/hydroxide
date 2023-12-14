import logging

from py.pgp import pgp_encrypt_file

# Example usage
file_path = 'path/to/your/file.txt'  # Replace with the path to your file
recipient_key = 'recipient_public_key.asc'  # Replace with the path to the recipient's public key


def main():
    logging.debug("Start Main Process")
    pgp_encrypt_file(file_path, recipient_key)


if __name__ == "__main__":
    logging.info("Start Application")
    main()
