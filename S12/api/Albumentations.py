import numpy as np
import albumentations as A
from albumentations.pytorch import ToTensor

class Albumentations:
    def __init__(self,Normalize_mean_std=None, H_F=None, Padding = None, R_Crop = None, Rotate=None, cutout=None):
      
        print("in the init of Albumentation" )

        self.transforms=[]
        
        if H_F is not None:
            self.transforms.append(A.HorizontalFlip(p=0.7))
            
        if Padding is not None:
            self.transforms.append(A.PadIfNeeded(min_height=70, min_width=70, border_mode=4, value=None, mask_value=None, 
                                                 always_apply=False, p=1.0))
        if R_Crop is not None:
            self.transforms.append(A.RandomCrop(64,64, always_apply = False, p = 1.0))
            
        if Rotate is not None:
            self.transforms.append(A.Rotate(limit=30, interpolation=1, border_mode=4, value=None, mask_value=None, always_apply=False, 
                                            p=0.5))
        if cutout is not None:
            self.transforms.append(A.Cutout(num_holes=1, max_h_size=32,max_w_size = 32,p=0.7))
            
        if Normalize_mean_std is not None:
            self.transforms.append(A.Normalize(Normalize_mean_std[0],Normalize_mean_std[1], always_apply=True))
            self.transforms.append(ToTensor())

        print("The transformations done are:{}".format(self.transforms))
        self.Transforms=A.Compose(self.transforms)
      
    def __call__(self,img):
      
        #print("__call__ is called in Albumentation")

        #img = np.fliplr(img)

        img=np.array(img)
        #img = np.fliplr(img)

        #img=self.Transforms(image=img)

        #   print("value of img without ['image']is: {}".format(img))


        img=self.Transforms(image=img)['image']
        #print("value of img is: {}".format(img))
        return img