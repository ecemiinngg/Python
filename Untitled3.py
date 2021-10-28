#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=3 #integer
b="c" #string
c=3.15 #float


# In[4]:


print(type(a))


# In[5]:


print(type(b))


# In[6]:


print(type(c))


# In[10]:


x=None
print(x)
#özel komutlardan biri none dır - tanımsız gibi kullanılır


# In[16]:


print(10 > 9)
print(10 == 9)
print(10 < 9)
#boolean (True-False verir) değer 1 ise (doğruysa) True değer 0 ise False verir.


# In[17]:


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# In[11]:


123=x
print(x)
#syntax(yazım) hatası verir, önce tanımlayacağımız karakteri-adı yazarız


# In[12]:


#kütüphane adı,özel kullanımı olan adlar tanımlama yaparken kullanılamazlar
import = 123
#import kelimesini kütüphane tanımlarken kullandığımız için hata verir


# In[13]:


#listeler
x = [1,2,3]
y=[1,2,3]
x=[4,5,6]
print(x)
#pythondaki derleyici kod okurken baştan sona okur ve değerleri değiştirir o yüzden en son tanımladığımız x bizim asıl değerimiz
#list,dict gibi typelar mutable(sonradan değişebilir) özelliğe sahiptirler 


# In[15]:


#nested iç içe geçen listeler
z=[1,2,[3,4,5],5,6]
print(z[2])
#içe içe olan listeyi bir eleman gibi okur
print(z[2][1])
#iç içe listedeki 1. elemanı verir


# In[18]:


myList=["ecem",1,1.5,"c"]
print(myList)
#listelerde type sorunu yoktur, tek bir type değil birden çok type olabilir :D


# In[19]:


thislist = list(("apple", "banana", "cherry")) 
print(thislist)
#list() liste olmayan bir veriyi listeye dönüştürür -make a list


# In[20]:


print(thislist[-1])
#listenin son elemanını verir hep ilk mi isticez :D    


# In[21]:


eco = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(eco[2:5])
#2 den başlayarak 5 e kadar olan elamanları 5 hariç sıralar


# In[22]:


print(eco[:4])


# In[25]:


isimler = ["ecem","selin","pelin","meltem"]
isimler.append("derin")
#listenin sonuna verilen elemanı ekler
print(isimler)


# In[26]:


isimler.insert(1,"mert")
print(isimler)
#belirlenen İNDEX e belirlenen elemanı ekler


# In[27]:


isimler.remove("mert")
print(isimler)
#verilen eleman ilk kullanımı için  listeden çıkarılır- eğer iki tane mert olsaydı rastlanan ilk mert çıkarılacak diğer mert kalacaktı


# In[28]:


isimler.index("selin")
#girilen elemanın indexini verir


# In[29]:


#listenin uzunluğunu bulmak(length)-eleman sayısını verir
len(isimler)


# In[30]:


#bir listede aranan bir elemanın kaç tane olduğunu bulmak
nums=[1,1,1,2,3,4,4,5]
nums.count(1)


# In[33]:


#bir listeyi ters çevirmek
myliste=[1,2,3,4,5,6]
myliste.reverse()
print(myliste)
#ya da
listem=[1,2,3,4,5,6]
listem[::-1]
#tersten başlayarak listeyi döndürür


# In[41]:


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#sort bir listeyi büyükten küçüğe sıralar


# In[43]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#alfabetik olarak sıralar türk alfabesi deellll


# In[45]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[46]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# In[47]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#extend 2 listeyi birbirine ekler


# In[48]:


#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list


# In[49]:


#if - else 

a= 10
b=20

if a>b :
    print("a büyüktür b")
elif a==b:
    print("a eşittir b")
else:
    print("a küçüktür b")


# In[50]:


#kullanıcıdan sayı alarak if else denemesi
a = int(input())
b=int(input())
if a>b :
    print("a büyüktür b")
elif a==b:
    print("a eşittir b")
else:
    print("a küçüktür b")


# In[51]:


# if else ile sayı tahmin oyunu
import random 
print("hello, whats u r name")
name= input()
number= random.randint(1,100)
print("well"+name+", I am thinking a number between 1-100")
print("guess 6 times")
for  guessesTaken in range(1, 7):
  print("take a guess")
  guess= int(input())
  if guess < number:
    print("your guess is to low")
  elif guess > number :
    print("your guess is to high")
  else:
    break   
if guess==number :
  print("good job"+name+"you guessed my number in"+str(guessesTaken)+"guesess" )
else:
  print("nope, ı was thinking number is "+str(number))


# In[52]:


# kısa şekilde yazımı
a = 2
b = 330
print("A") if a > b else print("B")


# In[53]:


#while döngüsü
#sınır değer sağlanmadığı sürece sonsuz döngüye girer
#döngünün ilerlemesi için elamanın arrtması gerekir
i = 1
while i < 5:
  print(i)
  i += 1


# In[54]:


#break ifadesi döngünün o anında döngüyü durdurur
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# In[55]:


#continue ifadesi o durumu atlayarak döngüyü devam ettirir
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[58]:


#for döngüsü (bir dizi,liste,dict vs. üstünde iterasyon - yineleme yapmak döngüye sokmak için kullanılır)
for x in "yapayzekadersi":
  print(x)
#kelimeyi bir liste gibi algılar ve her harfi bir eleman olarak saydırır


# In[60]:


#range fonksiyonu 0 dan başlayarak bir sayı dizisi döndürür son yazılan elemanı dahil etmez
for x in range(6):
  print(x)
#6 dahil olmadan 6 ya kadar tam sayıları yazdırır


# In[61]:


for x in range(2, 6):
  print(x)
#2 ile 6 arasındaki sayıları yazdırır başlangıç değeri dahildir ama bitiş değeeri dahil değildir


# In[63]:


for x in range(2, 30, 3):
  print(x)
#range(start,stop,artış miktarı)


# In[64]:


#faktöriyel hesaplama 
faktorial=1 
num = int(input("faktöriyel alınacak sayıyı giriniz")) 
#(başlanacak sayı, bitiş sayısı,artış miktarı) 
for  a in range (num,0,-1): #girilecek sayıdan 0 a kadar 0 dahil olmayacak şekilde azaltarak gider   
  faktorial=faktorial*a 
print("faktöriyel : ",faktorial) 


# In[ ]:




