---
title: Virtualization
theme: gaia
_class: lead
paginate: true
marp: true
backgroundColor: #fff
size: 4K
@auto-scaling true
footer: 'Tue Hellstern - 2022'
html: true
---

![bg right:40% 181%](https://github.com/officegeek/image/raw/main/agenda.jpg)
# Virtualization  17/18-03-2021
### Agenda

- Introduction
- It Infrastructures
- Cloud
- Azure

<!-- _footer: Tue Hellstern © 2022 -->


---

![bg right:25% 510%](https://github.com/officegeek/image/raw/main/It_Infrastructures_2.jpg)
# Evolution of IT Infrastructure

- General-purpose mainframe and minicomputer - *1959 >>*
- Personal computer - *1981 >>*
- Client/server era - *1983 >>*
- Enterprise computing - *1992 >>*
- Cloud and mobile computing - *2000 >>*)
- IoT - *1999 >>*

<!-- _footer: https://www.sutori.com/story/evolution-of-it-infrastructure--mipARdfNtNK4nRqJKTPwkNHf-->

---

![bg 30%](https://github.com/officegeek/image/raw/main/FG_05_002.jpg)

---

![bg right:40% 97%](https://github.com/officegeek/image/raw/main/FG_05_004.jpg)
# Technology drivers <!-- fit -->

- Moore’s Law and Microprocessing Power
- Law of mass digital storage
- Matcalfe's Law
- Communications cost
- Technology standards
- Serverless computing
- Security

---

![bg right:30% 350%](https://github.com/officegeek/image/raw/main/hardware.jpg)
# Trends in computer hardware <!-- fit -->

- Mobile digital platforms
- BYOD, *Bring Your Own Device*
- Quantum Computing
- **Virtualization**
- **Cloud Computing**
- Edge Computing
- Green Computing
- High-Performance and Power-Saving Processors
- VR and AR
- IoT

---

![bg right:45% 120%](https://github.com/officegeek/image/raw/main/software.png)
# Trends in software platforms  <!-- fit -->

- Open-Source Software
- Software for the Web: *Java, HTML, and HTML5*
- Web Services and Service-Oriented Architecture - *SOA*
- Outsourcing and Cloud Services
- Data Science - AI and ML
- VR and AR

---

![bg right:60% 97%](https://github.com/officegeek/image/raw/main/FG_05_008.jpg)
# Seven Major components modern IT infrastructure

---


<!-- _backgroundColor: black -->
<!-- _color: white -->
# Cloud <!-- fit -->

---

![bg right:35%](https://github.com/officegeek/image/raw/main/Cloud_computing.jpg)
# What is Cloud computing?

The cloud is sold through **services**

- Referring to some IT technology
- Sold as a product
- Provided by a Service Provider
- Bounded by a SLA (*Service Level Agreement*)
- Abstract - independent from the hardware
- Scalable - easy to expand or reduce (*amount of users, storage, etc.*)
- Accessed via a **browser** or an **API**

---

![bg left:35%](https://github.com/officegeek/image/raw/main/Cloud_computing.jpg)
# Advantages

## Low Cost

- Cheap - *on demand, pay-per-use formula*
- No need of expertise in security, clusters, networks, etc.
- Accessibility
- Multiplatform
- No worries about updates, upgrades, new licenses
- Easy to use / integrate

---

![bg right:35%](https://github.com/officegeek/image/raw/main/Cloud_computing.jpg)
# Disadvantages

## Lack of control

- **Once you go cloud, you cannot come back** – *at least it is very difficult*
- Cannot easily switch cloud technologies
- Legal issues: data policy, storing private data…

## Who has ownership of the data? <!-- fit -->

---

![bg 60%](https://github.com/officegeek/image/raw/main/FG_05_009.jpg)

---

<!-- _backgroundColor: black -->
<!-- _color: white -->
![bg right:10% 125%](https://github.com/officegeek/image/raw/main/OracleLogo.png)

## Assignment - Oracle’s Top 10 Cloud Predictions
Oracle have released their Top 10 : Oracle Cloud Computing prediction 2020.
Read it, and discuss, in groups - **The impact you think it will have on**: 

**Business**
- The way we do business
- Business models
- Core competencies

**People**
- Needed skills
- Kinds of jobs 
- Types of employment
- Lifelong education

[Oracle’s Top 10 Cloud Predictions](https://www.oracle.com/a/ocom/docs/cloud/oracle-cloud-predictions-2020.pdf)

---

![bg right:10% 125%](https://github.com/officegeek/image/raw/main/OracleLogo.png)
# Oracle’s Top 10 Cloud Predictions
## Module 4.2

- Prediction 1 & 5 - *Automated tasks*
- Prediction 2 & 9 - **Security - Cybersecurity**
- Prediction 3 & 4 & 5 & 7 & 8 - **Data science - AI - ML**
- Prediction 6 & 10 - **NoSQL**

<!-- _footer:  https://www.oracle.com/a/ocom/docs/cloud/oracle-cloud-predictions-2020.pdf-->

---


![bg left:40% 220%](https://github.com/officegeek/image/raw/main/aws_cloud.png)
# AWS
**Amazon Web Services - what-is-cloud-computing**

**YoyTube video**
https://www.youtube.com/embed/dH0yz-Osy54

https://aws.amazon.com/what-is-cloud-computing/

---

header: Cloud types
![bg left:100% 95%](https://github.com/officegeek/image/raw/main/Cloud_Types.png)

---

![bg 80%](https://github.com/officegeek/image/raw/main/NIST-visual-model-of-cloud-computing-definition-3.png)

<!-- _footer: NIST Definition of Cloud Computing - https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf -->

---

![bg right:40% 100%](https://github.com/officegeek/image/raw/main/IntegrantSoftware_cloud.png)
# IntegrantSoftware - Cloud types
https://www.youtube.com/embed/KgL3BfAc9Cs

---

![bg right:25% 100%](https://github.com/officegeek/image/raw/main/IaaS.jpg)
# IaaS - Infrastructure as a Service

- It offers everything, including the server - Network/Storage/Containers(Docker)
- **Remember** - That you don’t get to own a server, but an instance of it (virtual machine)
- **Constraints** - The VM cannot offer more capabilities than the physical HW

### You think you have the whole server, but actually your VM can travel across servers and run where it wants 
 
---

![bg right:25% 100%](https://github.com/officegeek/image/raw/main/PaaS.jpg)
# PaaS - Platform as a Service

- Offers a runtime environment
- The client has it’s own web applications and wants to host them (*i.e. a website*)
- Container orchestration (*Docker*)

---

![bg right:30% 90%](https://github.com/officegeek/image/raw/main/SaaS.jpg)
# SaaS - Software as a Service

- The applications are hosted in the cloud and offer a **WEB interface**
- The client accesses the applications through the **browser**

---

<!-- _header: Microsoft Azure-->

![bg 100%](https://github.com/officegeek/image/raw/main/azure_cloud_types.png)

<!-- _footer: https://azure.microsoft.com/en-us/-->

---

![bg 70%](https://github.com/officegeek/image/raw/main/Pizza-as-a-Service-Microsoft-Azure.jpg)

<!-- _footer: Microsoft Azure Service-->

---

![bg 80%](https://github.com/officegeek/image/raw/main/The_Cloud_Stack.png)

<!-- _footer: Different ways to manage the stack-->

---

![bg right:6% 185%](https://github.com/officegeek/image/raw/main/cloud_types.jpg)

# Types of Cloud – types of implementation

**Public cloud** (*Amazon, IBM, Googl, Microsoft Azure*)
- The client and the service provider are different organizations
- The client doesn’t necessarily know where the servers are
- Cheap: no investment, no HW maintenance, pay-per-use

**Private**
- The company owns the data-center
- More expensive: same as not having the cloud
- Still using virtualization

**Hybrid**
- Companies that own servers and also uses some cloud services
- Most common solutions for companies with data centers
    - *I.e. your monitoring solution is in the cloud but you own the data center*

---

<!-- _class: invert-->
<!-- _header: Microsoft Azure-->
![bg](https://github.com/officegeek/image/raw/main/azure_cloud.png)

---

![bg right:45% 66%](https://github.com/officegeek/image/raw/main/e_conomic2.jpg)
# E-conomic

- Accounting software in the cloud
- Design your own invoices
- Free support
- Safe and with backups of everything
- API 

[E-conomic Developer](http://www.e-conomic.com)
[E-conomic DK](http://www.e-conomic.dk)

---

![bg](https://github.com/officegeek/image/raw/main/oracle_cx.jpg)

---

<!-- _backgroundColor: black -->
<!-- _color: white -->

![bg right:30%](https://github.com/officegeek/image/raw/main/white-question-mark.png)
# Assignment
## NIST Definition of Cloud Computing

---

Fill in the blanks - Read NIST Definition of Cloud Computing - https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf

![width:950px](https://github.com/officegeek/image/raw/main/cloudservices_2.jpg)

---

https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf

![width:1000px](https://github.com/officegeek/image/raw/main/cloudservices_1.jpg)

---

![bg right:30%](https://github.com/officegeek/image/raw/main/Google_Data_center.png)
# Google server centers
**Tour with BBC**
https://www.youtube.com/embed/PBx7rgqeGG8


---

![bg right:35%](https://github.com/officegeek/image/raw/main/Google_DataSecurity.png)
# Google server centers
**More on Data Security**
https://www.youtube.com/embed/4IDD8BP2EmU


---

<!-- _backgroundColor: black -->
<!-- _color: white -->
# Virtualization <!-- fit -->

---

# Virtualization basics

![bg left:60% 100%](https://github.com/officegeek/image/raw/main/wm_2.png)

Virtualization is the practice of breaking down the **physical infrastructure** of computing and networking resources into smaller, reusable and more flexible **software units**.

---

# Reasons why you should use virtualization
- **Server consolidation** – Virtualization can reduce capital investments. In traditional environments it is common to dedicate each server to a single application. Virtualization enables you to consolidate all the workloads on one server, which reduces the number of physical machines
- **Virtual labs** – Run a virtual machine to try out application
- **Security purposes** – Uae Virtual machines for specific purposes
- **Faster server provisioning** – With a virtual machine, you can quickly clone an image, master template, or existing virtual machine to get a server up and running within a few minutes
- **Cost saving** – On the physical server hardware, power and cooling of the servers. Time used to administer physical servers

---

<!-- _backgroundColor: black -->
<!-- _color: white -->

![bg right:40%](https://github.com/officegeek/image/raw/main/white-question-mark.png)
## What is a Hypervisor?
## What is a Bare-Metal Hypervisor?
## What is VirtualBox?
## What is Docker?
## What is JupyterLab

---

![bg left:45% 100%](https://github.com/officegeek/image/raw/main/hypervisor.png)
# Hypervisor

A hypervisor is a program for creating and running virtual machines.

1. **Native** - *Bare metal* hypervisors that run guest virtual machines directly on a system's hardware, essentially behaving as an operating system - *Microsoft Hyper-V, Oracle VM server*
2. **Hosted** hypervisors behave like traditional applications that can be started and stopped like a normal program - *Microsoft Virtual PC, Oracle VirtualBox*

---
<!-- _header: Virtualized deployment-->

![bg right:100% 95%](https://github.com/officegeek/image/raw/main/Virtual_Machine_Orchestration.png)

<!-- _footer: https://kubernetes.io-->

---

# Links

- [azure.microsoft.com](https://azure.microsoft.com/en-us/)
- [IBM Learn Cloud computing](https://www.ibm.com/cloud/learn/cloud-computing-gbl)
- [IBM Cloud](https://www.ibm.com/cloud)
- [aws.amazon.com](https://aws.amazon.com/)


# LinkedIN Learning - Cloud

[Learning Cloud Computing: Core Concepts](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Flearning-cloud-computing-core-concepts-2%3Ftrk%3Dshare_ent_url%26shareId%3DgpnsdTh5TMKAVcmhOkyGag%253D%253D&account=36836804)
