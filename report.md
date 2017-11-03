1.DFT
The fourier trasnforms, cosine transform and magnitude are computed using the formulae given in the classwork slides.
a) Forward Fourier Transform
If I is an image of size N then the sin and cos images are
I1(i, j) = sin[2*pi/N * (ui + vj)] for 0<=i, j <= N-1 
I2(i, j) = cos[2*pi/N * (ui + vj)] for 0<=i, j <= N-1 

Here N = 15 since the size of the matrix is 15 X 15.

Used the below function to compute the DFT
 where sin part is the imaginary part in this.

This is calculated as below where N = 15 which is the size of the given matrix. i.e., 15 X 15

Since we have to sum up the values from 0 to N-1, I have written the loop to compute the values of real and imaginary part.

tempmatrix[u][v] = tempmatrix[u][v] + matrix[i][j] * complex(m.cos((2 * np.pi / 15 )* (u * i + v * j)), -m.sin((2 * np.pi / 15) * (u * i + v * j)))


b)Inverse Fourier Transform

Here we are summing up the real and imaginary parts i.e., the cosine and sin values instead of subtraction done for the forward fourier transform.

This is calculated as below where N = 15 which is the size of the given matrix. i.e., 15 X 15

Since we have to sum up the values from 0 to N-1, I have written the loop to compute the values of real and imaginary part.

tempmatrix[u][v] = tempmatrix[u][v] + matrix[i][j] * complex(m.cos((2 * np.pi / 15 )* (u * i + v * j)), m.sin((2 * np.pi / 15) * (u * i + v * j)))

c)Discrete cosine Transform
 This is the calculation of only the real part. The imaginary part value is 0 here since we are calculating only the cosine transform.

tempmatrix[u][v] = tempmatrix[u][v] + matrix[i][j] * m.cos((2 * np.pi /15) * (u * i + v * j))

d) Magnitude
This is the square root of the sum of squares of the real and imaginary values which is calculated using the formulae
tempmatrix[i][j] = m.sqrt(m.pow(np.real(matrix[i][j]), 2) + m.pow(np.imag(matrix[i][j]), 2))

2. Frequency Filtering
I implemented filtering using six different filters. Ideal low pass (ideal_l), ideal high pass (ideal_h), butterworth low pass (butterworth_l), butterworth high pass (butterworth_h), gaussian low pass (gaussian_l) and gaussian high pass filter (gaussian_h). Input to all the filters are image, mask, cutoff frequency. For butterworth, we are using order as well.
Each filter is implemented using the corresponding formulae.
I have taken order = 0 for gaussian, ideal filters since we do not need that parameter for these filters.

post_process_image
Post_process_image function is used to perform full contrast stretch using the formula J(i, j) = (K – 1/ B - A)[I(i, j) – A]

Filtering
* Computed the fft of the image using fft, fft2 inbuilt functions
* Shifted the fft image using fftshift
* Computed the mask
Filtered the image based on mask
Computed the inverse shift and inverse fourier transform
Computed the magnitude
 

