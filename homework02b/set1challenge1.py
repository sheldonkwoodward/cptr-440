import binascii
import base64

# conversion function
def hexToBase64(text):
    return base64.b64encode(binascii.unhexlify(text)).decode('ascii')

# text to convert
text = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# results
expected_result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
result = hexToBase64(text)

# output
print(expected_result)
print(result)
if result == expected_result:
    print('Success!')
else:
    print('Failure!')

