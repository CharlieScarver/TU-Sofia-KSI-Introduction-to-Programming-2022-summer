print("=== String formatting ===\n")

print("Placeholders %d, %f, %s")
a = 3
b = 9
s = "area"
print('a = %d ; b = %d ; %s = %d \n' % (a, b, s, a * b))

print("Using .format(...)")
print('a = {} ; b = {} ; area = {} \n'.format(a, b, a * b))

print("Using an f-string")
print(f'a = {a} ; b = {b} ; area = {a * b} \n')
