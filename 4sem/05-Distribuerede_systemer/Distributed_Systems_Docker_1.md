---
title: Distributed Systems & Docker 1
theme: gaia
_class: lead
paginate: true
marp: true
backgroundColor: #fff
size: 4K
@auto-scaling true
markdown.marp.enableHtml
---

![bg right:40% 181%](https://github.com/officegeek/image/raw/main/agenda.jpg)
# Web Distributed Systems & Docker 1  
## 23-03-2021
### Agenda

- Distributed Systems
- Coupling
- MVC
- Design Patterns
- Docker

<!-- _footer: Tue Hellstern © 2021-->

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Distributed Systems <!-- fit -->

---

# Centralized processing

- A host computer (*often a mainframe*) **handles all the processing**, including input, output, data storage and retrieval
- Predominant computing mode in the 80’s
    - Combined with very **thin clients** (*dumb terminals*)
- Still used in many websites and centralized service providers
- **Opposed to Distributed Architecture**

---

# Distributed system – *The system*

**A distributed system is a system where:**
- Hardware and software components are **linked by networked computers** and communicate by exchanging messages and coordinate their actions.

**Example** *The Internet*
- Largest connected distributed system
- Huge merger of heterogeneous computer networks
- "*Glue*" are the standardized Internet protocols
    - **IP** (*layer 3 protocol*) with IP addresses
    - **TCP/UDP** (*layer 4 protocol*)
- Users can use various services, regardless of the location
- Structuring through sub-networks (*intranets*) and backbones

---

#  Distributed system - *Application* 

**A distributed application is an application, that**
- Uses a distributed system to solve an application problem 
- Consists of different components, that communicate with each other, as well as the users.

**Examples**
- Web service, telnet, ftp
- Distributed information systems such as
    - Booking systems
    - Internet/web shops
- Automotive embedded control software
- Distributed calendars for smartphones

---

# Middleware

It is used by the distributed application as the uniform, high level access interface to the distributed system

**Objective:**
To hide the distributed aspects of the underlying system

- Typical very complex
- We distinguish between
    - Communication-oriented middleware
    - Application-oriented middleware
- It is based on the transport protocol (*e.g. TCP*) and the access interface to (*for example sockets*) used in the distributed system

---

![bg right:65% 95%](https://github.com/officegeek/image/raw/main/middleware.jpg)
# Example of Middleware

A distributed system organized via middleware

The middleware layer extends over multiple machines and offers **each application the same interface**


<!-- _footer: by M. van Steen and A. Tanenbaum, "Distributed Systems"  -->

---
![bg right:45% 95%](https://github.com/officegeek/image/raw/main/middleware_communication.png)
# Communication oriented
It is **directly based on the protocol** of the distributed system

- Services as a communication infrastructure
- Focuses on pure communication aspects

*Examples: Sun RPC, Java RMI, MQSeries*

---

![bg right:45% 95%](https://github.com/officegeek/image/raw/main/middleware_application.png)
# Application oriented
Is based on the **communication-oriented** middleware

Expanded to include
- Runtime environment
- Services
- Component model 

*Examples: CORBA, J2EE, .Net*

<!-- _footer: M. van Steen and A. Tanenbaum, "Distributed Systems"  -->
 
---

# Transparency

## Objective of middleware = Hides the distribution aspects

## Possibilities of transparency:
- **Location transparency** - *For the application it remains largely hidden where a resource someone wants to access, is physically located*
- **Access transparency** - *For the application it is hidden, whether a call is local or remote*

---

## Possibilities of transparency:
- **Concurrency transparency** - For the caller of an application it remains hidden if other calls are processed in parallel (*processes or threads*)
- **Fault transparency** - Typical errors, which can occur in distributed systems (*e.g. a communication error, a component failure*) are hidden
- **Replication transparency** - The use of replicas of individual hardware or software components remains transparent to the application
- Full transparency is **not always** useful
    - For example, a network printer, error messages

---

<!-- _backgroundColor: black -->
<!-- _color: white -->

![bg right:30%](https://github.com/officegeek/image/raw/main/white-question-mark.png)
# Transparency <!-- fit -->

- Explain why transparency is not useful for a network printer and error-messages
- Find other examples
    - Detail which specific factors makes transparency not desired/useful in the examples you identify

---

![bg right:54% 95%](https://github.com/officegeek/image/raw/main/form.jpg)
# Checking a form
The difference between letting a:

    1. Server
    2. Client

check forms as they are being filled

---

# Enterprise Information System (*EIS*)
Application-oriented middleware which is used mainly in the field of (*enterprise*) information systems.

## Typical properties of an information system:
- **Software-Intensive** - Can from thousands to millions of lines of code exis
- **Data-Centric** - Core task of an information system is the management and delivery of data
- **Concurrently** - Many users work in parallel with the application
- **Interactive** - Information systems provide an interactive user interface

---

# Inter-Process Communication (IPC)
**Components** of a distributed application run on **different nodes in different processes/threads**.

Communication is based on the exchange of messages in the form of bit strings.


## IPC is a mechanism for message exchange between processes:
- **Process** = Object of the operating system
- **Thread** = lightweight process provides applications with secure access to the resources of the computer. 
- Processes are isolated from each other.
- Thus, two processes can exchange information, they must use interprocess communication.

---

- There are different technical implementations:
    - Exchange of information on main memory (local only)
    - Via files
    - Via pipes (local only)
    - Via sockets (local and remote)

- Communication models define the protocol of the IPC.
- Middleware can be basically divided according to its communication model:
    - Synchronous communication 
    - Asynchronous communication

<!-- _footer: Inter-Process Communication (IPC) -->

---

# Why using Distribution?
Generally speaking, central, non-distributed applications are:
- Generally **safer**
- Generally **more performant**

---

## The main reason for distribution:
### Sharing of resources/scalability

- Sharing of hardware resources
    - Printers, plotters, scanners
    - Cost savings
- Sharing of data and information
-   File server, database, World Wide Web, search engine
    - Information exchange
- Sharing functionality
    - Centralization of functionality
    - Error Prevention
    - Reuse

<!-- _footer: Why using Distribution? -->

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

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Asynchronous <!-- fit -->
# Synchronous <!-- fit -->
# Communication <!-- fit -->

---

![bg right:24% 95%](https://github.com/officegeek/image/raw/main/Asynchronous_communication.png)
# Asynchronous communication
Sender is **not blocked**, the process may, **after sending** the message, **continue** immediately

**Answers are optional**
- The sender receives on occasion the result asynchronously
- The sender gets active on occasion
- Implementation uses in general queues

**Features**
- It is more complicated to implement, but more efficient
- **Loose coupling** of processes
- Lower error dependency
- Receiver does not need to be available to receive

---

![bg right:24% 95%](https://github.com/officegeek/image/raw/main/Synchronous_communication.png)
# Synchronous communication
Transmitter and **receiver block** when executing the **Send** or **Receive** operation

**Features**
- Tight coupling between the transmitter and receiver with all its advantages and disadvantages
- High dependence especially in case of failure

**Prerequisite**
- Secure and fast network connections are available
- Receiving process is available

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# False assumptions <!-- fit -->

---

# False assumptions
Developers making programs **sometimes make the mistake to assume things**. 
When this happens, the program run into problems, and this can have some problematic consequences.

- The network is reliable
- The network is secure
- The network is homogeneous
- The topology does not change
- Latency is zero
- Bandwidth is infinite
- Transport cost is zero
- There is one administrator

---

<!-- _backgroundColor: black -->
<!-- _color: white -->

![bg right:30%](https://github.com/officegeek/image/raw/main/white-question-mark.png)
# Discuss <!-- fit -->
**What happens when the assumption is *not* true ?**

- Make a list of examples, to show you understand when it is <u>*not*</u> true
- Make a list of consequences, what’s the result in those situations 

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# MVC <!-- fit -->
## Model-View-Controller

---

![bg right:50% 80%](https://github.com/officegeek/image/raw/main/mvc_1.png)
# MVC
**M**odel–**V**iew–**C**ontroller is a **software design pattern** commonly used for developing user interfaces that divides the related program logic into three **interconnected** elements.

---

# Python - HTML - MVC

When building a web app, you define what are known as routes.

Routes are, essentially, URL patterns associated with different pages. So when someone enters a URL, behind the scenes, the application tries to match that URL to one of these predefined routes.

There are four major components in play: 

- Routes
- **M**odels
- **V**iews
- **C**ontrollers

<!-- _footer: Python - HTML - MVC -->

---

# Routes
Each route is associated with a controller - more specifically, a certain function within a controller, known as a **controller action**. 

So when you enter a URL, the application attempts to find a **matching route**, and, if it’s *successful*, it calls that **route’s associated controller** action.

**Python - Flask example**

    @app.route('/')
    def main_page():
        pass

Here we establish the **/** route associated with the **main_page()** view function.

<!-- _footer: Python - HTML - MVC -->

---

# Models and Controllers
Within the controller action, **two main things** typically occur: 

- The models are used to **retrieve** all of the necessary **data** from a database
- Data is passed to a view, which renders the **requested page**

The data retrieved via the models is generally added to a data structure (*like a list or dictionary*), and that structure is what’s sent to the view.

<!-- _footer: Python - HTML - MVC -->

---

**Python - Flask example**

    @app.route('/')
    def main_page():
        """Searches the database for entries, then displays them."""
        db = get_db()
        cur = db.execute('select * from entries order by id desc')
        entries = cur.fetchall()
        return render_template('index.html', entries=entries)

Now within the view function, we **grab data from the database** and perform some basic logic.

This returns a list, which we assign to the variable entries, that is accessible within the **index.html** template.

<!-- _footer: Python - HTML - MVC -->

---

# Views
In the view, that structure of data is accessed and the information contained within is used to render the HTML content of the page the user ultimately sees in their browser.

Again, back to our Flask app, we can loop through the entries, displaying each one using the [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) syntax:

**HTML**

    {% for entry in entries %}
    <li>
        <h2>{{ entry.title }}</h2>
        <div>{{ entry.text|safe }}</div>
    </li>
    {% else %}
    <li><em>No entries yet. Add some!</em></li>
    {% endfor %}

---

# MVC Summary
**MVC request process is as follows**

- A user requests to view a page by entering a URL
- The application matches the URL to a predefined **route**
- The **controller action** associated with the route is called
- The controller action uses the **models** to retrieve all of the necessary data from a database, places the data in an array, and loads a **view**, passing along the data structure
- The **view** accesses the structure of data and uses it to render the requested page, which is then presented to the user in their browser

---

# API - FastAPI - ToDo Assignment

![bg right:60% 70%](https://github.com/officegeek/image/raw/main/todo_1.png)

- [FastApi_ToDo.pdf](https://github.com/officegeek/image/raw/main/pdf/FastApi_ToDo.pdf)
- [main.py](https://github.com/officegeek/image/raw/main/code/main.py)
- [todolist.html](https://github.com/officegeek/image/raw/main/code/todolist.html)
- [database.json](https://github.com/officegeek/image/raw/main/code/database.json)

---

# Links - MVC
- www.tutorialsteacher.com/mvc/mvc-architecture
- https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm - Only the Introduction rest is ASP.net

---

![bg right:50% 170%](https://github.com/officegeek/image/raw/main/MVC_Ruby.png)
[Understanding MVC architecture](https://youtu.be/eTdVkgF_Slo)

<!-- _footer: https://youtu.be/eTdVkgF_Slo -->

---

<!-- _backgroundColor: black -->
<!-- _color: white -->

![bg right:20% 170%](https://github.com/officegeek/image/raw/main/white-question-mark.png)
# Discuss how to understand the MVC pattern <!-- fit -->

**Explain in your own words**
- What does each part do?
- Think of the programs you have created in Python – what would you have to do to change it into MVC style?


---

<!-- _backgroundColor: black -->
<!-- _color: white -->
#  Design Patterns <!-- fit -->
## Well-known solutions to well-known problems - And that is called Design Patterns <!-- fit -->

---

![bg left:40% 297%](https://github.com/officegeek/image/raw/main/designpatterns_words.png)
# Design Patterns
In software engineering, a design pattern is a **general repeatable solution** to a commonly **occurring problem** in software design. 

A design pattern **isn't a finished design** that can be transformed directly into code. 

It is a description or **template** for how to **solve a problem** that can be used in many different situations.

<!-- _footer: https://sourcemaking.com/design_patterns -->

---

# Gang Of Four Design Patterns
**Elements of Reusable Object-Oriented Software(1994)** written by *Erich Gamma, Richard Helm, Ralph Johnson*, and *John Vlissides* is a book on software engineering highlighting the capabilities and pitfalls of object-oriented programming. 

They have listed **23 classic software design patterns** which are influential even in the current software development environment. 

The authors are often referred to as the **Gang of Four**.

---

# Benefits of the design pattern

- Design patterns can **speed up the development** process by providing tested, proven development paradigms.
- Reusing the design patterns helps to **prevent** subtle issues that can cause major **problems** and it also improves code readability
- Design pattern provides **general solutions**, documented in a format that doesn’t specifics tied to a particular problem
- In addition to that patterns allows developers to **communicate** well-known, well-understood names for software interactions, 
- Common design patterns can be **improved over time**, making them more robust than ad-hoc design
- A standard solution to a common programming problem enables large scale **reuse of software**

---

# Types of  Design Patterns

The 23 design patterns have been categorized into **3** verticals: 

1. **Creational** - Deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.
2. **Structural** - Deal with easing the design by identifying a simple way to realize relationships among entities.
3. **Behavioural** - Deal with

---

![bg right:71% 47%](https://github.com/officegeek/image/raw/main/Types_of_design_patterns.png)
# Types of Design Patterns

- Creational
- Structural
- Behavioural

---

# Uses of Design Patterns
Design patterns can **speed up the development** process by providing tested, proven development paradigms. 

Effective software design requires considering issues that may not become visible until later in the implementation. 

Reusing design patterns helps to **prevent** subtle issues that can cause major **problems** and **improves code readability** for coders and architects familiar with the patterns.

<!-- _footer: https://sourcemaking.com/design_patterns -->

---

<!-- _backgroundColor: black -->
<!-- _color: white -->

![bg right:20% 170%](https://github.com/officegeek/image/raw/main/white-question-mark.png)
#  Select one Design Pattern to understand together <!-- fit -->
You can use - https://sourcemaking.com/design_patterns - as a starting point.

# Understand and debate in the group <!-- fit -->

*This is not an easy assignment. - Don’t panic if you can not understand all details. Try to grab the main idea and then use your common sense.*

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Docker <!-- fit -->

---

![bg](https://github.com/officegeek/image/raw/main/what_docker.jpg)

