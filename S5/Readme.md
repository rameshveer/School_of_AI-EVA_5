Code 1: (C1)
https://github.com/rameshveer/School_of_AI-EVA_5/blob/master/S5/EVA5_S5_C1.ipynb


Target:

1. Get the set-up right
2. Set Transforms
3. Set Data Loader
4. Set Basic Working Code
5. Set Basic Training  & Test Loop

Results:

1. Parameters: 6.3M
2. Best Training Accuracy: 100.00
3. Best Test Accuracy: 99.28

Analysis:

1. Extremely Heavy Model for such a problem
2. Model is over-fitting, but we are changing our model in the next step



Code 2: (C2)
https://github.com/rameshveer/School_of_AI-EVA_5/blob/master/S5/EVA5_S5_C2.ipynb


Target:

1. Reduce parameters
2. Set Transforms to change angle of images to -7 to 7 degrees

Results:

1. Parameters: 12,650
2. Best Training Accuracy: 98.17
3. Best Test Accuracy: 99.14

Analysis:

1. Reduced the parameters to 12k.
2. Model is still over-fitting.



Code 3: (C3)
https://github.com/rameshveer/School_of_AI-EVA_5/blob/master/S5/EVA5_S5_C3.ipynb


Target:

1. Change model setup to reduce parameters below 10k

Results:

1. Parameters: 9,707
2. Best Training Accuracy: 98.87
3. Best Test Accuracy: 99.24

Analysis:

1. Reduced the parameters below 10k.
2. Model is still over-fitting. But better than previous model.



Code 4: (C4)
https://github.com/rameshveer/School_of_AI-EVA_5/blob/master/S5/EVA5_S5_C4.ipynb


Target:

1. Use optimizing techniques for adjusting learning rate during training

Results:

1. Parameters: 9,962
2. Best Training Accuracy: 98.87
3. Best Test Accuracy: 99.3

Analysis:

1. Parameters are less than 10k and Accuracy is close to 99.4 with 15 epochs.
