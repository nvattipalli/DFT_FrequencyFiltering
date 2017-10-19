# Digital Image Processing 
Assignment #2

Due: Thu 11/02/17 11:59 PM

1. DFT:
(8 Pts.) Write code for computing forward fourier transform, inverse fourier transform, discrete cosine transfrom and magnitude of the fourier transform. 
The input to your program is a 2D matrix of size 15X15.

  - Starter code available in directory DFT/
  - DFT/DFT.py: One is required to edit the functions "forward_transform", "inverse_transform", "discrete_cosine_tranform" and "magnitude", you are welcome to add more function.
  - For this part of the assignment, please implement your own code for all computations, do not use inbuilt functions like "fft" or "dft" from numpy, opencv or other libraries
  - Describe your method and findings in the report.md file
  - This part of the assignment can be run using dip_hw2_dft.py (there is no need to edit this file)
  - Usage: ./dip_hw1_dft
            python dip_hw1_dft.py
  - Please make sure your code runs when you run the above command from prompt/terminal
  - Any output images or files must be saved to "output/" folder (dip_hw1_dft.py automatically does this)
  
-------------
2. Frequency Filtering:
(15 Pts.) Write Code to perfrom image filtering in the frequency domain by modifying the DFT of images using different Masks. Filter images using six different filters ideal low pass, ideal high pass, butterworth low pass, butterworth high pass, gaussian low pass and gaussian high pass filter. The input to your program is an image, name of the mask, cuttoff frequency and order(only for butterworth filter).

- Starter code available in directory DFT/ 
- DFT/Filtering.py:

  - \__init__(): Will intialize the required variable for filtering (image, mask function, cutoff, order). There is no need to edit this function  
  - get_mask_freq_pass_filter(): There are six function definitions one for each of the of the filter. write your code to generate the masks for each filter here. 
  - filtering(): Write your code to perform image filtering here. The steps can be used as a guideline for filtering. All the variable have already been intialized and can be used as self.image, self.cutoff, etc. The varaible self.filter is a handle to each of the six fitler functions. You can call it using self.filter(shape, cutoff, ...)
    - The function returns three images, filtered image, magnitude of the DFT and magnitude of filtered dft 
    - To be able to display magnitude of the DFT and magnitude of filtered dft, one would have to perform a logrithmic compression and convert the value to uint8
  - post_process_image(): After fitlering and computing the inverse DFT, One would typically have to scale the image pixels to view it. You can write code to do a full contrast stretch here and in some cases you would also have to take a negative of the image. 
  
-------------
3. (2 Pts.) Describe your method and report you findings in report.md for each problem of the assignemnt.

-------------

Two images are provided for testing: Lenna.png and Lenna0.jpg  
PS. Files not to be changed: requirements.txt and .circleci directory 
If you do not like the structure, you are welcome to change the over all code, under two stipulations:

1. the first part has to run using command

  python dip_hw2_dft.py
 
  and the second part using
  
  python dip_hw2_filtering.py -i image-name -m ideal_l -c 50
  
2. Any output file or image should be written to output/ folder

The TA will only be able to see your results if these two conditions are met

1. DFT             - 8 Pts.
2. Filtering       - 15 Pts.
3. Report          - 2 Pts

    Total          - 25 Pts.

----------------------
