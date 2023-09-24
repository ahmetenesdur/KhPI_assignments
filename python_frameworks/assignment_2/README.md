# Laboratory Work No. 2 - Using Jinja Template Engine with Flask

## Introduction

This laboratory work is focused on creating a web application using the Flask framework and leveraging the Jinja template engine to implement business logic directly within the HTML template. This README contains details about the structure and functionality of the application.

## Table of Contents

1. [Cover Page](#cover-page)
2. [Code of Files](#code-of-files)
3. [File Structure](#file-structure)
4. [Screenshots](#screenshots)
5. [Conclusions](#conclusions)

## Cover Page

### Details

- **Title of the Laboratory Work**: Using Jinja Template Engine with Flask
- **Student's Name**: Ahmet Enes Dur
- **Student Group**: КН-221іа.е
- **Instructor's Name**: Svіtlana Kovalenko
- **Institution's Name**: National Technical University "Kharkiv Polytechnic Institute"
- **Department/Faculty**: Department of Software Engineering and Management Intelligent Technologies

## Code of Files

### `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {'example_data': [1, 2, 3, 4, 5]}
    return render_template('template.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
```

This script initializes the Flask application and defines a route that renders an HTML template with a data dictionary.

### `templates/template.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}"
    />
    <title>Jinja Template Example</title>
  </head>
  <body>
    <h1>Data Processed with Jinja</h1>
    {% for item in data.example_data %} {% if item % 2 == 0 %}
    <p>{{ item }} is even</p>
    {% else %}
    <p>{{ item }} is odd</p>
    {% endif %} {% endfor %}
  </body>
</html>
```

This HTML file demonstrates the use of Jinja template engine's expressions and statements to process and display data.

### `static/style.css`

```css
body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
  color: #333;
  margin: 0;
}

h1 {
  background-color: #4caf50;
  color: white;
  padding: 20px;
  margin: 0;
}

p {
  padding: 10px;
  background-color: #fff;
  border-bottom: 1px solid #ccc;
  transition: background-color 0.3s, color 0.3s;
}

p:nth-child(even) {
  background-color: #f9f9f9;
}

p:hover {
  background-color: #4caf50;
  color: white;
}
```

This stylesheet adds basic styles and hover effects to the HTML elements.

## File Structure

The project has the following file structure:

```lua
project_directory/
|-- templates/
|   |-- template.html
|-- static/
|   |-- style.css
|-- app.py
```

## Screenshots

![Screenshot 1](https://i.imgur.com/mrCKyKT.png)
![Screenshot 2](https://i.imgur.com/FEcoxD6.png)

## Conclusions

In this laboratory work I learned how to use the Jinja template engine to process data and display it in HTML templates. I also learned how to use the Flask framework to create a web application that renders HTML templates.
