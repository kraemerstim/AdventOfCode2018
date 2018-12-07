satz = input('Satz eingeben: ')
crypto_satz = []
for c in satz:
    if c == ' ':
        crypto_satz.append(' ')
        continue
    cryptochar = ord(c)-8
    print(str(cryptochar))
    if cryptochar < ord('a'):
        cryptochar = (ord('z')-(ord('a')-cryptochar)+1)
    crypto_satz.append(chr(cryptochar))
print(''.join(crypto_satz))