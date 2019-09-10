# Part 4: Share your Service
In this part we provide your method with the help of DIVAServices as a web service.
As DIVEServices is based on Docker we just have to write/adapt the installation request to make our method easily accessible though the web.

For both steps (installation and execution of the method) we have already prepared scripts to make your life easier.

Now we need a new package to make web requests so we have to install the python package **requests** as follows:
```
conda install -y requests
```

## Installation of the method
In this part we will execute your method with the help of a little script.

1. Download the script **createMthod.py** from Github
2. Change the name of the method (your first or last name) such that we do not have conflicts.
   You can also edit the developer, author, affiliation and email, if you want.
3. Change the docker image to your own one and we are already good to go
4. Execute the script with your conda environment activated
   ```
   python createMethod.py URL_TO_DIVASERVICES
   ``` 
   We will provide you with the url of the local DIVAServices instance
   
If you are interested how the whole request looks like you can just check the next subsection.

### POST request

This is the post request we send to DIVAServices to install the method.
You do not need to copy that one, we have everything already prepared in the **createMethod.py** script.
```
{
  "general": {
    "name": "Gaussian Binarization",
    "description": "Binarization",
    "developer": "Lars Vögtlin",
    "affiliation": "University of Fribourg",
    "email": "lars.voegtlin@unifr.ch",
    "author": "Lars Vögtlin",
    "type": "binarization",
    "license": "Other",
    "ownsCopyright": "1"
  },
  "input": [
    {
      "file": {
        "name": "inputImage",
        "description": "RGB image",
        "options": {
          "required": true,
          "mimeTypes": {
            "allowed": [
              "image/jpeg",
              "image/png",
              "image/tiff"
            ],
            "default": "image/jpeg"
          },
          "visualization": false
        }
      }
    },
    {
      "outputFolder": {}
    },
    {
      "number": {
        "name": "sigma1",
        "description": "xc0",
        "options": {
          "required": false,
          "default": 1,
          "min": 0,
          "steps": 1
        }
      }
    },
    {
      "number": {
        "name": "sigma2",
        "description": "yc0",
        "options": {
          "required": false,
          "default": 30,
          "min": 0,
          "steps": 1
        }
      }
    },
    {
      "number": {
        "name": "threshold",
        "description": "xc1",
        "options": {
          "required": false,
          "default": 0.87,
          "min": 0,
          "steps": 0.01
        }
      }
    }
  ],
  "output": [
    {
      "file": {
        "name": "binarizedImage",
        "description": "binarized image",
        "options": {
          "mimeTypes": {
            "allowed": [
              "image/jpeg",
              "image/png",
              "image/tiff"
            ],
            "default": "image/jpeg"
          },
          "visualization": false
        }
      }
    }
  ],
  "method": {
    "imageType": "docker",
    "imageName": "ecrop/binarization",
    "testData": "https://dl.getdropbox.com/s/jpltecvxw2aziyn/icdar_test_data.zip",
    "executableType": "bash",
    "executable_path": "/input/script.sh"
  }
}
```

## Execution of the method
As we now have installed the method we can also use it.
Normally, as DIVAServices need the data, you would first have to upload the data and then execute the method with this data.
But we have created a script which does that for you.

1. Download the script **executeOnDivaServices.py** from Github
2. Execute the script 
   ```
   python executeOnDivaservices.py URL_TO_METHOD PATH_TO_INPUT_IMAGE PATH_TO_OUTPUT_FOLDER
   
   e.g.
   python executeOnDivaservices.py http://134.21.57.191:8080/binarization/gaussianbinarization/1 ../../Part_1/code/data/inputImage.jpeg ./
   ```
3. After some seconds the script will download the result and you executed for the first time something on DIVAServices

### POST request
This is the post request we send to DIVAServices to execute a method.
The address for the method would be something like ```http://134.21.57.191:8080/binarization/gaussianbinarization/1```.
In this case the inputImage must already been uploaded to DIVAServices.

You do not need to do anything with that. We created a script for you **executeOnDivaServices.py**, sucht that you dont have to care about the whole image upload and method execution. 
```
{
	"parameters": {
	},
	"data": [
		{
			"inputImage": "COLLECTION_NAME/IMAGE_NAME.jpeg"
		}
	]
}
```