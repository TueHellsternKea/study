# f-string
**f-string** is the latest Python syntax to perform string formatting - Called f-strings because you need to prefix a string with the letter **f'** in order to get an f-string. 

    “F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value. In Python source code, an f-string is a literal string, prefixed with f, which contains expressions inside braces. The expressions are replaced with their values.” (www.python.org/dev/peps/pep-0498/#abstract)

The letter **f** also indicates that these strings are used for formatting.

- f-string has been available since Python 3.6. 
- It is more readable, concise, faster and error-free than traditional string formatting.

### Links
- https://docs.python.org/3/reference/lexical_analysis.html#f-strings
- https://www.python.org/dev/peps/pep-0498/

### This as Jupyter Lab file
[f-string.ipynb](./f-string.ipynb)

## Interpolation
String interpolation is the most commonly used f-string feature. 

You just need to do enclose the value or variable in curly braces **{ }** and start with **f'**


```python
name = 'Eric'
age = 24

print(f'Hello, {name}. You are {age}')
```

    Hello, Eric. You are 24
    

# Variable names
You can get get both a variable’s **value** and its **name**. 

This can be very useful, especially when debugging, and can be easily done by putting an equal sign **{=}** in curly braces after calling the variable.


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
    

# Date time formatting
f-strings also support the formatting of datetime.

Dates are formatted the same way as numbers, using format specifiers. 

- %d - day
- %m - month
- %Y - year


```python
from datetime import datetime;

date_val = datetime.now()

print(date_val)

print(f'{date_val:%d-%m-%Y}')
```

    2021-12-25 19:26:09.276564
    25-12-2021
