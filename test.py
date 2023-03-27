import time

# Define the letters in ASCII art
W = ["*       * ", "*       * ", "*   *   * ", "* *   * * ", "*       * "]
E = ["* * * * * ", "*         ", "* * * *   ", "*         ", "* * * * * "]
L = ["*         ", "*         ", "*         ", "*         ", "* * * * * "]
C = ["  * * * * ", "*         ", "*         ", "*         ", "  * * *   "]
O = ["  * * *   ", "*     *   ", "*     *   ", "*     *   ", "  * * *   "]
M = ["*       * ", "* *   * * ", "*   *   * ", "*       * ", "*       * "]

# Print the letters line by line with a delay, and add a space between each letter
for i in range(5):
    print(W[i], E[i], L[i], C[i], O[i], M[i], sep='  ')
    time.sleep(0.2)
print()

for i in range(5):
    if i == 1:
        print(W[i], E[i], L[i], C[i], O[i+1], M[i], sep='  ')
    else:
        print(W[i], E[i], L[i], C[i], O[i], M[i], sep='  ')
    time.sleep(0.2)
print()

for i in range(5):
    print(W[i], E[i], L[i], C[i], O[i], M[i], sep='  ')
    time.sleep(0.2)
print()

print(W[0], E[0], L[0], C[0], O[0], M[0], sep='  ')
time.sleep(0.2)

print(W[1], E[1], L[1], C[1], O[1], M[1], sep='  ')
time.sleep(0.2)

for i in range(2, 5):
    print(W[i], E[i], L[i], C[i], O[i], M[i], sep='  ')
    time.sleep(0.2)
