---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Coupling and Cohesion <!-- fit -->

## Connection between parts in the system
## High and Low
## Synchronous - Asynchronous

---

![bg right:30% 280%](https://github.com/officegeek/image/raw/main/programming.jpeg)
# Low Coupling
How much do your different modules **depend on each other**?

Modules should be as **independent as possible** from other modules, so that changes to module don’t heavily impact other modules.

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# iPods are a good example of High Coupling

## Once the battery dies you might as well buy a new iPod because the battery is soldered fixed and won’t come loose, thus making replacing very expensive. 

## A **Low Coupled** player would allow effortlessly changing the battery.

---

![bg right:30% 280%](https://github.com/officegeek/image/raw/main/programming.jpeg)
# We aim for *Low* Coupling
This can be obtained via encapsulation:
- Objects
- Layers
- Tasks

**=> As few dependencies as possible**
**=> As easy to manage connections as possible**
**=> As easy to maintain as possible**

---

![bg right:30% 280%](https://github.com/officegeek/image/raw/main/programming.jpeg)
# High Cohesion
Cohesion often refers to how the elements of a module belong together. Related code should be close to each other to make it highly cohesive.

Easy to maintain code usually has high cohesion. The elements within the module are directly related to the functionality that module is meant to provide.

---

![bg 80%](https://github.com/officegeek/image/raw/main/coupling_cohesion.png)

---

![bg 97%](https://github.com/officegeek/image/raw/main/python_coupling.jpg)

<!-- _footer: Python Example https://github.com/officegeek/image/raw/main/code/Tight_and_Loos_Coupling.ipynb -->

---