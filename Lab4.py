#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9


# In[3]:


image_pixels = image_size * image_size
data_path = "Downloads/Yeni Klasör/"


# In[4]:


test_data = np.loadtxt(data_path + "mnist_test.csv",delimiter=",") 


# In[5]:


train_data = np.loadtxt(data_path + "mnist_train.csv", 
                        delimiter=",")


# In[6]:


train_data.ndim, train_data.shape #785 = 28*28 +1 class ve kendisi


# In[7]:


test_data[:10]


# In[8]:


train_data[10,0]


# In[9]:


im_3=train_data[10,:] #resimde 10.satır tamamen alındı 3 dahil 


# In[10]:


im_4=im_3[1:] #label ı attık


# In[11]:


im_4.shape


# In[12]:


im_5=im_4.reshape(28,28)


# In[13]:


plt.imshow(im_5)
plt.show()


# In[14]:


im_6=plt.imshow(im_5,cmap="gray")
plt.show(im_6)


# In[15]:


#train datada kac tane 3 oldugunu bulan fonksiyonu yaz.
#60000 data var 785 lik ve bir tanesi label 28*28lik resimler.


# In[16]:


m,n=train_data.shape
m,n


# In[17]:


s=0
for i in range(m):
    if(train_data[i,0]==3): # burada 3 degeri label degeri oluyor ve label'da hangi sayı oldugunu gosteriyor datasetinde.
        s=s+1 #i satır j sutun degerleri


# In[18]:


s


# In[19]:


def kactane(k):
    m,n=train_data.shape
    s=0
    for i in range(m):
        if(train_data[i,0]==k): # burada 3 degeri label degeri oluyor ve label'da hangi sayı oldugunu gosteriyor datasetinde.
            s=s+1 #i satır j sutun degerleri
    
    return s

    


# In[20]:


print(kactane(2))


# In[21]:



for i in range(10): # herbir rakam icin kaçtane resim oldugunu yazdırdık.
    c=kactane(i)
    print(i, "  ",c)
    


# In[22]:


#sıfır digitinin sol üstteki pixelin ortalaması ve standart sapma degeri nedir ?


# In[23]:


# digit_class=train_data[i,0]
# top_left=train_data[i,1]
# bottom_right=train_data[i,784]
# print(digit_class,end=" ")
# print(top_left,end=" ")
# print(bottom_right,end=" ") #end son kareketere bosluk bırakıyor.


# In[24]:


import math
def my_pdf_1(x, mu=0.0, sigma=1.0): #x değerinin datasette bulunma olasılığı x=piksel
    x = float(x - mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma

my_pdf_1(10,1,3)


# In[25]:


m=10000
def get_my_mean_and_std(k=0,l=0):


    s=0 # kactane sıfır var onu saysın//kac digit oldugu
    # k=0 # sınfı bilgisi yani digitin 
    t=0 #intersitiy degeri pixeldeki
    # l=350 #location ı belirtiyor.classın pixel degeri
    for i in range (m):
        if(train_data[i,0]==k):
            s=s+1
            t=t+test_data[i,l+1]
    mean_1=t/s #ortalamayı veriyor
    s=0
    t=0

    for i in range(m):
        if(test_data[i,0]==k):
            s=s+1
            diff_1=test_data[i,l+1]-mean_1
            t=t+diff_1*diff_1
    var_1=t/(s-1)
    std_1=np.sqrt(var_1)
    #print(mean_1,std_1)
    return mean_1,std_1
        # train_data[i,0] #label
        # train_data[i,1] #sol üstteki deger
        # train_data[i,784]#en alt kosedeki deger   


# In[26]:


#yukarda ortalamayı bulduk, ortalama ve varyansı olan degerin pdf degeri nedir ?


# In[27]:



my_pdf_1(45.8,2.0,4.0)


# In[28]:


#my_pdf_1(test_value,m_1,std_1) #(40 intersitiy degerinin ) 2.labelın 100. pixelinde 40 degerinin bulunma olasılıgı
2#test value yerine normalde 40 degerini yazmıstık.


# In[29]:


im_1=plt.imread('dokuz.jpg')
im_1=im_1[:,:,0]
im_1.ndim

plt.imshow(im_1,cmap='gray')
plt.show()
test_value=im_1[0,0]

#resmin hangi sayı oldugunu buldurunuz.


# In[30]:


im_2=test_data[1,1:]
im_2=im_2.reshape(28,28)
plt.imshow(im_2,cmap='gray')


# In[31]:


im_2=im_2[:,:]
im_2.ndim


# In[32]:


im_8=im_2.reshape(1,784)


# In[35]:


eps=np.finfo(float).eps
liste=[]


# In[ ]:



pdf=0
buyuk=0

for i in range(10):
    pdf_t=0
    for j in range(784):#resmin boyutu
        x=im_8[0,j]#butun pixelleri yazdırdık.
        m_1,std_1=get_my_mean_and_std(i,j)#butun classlarda butun pixeller icin mü ve std degerlerini getirdi.
        pdf_deger=my_pdf_1(x,m_1,std_1+eps)
        pdf_t=pdf_t+pdf_deger
        liste.append(pdf_t)
    if(buyuk<liste[i]):
        buyuk=liste[i]
        rakam=i
print(buyuk,rakam)        


# In[ ]:


print(test_data[100,200:400])
x,y=im_1.shape
import math


# In[ ]:


#enbuyukpdf=0
enbuyukpdf1=0
sayi=0
for i in range(10):
    enbuyukpdf=1
    for j in range(x):
        for k in range(y):
            test_values=im_1[j,k]
            #print(test_values)
            m_1,std_1=get_my_mean_end_std(i,(28*j)+k)
            #print((28*j)+k)
            if (math.isnan(std_1)==False):
                if(std_1!=0.0):
                    #print("STD\n"+str(std_1))
                    pdf_deger=my_pdf_1(test_values,m_1,std_1)
                    if (math.isnan(pdf_deger)==False):
                        if (pdf_deger!=0.0):
                            #print("PDF\n"+str(pdf_deger))
                            #pdf_deger=math.log(pdf_deger)
                            enbuyukpdf+=pdf_deger
                            

    if (enbuyukpdf1<enbuyukpdf):
        enbuyukpdf1=enbuyukpdf
        sayi=i
print("Değer")
print(sayi,enbuyukpdf1)
            

