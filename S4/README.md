Assignment:

WRITE IT AGAIN SUCH THAT IT ACHIEVES
* 99.4% validation accuracy
* Less than 20k Parameters
* You can use anything from above you want. 
* Less than 20 Epochs
* No fully connected layer


Approach used:

* The input shape of MNIST images are 1 x 28 x 28

* Lets start with a channel no. as 16 since input image has only 28 pixels

* Layers used are Conv2d, RELU, BatchNorm, Dropout & AvgPool2d multiple times to reduce parameters and increase accuracy.


Parameters used:

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 16, 26, 26]             160
              ReLU-2           [-1, 16, 26, 26]               0
       BatchNorm2d-3           [-1, 16, 26, 26]              32
         Dropout2d-4           [-1, 16, 26, 26]               0
            Conv2d-5           [-1, 16, 24, 24]           2,320
              ReLU-6           [-1, 16, 24, 24]               0
       BatchNorm2d-7           [-1, 16, 24, 24]              32
         Dropout2d-8           [-1, 16, 24, 24]               0
            Conv2d-9           [-1, 32, 22, 22]           4,640
             ReLU-10           [-1, 32, 22, 22]               0
      BatchNorm2d-11           [-1, 32, 22, 22]              64
        Dropout2d-12           [-1, 32, 22, 22]               0
           Conv2d-13           [-1, 16, 22, 22]             528
             ReLU-14           [-1, 16, 22, 22]               0
        AvgPool2d-15           [-1, 16, 11, 11]               0
           Conv2d-16             [-1, 16, 9, 9]           2,320
             ReLU-17             [-1, 16, 9, 9]               0
      BatchNorm2d-18             [-1, 16, 9, 9]              32
        Dropout2d-19             [-1, 16, 9, 9]               0
           Conv2d-20             [-1, 16, 7, 7]           2,320
             ReLU-21             [-1, 16, 7, 7]               0
      BatchNorm2d-22             [-1, 16, 7, 7]              32
        Dropout2d-23             [-1, 16, 7, 7]               0
           Conv2d-24             [-1, 10, 7, 7]             170
        AvgPool2d-25             [-1, 10, 1, 1]               0
================================================================
Total params: 12,650
