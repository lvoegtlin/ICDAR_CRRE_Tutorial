# Part 3: Share your System

This time we will build a container for our binarization method locally and we will also create an automatic building system.
Please be sure, that you have docker installed and are registered on [DockerHub](https://hub.docker.com/)
```
docker --version
```

## Build a container locally

First we will have to write the Dockerfile, which defines the Docker image and then we have to test our container.

To not forget to delete the build numbers and the prefix from the **environment.yml** file!
```
  change
  - scikit-image=0.13.1=py36_0
  to 
  - scikit-image=0.13.1
```

### Create execution script
To make it easier to run the method inside the container with parameters we have to create a bash script that takes all the parameters and executes the method.

1. Create in your tutorial folder a file **script.sh**
2. We start with the shebang at the top of the file
   ```
   #!/bin/bash
   ```
3. Then we need to take care about the incoming parameters
   ```
   image=${1}
   output=${2:-None}
   sigma1=${3:-1}
   sigma2=${4:-30}
   threshold=${5:-0.87}
   ```
   The part after **:-** is the default value
4. The last command to execute is the call of the method
   ```
   python binarize.py --img $image --sigma1 $sigma1 --sigma2 $sigma2 --threshold $threshold --output_path $output
   ``` 
5. That we can execute the script we need to give the user execution permission for this file (terminal)
   ```
   $ chmod +x script.sh
   ```
6. Now we can test the script with the following command
   ```
   $ ./script.sh /path/to/image.jpg
   ```

### Create the Dockerfile
1. Create a file with the name **Dockerfile** in your tutorial folder (image definition)
2. First we define the base image (A ubuntu image with conda pre-installed)
   ```
   FROM continuumio/anaconda3
   ```
3. Now we need to copy our environment file into the container and build the environment
   ```
   COPY environment.yml environment.yml
   RUN /bin/bash -c "source ~/.bashrc && conda env create -f environment.yml"
   ```
4. Then we create our execution folder and copy our script and the method into the container
   ```
   RUN mkdir /input
   COPY binarize.py /input/binarize.py
   COPY script.sh /input/script.sh
   ```
5. Now we need to hook in the environment such that it gets activated when we start a container
   ```
   RUN echo "source activate ICDAR_Tutorial" > ~/.bashrc
   ENV PATH /opt/conda/envs/ICDAR_Tutorial/bin:$PATH
   ```
6. Last we have to set the working directory to our newly created **input** folder
   ```
   WORKDIR /input
   ```

### Build the image
Now we have all the elements needed to build our image.

Just execute the following command in your tutorial folder and docker will start building the image
```
$ docker build -t MY_DOCKERHUB_NAME/binarization -f Dockerfile .
```

### Test the container
Now we have an image, so we can create containers out of it.
To test if the image works as expected we test it with the test image we have from part 1.

```
docker run -it --rm -v /PATH_TO_ICDAR_CRRE_Tutorial/Part_1/code/data/270.jpg:/input/image.jpg -v /PATH_TO_ICDAR_CRRE_Tutorial/Part_3/code/:/output/:rw MY_DOCKERHUB_NAME/binarization sh /input/script.sh /input/image.jpg /output/
```

After some time you should find a **270_binary.jpg** file in your folder.

### Publish the container
As we have now a running container we can publish it on our Dockerhub page.

1. First we have to log into our Dockerhub account
  ```
  docker login
  ```
2. To see all our images we can use the ```docker images``` command
3. Now, as we know the name of our image (MY_DOCKERHUB_NAME/binarization) we can push it onto Dockerhub
   ```
   docker push MY_DOCKERHUB_NAME/binarization
   ```
   This will create a public repository with your image

## Create an automatic building system
Now we can push all our files (binarize.py, Dockerfile, script.sh, environment.yml) to Github to make then public. 
This allows other peaople to change the code and rebuild the image without the need of downloading the image and manipulate the container.
With all our code on Github we can use another feature of Dockerhub: autobuilds!
An autobuild is a build, which is done automatically based on an event, like a new push.


### Connect Github and DockerHub

1. We have to connect our Github account with our Dockerhub so log in on [Dockerhub](https://cloud.docker.com/)
2. Click on the arrow besides your name and go to **Account settings**
3. There chose the menu **Linked Account**
4. Click on **connect** right beside GitHub and follow the wizard. 
5. After finishing the wizard, the two accounts should be connected

### Link the two repositories
Now you should have under the menu point **Respositories** a repository with the name **MY_DOCKERHUB_NAME/binarization**.

1. Click on the repository
2. Go to **Builds**
3. Click on **Link to Github**
4. Select your organisation (should be your github name) and the repository name where you have the files (e.g. ICDAR_Tutorial)
5. Click on **Save and Build** and wait
6. After some time the build should be finished

From now on, every time you push something into your github repo, Dockerhub will pull the changes and build the new image.
 
For testing reasons, you can change a comment or something in your code and push it.  