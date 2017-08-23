# ! python3.
# mapIt.py - Lanuches a map in the browser using an address fro the
# command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)

# TODO: Get address from clipboard.
    
