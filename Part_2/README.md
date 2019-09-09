# Part 2: Share your Environment

In this part we will create a virtual environment with the help of conda and install all required dependencies to run the binarize.py method.

### Requirements:
- Python
- [Conda](https://docs.conda.io/en/latest/miniconda.html)


## Setup the Environment

1. Open a terminal and navigate to your tutorial folder (folder where you store the binarize.py file / git root folder)
2. Create a new Conda environment called "ICDARF_Tutorial" and python version 3.7 with the following command
   ```
   conda create -n ICDAR_Tutorial python=3.7
   ``` 
3. After some time you will be able to activate the environment
   ```
   conda activate ICDAR_Tutorial
   ```
   ```which python``` should now point on the non-default python location
   
4. As the method needs the package **skimage** we have to install it
   ```
   conda install scikit-image=0.13.1
   ```
   This will install the skimage version 0.13.1 with all its dependencies

## Test the Environment 

1. Download from **Part_1** the folder **code/data** and save it into your tutorial folder
2. Make sure your environment is activated
3. Run the method
   ```
   python binarize.py /path/to/the/test/image.jpg
   ```
4. If everything worked fine you have now a file **270_binarized.jpg** in your folder

## Export Environment

Now we want to share our environment. For that we have to export it and push it into out git repo.

1. To export the environment just execute this command when the environment is activated
   ```
   conda env export > environment.yml
   ```
   This creates a environment.yml file in your folder
2. Now you can add all the files to the stash, commit them and then push them to github

## Trick

If you use one kind of environment multiple times/have a kind of a template environment you can create new environments base on it.
Just execute
```
conda create -n NAME_OF_NEW_ENVIRONMENT --clone NAME_OF_TEMPLATE
```
This creates a copy of the template environment (similar to the github template) which you then can adapt on your actual project. 