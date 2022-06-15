kn_iris is a module for eye iris recognition, can implemented as a biometric system through iris. In future versions this helps in diagnosing dieases through iris pattern
           
## Installation needs before installing package module 
```
     python 
     numpy
     opencv-python
     matplotlib
     opencv-contrib-python
     requests
     scikit-image
     scipy
     imutils==0.5.2
```  
- Create a Models directory & in that directory create a file name irisencodings.pickle on your project folder (Models/irisencodings.pickle).
- Create a irisdataset directory & in that directory put person's eye iris images under person's name directory.
        
        
```shell

    Project/
    ├── Models/
    │   ├── irisencodings.pickle/                               # train model
    | 
    ├── irisdataset/ 
    │   ├── person1 name/                                       # person1 directory
    |   │   ├── eye iris images of person1 /                    # images of person eye iris
    │   ├── person2 name/                                       # person2 directory
    |   │   ├── eye iris images of person2 /                    # images of person eye iris
    │   ├── person3 name/                                       # person3 directory
    |   │   ├── eye iris images of person3 /                    # images of person eye iris                   
 
```
## Installation

##### - Install Python

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/), [Mac](http://docpython-guide.org/enlatest/starting/install/osx/), [Linux](https://docs.aws.amazon.com/cli/latest/userguidawscli-install-linux-python.html)


##### - Install package module using setup.py::
  ```
    $ cd kn_iris/ 
    $ python3 setup.py
  ```  
#### use package within your project
    clone repository to your project path
    using gitclone:
    
 
## Run Project

Once all the settings of project are configured, you are ready to run your project. To start import kn_iris module.

```shell
   import kn_iris
```

After import, need to train existing images and create encoding module once on start :

```shell
   kn_iris.iris_model_train(dataset_path, encoding_model_path)
   irisdataset_path        ===>  'irisdataset/'
   encoding_model_path  ===>  'Models/irisencodings.pickle'
```

Once model is trained then its ready to test with real-time images:

```shell
   iris_name = kn_iris.iris_model_test(encoding_model_path,real_time_image_path) 
   encoding_model_path   ===>  Models/irisencodings.pickle
   real_time_image_path       ===>  real-time_image_path
   iris_name                  ===>  it returns predicted person name if image matches with trained image model person image & if not then it returns name as unmatch.
```


##Requirements

  * Need clearer images from the scanner.
  * Images shouldn't capture on direct sunlight.
  * Person shouldn't use glass or lens on eye scanning.
  * All scanned images need to be on same shapes/size(eg - 320x240).
  * As per image size and quality/noise, need to change parameter of filters according.
  * 90% above eye iris need to be capture on image taken from scanner.
  * Need min 5 clearer images to train a model.
  * After all this done according, set threshold of Hamming Distance to recognize.



## Support

Still a lot need to be implemented open for your contributions
kn_iris is a module for eye iris recognition, can implemented as a biometric system through iris. In future versions this helps in diagnosing dieases through iris pattern
           
## Installation needs before installing package module 
```
     python 
     numpy
     opencv-python
     matplotlib
     opencv-contrib-python
     requests
     scikit-image
     scipy
     imutils==0.5.2
```  
- Create a Models directory & in that directory create a file name irisencodings.pickle on your project folder (Models/irisencodings.pickle).
- Create a irisdataset directory & in that directory put person's eye iris images under person's name directory.
        
        
```shell

    Project/
    ├── Models/
    │   ├── irisencodings.pickle/                               # train model
    | 
    ├── irisdataset/ 
    │   ├── person1 name/                                       # person1 directory
    |   │   ├── eye iris images of person1 /                    # images of person eye iris
    │   ├── person2 name/                                       # person2 directory
    |   │   ├── eye iris images of person2 /                    # images of person eye iris
    │   ├── person3 name/                                       # person3 directory
    |   │   ├── eye iris images of person3 /                    # images of person eye iris                   
 
```
## Installation

##### - Install Python

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/), [Mac](http://docpython-guide.org/enlatest/starting/install/osx/), [Linux](https://docs.aws.amazon.com/cli/latest/userguidawscli-install-linux-python.html)


##### - Install package module using setup.py::
  ```
    $ cd kn_iris/ 
    $ python3 setup.py
  ```  
#### use package within your project
    clone repository to your project path
    using gitclone:
    
 
## Run Project

Once all the settings of project are configured, you are ready to run your project. To start import kn_iris module.

```shell
   import kn_iris
```

After import, need to train existing images and create encoding module once on start :

```shell
   kn_iris.iris_model_train(dataset_path, encoding_model_path)
   irisdataset_path        ===>  'irisdataset/'
   encoding_model_path  ===>  'Models/irisencodings.pickle'
```

Once model is trained then its ready to test with real-time images:

```shell
   iris_name = kn_iris.iris_model_test(encoding_model_path,real_time_image_path) 
   encoding_model_path   ===>  Models/irisencodings.pickle
   real_time_image_path       ===>  real-time_image_path
   iris_name                  ===>  it returns predicted person name if image matches with trained image model person image & if not then it returns name as unmatch.
```


##Requirements

  * Need clearer images from the scanner.
  * Images shouldn't capture on direct sunlight.
  * Person shouldn't use glass or lens on eye scanning.
  * All scanned images need to be on same shapes/size(eg - 320x240).
  * As per image size and quality/noise, need to change parameter of filters according.
  * 90% above eye iris need to be capture on image taken from scanner.
  * Need min 5 clearer images to train a model.
  * After all this done according, set threshold of Hamming Distance to recognize.



## Support

***Still a lot need to be implemented open for your contributions***
