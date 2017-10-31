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

