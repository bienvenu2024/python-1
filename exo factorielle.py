Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def factorielle(n):
...     """calcule la factorielle d'un nombre entier positif"""
...     if n<0:
...         return "la factorielle n'est pas difinie pour les entiers negatifs"
...     elif n==0 or n==1:
...         return 1
...     else:
...         result=1
...         for i in range(2, n+1):
...             result*=i
...             return result
...         def main():
...             print("calcul de la factorielle de deux nombres ")
...             #Entrée des deuxnombres
