Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def primitive(a,b):
...     D=f"f'(x)={2*a}x+{b} if b !=0 elsef"f'(x)={2*a}x"
...     
SyntaxError: unterminated f-string literal (detected at line 2)
>>> def primitive(a,b):
...     D = f"f'(x)={2*a}x+{b} if b !=0 else f"f'(x)= {2*a}x"
...     
SyntaxError: unterminated f-string literal (detected at line 2)
>>> def derivée(a,b):
...     D = f"f'(x)={2 * a}x+ {b}" if b !=0 else f"f'(x)= {2*a}x"
...     return D
...     def primitive(a,,b,c):
...         
SyntaxError: invalid syntax
>>> def derivée(a,b):
...     D = f"f'(x)={2 * a}x+ {b}" if b !=0 else f"f'(x)= {2*a}x"
...     return D
...     def primitive(a,b,c):
...         P = f"F(x)={a/3}x^3 + {b/2}^2 + {c}x + c"
...         return P
...     try:
...         a=float(input("Entrez le coeficient a de la fonction:"))
...         b=float(input("Entez le coeficient b de la fonction:"))
...         c=float(input("Entrez le coeficient c de la fonction:"))
...         D=derivée(a,b)
...         print(f"Derivée : {D}")
...         P=primitive(a,b,c)
...         print(f"primitive:{p}")
...         except valueError:
