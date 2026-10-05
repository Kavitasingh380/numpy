# =============================================================================
# NumPy ufuncs (universal functions)
# =============================================================================
# A ufunc is a NumPy function that works element by element on whole arrays.
# Instead of writing a Python for-loop, you call one function and NumPy
# applies it to every item - much faster, and the code is shorter.
#   e.g. np.add([1,2,3], [4,5,6]) -> [5 7 9]
#
# Most ufuncs also accept optional arguments:
#   where = a True/False condition saying which elements to work on
#   dtype = the data type of the result (e.g. float)
#   out   = an existing array to store the result in

# create your own ufunc
# -----------------------------------------------------------------------------
# np.frompyfunc(function, inputs, outputs) turns a normal Python function
# into a ufunc, so it can be applied to whole arrays.
#   add -> the Python function to convert
#   2   -> number of input arguments it takes (x and y)
#   1   -> number of values it returns
# Output: [6 8 10 12]  (1+5, 2+6, 3+7, 4+8)
# -----------------------------------------------------------------------------
import numpy as np
# def add(x,y):
#     return x+y

# myfrompy= np.frompyfunc(add,2,1)
# print(myfrompy([1,2,3,4],[5,6,7,8]))



# checking if this function in ufunc or not
# -----------------------------------------------------------------------------
# type() tells you what kind of object something is. For a ufunc it prints
# <class 'numpy.ufunc'>. For a normal NumPy function (like np.concatenate)
# it prints something else, such as <class 'function'>.
# -----------------------------------------------------------------------------
# print(type(myfrompy))

#what if ufunc does not exist:
# -----------------------------------------------------------------------------
# Using a name NumPy doesn't have raises an error:
#   AttributeError: module 'numpy' has no attribute 'hdshgk'
# -----------------------------------------------------------------------------
# print(type(np.hdshgk))

#use an if argument to check if the function ufunc or not
# -----------------------------------------------------------------------------
# Compare the type with np.ufunc to check in code whether a function is a
# ufunc. np.add is a ufunc, so this prints "yes, this is ufunc".
# -----------------------------------------------------------------------------

# import numpy as np
# if type(np.add) == np.ufunc:
#     print("yes, this is ufunc")
# else :
#     print("This is not the ufunc")


#arthmetic operator(+,-,/,*)
# by using ufunc addition arguments like, where,dtype and out
# -----------------------------------------------------------------------------
# These ufuncs do the same thing as + - * / but on whole arrays.
# The two arrays must be the same shape; element 1 is matched with element 1,
# element 2 with element 2, and so on.
#
# add() - adds matching elements (same as arr + arr2)
# Output: [ 32  80 156 101 156 119]
# -----------------------------------------------------------------------------

# import numpy as np
# arr = np.array([12,56,89,23,67,29])
# arr2 = np.array([20,24,67,78,89,90])
# arradd = np.add(arr,arr2)
# print(arradd)

# # subtract method
# -----------------------------------------------------------------------------
# subtract() - subtracts each element of arr2 from arr (same as arr - arr2)
# Output: [ -8  32  22 -55 -22 -61]
# -----------------------------------------------------------------------------
# import numpy as np
# arr = np.array([12,56,89,23,67,29])
# arr2 = np.array([20,24,67,78,89,90])
# arrsub = np.subtract(arr,arr2)
# print(arrsub)

# # multiple method
# -----------------------------------------------------------------------------
# multiply() - multiplies matching elements (same as arr * arr2)
# Output: [ 240 1344 5963 1794 5963 2610]
# -----------------------------------------------------------------------------
# import numpy as np
# arr = np.array([12,56,89,23,67,29])
# arr2 = np.array([20,24,67,78,89,90])
# arrmul = np.multiply(arr,arr2)
# print(arrmul)

# # divide method
# -----------------------------------------------------------------------------
# divide() - divides arr by arr2 (same as arr / arr2).
# The result is always float (decimal), even when both inputs are integers.
# Output: [0.6  2.333  1.328  0.295  0.753  0.322]  (rounded here)
# -----------------------------------------------------------------------------
# import numpy as np
# arr = np.array([12,56,89,23,67,29])
# arr2 = np.array([20,24,67,78,89,90])
# arrdivide = np.divide(arr,arr2)
# print(arrdivide)


