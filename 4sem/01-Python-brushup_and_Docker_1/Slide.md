---
title: Python brushup Docker and Azure
theme: gaia
_class: lead
paginate: true
marp: true
backgroundColor: #fff
size: 4K
@auto-scaling true
markdown.marp.enableHtml
---

<!--
_backgroundColor: black
_color: white
-->

# Python brushup Docker and Azure
### 2022 - Tue Hellstern

---

# Agenda

- GitHub
- Virtual Environment
- MySQL
- Dashboard - Dash - Python

---
<!--
_backgroundColor: black
_color: white
-->

# GitHub <!-- fit -->

---

<!--
_backgroundColor: black
_color: white
-->

# Virtual Environment <!-- fit -->

---
![bg right:30% 110%](./image/virtual-environment.png)

## Virtual environments help you to:

- Resolve dependency issues by allowing you to use different versions of a package for different projects. *For example, you could use Package A v2.7 for Project X and Package A v1.3 for Project Y.*
- Make your project self-contained and reproducible by capturing all package dependencies in a requirements file.
- Install packages on a host on which you do not have admin privileges.
- Keep your global site-packages/directory tidy by removing the need to install packages system-wide which you might only need for one project.

---


## Step by Step

1. **Create directory**
    - *mkdir*
2. **Create a new virtual environment**
    - *python3 -m venv venv-name*
3. **Activate the virtual environment**
    - macOS - *source env/bin/activate*
    - Windows - *.\Scripts\activate*
4. **Packages**
    - Install 
        - *pip3 install name*
    - requirements.txt
        - *pip3 install -r requirements.txt*

---

<!--
_backgroundColor: black
_color: white
-->

# MySQL <!-- fit -->

---

<!--
_backgroundColor: black
_color: white
-->

# Dashboard - Dash <!-- fit -->

---
