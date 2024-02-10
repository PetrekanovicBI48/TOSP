#ucitavanje slike
img=io.imread('leana.png');
fig=px.imshow(img,zmin=0,zmax=255,color_continuous_scale='grey')

plt.imshow(img,cmap='grey',vmin=0,vmax=255)
plt.show()

io.imsave('a2.png',img)#cuvanje slike

img_flipud=np.flipud(img)#okretanje desno levo
img_fliplr=np.fliplr(img)#okretanje levo desno

#V3
#Kvantizacija
bin_num=3
bin_string='1'*bin_num+'0'*(8-bin_num)
quant_mask=int(bin_string,2)
Q=img&quant_mask
Q=np.round(Q/quant_mask*255).astype('uint8')

#rescale i resize
A=rescale(img,1/2,order=1,preserve_range=True)
B=resize(img,(256,256),order=1,preserve_range=True)

#Eukalidsko merenje rastojanja piksela
promenaporedu=(0,41,1)
promenapokoloni=(0,41,1)
x,y=np.meshgrid(promenapokoloni,promenaporedu)
DE=np.sqrt((x-20)**2+(y-20)**2)

#v4
#deo po deo linearna transformacija
lut1=np.linspace(0,50,101)
lut2=np.linspace(50,250,101)
lut3=np.linspace(250,255,56)
LUT=np.concate((lut1[:-1],lut2[:-1],lut3,)axis=0)#ovaj je bitan

#V5
#Izracunavanje histograma
B_hist,bins=skimage.exposure.histogram(B,source_range='dtype')
#Ekvalizacija histograma
dark_e=img_as_byte(exposure.equalize_hist(dark))

#V6
#konvolucija
A1=signal.covolve2d(A,w,mode='full,same,valid,nearest',boundary='symm',output='float')

#implementacija laplasijana
img_lap=ndimage.convolve(img.astype('float'),L,mode='reflect')


#V7
#frekvencijsko filtriranje DFT 2D
img=np.zeros(256,256)
img[0,0]=1
IMG=np.fft.fft2(img)#2D dft
AMP=np.abs(IMG)#amplitutski spektar
PHASE=np.angle(IMG)#fazni spektar
IMG=np.fft.fftshift(img)#dodavanje jednosmernje komponente
#inverzna DFT
A1=np.fft.ifft2(np.ifftshift(IMG))
A1=np.real(np.fft.ifft2(np.fft.fftshift(IMG))



#V8
#Dodavanje gausovog suma varijanse 100
rng=np.random.default_rng()
gsum=rng.standar_normal(size=E.shape)
e=E+gsum*np.sqrt(100)
e[z>255]=255
e[z<0]=0

#SO i biber
imgSO=img.copy()
p0=0.2
imgSO[p<p0]=255

imgBIBER=img.copy()
imgBIBER[rng.uniform(size=img.shape)<p0]=0

imgSB=img.copy()
p=rng.uniform(size=img.shape)
p0=0.05
imgSB=[p<p0/2]=0
imgSB=[(p0/2<=p)&(p/p0)]=255

#v10
#Prikazivanje RGB
fig=px.imshow(img[:,:,0r(1g,2b)],color_continuous_scale='gray')

#izdvajanje pojedinacnekomponente boje
r,g,b=np.abs(img[:,:,(0,1,2)].astype('float')-(230,70,50))<=30
m=r&g&b
img_mask=img*np.stack((m,m,m),axis=2)

#RGB->HSV
img_HSV=color.rgb2hsv(img)
img_RGB=color.hsv2rgb(img)

#V11
#Morfologija
se=skimage.morphology.diamond(5)#square,, DISK, RECTANGLE, OCTAGON
dilatacija=skimage.morphology.dilatation(F,se)

erozija=skimage.morphology.erosion(F,se)

#otvaranjeerozija pa dilatacija
img_open_erozija/dilatacija=skimage.morphology.erosion/dilatation(morphology.dilatation/erosion(A,se),se)

#zatvaranje
img_close_erozija/dilatacija=skimage.morphology.erosion/dilatation(morphology.dilatation/erosion(A,se),se)

#V12
#segmentacija
edges=feature.canny(img.low_threshold=100,high_treshold=150,sigma=2)
fig = px.imshow(edges, color_continuous_scale='gray')


