# #power method
# -----------------------------------------------------------------------------
# power() - raises each element of arr to the power of the matching element
# of arr2 (same as arr ** arr2), e.g. 12 to the power 20.
# Careful: these numbers are far too big for an integer array (int64 holds
# up to about 9.2 x 10^18), so NumPy silently "overflows" and prints
# meaningless values, including negatives. Use small powers, or floats:
#   np.power(arr, arr2, dtype=float)
# -----------------------------------------------------------------------------
# arr = np.array([12,56,89,23,67,29])
# arr2 = np.array([20,24,67,78,89,90])
# arrdivide = np.power(arr,arr2)
# print(arrdivide)

# #mod method
# -----------------------------------------------------------------------------
# mod() - the remainder after dividing arr by arr2 (same as arr % arr2).
# e.g. 56 / 24 = 2 remainder 8.  When the first number is smaller, the
# remainder is the number itself (12 / 20 = 0 remainder 12).
# Output: [12  8 22 23 67 29]
# -----------------------------------------------------------------------------
# arr = np.array([12,56,89,23,67,29])
# arr2 = np.array([20,24,67,78,89,90])
# arrdivide = np.mod(arr,arr2)
# print(arrdivide)


# #reminder method
# -----------------------------------------------------------------------------
# remainder() - exactly the same as mod(); it's just another name.
# Output: [12  8 22 23 67 29]
# -----------------------------------------------------------------------------
arr = np.array([12,56,89,23,67,29])
arr2 = np.array([20,24,67,78,89,90])
# arrdivide = np.remainder(arr,arr2)
# print(arrdivide)

#divmode method
# -----------------------------------------------------------------------------
# divmod() - gives two arrays at once:
#   1. the quotient  (how many whole times arr2 fits into arr, like arr // arr2)
#   2. the remainder (same as mod)
# Output: (array([0, 2, 1, 0, 0, 0]), array([12,  8, 22, 23, 67, 29]))
# -----------------------------------------------------------------------------

# arrmode = np.divmod(arr,arr2)
# print(arrmode)

#absolute and abs()
# -----------------------------------------------------------------------------
# absolute() - removes the minus sign, giving how far each number is from 0.
# np.abs() is a shorter name for the same function.
# Output: [1 2 3 4 5]
# -----------------------------------------------------------------------------

# arr= np.array([-1,-2,-3,-4,-5])
# arr1 = np.absolute(arr)
# print(arr1)

# -----------------------------------------------------------------------------
# Rounding decimals - the next five functions all round numbers, but in
# different ways. Compare what happens to the negative number -3.1666:
#   trunc / fix -> -3   (just drop the decimals, move toward 0)
#   floor       -> -4   (always round DOWN)
#   ceil        -> -3   (always round UP)
#   around      -> round to the nearest value, with a chosen number of decimals
# -----------------------------------------------------------------------------

#trunc() method
# -----------------------------------------------------------------------------
# trunc() - cuts off the decimal part and keeps the whole number,
# i.e. rounds toward 0.
# Output: [-3.  3.]
# -----------------------------------------------------------------------------
# arr = np.trunc([-3.1666,3.6666])
# print(arr)

#fix() method
# -----------------------------------------------------------------------------
# fix() - also rounds toward 0, so it gives the same result as trunc().
# Output: [-3.  3.]
# -----------------------------------------------------------------------------
# arr = np.fix([-3.1666,3.6666])
# print(arr)

#around method
# -----------------------------------------------------------------------------
# around(value, decimals) - normal rounding to the given number of decimal
# places. Here 3.166 rounded to 2 places -> 3.17 (because the 3rd digit, 6,
# is 5 or more, so the 2nd digit goes up).
# Output: 3.17
# -----------------------------------------------------------------------------
# arr = np.around(3.166,2)
# print(arr)

#floor() method
# -----------------------------------------------------------------------------
# floor() - rounds DOWN to the nearest whole number (toward minus infinity).
# Note -3.166 becomes -4, because -4 is lower than -3.166.
# Output: [-4.  3.]
# -----------------------------------------------------------------------------
# arr = np.floor([-3.166,3.66])
# print(arr)

#ceil() method
# -----------------------------------------------------------------------------
# ceil() ("ceiling") - rounds UP to the nearest whole number.
# Note -3.166 becomes -3, because -3 is higher than -3.166.
# Output: [-3.  4.]
# -----------------------------------------------------------------------------
# arr = np.ceil([-3.166,3.66])
# print(arr)

#sum() method
# -----------------------------------------------------------------------------
# sum() - adds up elements.
#   Without axis: adds every number together -> 1+2+3+1+2+3 = 12
#   axis=0: adds down the columns            -> [2 4 6]
#   axis=1: adds across each row             -> [6 6]
# Difference from add(): add() combines two arrays element by element and
# gives an array; sum() reduces the values down to a total.
# Output: 12
# -----------------------------------------------------------------------------
# arr = np.array([1,2,3])
# arr2 = np.array([1,2,3])
# print(np.sum([arr,arr2]))


