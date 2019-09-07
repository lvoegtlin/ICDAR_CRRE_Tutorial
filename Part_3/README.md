`docker build -t binarization .`

`docker run -it --rm -v /PATH_TO_ICDAR_CRRE_Tutorial/Part_1/data/270.jpg:/input/image.jpg -v /PATH_TO_ICDAR_CRRE_Tutorial/Part_3/:/output/:rw binarization /bin/bash`

`python binarize_manager.py --img /input/image.jpg --output_path /output/binary.jpg`

`docker run -it --rm -v /Users/voegtlil/Documents/11_tutorials_workshops/ICDAR_CRRE_19/Materials/ICDAR_CRRE_Tutorial/Part_1/data/270.jpg:/input/image.jpg -v /Users/voegtlil/Documents/11_tutorials_workshops/ICDAR_CRRE_19/Materials/ICDAR_CRRE_Tutorial/Part_3/:/output/:rw ecrop/binarization_icdar sh /input/script.sh /input/image.jpg /output/`