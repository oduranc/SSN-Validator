# SSN (Social Security Number) Validator

# User Manual

## Index
1. [Description](#Description)
2. [Download and Installation](#download-and-installation)
3. [How to use the software](#how-to-use)

## Description

A Social Security number (SSN) is a nine-digit number that is generally issued to U.S. citizens, lawful permanent residents, and certain (working) nonimmigrants. The Social Security Administration issues the number to track individuals employment for Social Security benefits.

The SSN Validator is a software that seeks to offer Americans, or whoever needs it, the ability of check if certain numbers combination could be a valid Social Security Number.

## Download and Installation

1. Check if you have the latest version of Python installed in your computer.

2. In case you haven't installed Python or is not up to date, download and install the latest version of Python from this link: https://www.python.org/downloads/.

3. Also, linux users can install latest version of python by writing in their terminal ``` sudo apt install python3 ```.

4. After installation is completed, ``` git clone ``` this repository.

5. After clonning, ``` cd Requerimientos-Criterios-Casos ```.

6. Then, all you have to do to init the software is to ``` python principal.py ```, ``` python3 principal.py ``` or ``` pip3 principal.py ```. If you followed item 3 then ``` python3 principal.py ``` should work for you.

## How to use

Once you have installed the software, all you have to do is use it!

The first thing you're going to see is a Welcome message. Right after this welcome message, the software will ask for the first three numbers of the combination, which you're going to type by keyboard (Ex.: *123*) and then press *Enter*. Then, it will ask you two more times for the rest of the combination.

Once you've finished typing all three parts, the software will automatically show you the three parts divided by hyphen (like this: XXX-XX-XXXX).

In case the SSN shown is valid, it will tell you and will ask you if you want to try with another number or to exit the application. Otherwise, it will tell you which parts of your input makes the social security number invalid and why.