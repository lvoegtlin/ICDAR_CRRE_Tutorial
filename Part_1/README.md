# Part 1: Share your Code

In this part we will show you how to create a github repository, and clone it as well as commit and push your changes.
For a little bit of additional knowledge we will also create a Github template repository and use it.

## Create a github repository

1. Go to your home on Github.com 
2. In the upper-right corner click **+**, and then click **New repository**.

   ![](https://help.github.com/assets/images/help/repository/repo-create.png)
3. Use a short name for the repo e.g. ICDAR_Part_1 
4. Optionally you can add a description
5. Tick Initialize this repository with a README
6. Click **Create Repository**

### Clone your Repository

1. Open a terminal and navigate to your tutorial folder
2. Go on the the github page of your repository
3. Chlick on **Clone or Download** (chose HTTPS if you did not yet install your SSH keys)

   ![](https://raw.githubusercontent.com/lvoegtlin/ICDAR_CRRE_Tutorial/master/Part_1/figures/d_o_c.png)
4. Copy the link
5. Go back to your terminal and execute
   ```
   git clone GIT_LINK_TO_YOUR_REPO
   ```
6. Download the file **Part_1/binarize.py** from this repo and move into your tutorial folder (or copy if you already cloned this repo)
7. Check the status of your git
   ```
   git status
   ```
8. Add the file to the stage
   ```
   git add binarize.py
   ```
9. Commit the change and write a message
   ```
   git commit -m "binarization method added"
   ```
10. Push the change to the remote repository
   ```
   git push origin master
   ``` 

### Create a template repository

Follow again the steps from the part **Create a github repository** (give the repository a new like "ICDAR_tutorial_template")

1. Go to the github page of your repository
2. Click settings

   ![](https://help.github.com/assets/images/help/repository/repo-actions-settings.png)
3. Select **Template repository**

   ![](https://help.github.com/assets/images/help/repository/template-repository-checkbox.png)
4. Execute step 1-5 from **Clone your Repository**
5. Move to your tutorial folder and create a new file names .gitignore (files we dont want to upload) and fill it with the following content
   ```
   # Byte-compiled / optimized / DLL files
   __pycache__/
   *.py[cod]

   # C extensions
   *.so

   # Distribution / packaging
   .Python
   env/
   build/
   develop-eggs/
   dist/
   downloads/
   eggs/
   .eggs/
   lib/
   lib64/
   parts/
   sdist/
   var/
   *.egg-info/
   .installed.cfg
   *.egg
   ```
6. Execute step 7-10 of part **Clone your Repository**
7. You created a repository template!

### Use the template

Now we can create based on the template a new repository which then automatically contains all the files and have the same structure of the template repository.
This is very useful if you have a lot of projects with the same structure or the same programming language.

1. Go on the github page of your template
2. Click **Use this template**

   ![](https://raw.githubusercontent.com/lvoegtlin/ICDAR_CRRE_Tutorial/master/Part_1/figures/use_template.png)
3. Add name and description of the repository and create it
4. Done with part 1
