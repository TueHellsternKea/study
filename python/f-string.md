# f-string
f-string is the latest Python syntax to perform string formatting - They are called f-strings because you need to prefix a string with the letter **f** in order to get an f-string. 

*“F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value. In Python source code, an f-string is a literal string, prefixed with f, which contains expressions inside braces. The expressions are replaced with their values.”* [Source](https://www.python.org/dev/peps/pep-0498/#abstract)

The letter **f** also indicates that these strings are used for formatting.

- f-string has been available since Python 3.6. 
- It is more readable, concise, faster and error-free than traditional string formatting.

### Links
- https://docs.python.org/3/reference/lexical_analysis.html#f-strings
- https://www.python.org/dev/peps/pep-0498/

## Interpolation
String interpolation is the most commonly used f-string feature. 

You just need to do enclose the value or variable in curly braces **{ }** and start with **f**


```python
name = 'Eric'
age = 24

print(f'Hello, {name}. You are {age}')
```

    Hello, Eric. You are 24
    

# Variable names
You can get get both a variable’s **value** and its **name**. 

This can be **very useful when debugging**, and can be easily done by putting an equal sign **{=}** in curly braces after calling the variable.


```python
name = 'Eric'
age = 24

print(f'Hello, {name=}. You are {age=}')
```

    Hello, name='Eric'. You are age=24
    

# Mathematical operations
It is also possible to preform math operations on f-strings.

You can put a mathematical expression inside the curly braces and add an equal sign, then you get the expression and its result.


```python
num_val = 10

print(f'{num_val * 2 = }')
```

    num_val * 2 = 20
    

# Number formatting
f-strings are a simple and practical way for formatting a string.

You just add a **:** (*colon*) followed by a format specifier.

- s - String format, this is the default type for strings
- d - Decimal Integer, outputs the number in base 10
- n - Number, the same as d except that it uses the current locale setting
- e - Exponent notation, scientific notation using the letter ‘e’, default precision is 6
- f - Fixed-point notation. Default precision is 6.
- % - Percentage, multiplies the number by 100, displays in fixed ('f') format, followed by a percent sign



```python
# Excamples
price_val = 1366.1265
discount = 0.22

# .2f
print(f'{price_val:.2f}')

# ,.2f - 
print(f'{price_val:,.2f}')

# .2n
print(f'{price_val:.1n}')

# .0%
print(f'{discount:.0%}')

```

    1366.13
    1,366.13
    1e+03
    22%
    


```python
# Format pi by changing precision
from math import pi

for i in range(1, 7):
    print(f'{pi:.{i}f}')
```

    3.1
    3.14
    3.142
    3.1416
    3.14159
    3.141593
    

# Padding numbers with zeros
You can pad any number with zeros by using f-strings. A well-known example is to append leading zeros to ID numbers. The purpose here is to have the numbers with the same length by using leading zeros.

    f'{variable:0{width}}'

**width** is used to specify the total number of digits of a number after leading zeros.


```python
# 10 step countdown
for i in range(10, -1, -1):
    print(f'{i:02}')
```

    10
    09
    08
    07
    06
    05
    04
    03
    02
    01
    00
    


```python
# Find the longest id and pad with 0 in front of the numbers
product_ids = [93, 123456789, 5332493, 32641, 15279535]

longest_product_id = len(max(map(str, product_ids), key=len))

for product_id in product_ids:
    print(f'{product_id:0{longest_product_id}}')
```

    000000093
    123456789
    005332493
    000032641
    015279535
    

# Date time formatting
f-strings also support the formatting of datetime.

Dates are formatted the same way as numbers, using format specifiers. 

- %d - day
- %m - month
- %Y - year
- %H - hours
- %M - minutes


```python
from datetime import datetime;

date_val = datetime.now()

print(date_val)

print(f'{date_val:%d-%m-%Y}')
```

    2021-12-25 19:26:09.276564
    25-12-2021
    

# Align Strings
With f-string you can control the alignment of a string.

    f'{variable:{aligment}{width}}'

A variable name is followed by **:** (colon). Then, alignment is specified by one of these symbols:

- Right alignment: **<**
- Center alignment: **^**
- Left alignment: **>**

Lastly, decide the total width of the line.


```python
align = ['left', 'center', 'right']

print(f'{align[0]:<25}')
print(f'{align[1]:^25}')
print(f'{align[2]:>25}')
```

    left                     
             center          
                        right
    

# Formatet output

### Loop and formating, tabs and calucation


```python
print(f'Number\t\tSquare\t\tCube')
for x in range(1, 11):
    x = float(x)
    print(f'{x:5.2f}\t\t{x*x:6.2f}\t\t{x*x*x:8.2f}')
```

    Number		Square		Cube
     1.00		  1.00		    1.00
     2.00		  4.00		    8.00
     3.00		  9.00		   27.00
     4.00		 16.00		   64.00
     5.00		 25.00		  125.00
     6.00		 36.00		  216.00
     7.00		 49.00		  343.00
     8.00		 64.00		  512.00
     9.00		 81.00		  729.00
    10.00		100.00		 1000.00
    

### Use of strings, decimals, and floats, as well as tabs for a *print report*.


```python
APPLES = .50
BREAD = 1.50
CHEESE = 2.25

numApples = 3
numBread = 4
numCheese = 2

prcApples = 3 * APPLES
prcBread = 4 * BREAD
prcCheese = 2 * CHEESE

strApples = 'Apples'
strBread = 'Bread'
strCheese = 'Cheese'

total = prcBread + prcBread + prcApples

print(f'{"My List"}')
print(f'{"="*40}')
print(f'{strApples}\t{numApples:10d}\t\tkr.{prcApples:>5.2f}')
print(f'{strBread}\t{numBread:10d}\t\tkr.{prcBread:>5.2f}')
print(f'{strCheese}\t{numCheese:10d}\t\tkr.{prcCheese:>5.2f}')
print(f'{"Total:"}\t\t\t\tkr.{total:>4.2f}')
```

    My List
    ========================================
    Apples	         3		kr. 1.50
    Bread	         4		kr. 6.00
    Cheese	         2		kr. 4.50
    Total:				kr.13.50
    

### Example of how to draw stairs on your console using f-strings.


```python
step = '|__'

for i in range(1, 10):
    print(f'{step:>{3*i}}')
```

    |__
       |__
          |__
             |__
                |__
                   |__
                      |__
                         |__
                            |__
    
