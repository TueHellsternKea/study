# Design Pattens
In Python, nothing obliges you to write classes and instantiate objects from them.

If you don’t need complex structures in your project, you can just write functions. Even better, you can write a flat script for executing some simple and quick task without structuring the code at all.

At the same time Python is a 100 percent object-oriented language. 

Everything in Python is an **object**. Functions are objects, first class objects.

Because Python is so powerful and flexible, we need some rules - **patterns** - when programming. 

Some design patterns are built into Python, so we use them even without knowing. Other patterns are not needed due of the nature of the language.

**Design patterns** are a common way of **solving well known problems**. 

Two main principles are in the bases of the design patterns defined by the Gang of Four (*GOF*):

- Program to an interface not an implementation
- Favor object composition over inheritance

# Pattens
- [Design Pattens](#design-pattens)
- [Pattens](#pattens)
- [MVC](#mvc)
- [Command Patten](#command-patten)
- [Facade Patten](#facade-patten)
- [Links](#links)

# MVC

![](https://miro.medium.com/max/1400/1*e8xGpHM6bW9DVNxDaVPi8Q.png)

# Command Patten
The command pattern is handy in situations when, for some reason, we need to start by preparing what will be executed and then to execute it when needed.

The advantage is that encapsulating actions in such a way enables Python developers to add additional functionalities related to the executed actions, such as undo/redo, or keeping a history of actions and the like.

```python
class RenameFileCommand(object):
    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)

class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

# Change name
history = History()

# Rename
history.execute(RenameFileCommand('cv.docx', 'new_cv.docx'))

# Rename with undo
history.execute(RenameFileCommand('cv1.docx', 'new_cv1.docx'))
history.undo()
```

[Code file](./code/demo_command_patten.py)

# Facade Patten
This may very well be the most famous Python design pattern.

Imagine you have a system with a considerable number of objects. Every object is offering a set of API methods. 

You can do a lot of things with this system, but how about simplifying the interface? 

Why not add an interface object exposing a well thought-out subset of all API methods? **A Facade!**

[](https://uploads.toptal.io/blog/image/126801/toptal-blog-image-1533728107288-9a9f20e7ad317bb61565c5e176327662.png)

Python Facade design pattern example

```python
class Car(object):

    def __init__(self):
        self._tyres = [Tyre('front_left'),
                             Tyre('front_right'),
                             Tyre('rear_left'),
                             Tyre('rear_right'), ]
        self._tank = Tank(70)

    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]

    def fuel_level(self):
        return self._tank.level
```

 The Car class is a Facade.

 # Links
 - [python-patterns.guide](https://python-patterns.guide/)
 - [refactoring.guru/design-patterns/python](https://refactoring.guru/design-patterns/python)
 - [www.geeksforgeeks.org/python-design-patterns](https://www.geeksforgeeks.org/python-design-patterns/)