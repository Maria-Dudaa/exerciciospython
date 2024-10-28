a, b = 0, 1

fibonacci = []


for _ in range(10):
    fibonacci.append(a)  
    a, b = b, a + b  

print("Os primeiros 10 termos da sequência de Fibonacci são:")
print(fibonacci)
