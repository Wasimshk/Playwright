import numpy
numpy.set_printoptions(legacy='1.13')
A = list(map(float, input().split()))
my_array = numpy.array(A)
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))