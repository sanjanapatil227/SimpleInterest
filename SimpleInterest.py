import sys
principal=float(sys.argv[1])
rate=float(sys.argv[2])
time=float(sys.argv[3])
Interest=(principal * rate * time)/100
print("Simple Interest:",Interest)