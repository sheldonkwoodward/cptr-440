import binascii

def encrpyt(text, key):
    return bytes([text[i] ^ key[i % len(key)] for i in range(len(text))])

text = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = b'ICE'

expected_result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
result = binascii.hexlify(encrpyt(text, key)).decode('ascii')

print(expected_result)
print(result)

if result == expected_result:
  print("Success!")
else:
  print("Failure!")

