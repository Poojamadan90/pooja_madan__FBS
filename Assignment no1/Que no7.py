#find the roots quadratic equaition

A = int(input('Enter A:'))
B = int(input('Enter B:'))
C = int(input('Enter C:'))

Ans = (B*B) - (4*A*C)
Ans = Ans ** 0.5
root1 = (-B+ Ans)/ (2*A)
root2 = (-B- Ans)/ (2*A)

print("Root1:",root1)
print("Root2:",root2)