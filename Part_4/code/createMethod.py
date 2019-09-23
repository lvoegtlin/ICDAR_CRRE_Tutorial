import requests
import json
import sys
import time

"""This script creates a method on DIVAServices. The script can be executed as follows:
            python createMethod.py URL_TO_DIVASERVICES (e.g. ptyhon createMethod.py http://divaservices.unifr.ch/api/v2)
"""

if (len(sys.argv) < 2):
    sys.stderr.write('The method needs 3 parameters!')
    exit()

url = sys.argv[1] + "/algorithms"

# The request body for creating the method on DIVAServices
# This contains all required information about:
#   - general information about the method
#   - the parameters the method needs
#   - the ouputs the method generates
#   - which Docker Image to use and what script to execute
# DO NOT FORGET TO CHANGE THE METHOD NAME AND THE DOCKER IMAGE NAME
payload = "{\n\t\"general\": " \
          "{\n\t\t\"name\": \"YOUR NAME Gaussian Binarization\"," \
          "\n\t\t\"description\": \"Binarization\"," \
          "\n\t\t\"developer\": \"Lars Vögtlin\"," \
          "\n\t\t\"affiliation\": \"University of Fribourg\"," \
          "\n\t\t\"email\": \"lars.voegtlin@unifr.ch\"," \
          "\n\t\t\"author\": \"Lars Vögtlin\",\n\t\t\"type\": \"binarization\",\n\t\t\"license\": \"Other\",\n\t\t\"ownsCopyright\": \"1\"\n\t},\n\t\"input\": [\n\t\t{\n\t\t\t\"file\": {\n\t\t\t\t\"name\": \"inputImage\",\n\t\t\t\t\"description\": \"RGB image\",\n\t\t\t\t\"options\": {\n\t\t\t\t\t\"required\": true,\n\t\t\t\t\t\"mimeTypes\": {\n\t\t\t\t\t\t\"allowed\": [\n\t\t\t\t\t\t\t\"image/jpeg\",\n\t\t\t\t\t\t\t\"image/png\",\n\t\t\t\t\t\t\t\"image/tiff\"\n\t\t\t\t\t\t],\n\t\t\t\t\t\t\"default\": \"image/jpeg\"\n\t\t\t\t\t},\n\t\t\t\t\t\"visualization\": false\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t{\n\t\t\t\"outputFolder\": {}\n\t\t},\n\t\t{\n\t\t\t\"number\": {\n\t\t\t\t\"name\": \"sigma1\",\n\t\t\t\t\"description\": \"xc0\",\n\t\t\t\t\"options\": {\n\t\t\t\t\t\"required\": false,\n\t\t\t\t\t\"default\": 1,\n\t\t\t\t\t\"min\": 0,\n\t\t\t\t\t\"steps\": 1\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t{\n\t\t\t\"number\": {\n\t\t\t\t\"name\": \"sigma2\",\n\t\t\t\t\"description\": \"yc0\",\n\t\t\t\t\"options\": {\n\t\t\t\t\t\"required\": false,\n\t\t\t\t\t\"default\": 30,\n\t\t\t\t\t\"min\": 0,\n\t\t\t\t\t\"steps\": 1\n\t\t\t\t}\n\t\t\t}\n\t\t},\n\t\t{\n\t\t\t\"number\": {\n\t\t\t\t\"name\": \"threshold\",\n\t\t\t\t\"description\": \"xc1\",\n\t\t\t\t\"options\": {\n\t\t\t\t\t\"required\": false,\n\t\t\t\t\t\"default\": 0.87,\n\t\t\t\t\t\"min\": 0,\n\t\t\t\t\t\"steps\": 0.01\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t],\n\t\"output\": [\n\t\t{\n\t\t\t\"file\": {\n\t\t\t\t\"name\": \"binarizedImage\",\n\t\t\t\t\"description\": \"binarized image\",\n\t\t\t\t\"options\": {\n\t\t\t\t\t\"mimeTypes\": {\n\t\t\t\t\t\t\"allowed\": [\n\t\t\t\t\t\t\t\"image/jpeg\",\n\t\t\t\t\t\t\t\"image/png\",\n\t\t\t\t\t\t\t\"image/tiff\"\n\t\t\t\t\t\t],\n\t\t\t\t\t\t\"default\": \"image/jpeg\"\n\t\t\t\t\t},\n\t\t\t\t\t\"visualization\": false\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t],\n\t\"method\": {\n\t\t\"imageType\": \"docker\"," \
          "\n\t\t\"imageName\": \"ecrop/binarization\",\n\t\t\"testData\": \"https://dl.getdropbox.com/s/jpltecvxw2aziyn/icdar_test_data.zip\",\n\t\t\"executableType\": \"bash\",\n\t\t\"executable_path\": \"/input/script.sh\"\n\t}\n}"

headers = {'content-type': "application/json"}

# start the installation process on DIVAServices
response = requests.request("POST", url, data=payload, headers=headers)
response = json.loads(response.text)

identifier = response['identifier']
status_link = sys.argv[1] + "/algorithms/" + identifier
print(response)
# check the current status of the installation
status_response = json.loads(requests.request("GET", status_link).text)
status_code = status_response['status']['statusCode']
while (status_code != 200):
    # quit the program if something went wrong
    if (status_code == 500):
        sys.stderr.write('Error in creating the method on DIVAServices')
        sys.exit()
    time.sleep(1)
    status_response = json.loads(requests.request("GET", status_link).text)
    status_code = status_response['status']['statusCode']
    print('current status: ' + str(status_code) + ' current message: ' + status_response['status']['statusMessage'])

print("Sucessfully created method on DIVAServices")
