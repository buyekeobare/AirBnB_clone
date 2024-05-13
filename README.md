# AirBnB clone - The console Project

<p align="center">
  <img src="https://github.com/buyekeobare/AirBnB_clone/blob/main/images/hbnb_logo.png" alt="logo">
</p>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [Project Description](#overview)
  - [Console Design](#design)
- [💻 Prerequisites](#prerequisites)
- [🚀 Feautures and functionalities](#features)
  - [Classes](#classes)
  - [Storage](#storage)
  - [Console](#console)
- [🛠 Installation](#installation)
- [🛠 Run](#run)
- [🛠 Test](#test)


<!-- About the Project -->

## About the Project

### Project Description

An AirBnB clone is a copy of the AirBnB website, where you can find and rent accommodations. 

To recreate its functionalities, we're developing a system that mimics AirBnB's operations. We're using a special type of database format called JSON and employing techniques like object-oriented programming, Python data translation, and command interpretation. The outcome is a local database that can be easily adjusted using specific commands, offering a flexible and efficient method for handling data.

The project currently only implements the back-end console.

### Console Design

<p align="center">
  <img src="https://github.com/buyekeobare/AirBnB_clone/blob/main/images/console_airbnb.png" alt="Console">
</p>

<!-- Prerequisities -->

## Prerequisites

- Python 3.x
- Additional dependencies:
	* import os
	* import json
	* import re
	* import unittest

<!-- Features and Functionalities -->

## Features and Functionalities

### Classes

  - BaseModel -> id, created_at, updated_at
  - FileStorage -> Inherits from BaseModel
  - User -> Inherits from BaseModel
  - State -> Inherits from BaseModel
  - City -> Inherits from BaseModel
  - Amenity -> Inherits from BaseModel
  - Place -> Inherits from BaseModel

### Storage

The classes mentioned above are managed by the abstracted storage engine, which is defined within the FileStorage class.

Whenever the backend of our AirBnB is initialized, it creates an instance of FileStorage named storage. This storage object is responsible for loading or reloading data from any class instances stored in the JSON file named file.json. As new class instances are created, existing ones are updated, or some are deleted, the storage object ensures that these changes are accurately reflected in the file.json.

### Console

The console serves as a command-line interpreter specifically designed for managing the backend operations of our AirBnB. It allows users to handle and manipulate all classes utilized by theapplication through calls on the storage object defined within the system.

<!-- Installation -->

## Installation

Clone the repository:

   ```
  git clone https://github.com/buyekeobare/AirBnB_clone.git
  ```

<!-- Run -->

## Run

You first chnage directory to the AirBnb using this command: cd AirBnB; then

To execute the console use:

```
python3 console.py
```
or

```
./console.py
```

<!-- Test -->

## Test 

To personalize the classes and execute unit tests to confirm that your changes haven't modify the functionality use:

```
python3 -m unittest discover tests
```
