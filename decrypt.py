import random

for i in range(1):
    key_gen = (random.randint(11111111111, 999999999999999))

message = input ('Enter message you want to decrypt: ')
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = input("Encryption Key:")
encrypt = ''

for i in message:
  position = alphabet.find(i)
  new_position = (position+ -int(key)) % 94
  encrypt += alphabet[new_position]
  
output = encrypt
keyout = key_gen

print('Decrypted message: '+ output)