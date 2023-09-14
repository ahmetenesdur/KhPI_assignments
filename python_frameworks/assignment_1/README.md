# Tourist Trips Flask Application

This repository contains the Flask application developed as a part of the assignment. The application helps in managing and finding tourist trips information.

#### Task Selection Screenshot

![Task Selection Screenshot](https://i.imgur.com/wKqR5oT.png)

## Objective

The main objective of this assignment was to gain basic skills in creating simple Flask applications using layouts.

## Features

- Three different pages utilizing Flask layouts and Jinja2 template blocks.
- Ability to filter tours by the tour operator or by the minimum number of days directly from the address bar.
- Displays a suitable picture or message based on the request result.
- 404 error handling page for non-existing routes.
- CSS styling using selectors for tags, classes, and IDs.

## Installation

1. **Install Virtual Environment**
   Run the following command to install a virtual environment:

   ```
   python -m venv env
   ```

2. **Activate Virtual Environment**

- On Windows:
  ```
  .\env\Scripts\activate
  ```
- On Linux/Mac:
  ```
  source env/bin/activate
  ```

3. **Install Flask**
   Install Flask using the following command:

   ```
   pip install flask
   ```

4. **Running the Application**
   Run the following command to start the application:

   ```
    python app.py
   ```

## Usage

1. **Home Page**
   Visit `http://127.0.0.1:5000/` to access the home page.

2. **Filtering Tours**

- By Tour Operator:
  ```
  http://127.0.0.1:5000/tour?operator=OperatorName
  ```
- By Minimum Number of Days:
  ```
  http://127.0.0.1:5000/tour?days=NumberofDays
  ```

3. **Finding the Most Expensive Tour to Turkey**
   ```
   http://127.0.0.1:5000/expensive_turkey_tour
   ```

## Screenshots

Home Page:
![Home Page Screenshot](https://i.imgur.com/hqJOyu4.png)
Tour Operator Filter:
![Tour Operator Filter Screenshot](https://i.imgur.com/nT0XBYq.png)
Minimum Days Filter:
![Minimum Days Filter Screenshot](https://i.imgur.com/rKKhSQq.png)
Most Expensive Tour to Turkey:
![Most Expensive Tour to Turkey Screenshot](https://i.imgur.com/mRerJqH.png)
404 Error Handling:
![404 Error Handling Screenshot](https://i.imgur.com/20n3bx5.png)
