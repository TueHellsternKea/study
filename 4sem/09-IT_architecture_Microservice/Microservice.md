# Microservice
A microservice architecture – A variant of the service-oriented architecture (**SOA**) – arranges an application as a collection of loosely-coupled services.

In a microservice architecture, services are **fine-grained and the protocols are lightweight**.

### Monolit - Microservice
![](./image/mono_micro.png)

The goal is that teams can bring their services to life independent of others. **Loose coupling reduces all types of dependencies** and the complexities around it, as service developers do not need to care about the users of the service, they do not force their changes onto users of the service.

The microservice architecture brings the idea of **decoupling functional parts of software applications into lightweight, deployable solutions, each having its own goal in the general ecosystem**.

---

![](https://microservices.io/i/Microservice_Architecture.png)

----

Microservices build in Python is considered to have an edge over other languages. Microservices in Python use a RESTful API approach. With this technology, it becomes easier to monitor the application since it is now broken into components.

There is a broad range of Python Microservices frameworks to choose from for your web application development. One of the most popular is Flask.

### Multiple components
- Each service is a standalone component of its own
- Components deployment, replacing and removal is possible without compromising other services
- You have a relatively explicit component interface without tight data coupling

### Business-oriented
- The services are built around business context and needs
- Each microservice is a product of its own
- Microservices necessitate having cross-functional teams that manage their respective products

### Smart connection
- The services are usually connected by simple, ‘smart’ HTTP requests,
- The information flows through ‘dumb’ pipelines.

### Decentralize everything
- Each service has its own resources and data storages
- Naming decisions can be different across the system
- You need to implement Data Transfer Objects (DTOs) for communication.

### Let it fail
- Microservices must acknowledge that other services may fail
- Service failure is common due to availability issues triggered by, for example, connection problems, server downtime, and the like.

# UML Diagrams
Microservices are just components (*distributed components, not the architecture style per se*) that have a clear provided interface.

As such, they should be represented in UML using the Components Diagram, with:

- **Deployment diagram**, to highlight its infrastructure and nodes used
- **Sequence or activity diagram** to highlight its aspects in relation to other Microservices or needed dependencies
- **Package diagram** to give a broader/clear overview of the Microservice organization and dependencies of other Microservices in the architecture solution.

## When to Use Microservices?
Ultimately, any size company can benefit from the use of a microservices architecture if they have applications that need frequent updates, experience dynamic traffic patterns, or require near real-time communication.

## Who Uses Microservices?
Social media companies like Facebook and Twitter, retailers like Amazon, media provider like Netflix, ride-sharing services like Uber and Lyft, and many of the world’s largest financial services companies all use microservices.

## Flask demo
You can build a Microservice architecture with Flask.

```python
# Import
from flask import Flask
import platform

# Flask App
app = Flask(__name__)

# Start point - Hello KEA
@app.route('/')
def hello():
    return 'Hello KEA!'

# Check the operation system of your computer
@app.route('/oscheck')
def oscheck():
    my_os = platform.system()
    return 'Your operation system is: ' + my_os

# NoSQL Data
@app.route('/nosqldata')
def nosqldata():
    return 'Test NoSQL'

# NoSQL Data
@app.route('/mysqldata')
def mtsqldata():
    return 'Test MySQL'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

## Resources
- Martin Fowler's [microservices article](http://martinfowler.com/articles/microservices.html)
- [microservices.io](https://microservices.io)


