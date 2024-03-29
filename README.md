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