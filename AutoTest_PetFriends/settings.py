import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

unvalid_email = os.getenv('unvalid_email')
unvalid_password = os.getenv('unvalid_password')

invalid_auth_key = {'key': '111d0c8710cd04e2f53c3699907c7b2222e9f40be53e41a84dc94444'}