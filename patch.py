with open('libapp.so', 'rb') as f:
    data = bytearray(f.read())

patches = [
    (b'not_subscribed\x00', b'yes_subscribed\x00'),
    (b'not_paid\x00',       b'yes_paid\x00\x00'),
    (b'notPaid\x00',        b'yesPaid\x00'),
]

total = 0
for old, new in patches:
    n = data.count(old)
    if n:
        data = data.replace(old, new)
        print(f"Patched {old!r} x{n}")
        total += n

print(f"Total: {total}")
with open('libapp_patched.so', 'wb') as f:
    f.write(bytes(data))
