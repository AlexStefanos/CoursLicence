# -*- coding: utf-8 -*-

"""
def mystere0(s) :
    Str -> Str
    if len(s) == 0 :
        return ""
    else :
        return mystere0(s[1,len(s)]) + s[0])"""

def mystere1(n) :
    """Int -> Str
    Donne l'heure à partir d'un nombre de secondes"""
    a = n // 3600
    c = n % 3600
    b = c // 60
    c = c % 60
    return (str(a) + ":" + str(b) + ":" + str(c))

def mystere2(n) :
    """Int -> Int
    Factorielle de n-1 """
    u = 1
    for x in range(1, n, 1) :
        u = u * x
    return u

def mystere3(n) :
    """Int -> Int
    A partir de quel carré m > n"""
    m = 0
    while (m+1)**2 < n :
        m = m + 1
    return m


def mystere4(n):
    """Int -> Int
    Renvoie le mystere5(n-1) au carré si n=/0, sinon il renvoie 2"""
    if (n==0):
        return 2
    else:
        return mystere5(n-1) * mystere5(n-1)

    
def mystere5(n):
    """ Int -> Int
    Retourne la somme des n premiers entiers impairs"""
    a = 1
    s = 0
    t = -1
    while (a <= n) :
        a = a + 1
        s = s + t + 2
        t = t + 2
    return s

def mystere6(n):
    """Int -> Int
    Retourne 2^n"""
    b, m = 2, n
    r = 1
    while m > 0:
        if m % 2 == 1:
            r = r * b
        b = b * b
        m = m // 2
    return r 

