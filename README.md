# Shapes Drawing Tool

This is a Django-based drawing tool that allows users to draw shapes on a floor plan and manage them through a database. Users can also submit their suggestions for future enhancements.

## Features

- Draw shapes (rectangles) with specified dimensions, positions, and colors.
- Manage shapes: add, view, and delete.
- Customizable floor dimensions and background color.
- Submit suggestions and view them in the admin interface.

## Demo
Open the demo file, and you will be taken to the video file in the GitHub repository, where you can play it directly in the browser.

## Installation

### Prerequisites

- Python 3.x
- Django

### Setup

1. **Clone the repository:**
  ```bash
   git clone https://github.com/yourusername/shapes_project.git
   cd shapes_project
   ```
2. **Create and activate a virtual environment:**
  ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install dependencies:**
  ```bash
   pip install -r requirements.txt
  ```
4. **Apply migrations:**
  ```bash
   python manage.py makemigrations
   python manage.py migrate
  ```
5. **Create a superuser:**
  ```bash
   python manage.py createsuperuser
  ```
6. **Run the development server:**
  ```bash
   python manage.py runserver
  ```
7. **Access the application:**
   - Open a web browser and go to http://127.0.0.1:8000.
  

