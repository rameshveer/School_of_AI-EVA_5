#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:15:43 2020

@author: divva93.2
"""

from torch.utils.data import Dataset
import numpy as np

class TinyImageNet(Dataset):
    def __init__(self, data,labels, type_data, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform

        if type_data == "train":

          print("Train Data Image Shape:{}".format(self.data.shape))
          print("Train Label Label Shape:{}".format(self.labels.shape))

        if type_data == "test":
          print("Test Data Image Shape:{}".format(self.data.shape))
          print("Test Data Label Shape:{}".format(self.labels.shape))

        
        
    
    def __len__(self):
        len_data = self.data.shape[0]
        return len_data
    
    def __getitem__(self, index):
        image = self.data[index]
        #image_tensor = torch.FloatTensor(image)
        #img =torch.from_numpy(image).permute(2,1,0)
        #img_tensor = torch.FloatTensor(img)
        
        #print("sape of image is:{}".format(img.shape))
        
        y_label = self.labels[index]
        
        if self.transform:
            image = self.transform(image)
            
            
            
            
        
        
        return image, y_label
 