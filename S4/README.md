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


Parameters used: 12650

Accuracy: 
