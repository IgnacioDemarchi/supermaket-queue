# Supermarket Queue

## Description

Supermarket Queue is a simple Python program that simulates a queue system in a supermarket.

## Features

- The function `queue_time` calculates the amount of time it will take to serve all customers.
- You can test the different implementations of queue_time and analize them plotting their perfomance
- The main would be showing the python implementation performance first and then the C implementations

## Installation

To run the C code, you first need to compile it. You can do so by executing:

```bash
gcc -shared -o libqueue.so -fPIC queue.c
```

## Usage

To run the program and test the function, run:

```bash
python3 main.py
```
