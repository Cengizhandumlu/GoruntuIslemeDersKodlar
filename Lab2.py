my_list=[9,3,5,6,2,3,6]
my_list
for i in my_list:
    print(i)
    
def my_function_1(my_list=[9,3,5,6,2,3,6]):
    #mylist=[9,3,5,6,2,3,6]
    for i in range(len(my_list)):
        print(i,my_list[i])
        my_list[i]+=1
    print(my_list)
    
my_function_1([1,2,3,4,54,5,56,6])
#my_function_1(['bir',2,3,4,54,5,56,6])burdaki 1=bir olarak yazılması hataya sebeb olur.
my_function_1()
import numpy as np
import os
os.getcwd()
my_list_1=np.array([9,3,5,6,2,3,6])
my_list_1
my_list_1+1
def my_function_2(my_array=np.array(list([9,3,5,6,2,3,6]))):
    return my_array+10 # or -10
my_function_2()
import matplotlib.pyplot as plt
im_1=plt.imread('istanbul.jpg')
plt.imshow(im_1)
im_1.ndim #resim uc boyutlu oldugu icin 3 rakamı gelecek
im_1.shape

def my_f_3(im_100,s=5):
    im_1=im_100

    m,n,p=im_1.shape
    im_2=np.zeros((m,n,3),dtype=int)
    m,n,im_2.shape
    im_2.shape
    for m in range(im_1.shape[0]): #shape oldugu icin basına range koymamız gerekiyor.
        for n in range(im_1.shape[1]):
            im_2[m,n,0]=im_1[m,n,0]-25
            im_2[m,n,1]=im_1[m,n,0]
            im_2[m,n,2]=im_1[m,n,0]

    return im_100

# im_1=im_1+100 ## butun piksellerdeki ARG degerlerini 10 arttırdı.

def my_f_4(im_500): #resmi kucultme islemi yaptık.
    m,n,p=im_500.shape#gelen resmin boyutları alındı.
    new_m=int(m/2)#float turunden kabul etmedigi icin int cevirisi yaptık
    new_n=int(n/2)    
    im_600=np.zeros((new_m,new_n),dtype=int)    
    
    for m in range(new_m): #shape oldugu icin basına range koymamız gerekiyor.
        for n in range(new_n):
            #s0=(im_500[m*2,n*2,0]+im_500[m*2,n*2,1]+im_500[m*2,n*2,2])/3 #bulundugum yerdeki butun RGB degerlerini aldık.
            s0=(im_500[m*2,n*2,0]/3 +im_500[m*2,n*2,1]/3+im_500[m*2,n*2,2]/3)
            s1=(im_500[m*2,n*2+1,0]/3+im_500[m*2,n*2+1,1]/3+im_500[m*2,n*2+1,2]/3) #bi sagındaki
            s2=(im_500[m*2+1,n*2,0]/3+im_500[m*2+1,n*2,1]/3+im_500[m*2+1,n*2,2]/3) #alttaki
            s3=(im_500[m*2+1,n*2+1,0]/3+im_500[m*2+1,n*2+1,1]/3+im_500[m*2+1,n*2+1,2]/3) #caprazdaki
            
            #s=(s0+s1+s2+s3)/8
            s=(s0+s1+s2+s3)/12
            im_600[m,n]=int(s)

    return im_600

#im_2=my_f_4(im_1)
#plt.imshow(im_2,cmap='gray')
#plt.show(im_2)

def my_f_5(im_20): #resmi kucultme islemi yaptık.
    m,n,p=im_20.shape#gelen resmin boyutları alındı.
    new_m=int(m/2)#float turunden kabul etmedigi icin int cevirisi yaptık
    new_n=int(n/2)    
    im_30=np.zeros((new_m,new_n,3),dtype=int)    
    
    for m in range(new_m): #shape oldugu icin basına range koymamız gerekiyor.
        for n in range(new_n):          
            im_30[m,n,0]=int(im_20[m*2,n*2,0])
            im_30[m,n,1]=int(im_20[m*2,n*2,1])
            im_30[m,n,2]=int(im_20[m*2,n*2,2])
            

    return im_30

im_70=my_f_5(im_1)
im_80=my_f_5(im_70)
plt.imshow(im_80) #resimin boyutu kuculdukce resimde bozulma oldu.
