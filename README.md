# PyWeekend-Kiwi.com
Entry task for applying for Python weekend (April 5–7, 2019) in Bratislava, Slovakia organized by Kiwi.com

# Kiwi.com Python weekend Entry task
This task was designed to test your Python and problem solving skills and by solving it, you'll provide us with proof that you will benefit from Python Weekend workshop.

## What you can use
 * Python - version 2 or 3, you already know the right answer in 2019 :)
 * all modules are allowed

## Task description
Your task is to create a program that will get airports in the United Kingdom and display them on standard output.
You will then create a structure with cities, airport names, IATA codes and latitute/longitude from Kiwi.com locations API.

You are encouraged to use the Kiwi locations API located at:
 * https://docs.kiwi.com/locations/

If you encounter any problems, use your own best judgement to solve them.

## Input and output
The program does not take any arguments (you can specify options described below), the output will be list of airports with related information.

## Ways how to run the program
You can specify multiple options in the program:
 * **--help** - print help message
 * **--cities** - cities with airports
 * **--coords** - coordinates of each airport
 * **--iata** - IATA codes
 * **--names** - name of the airport
 * **--full** - print every detail from each airport
 
When run without any option, provide only name and IATA code of airport.
```
$ python kiwi_airports.py
$ python kiwi_airports.py --help
$ python kiwi_airports.py --cities
$ python kiwi_airports.py --iata --cities
$ python kiwi_airports.py --coords
$ python kiwi_airports.py --full
```

## Output
Output data should be in a format that is suitable for further processing.