#cumsum() method
# -----------------------------------------------------------------------------
# cumsum() ("cumulative sum") - a running total: each element is the sum of
# itself and everything before it.
#   [1, 1+2, 1+2+3] -> [1 3 6]
# -----------------------------------------------------------------------------
# arr = np.array([1,2,3])
# print(np.cumsum(arr)) #[1 3 6]


#prod() method
# -----------------------------------------------------------------------------
# prod() ("product") - multiplies elements together.
# axis=1 multiplies across each row separately:
#   5*6*7*8 = 1680   and   4*6*1*4 = 96
# Without axis it would multiply all 8 numbers together.
# Output: [1680   96]
# -----------------------------------------------------------------------------
# arr = np.array([5,6,7,8])
# arr2 = np.array([4,6,1,4])
# print(np.prod([arr,arr2],axis=1))


#cumprod() method
# -----------------------------------------------------------------------------
# cumprod() ("cumulative product") - a running product: each element is
# itself multiplied by everything before it.
#   [1, 1*2, 1*2*3, 1*2*3*4] -> [ 1  2  6 24]
# -----------------------------------------------------------------------------

# arr = np.array([1,2,3,4])
# print(np.cumprod(arr))


#diff method
# -----------------------------------------------------------------------------
# diff() ("difference") - subtracts each element from the next one:
#   [15-10, 25-15, 5-25] -> [  5  10 -20]
# The result has one element fewer than the input.
# Useful for seeing how much a value changed step by step, e.g. daily
# change in a stock price.
# Add n=2 to repeat the process twice: np.diff(arr, n=2) -> [  5 -30]
# -----------------------------------------------------------------------------
# arr= np.array([10,15,25,5])
# print(np.diff(arr))


#LCM
# -----------------------------------------------------------------------------
# lcm() ("lowest common multiple") - the smallest number that both numbers
# divide into evenly.
#   Multiples of 4: 4, 8, 12, 16 ...
#   Multiples of 6: 6, 12, 18 ...
#   The first one they share is 12.
# Output: 12
# -----------------------------------------------------------------------------
# num1 = 4
# num2 = 6
# num = np.lcm(num1,num2)
# print(num)

## finding LCM in array
# -----------------------------------------------------------------------------
# lcm.reduce() - finds the LCM of ALL the numbers in an array.
# reduce() applies lcm again and again until one value is left:
#   lcm(3, 6) = 6,  then  lcm(6, 9) = 18
# Output: 18
# -----------------------------------------------------------------------------
# arr = np.array([3,6,9])
# arrnew = np.lcm.reduce(arr)
# print(arrnew)

# -----------------------------------------------------------------------------
# np.arange(1,11) makes [1 2 3 ... 10] (the end value 11 is not included).
# So this finds the smallest number that every number from 1 to 10
# divides into evenly.
# Output: 2520
# -----------------------------------------------------------------------------
# arr = np.arange(1,11)
# arrnew =np.lcm.reduce(arr)
# print(arrnew)


#gcd
# -----------------------------------------------------------------------------
# gcd() ("greatest common divisor", also called HCF) - the biggest number
# that divides into all the numbers evenly. It is the opposite idea of lcm.
#   e.g. np.gcd(6, 9) -> 3
# gcd.reduce() works on the whole array. 23 is a prime number, so the only
# number that divides 23, 45, 12 and 4 evenly is 1.
# Output: 1
# -----------------------------------------------------------------------------
# arr = np.array([23,45,12,4])
# arrnew = np.gcd.reduce(arr)
# print(arrnew)


#trigonometric functions - sin()
# -----------------------------------------------------------------------------
# sin() - finds the sine of each value. NumPy's trig functions (sin, cos,
# tan) expect angles in RADIANS, not degrees.
#   np.pi/2 = 90 degrees -> sin = 1
#   np.pi/3 = 60 degrees -> sin = 0.866
#   np.pi/4 = 45 degrees -> sin = 0.707
#   np.pi/5 = 36 degrees -> sin = 0.588
# Output: [1.         0.8660254  0.70710678 0.58778525]
# -----------------------------------------------------------------------------
# num = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
# numnew = np.sin(num)
# print(numnew)


# degree to radians
# -----------------------------------------------------------------------------
# deg2rad() - converts angles from degrees to radians.
# Formula: radians = degrees * pi / 180   (180 degrees = pi radians)
#   90 -> pi/2,  180 -> pi,  270 -> 1.5*pi,  360 -> 2*pi
# Output: [1.57079633 3.14159265 4.71238898 6.28318531]
# -----------------------------------------------------------------------------
# arr = np.array([90,180,270,360])
# arrnew = np.deg2rad(arr)
# print(arrnew)

#radian to degree
# -----------------------------------------------------------------------------
# rad2deg() - the reverse: converts angles from radians to degrees.
# Formula: degrees = radians * 180 / pi
# Output: [ 90. 180. 270. 360.]
# -----------------------------------------------------------------------------
# arr = np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
# arrnew = np.rad2deg(arr)
# print(arrnew)


#hyperbolic functions - arctanh()
# -----------------------------------------------------------------------------
# arctanh() - the inverse hyperbolic tangent: it gives back the value x
# for which tanh(x) equals the input. So np.tanh(np.arctanh(0.5)) -> 0.5.
# Input must be between -1 and 1; at exactly 1 or -1 the result is
# infinity, and outside that range it is nan (not a number).
# Similar functions: arcsinh(), arccosh(), and sinh(), cosh(), tanh().
# Output: [0.10033535 0.20273255 0.54930614]
# -----------------------------------------------------------------------------
# arr =np.array([0.1,0.2,0.5])
# arrnew = np.arctanh(arr)
# print(arrnew)





# -----------------------------------------------------------------------------
# Set operations - a "set" is a collection where every value appears only
# once. These functions treat arrays like sets: they remove duplicates and
# always return the result sorted. The "1d" in the names means they work on
# 1-D (flat) arrays.
#   unique      -> each value once
#   union1d     -> everything in either array
#   intersect1d -> only what is in both arrays
#   setdiff1d   -> what is in the first array but not the second
#   setxor1d    -> what is in only one of the arrays, not both
# -----------------------------------------------------------------------------

# unique method
# -----------------------------------------------------------------------------
# unique() - removes repeated values and returns each value once, sorted.
# Here the extra 2 and 5 are dropped.
# Output: [1 2 3 4 5 6]
# -----------------------------------------------------------------------------
# arr = np.array([1,2,2,3,4,5,5,6])
# arrnew = np.unique(arr)
# print(arrnew)


#union1d method
# -----------------------------------------------------------------------------
# union1d() - joins two arrays and keeps each value only once, i.e. every
# value that is in arr1 OR arr2 (or both).
#   arr1 has 1 2 3 5,  arr2 adds 4 and 6
# Output: [1 2 3 4 5 6]
# -----------------------------------------------------------------------------
# arr1 = np.array([1,2,3,3,5])
# arr2 = np.array([3,2,4,5,6])
# arrnew = np.union1d(arr1,arr2)
# print(arrnew)

#intersect1d
# -----------------------------------------------------------------------------
# intersect1d() - keeps only the values found in BOTH arrays.
# assume_unique=True tells NumPy "trust me, there are no duplicates", so it
# skips removing them and runs faster. Only use it when that is true!
# Here arr1 has 3 twice, so the duplicate leaks into the result:
#   with assume_unique=True -> [2 3 3 5]   (wrong - 3 appears twice)
#   without it              -> [2 3 5]     (correct)
# -----------------------------------------------------------------------------
# arr1 = np.array([1,2,3,3,5])
# arr2 = np.array([3,2,4,5,6])
# arrnew = np.intersect1d(arr1,arr2,assume_unique =True)
# print(arrnew)

#setdiff1d method
# -----------------------------------------------------------------------------
# setdiff1d() ("set difference") - the values in arr1 that are NOT in arr2.
# Order matters: 3 and 4 are in both, so they are removed from arr1.
# Swapping the arrays, np.setdiff1d(arr2, arr1), would give [5 6].
# assume_unique=True is safe here because neither array has duplicates.
# Output: [1 2]
# -----------------------------------------------------------------------------
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# arrnew = np.setdiff1d(arr1,arr2,assume_unique = True)
# print(arrnew)

#setxor1d method
# -----------------------------------------------------------------------------
# setxor1d() ("set exclusive or") - the values that are in only ONE of the
# arrays. Anything in both (here 3 and 4) is left out.
# It is the opposite of intersect1d().
# Output: [1 2 5 6]
# -----------------------------------------------------------------------------
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
arrnew = np.setxor1d(arr1,arr2,assume_unique = True)
print(arrnew)
