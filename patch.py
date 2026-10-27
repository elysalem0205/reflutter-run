with open('libapp.so', 'rb') as f:
    data = bytearray(f.read())

patches = [
    (b'not_subscribed', b'yes_subscribed'),
    (b'not_paid\x00',   b'is_paid\x00\x00'),
    (b'notPaid\x00',    b'isPaid\x00\x00'),
]

for old, new in patches:
    count = data.count(old)
    if count:
        data = data.replace(old, new)
        print(f"Patched '{old}' x{count}")

with open('libapp_patched.so', 'wb') as f:
    f.write(bytes(data))
print("Done")
