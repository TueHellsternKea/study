---
title: It Architecture
theme: gaia
_class: lead
paginate: true
marp: true
backgroundColor: #fff
size: 4K
@auto-scaling true
footer: 'Tue Hellstern - 2021'
html: true
---

# Agenda
- It Architecture
- 4+1 Model
- ISO/IEC/IEEE 42010
- Design Steps
- Enterprise Architecture Frameworks
- Quality Attributes - Non Functions Requirements

<!-- _footer: Tue Hellstern © 2021 -->

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# It Architecture <!-- fit -->

---

> The architecture of a software-intensive system is the structure or structures of the system, which comprise software elements, the externally visible properties of those elements, and the relationships among them.

<!-- _footer: Software Engineering Institute (SEI)  Carnegie-Mellon University in Pittsburgh -->

---

> An **architectural element** (or just element) is a fundamental piece from which a system can be considered to be constructed.

> A **stakeholder** in a software architecture is a person, group, or entity with an interest in or concerns about the realization of the architecture.

> A concern about an architecture is a **requirement**, an objective, an intention, or an aspiration a stakeholder has for that architecture.

<!-- _footer: Software Engineering Institute (SEI)  Carnegie-Mellon University in Pittsburgh -->

---

# The Problem of Architectural Description 
 
- What are the main functional elements of your architecture? 
- How will these elements interact with one another and with the outside world? 
- What information will be managed, stored, and presented? 
- What physical hardware and software elements will be required to support these functional and information elements? 
- What operational features and capabilities will be provided? 
- What development, test, support, and training environments will be provided?

---

> An architectural description (AD) is a set of artifacts that documents an architecture in a way its stakeholders can understand and demonstrates that the architecture has met their concerns. 

<!-- _footer: Software Engineering Institute (SEI)  Carnegie-Mellon University in Pittsburgh -->

---

# What Architecture?
**SW Architecture**
Focus on a program, or sometimes used to refers to the SW part of a system.

**System Architecture**
Includes SW, HW and human interaction

**Enterprise Architecture**
Company wide (or Business wide) system Architecture

---

# Architecture Definition
Software architecture refers to the fundamental structures of a software system and the discipline of creating such structures and systems.

Each structure comprises software elements, relations among them, and properties of both elements and relations.

The architecture of a software system is a metaphor, analogous to the architecture of a building.

It functions as a blueprint for the system and the developing project, laying out the tasks necessary to be executed by the design teams.

---

# What is bad architecture and how to recognize it?
- **Unnecessarily Complex** — It is easy to write complex code, anyone can do it, but it is hard to write simple code.
- **Rigid/Brittle** — Since it is unnecessarily complex, it is not easy to understand and therefore making it non-maintainable, easy to break for even a small code change.
- **Untestable** — Such code will be tightly coupled, will typically not follow the single responsibility principle, will be difficult to test.
- **Unmaintainable** — Brittle code with less test coverage evolves to becomes a maintenance nightmare

---

# What is good architecture and what properties do they exhibit?
- **Simple** — Easy to understand.
- **Modularity/Layering/Clarity** — This is important so that one layer is able to change independently of the others with as minimum coupling between the layers
- **Flexible/Extendable** — Can be easily adapted to new evolving requirements
- **Testable/Maintainable** — Easy to test, add automated tests, and encourage the culture of TDD and therefore maintainable

---

