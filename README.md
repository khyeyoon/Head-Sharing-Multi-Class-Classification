# Head-Sharing-Multi-Class-Classification

* The classification network implemented based on resnet 50

* Head layers share features using the same network, and subsequent layers are separated for each detailed classification

### Code

You can set the subnet structure using 'output_feature_list' argument

* model.py 

    Classification network 

* transform.py 

    Augmentation using albumentations


<img src="https://github.com/khyeyoon/Head-Share-Multi-Classification/blob/main/img/task.JPG">

<img src="https://github.com/khyeyoon/Head-Share-Multi-Classification/blob/main/img/model.JPG">

<img src="https://github.com/khyeyoon/Head-Share-Multi-Classification/blob/main/img/architecture.JPG">

