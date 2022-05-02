def alphabet_position(text):
    alp = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alp.find(c) + 1) for c in text.lower() if c in alp])

print(alphabet_position('jose'))

x = 'jose'

print(x[::-1])


y = [5,6,15,5,12]

print(max(y))


