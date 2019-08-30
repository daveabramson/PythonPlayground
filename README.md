# PythonPlayground
a place to play and learn some stuff about writing python...

This project contains code I wrote during my initial learning with python. It is likely not useful outside of trivial examples.

There is a VS code snippet in the project that you can import and use. Once imported, type "pytest" to access the snippet. The snippet uses the test naming convention from "The Art Of Unit Testing" by Roy Osherove.

Things that I learned while creating this project:
1. How to create python projects in VS
2. That splitting python code up into multiple projects is just as easy as other languages
3. Python comes with a unit test module that is easy to use, so there is no excuse for un-unit-tested python code
4. A basic Abstract Base Class with two children
5. Basic dependency injection (without the dependency injector framework - which seems to be the popular choice in python)
6. How to place tombstones so the help() function outputs their contents
7. Multi-line statements - continue to the next line with \ (just like a C/C++ macro)
8. Private methods are defined by double underscore in front of the name (ex: def __privateFunc(self))
9. Looping through two lists in parallel using the zip() function (see TestCosineListMaker.py)
10.Here is one way to create a form and use it. It assumes using PySide2. (https://nikolak.com/pyqt-qt-designer-getting-started/)
   a. Use designer.exe to drag and drop stuff onto a form
   b. Save that to a .ui file (via save in designer.exe)
   c. convert the .ui file to a .py file with the pyside2-uic tool
   d. Create a class that inherits from the coverted ui class that will handle all
      of the event connections (because the converted ui .py file is completely
      overwritten whenever changes are made).
11.designer.exe is installed with pyside2 at the root
12.pyside2-uic is installed under <pythonroot>\Scripts (where pip is)
13. __init__.py in every directory containing .py files in the project allows them to be imported
directories. This allows the code files to be nicely structured
14. A .py at the root of the project (above all sub-directories contianing py files) can be used to 
start executing a program from a regular terminal that is entirely contained within the sub directories (see runconsoleapp.py and runsimpleguiapp.py)
   EX: python runconsoleapp.py
   - that will run the console app in the terminal, but all of the source is contained in sub-dirs
15. The following extensions for VS Code are useful 
   a. Git History
   b. Git Lens (more functionality that Git History)
16. The Qt for Python extension lets you add a form, or open one (.ui) in the designer that you 
set in the extension settings. You can make visual edits there, save, then return to visual studio code. Then you can right click the .ui file and compile it to a python file. The converted python file comes out in the output window. It is best to clear the output first, then you can just select all in the output window, copy, select all in the .py file and paste. There, now your changes are in the python version.