![bg right:53% 90%](https://github.com/officegeek/image/raw/main/Are_you_a_software_architect.png)
# Are You a Software Architect?


https://www.infoq.com/articles/brown-are-you-a-software-architect/

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# 4+1 Model <!-- fit -->

---


![bg right:53% 90%](https://github.com/officegeek/image/raw/main/4_1_Architectural.png)
# 4+1 Model
Designed by - **Philippe Kruchten**

Describing the architecture of software-intensive systems, based on the use of 4, concurrent views.

- **Logical** (*End user*)
- **Process** (*Integrator*)
- **Development** (*Programmers*)
- **Physical** (*System engineer*)

---

  *The “4+1” view model is rather “generic”: other notations and tools can be used, other design methods can be used, especially for the logical and process decompositions, but we have indicated the ones we have used with success.*

**Philippe Kruchten,
Architectural Blueprints - The "4+1" View Model of Software Architecture**

<!-- _footer: http://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf -->

---

# Scenarios
The description of an architecture is illustrated using a small set of use cases, or scenarios, which become a fifth view. 

The scenarios describe sequences of interactions between objects and between processes. They are used to identify architectural elements and to illustrate and validate the architecture design. 

They also serve as a starting point for tests of an architecture prototype. 

This view is also known as the **Use Case** view.

---

# Logical View (*End user*)
The logical view is concerned with the functionality that the system provides to end-users.

UML diagrams are used to represent the logical view, and include **Class diagrams**, **Object diagram** and **State diagrams**.

---

# Process View (*Integrator*)
The process view deals with the dynamic aspects of the system, explains the system processes and how they communicate, and focuses on the run time behavior of the system.

The process view addresses concurrency, distribution, integrator, performance, and scalability, etc. 

UML diagrams to represent process view include the **Sequence diagram, Communication diagram, Activity diagram**.

---

# Development View (*Programmers*)
The development view illustrates a system from a programmer's perspective and is concerned with software management.

This view is also known as the implementation view. It uses the UML Component diagram to describe system components.

UML Diagrams used to represent the development view include the **Package diagram** and **Component diagram**.

---

# Physical View (*System engineer*)
The physical view depicts the system from a system engineer's point of view.

It is concerned with the topology of software components on the physical layer as well as the physical connections between these components. This view is also known as the deployment view.

UML diagrams used to represent the physical view include the **Deployment diagram**.

---

![bg right:60% 95%](https://github.com/officegeek/image/raw/main/OverviewUML.png)

- Logical - *Green*
- Process - *Blue*
- Development - *Orange*
- Physical - *Brown*

---

# Viewpoints and Perspectives
## Nick Rozanski & Eoin Woods


- https://www.viewpoints-and-perspectives.info/
- https://github.com/officegeek/image/raw/main/pdf/VPandV_WhitePaper.pdf

---

![bg 65%](https://github.com/officegeek/image/raw/main/Views_Viewpoints.jpg)

---

# Architectural Concepts and Relationships 
- A **system** is built to address the needs, concerns, goals and objectives of its **stakeholders**. 
- The **architecture** of a **system** is characterized by its static and dynamic structures, and its externally-visible behavior and properties. 
- The **architecture** of a **system** is comprised of a number of architectural **elements** and their interrelationships. 
- The **architecture** of a **system** can potentially be documented by an **architectural description** (fully, partly or not at all). In fact, there are many potential ADs for a given architecture, some good, some bad.

---

- An **architectural description** documents an architecture for its **stakeholders**, and demonstrates to them that it has met their needs.
- A **viewpoint** defines the aims, intended audience, and content of a class of **views** and defines the concerns that views of this class will address. 
- A **view** conforms to a **viewpoint** and so communicates the resolution of a number of concerns (and a resolution of a concern may be communicated in a number of views). 
- An **architectural description** comprises a number of **views**.

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# ISO/IEC/IEEE 42010 <!-- fit -->
## Conceptual Model of Architecture Description <!-- fit -->

---

# A Conceptual Model of Architecture Description
ISO/IEC/IEEE 42010 is based upon a conceptual model – or *meta model* – of the terms and concepts pertaining to Architecture Description.

The conceptual model is presented in the Standard using UML class diagrams to represent classes of entities and their relationships.

###### http://www.iso-architecture.org/ieee-1471/cm/#:~:text=A%20Conceptual%20Model%20of%20Architecture,of%20entities%20and%20their%20relationships.

---

![bg 95%](https://github.com/officegeek/image/raw/main/Conceptual-Realm.png)

<!-- _footer: Context -->


---

- **Systems** is situated in its Environment. That environment could include other Systems
- **Stakeholders** have interests in a System; those interests are called Concerns
- An **Architecture Description** is used to express an Architecture of a System
- **System** is used as a placeholder – e.g., it could refer to an enterprise, a system of systems, a product line, a service, a subsystem, or software
- Every System inhabits its **Environment**
- Systems have architectures
- An **Architecture Description** (*AD*) is an artifact that expresses an Architecture

---

![bg right:60% 99%](https://github.com/officegeek/image/raw/main/Core-Realm.png)
# Core of AD
The Standard is organized around the terms and concepts of this diagram

It depicts the contents of an AD and the relations between those content items when applying the Standard to produce an Architecture Description to express an Architecture for some System of Interest.

---

![bg right:40% 90%](https://github.com/officegeek/image/raw/main/ad.png)
# AD Elements and Correspondences
Architecture Descriptions are comprised of AD Elements. 

Correspondences capture relationships between AD Elements. 

Correspondences and Correspondence Rules are used to express and enforce architecture relations such as composition, refinement, consistency, traceability, dependency, constraint and obligation within or between ADs.

---

# Architecture Decisions and Rationale
![bg right:50% 98%](https://github.com/officegeek/image/raw/main/Rationale-Realm.png)
Architecture Decisions and Rationale
Creating an Architecture involves making Architecture Decisions.

---

![bg right:50% 98%](https://github.com/officegeek/image/raw/main/Architecture-Framework.png)
# Architecture Frameworks and Architecture Description Languages
Architecture frameworks and architecture description languages (*ADL*) are two mechanisms widely used in architecting. Instances of each can be specified by building on the concepts of Architecture Description.

---

![bg right:56% 98%](https://github.com/officegeek/image/raw/main/ADL.png)

# Architecture Framework
An architecture framework establishes a common practice for creating, interpreting, analyzing and using architecture descriptions within a particular domain of application or stakeholder community.

---

# 4210 Template

- Architecture Viewpoint (VP) - [42010-vp-template.doc](http://www.iso-architecture.org/42010/templates/42010-vp-template.doc)
- Architecture Description (AD) - [42010-ad-template.doc](http://www.iso-architecture.org/42010/templates/42010-ad-template.doc)

---

# Exercise – Inventory example
**The following happens**
- A webstore displays an item showing 1 element in stock.
- The shopper puts it in the basket
- The shopper goes to exit/checkout and pays the order.
- A message is sent to the warehouse: ”pack and send item”
- An employee picks the last item from the stock
- Parcel is sent
- Stock-count is updated
- Invoice is sent

---

![bg right:54% 98%](https://github.com/officegeek/image/raw/main/iso_42010_diagram_2.png)
# Exercise
## Inventory example
**As Architects You must**
- Identify what IT components are actively participating in the scenario above.
- Decide: **Where in the system do you decide to store the stock-count?**

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Enterprise Architecture Frameworks <!-- fit -->
## Zachman framework
## The Open Group Architecture Framework - TOGAF

---

![bg right:50% 110%](https://github.com/officegeek/image/raw/main/Linkind_learning_Enterprise.png)
# LinkedIn Learning
## Enterprise Architecture Foundations
Cource 52 min.

<!-- _footer: https://www.linkedin.com/learning-login/share?account=36836804&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fenterprise-architecture-foundations%3Ftrk%3Dshare_ent_url%26shareId%3DEufmp%252FU5Sr2ksLwSc3B%252B9g%253D%253D -->

---


> “The process of translating business strategy and vision into effective structural change by creating, communicating, and improving key requirements, principles and models that describe the future state of the organization and enable its evolution”

*Gartners definition of Enterprise Architecture*

---

![bg 75%](https://github.com/officegeek/image/raw/main/Enterprice_architecture.jpeg)

---

# Enterprise Architecture Frameworks
There are different Frameworks that offer guidelines for Enterprise Architecture:

- **Private Frameworks**
EA IBM, SAP EA, EA Oracle
- **Semi-proprietary Frameworks**
**Zachman**, EA3 Cube, SOMF, OBASHI
- **Open Frameworks**
**TOGAF** (*The Open Group Architecture Framework*)
- **Frameworks of State Organizations**
DoDAF FEAF, DODAF, MODAF, AGATE

---

# Zachman Framework <!-- fit -->

---

# Zachman Framework
The Zachman Framework is an ontology that is used to organize, categorize, and share knowledge used to build IT systems.

The Zachman Framework is named for **John Zachman**, who developed it at IBM beginning in the early 1980s.

The current version, 3.0, is represented as a **two-dimensional six by six matrix** that organizes data along two axes.

---

![bg 75%](https://github.com/officegeek/image/raw/main/ZF3.0.jpg)

---

## The columns represent questions asked of the enterprise

- **What** (*Data*) - What is the business data, information or objects?
- **How** (*Function*) - How does the business work
- **Where** (*NMetwork*) - Where are the businesses operations?
- **Who** (*People*) - Who are the people that run the business, what are the business units and their hierarchy?
- **When** (*Time*) - When are the business processes performed
- **Why** (*Motivation*) - Why is the solution the one chosen? How was that derived from? What motivates the performance of certain activities?

---
## The row represents a distinct view of the organization, from the perspective of different stakeholders

- **Planner** (*Scope Contexts*)
This view describes the business purpose and strategy, which defines the playing field for the other views. It serves as the context within which the other views will be derived and managed.
- **Owner** (*Business Concepts*)
This is a description of the organization within which the information system must function. Analyzing this view reveals which parts of the enterprise can be automated.
- **Designer** (*System Logic*)
This view outlines how the system will satisfy the organization's information needs. The representation is free from solution specific aspects or production specific constraints.

---

- **Implementer** (*Technology Physics*)
This is a representation of how the system will be implemented. It makes specific solutions and technologies apparent and addresses production constraints.
- **Sub-Constructor (*Component Assembles*)
These representations illustrate the implementation-specific details of certain system elements: parts that need further clarification before production can begin. This view is less architecturally significant than the others because it is more concerned with a part of the system than with the whole.
- **User* (*Operations Classes*)
This is a view of the functioning system in its operational environment.

---

# Rules of Zachman Framework
The framework offers a set of descriptive representations or models relevant for describing an enterprise.

Each cell in the Zachman Framework must be aligned with the cells immediately above and below it.
All the cells in each row also must be aligned with each other.
Each cell is unique.
Combining the cells in one row forms a complete description of the enterprise from that view.

---

![bg 69%](https://github.com/officegeek/image/raw/main/ZACHMAN-FRAMEWORK.jpg)

---

![bg 85%](https://github.com/officegeek/image/raw/main/Zachman_overview_2.png)

---

# What is Zachman Framework?
- https://www.visual-paradigm.com/guide/enterprise-architecture/what-is-zachman-framework/
- https://www.visual-paradigm.com/support/documents/vpuserguide/4402/4405/86418_creatingzach.html

---

# TOGAF <!-- fit -->
## The Open Group Architecture Framework

---

**The Open Group Architecture Framework**, *TOGAF* is a framework for developing enterprise architectures.

TOGAF is a **methodology** to **develop** architectures, **document** them, **build** systems based on them, and govern their development and implementation.

It was originally developed in the early 1990s based on a U.S. Department of Defense framework called TAFIM.

The current version is version 9.2 released in April 2018.

---

![bg right:20% 97%](https://github.com/officegeek/image/raw/main/Types-of-Architecture.jpg)
# TOGAF covers the development of four related types of architecture

- **Business Architecture**
Business strategy, governance, organization
- **Data Architecture**
Structure of an organization’s logical and physical data assets and data management resources.
- **Application Architecture**
The individual applications to be deployed, their interactions, relationships to the core business processes.
- **Technology Architecture**
Logical software and hardware capabilities required to support the deployment of business, data, and application services.

---

![bg 65%](https://github.com/officegeek/image/raw/main/TOGAF_structure.png)

---

# TOGAF – Six Components
- **I - Introduction**
 A high-level introduction to the key concepts of Enterprise Architecture and in particular the TOGAF approach. It contains the definitions of terms used throughout this standard.
- **II - Architecture Development Method**
The core of the TOGAF framework. It describes the TOGAF Architecture Development Method (ADM) - a step-by-step approach to developing an Enterprise Architecture.
- **III - ADM Guidelines & Techniques**
Contains a collection of guidelines and techniques available for use in applying the TOGAF approach and the TOGAF ADM. Additional guidelines and techniques are available in the TOGAF Library.

<!-- _footer: https://pubs.opengroup.org/architecture/togaf92-doc/arch -->

---

# TOGAF – Six Components
- **IV - Architecture Content Framework**
Describes the TOGAF content framework, including a structured metamodel for architectural artifacts, the use of re-usable Architecture Building Blocks (ABBs), and an overview of typical architecture deliverables.
- **V - Enterprise Continuum & Tools**
Discusses appropriate taxonomies and tools to categorize and store the outputs of architecture activity within an enterprise.
- **VI - Architecture Capability Framework**
Discusses the organization, processes, skills, roles, and responsibilities required to establish and operate an architecture function within an enterprise.


<!-- _footer: https://pubs.opengroup.org/architecture/togaf92-doc/arch -->

---

# ADM - The Central Part of TOGAF
The ADM describes how to derive an organization-specific enterprise architecture that addresses business requirements. The ADM is the major component of TOGAF and guides architects on several levels:

- The core of TOGAF
- A proven way of developing an architecture
- Specifically designed to address business requirements
- An iterative method
- A set of architecture views to ensure that a complex set of requirements are adequately addressed

---

![bg right:79% 89%](https://github.com/officegeek/image/raw/main/ADM_2.gif)
# ADM

---

# A Practical Tutorial for TOGAF

- https://www.visual-paradigm.com/guide/togaf/practical-togaf-tutorial
- https://www.visual-paradigm.com/guide/enterprise-architecture/step-by-step-enterprise-architecture-tutorial-with-togaf-adm


---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Quality Attributes - Non Functions Requirements <!-- fit -->

---

# Architecture quality
Quality is how well an architecture satisfies **Functional** and **NON-Functional** requirements

**NON-functional** (*NFR*) requirements define the criteria that are used to evaluate the whole system, but not for specific behavior, and are also called quality attributes and described in detail in architectural specifications.

NFRs can be divided into two main categories:

- Attributes that affect system behavior, design, and user interface during work.
- Attributes that affect the development and support of the system.

---

## Functional requirements
- Things that can be captured in a use-case.
- Things that can be analyzed in diagrams
- Most likely translate to code somewhere in a program

---

## NON-functional requirements
- Development constraints like:
  - Development cost, time, operational cost, performance
- Many dynamic qualities like:
  - maintainability, testability, usability, etc.
  - Is seldom to be found in a single part of a program
  - Also known as Quality attributes

---

![bg 97%](https://github.com/officegeek/image/raw/main/software_quality.png)

<!-- _footer: ISO / IEC FCD 25010 diagram -->

---

## 12 software architecture quality attributes
- **Performance** – shows the response of the system to performing certain actions for a certain period of time.
- **Interoperability** is an attribute of the system or part of the system that is responsible for its operation and the transmission of data and its exchange with other external systems.
- **Usability** is one of the most important attributes, because, unlike in cases with other attributes, users can see directly how well this attribute of the system is worked out.
- **Reliability** is an attribute of the system responsible for the ability to continue to operate under predefined conditions.

---

- **Availability** is part of reliability and is expressed as the ratio of the available system time to the total working time.
- **Security** is responsible for the ability of the system to reduce the likelihood of malicious or accidental actions as well as the possibility of theft or loss of information.
- **Maintainability** is the ability of the system to support changes.
- **Modifiability** determines how many common changes need to be made to the system to make changes to each individual item.

---

- **Testability** shows how well the system allows performing tests, according to predefined criteria.
- **Scalability** is the ability of the system to handle load increases without decreasing performance, or the possibility to rapidly increase the load.
- **Reusability** is a chance of using a component or system in other components/systems with small or no change.
- **Supportability** is the ability of the system to provide useful information for identifying and solving problems.

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Domain vs Subdomain vs Bounded Context <!-- fit -->

---

# An area of interest or an area over which a person has control

This definition of a domain is very fuzzy. What is an area of interest? It can be anything. A domain is effectively an arbitrary boundary around some subset of concepts in the universe.

<!-- _footer: Cambridge Dictionary -->

---

![bg 100%](https://github.com/officegeek/image/raw/main/DDD_Domain.jpeg)

---

![bg 100%](https://github.com/officegeek/image/raw/main/DDD_Domain_2.jpeg)

---

# Sub Domains
**In DDD, a subdomain is a relative term.**

Domain and subdomain can be used interchangeably.

When we use the word subdomain, we are emphasizing that the domain we are talking about is a child of another higher-level domain which we have identified.

Every subdomain is, therefore, a domain, and most domains are a subdomain. 

---

# Subdomain vs Bounded Context


---

![bg 50%](https://github.com/officegeek/image/raw/main/Domain_sub_BC.jpeg)

---

# Aggregates
Aggregate is a pattern in Domain-Driven Design.

A DDD aggregate is a cluster of domain objects that can be treated as a single unit.

*An example may be an order and its line-items, these will be separate objects, but it's useful to treat the order (together with its line items) as a single aggregate.*

---

# Links

- http://www.iso-architecture.org/ieee-1471/index.html
- https://dzone.com/articles/%E2%80%9C41%E2%80%9D-view-model-software
- https://philippe.kruchten.com
- https://www.uml-diagrams.org
- http://www.iso-architecture.org/ieee-1471/cm/#:~:text=A%20Conceptual%20Model%20of%20Architecture,of%20entities%20and%20their%20relationships.

---

# Links

- https://link.springer.com/chapter/10.1007/978-3-030-44999-5_32
- https://pubs.opengroup.org/architecture/togaf8-doc/arch/toc.html
- https://iso25000.com/index.php/en/iso-25000-standards/iso-25010
- https://www.opengroup.org/togaf
- https://pubs.opengroup.org/architecture/togaf9-doc/arch/
  
