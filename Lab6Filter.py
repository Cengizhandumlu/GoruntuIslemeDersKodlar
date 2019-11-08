#!/usr/bin/env python
# coding: utf-8

# In[92]:


# morfoloji olarak adlandırılan filter.
# daha once fonksiyon x degeri alıyordu, simdi sadece x degil komsularınıda alacak.
import os
os.getcwd()
import numpy as np
import matplotlib.pyplot as plt
im_1=plt.imread('lab6.jpg')
im_1.shape
im_2=np.zeros((341,306),dtype=np.uint8)
im_2.shape
im_2=im_1[:,:,0]
im_3=im_1[:,:,0]#filter uygulayacagım resim
plt.imshow(im_2,cmap='gray')
plt.show
im_3=np.zeros((341,306),dtype=np.uint8)
m,n=im_2.shape


for i in range(1,m-1):
    for j in range(1,n-1):
        s=         im_2[i-1,j-1]/9+         im_2[i-1,j]/9+         im_2[i-1,j+1]/9+         im_2[i,j-1]/9+         im_2[i,j]/9+         im_2[i,j+1]/9+         im_2[i+1,j-1]/9+         im_2[i+1,j]/9+         im_2[i+1,j+1]/9
        
        s=int(s)
        
        #print(s  ,end='*')
        
        im_3[i,j]=s


# In[94]:


plt.subplot(1,2,1)#grafik cizdirme alanını parcalara boluyor. 1 satır 2 sutun ve 1.resim
plt.imshow(im_2,cmap='gray')
plt.subplot(1,2,2)#grafik cizdirme alanını parcalara boluyor. 1 satır 2 sutun ve 2.resim
plt.imshow(im_2,cmap='gray')


# In[ ]:




