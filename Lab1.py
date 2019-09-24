import os
import numpy as np
import matplotlib.pyplot as plt
print(os.getcwd())
print(os.listdir())
im_1=plt.imread('111.jpeg')
print(im_1.ndim) #boyut bilgisi
print(type(im_1))
print(im_1.shape) #yukseklik,genislik ve RGB
print(im_1[100,100,:]) #enerji seviye
m,n,p=im_1.shape 
#fotograf gosterimi
plt.imshow(im_1)
plt.show()
new_image=np.zeros((m,n),dtype=float)
for i in range(m):
    for j in range(n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3
        new_image[i,j]=s

#plt.imshow(new_image,cmap="gray")#siyah beyaz
#plt.show()
plt.imsave("test.png",new_image,cmap="gray")
new_image=np.zeros((n,m),dtype=float)
for i in range(m):
    for j in range(n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3
        new_image[j,i]=s
plt.imshow(new_image,cmap="gray")
plt.show()

