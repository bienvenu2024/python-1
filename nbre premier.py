Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def est_premier(n):
...     if n<=1:
...         return False
...     for i in range (2,int(n**0.5) +1):
...         if n%i==0:
...             return False
...         return True
...     def nombre_preiers_1_a_100():
...         premiers=[]
...         for num in range(1,101):
...             if est_premiers(num):
...                 premiers.append(num)
...                 return premiers
...             print("Les nombres de 1 à 100 sont:")
