# PyClick - automated VPN enabling

### Script for enabling VPN using pynput Python library.
### Project was created in Python

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project was created to automate VPN enabling using Python script.
In project was used "pynput" library. It's library for taking control of
mouse and/or keyboard and making specified actions instead of user.
Actions for pynput lib are configure in JSON file. Sensitive datas like
passwords, pin/code are located in .env file and write to environment
variables. Modification of JSON file could be a way to automate different
things.

## Technologies
Python

## Setup
Before use script it is better to close authentication program and Cisco 
AnyConnect. The best way is a status just after start your computer, then
any action is needed.
Be aware that on different monitor, script could not work properly,
because of different resolution.

At the beginning install needed modules: pynput, python-dotenv and
pyperclip libs using commands:
_pip install pynput_
_pip install python-dotenv_
_pip install pyperclip_

Create and fill .env file based on .env.dist. Put the file
to the project catalog.

 Execute main.py

