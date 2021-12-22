# Virtual environment - *venv*
A virtual environment, is a self-contained directory that comes with a specific Python version and additional packages.

Additionally, you can install or uninstall any Python libraries (*using pip*) once the virtual environment is activated.

![](./image/virtualenv.png)

The Python version (*by default the one installed on your Operating System will be included unless you explicitly specify a different one*), additional libraries and scripts installed in one virtual environment, are **completely isolated** from those installed in your machine or any other virtual environment.

Python comes with a virtual environment manager called **venv** for Python 3.

# venv commands
The first thing you need to do when developing your own Python application or library, is to create a virtual environment.

## Install 
Depending on your current syatem setup, you might need to install **virtualenv**

```
pip3 install -U pip virtualenv
```

## Create the virtual environment
This command, will create a virtual environment called **my_venv** which is placed in the current directory.

```
# macOS/Linux
python3 -m venv .my_venv

# Windows
python -m venv .my_venv
```

If you want to create a virtual environment in a specific directory, then include it with the *venv name*.

```
python3 -m venv path/to/your/venv/.my_venv
```

## Activate a virtual environment
When you have created a virtual environment, you need to *tell* the Operating System to make use of it.

To do so, you need to call the activate script which is located under the **bin/** sub-directory in the created tree structure of your virtual environment.

![](./image/venv_script.jpg)

Ther are different scripts for different OS, this is the Windows scripts.

```
# macOS/Linux
source my_venv/bin/activate

# Windows
.\Scripts\activate
```

If you look at the start of the terminal you should that each line begins with (**my_venv**) that indicates that currently, the virtual environment called **my_venv** is activated.

![](./image/vevn_cmd.jpg)

Once the virtual environment is activated, everything you install or uninstall will only have effect **within that specific environment and nowhere else**.

## Confirm
You can confirm you’re in the virtual environment by checking the location of your Python interpreter.

```
# macOS/Linux
which python

# Windows
where python
```

It should be in the env directory


##  Deactivate a virtual environment
Deactivate a virtual environment, when you are finished using it.

```
deactivate
```

Notice that the virtual environment named (**my_venv**) has disappeared which means that no virtual environment is currently active.

## Remove/Delete a virtual environment
A virtual environment is really nothing more than a tree directory which gets automatically created with a specific content. Therefore, in order to get rid of a *venv* you simply need to remove/delete the directory from the disk.


## Clear an existing virtual environment
Sometimes, instead of completely deleting a virtual environment, you may instead want to **clear** all the packages that were previously installed.

```
# macOS/Linux
python3 -m venv --clear path/to/my_venv

# Windows
python -m venv --clear path/to/my_venv
```

## Help
You can find a comprehensive list of all the options you have when using **venv** by running this command:

```
# macOS/Linux
python3 -m venv -h

# Windows
python -m venv -h
```

![](./image/venv_help.jpg)

## Install packages
When you are in the virtual environment you install the packages as normal.

```
pip install 'xxx'
```