# Hand-gesture-virtual-calculator
A Simple application which recognizes hand gestures and perform basic arithmetic [addition, subtraction, multiplication, division]

## Dependencies
* tensorflow
* keras
* Opencv 
* pandas (optional)

## Working
* To form the first number, user needs to show gestures which correspond to number-characters (1, 2, 3, 4, 5) one by one, each number should be seperated by "Empty" gesture so that it knows a new number has to be appended to the first number
* When first number is complete, show a gesture which correspond to operator-character (addition, subtraction, multiplication, division) and then repeat Step 1 to read the second number
* After second number is complete, show a gesture of any operator to End the gesture recognition and performs the calculation
* To reset the calculator, just show a yellow color object to the camera having a size roughly greater than 10 % of the frame size
* To stop the calculator and the application, show a RED color ojbect to the camera having a size roughly greater than 10 % of the frame size 

## Gestures: list is in the order of training
![division](https://user-images.githubusercontent.com/31381335/115984242-9d3a9500-a5c3-11eb-9183-c0992b60e3c8.jpg)
* Division


![multi](https://user-images.githubusercontent.com/31381335/115984396-93fdf800-a5c4-11eb-8ed3-e18b9bb0f54b.jpg)
* Multiplication


![addition](https://user-images.githubusercontent.com/31381335/115984415-9c563300-a5c4-11eb-974c-a989481ecef3.jpg)
* Addition


![subtraction](https://user-images.githubusercontent.com/31381335/115984517-14bcf400-a5c5-11eb-8567-bcfb3725ffc1.jpg)
* Subtraction


![0](https://user-images.githubusercontent.com/31381335/115984440-abd57c00-a5c4-11eb-80cb-4a9c4873cc38.jpg)
* 0


![1](https://user-images.githubusercontent.com/31381335/115984489-f8b95280-a5c4-11eb-8c86-e8e07cc463f0.jpg)
* 1


![2](https://user-images.githubusercontent.com/31381335/115984497-fe169d00-a5c4-11eb-8b93-668b4cde2d52.jpg)
* 2


![3](https://user-images.githubusercontent.com/31381335/115984450-c14aa600-a5c4-11eb-916a-3fa992da077a.JPG)
* 3


![4](https://user-images.githubusercontent.com/31381335/115984456-c60f5a00-a5c4-11eb-9fa3-9ce2ce6d42ab.JPG)
* 4


![5](https://user-images.githubusercontent.com/31381335/115984462-cb6ca480-a5c4-11eb-8f4c-09280742444d.JPG)
* 5


## Datasets have been collected from the following sources but not limited to them 
* https://github.com/imRishabhGupta/Indian-Sign-Language-Recognition
* https://labicvl.github.io/ges_db.htm
* https://github.com/SparshaSaha/Hand-Gesture-Recognition-Using-Background-Elllimination-and-Convolution-Neural-Network
* https://www.kaggle.com/datamunge/sign-language-mnist
