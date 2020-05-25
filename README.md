# MLOps-project

Problem Statement:

1.	Create container image that’s has Python3 and Keras or numpy  installed  using dockerfile 

2.	When we launch this image, it should automatically starts train the model in the container.

3.	Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 

4.	 Job1 : Pull  the Github repo automatically when some developers push repo to Github.

5.	 Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code  and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

7.	Job3 : if metrics accuracy is less than 98%  , then tweak the machine learning model architecture and retrain it.

8.	Job4: Notify that the best model is being created

9.	Create one extra job job5 for monitor - if the model was not trained due to some reason then it will be trained again.

# Steps:

1. Upload your Machine learning code to gitHub by commiting to local git and also create a hook to automatically push it to github while commiting.

![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/13.png)

2. After this create a docker file in redhat and install your requirements in it.

![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/12.png)

3. Now start your jenkins and start creating jobs.

# Job 1 : 
This will pull the code from github as soon as it is uploaded and copy it to the directory specified.

![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/1.png)


![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/2.png)


![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/3.png)

# Job 2 : 

This job will run after job 1.

By looking at the code or program file, Jenkins will automatically start the respective dockerfile and start training.

![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/4.png)


![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/5.png)


![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/14.png)

# Job 3 :

It will check the accuracy and if it is less than 98% it will retrain the model after making some changes , you can view the changes in the correct.py file uploaded above.

![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/6.png)


![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/7.png)

Output if accuracy is correct: 

![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/15.png)

# Job 4 :

This job will send a mail to notify.

![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/9.png)

# Job 5:

This job will check for mnist_LeNet_correct.h5 file , if it is present that means the model was trained successfully anf if not then it will train it again.

![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/10.png)


![](https://github.com/SuhaniArora/MLOps-project/blob/master/images/11.png)

And your task is completed !!!!!
