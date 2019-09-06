`docker build -t binarization .`

`docker run -it --rm -v /PATH_TO_ICDAR_CRRE_Tutorial/Part_1/data/270.jpg:/input/image.jpg -v /PATH_TO_ICDAR_CRRE_Tutorial/Part_3/:/output/:rw binarization /bin/bash`

`python binarize_manager.py --img /input/image.jpg --output_path /output/binary.jpg`