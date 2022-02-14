def defangIPaddr(address):
	return '[.]'.join(address.split('.'))

print(defangIPaddr("1.1.1.1"))