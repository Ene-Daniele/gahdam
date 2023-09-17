# Instructions for my colleagues

- Creating a python file:
> Include a top comment with the date, hour, and your name, followed by a description

ex from close.py:
```py
"""
15/09/2023 10:40am ENE DANIELE
Script used for closing operations
"""
```

# Project structure
`launch.bat` starting batch script
> Make sure to use `CTRL+C` and `N` to allow the batch script to finish while stopping the main python script, the batch script has priority over the python one, so the keyboard interrupt will assume you are trying to stop the batch one too (the main python script will stop either way).

`close.py` closing operations
<h3>images/</h3>

+ `idle.jpg` still image with nobody in frame
+ `frame.jpg` image compared with idle 10 times a second

> This should contain 2 files, `idle.jpg` and `frame.jpg` which at the end of the program are deleted, the reason they are in a folder is to prevent shenanigans where i end up with thousands of files in the main folder

<h3>src/</h3>

+ `main.py` main entry point
+ `utils.py` utility functions

