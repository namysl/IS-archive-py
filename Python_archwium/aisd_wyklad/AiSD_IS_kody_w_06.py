#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Wyszukianie maksimum w tablicy
# Przyklad zastosowania metody "dziel i zwyciezaj"
# Ta implementacja jest generalnie optymalna i ma taka sama zlozonosc jak algorytm klasyczny
# Michal Baczynski (AiSD wyklad 06)

def maks_dz_zw(A,l,r):
    if l==r:
        return A[l]
    m=(l+r)//2
    m1=maks_dz_zw(A,l,m)
    m2=maks_dz_zw(A,m+1,r)
    if m1>m2:
        return m1
    else:
        return m2


# In[2]:


A=[3,5,7,9,1,3,10,11,0]
maks_dz_zw(A,0,len(A)-1)


# In[3]:


# Sortowanie przez scalanie
# Przyklad zastosowania metody "dziel i zwyciezaj"
# Ta implementacja jest stabilna i ma zlozonosc O(nlg(n))
# Michal Baczynski (AiSD wyklad 06)

def scalaj(T,l,m,r):
    i=l
    j=m+1
    A=[]
    while (i<=m) and (j<=r):
        if T[i]<=T[j]:
            A.append(T[i])
            i=i+1
        else:
            A.append(T[j])
            j=j+1
    while (i<=m):
        A.append(T[i])
        i=i+1
    while (j<=r):
        A.append(T[j])
        j=j+1
    for k in range(l,r+1):
        T[k]=A[k-l]
    return 

def mergesort(T,l,r):
    if l<r:
        # dzielimy na pol
        m=(l+r)//2
        # rekurencyjnie sortujemy lewa podtablice (ale operujemy tylko na indeksach!)
        mergesort(T,l,m)
        # rekurencyjnie sortujemy prawa podtablice (ale operujemy tylko na indeksach!)
        mergesort(T,m+1,r)
        # a teraz scalamy!
        scalaj(T,l,m,r)
    return T


# In[4]:


A=[2,8,1,3,4,0]

print(mergesort(A,0,len(A)-1))


# In[5]:


# Sortowanie szybkie na przykladzie ksiazki Cormen i inni "Wprowadzenie do algorytmow"
# Przyklad zastosowania metody "dziel i zwyciezaj"
# Ten algorytm nie jest stabilny
# Zlozonosc optymistyczna i srednia O(nlg(n)), pesymistyczna O(n^2)
# Michal Baczynski (AiSD wyklad 07)

def podzial(T,l,r):
    # ustalamy element podzialu
    x=T[r]
    i=l-1
    # przegladamy wszystkie elementy za wyjatkiem ostatniego
    for j in range(l,r):
        if T[j]<=x:
            i=i+1
            # zamiana
            y=T[i]
            T[i]=T[j]
            T[j]=y
    # zamiana z elementem podzialu
    y=T[i+1]
    T[i+1]=T[r]
    T[r]=y
    # Zwracamy miejsce, gdzie znalazl sie element podzialu, czyli u nas ostatni element
    return i+1

def quicksort(A,l,r):
    if l<r:
        # wykonujemy podzial, dzieki temu wiemy, ze na pozycji j jest odpowiedni element
        j=podzial(A,l,r)
        # rekurencyjnie sortujemy lewa podtablice (ale operujemy tylko na indeksach!)
        quicksort(A,l,j-1)
        # rekurencyjnie sortujemy prawa podtablice (ale operujemy tylko na indeksach!)
        quicksort(A,j+1,r)
    return A


# In[6]:


A=[2,8,1,3,4,0]
print(quicksort(A,0,len(A)-1))


# In[ ]:




