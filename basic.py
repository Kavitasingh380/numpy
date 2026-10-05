# =============================================================================
# NumPy basics - practice notes
# Most examples are commented out. Uncomment one block at a time to run it.
# =============================================================================

# ----- Imports -----
import array                  # Python's built-in array module (not used below; also later shadowed by a variable named "array")
from typing import Any        # Any = "any type", used only in the type[...] examples below


from numpy import dtype       # dtype describes the data type of array elements (int32, float64, ...)

from numpy import random      # NumPy's random-number module (randint, choice, ...)
import numpy as np            # import NumPy with the usual short name "np"
# print(np.__version__)       # check which NumPy version is installed


# =============================================================================
# 1. Creating arrays and checking their properties
# =============================================================================
# x = np.array([1, 2, 3, 5,7])        # 1D array created from a list
# print(x)                            # [1 2 3 5 7]
# print(type(x))                      # <class 'numpy.ndarray'>
# y= np.array((1,2,3,4,5))            # arrays can also be created from a tuple
# print(y)                            # [1 2 3 4 5]
# print(type(y))                      # <class 'numpy.ndarray'>
# z= np.array([[1,2,3,4,5], [6,7,8,9,10]])   # 2D array: 2 rows, 5 columns
# print(z)
# print(type[Any, dtype[Any]](z))     # same result as type(z) -> numpy.ndarray (type(z) is simpler)
# print(z.shape)                      # (2, 5)  -> rows, columns
# print(z.size)                       # 10      -> total number of elements
# print(z.ndim)                       # 2       -> number of dimensions
# print(z.dtype)                      # int64   -> data type of each element
# print(z.itemsize)                   # 8       -> bytes used by one element
# print(z.nbytes)                     # 80      -> total bytes (size * itemsize)

# 3D array: 2 blocks, each with 2 rows of 5 numbers -> shape (2, 2, 5)
# d= np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[11,12,13,14,15], [16,17,18,19,20]]])
# print(d)
# print(type[Any, dtype[Any]](d))     # numpy.ndarray
# print("dimension of d is", d.ndim)  # 3
# print("size of d is", d.size)       # 20
# print("dtype of d is", d.dtype)     # int64
# print("itemsize of d is", d.itemsize)   # 8
# print("nbytes of d is", d.nbytes)   # 160
# print("shape of d is", d.shape)     # (2, 2, 5)
# (the lines below repeat the same checks as above)
# print("size of d is", d.size)
# print("ndim of d is", d.ndim)
# print("dtype of d is", d.dtype)
# print("itemsize of d is", d.itemsize)
# print("nbytes of d is", d.nbytes)


# 3D array with 3 blocks -> shape (3, 2, 5)
# array = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
# [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
# [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
# print(array)
# print(array.shape)                  # (3, 2, 5)
# print(array.size)                   # 30
# print(array.ndim)                   # 3
# print(array.flatten())              # all 30 values in a single 1D array
# print(array[1, 0, 1])               # block 1, row 0, column 1 -> 12


# =============================================================================
# 2. Indexing and slicing
# =============================================================================
# //negative indexing  (negative numbers count from the end: -1 = last element)
# array = np.array([1,2,3,4,5])
# print(array[-1])                    # 5
# print(array[-2])                    # 4
# print(array[-3])                    # 3
# print(array[-4])                    # 2
# print(array[-5])                    # 1
# print(array[-3:-1])  # [3,4]        # slice [start:stop] - stop is NOT included
# print(array[1:5:2])  # [2,4]        # slice [start:stop:step] - every 2nd element
#2d slicing  -> array[rows, columns]
# array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(array[0,2:])                  # row 0, columns 2 to end -> [3 4 5]
# print(array[0:2,2:4])               # rows 0-1, columns 2-3 -> [[3 4] [8 9]]

# print(array[:1,4:]) # [[5]]         # first row only, last column -> still 2D

# 3d slicing  -> array[block, row, column]
# array = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[11,12,13,14,15], [16,17,18,19,20]]])
# print(array[0,1,2]) # 8             # block 0, row 1, column 2
# print(array[0,1,2:4]) # [8,9]       # block 0, row 1, columns 2-3
# print(array[0,1,2:5:2]) # [8,10]    # columns 2 and 4 (step 2)
# print(array[0,1,2:4:2]) #[8]        # columns 2 only (step 2 skips 3)
# print(array[0:2,1:3,2:4])           # both blocks, row 1, columns 2-3 -> [[[8 9]] [[18 19]]]


# =============================================================================
# 3. Data types
# =============================================================================
# // data types
# array = np.array(['a','2','3','4'], dtype='S')   # 'S' = byte string -> [b'a' b'2' b'3' b'4']
# array = np.array([1,2,3,4], dtype='i4')          # 'i4' = 4-byte integer (int32)
# print(array) # [1 2 3 4]
# print(array.dtype) # int32


# =============================================================================
# 4. Reshaping and iterating
# =============================================================================
# reshaping of array  (the total number of elements must stay the same)
# array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# # print(array.reshape(2,3,-1))/     # -1 lets NumPy work out that size -> shape (2, 3, 2)


# arr = np.array([[1,2,3,4], [5,6,7,8]])
# print(arr.reshape(-1))              # reshape(-1) flattens to 1D -> [1 2 3 4 5 6 7 8]

# np.nditer loops over every element of an array, whatever its shape
# array = np.array([[[1,2,3,4], [5,6,7,8],[9,10,11,12]]])    # shape (1, 3, 4): only ONE block
# for x in np.nditer(array[1:3,:3,2]): #this will give error  # blocks 1-2 don't exist, so the slice is empty -> ValueError
#     print(x)

# Error: np.array needs ONE list, not separate values -> use np.array(["a","b","c","d"])
# array = np.array("a","b","c","d")
# print(array)


# =============================================================================
# 5. Joining arrays
# =============================================================================
# array = np.array([[1,2,3,4], [5,6,7,8]])
# array2 = np.array([[9,10,11,12], [13,14,15,16]])
# array3 = np.concatenate((array, array2),axis=2)   # Error: 2D arrays only have axis 0 (rows) and 1 (columns)
# print(array3)                                     # axis=0 -> stack rows (4x4), axis=1 -> side by side (2x8)

# array = np.array([1,2,3])
# array2 = np.array([4,5,6])
# array3 = np.vstack((array, array2))   # vstack = stack vertically (as rows)
# print(array3)                         # [[1 2 3] [4 5 6]]


# =============================================================================
# 6. Splitting arrays
# =============================================================================
# arr = np.array([[1,2,3], [4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])   # shape (6, 3)
# print(arr)
# arr2 = np.array_split(arr, 3, axis=0)   # split rows into 3 parts -> 3 arrays of 2 rows each
# print(arr2)
# print("--------------------------------")

# arr3 = np.array_split(arr, 3, axis=1)   # split columns into 3 parts -> 3 arrays of 1 column each
# print(arr3)

# arr4 = np.array_split(arr, 3, axis=2)   # Error: arr is 2D, there is no axis 2
# print(arr4)

# arr5 = np.array_split(arr, 3, axis=3)   # Error: arr is 2D, there is no axis 3
# print(arr5)


# =============================================================================
# 7. Searching and sorting
# =============================================================================
# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# arr2 = np.where(arr % 2 == 0)       # np.where returns the INDEXES where the condition is True
# print(arr2) # (array([1, 3, 5, 7, 9], dtype=int64),)   # indexes of the even numbers 2,4,6,8,10

# searchsorted finds where a value should be inserted to keep the array sorted
# arr = np.array([11,22,3,41,5,62,17,8,9,10])
# arr2 = np.searchsorted(arr, 5)
# print(arr2) # 4                     # actually prints 3 - and the answer is only meaningful on a SORTED array

# arr = np.array([[23,2,21,34,5], [16,72,8,9,10]])
# arr2 ==                             # incomplete line - would be a SyntaxError if uncommented
# arr1= np.sort(arr,axis=None)        # axis=None flattens, then sorts -> [ 2  5  8  9 10 16 21 23 34 72]
# print(arr1)
# print(np.sort(arr.flatten()).reshape(2,-1))   # same sorted values, reshaped back to 2 rows

# Build a True/False list by hand: True for even numbers
# arr2 = []
# for i in arr1:
#     if i % 2 == 0:
#         arr2.append(True)
#     else :
#         arr2.append(False)
# print(arr2)
# print("--------------------------------")
# print(np.where(arr2))               # indexes where the list is True
# print("--------------------------------")
# print(arr1[arr2])                   # boolean indexing: keep only the True positions -> the even numbers
# print("--------------------------------")

# print(arr1[arr1 % 2 == 0])          # the same filter in one line (NumPy way, no loop needed)


# =============================================================================
# 8. Random numbers
# =============================================================================
# arr = random.randint(1,100,10)      # 10 random integers from 1 to 99
# print(arr)
# print(np.sort(arr))                 # ascending order
# print(np.sort(arr)[::-1])           # [::-1] reverses -> descending order
# print(np.sort(arr)[::-1][:5])       # 5 largest values
# print(np.sort(arr)[::-1][:5][::-1]) # 5 largest, back in ascending order
# each extra [::-1] below just flips the order again
# print(np.sort(arr)[::-1][:5][::-1][::-1])
# print(np.sort(arr)[::-1][:5][::-1][::-1][::-1])
# print(np.sort(arr)[::-1][:5][::-1][::-1][::-1][::-1])
# print(np.sort(arr)[::-1][:5][::-1][::-1][::-1][::-1][::-1])

# random.choice picks values from the list using probabilities p (they must add up to 1)
# here 7 is picked most often (50%), 6 next (30%), 3 and 9 rarely (10% each)
# arr = random.choice([3,6,7,9],p=[0.1,0.3,0.5,0.1],size=(10,5))   # result is a 10x5 array
# print(arr)

