# Split Expenses App - Backend

This is the backend service for the Split Expenses application, built using Django and PostgreSQL. The backend provides a RESTful API for managing expenses, user authentication, and group functionalities.

## Features

- User authentication and management
- Expense tracking and management
- Group expense sharing
- RESTful API for frontend integration

## Requirements

- Python 3.x
- Django
- PostgreSQL

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd split-expenses-app/backend
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**

   Update the `settings.py` file with your PostgreSQL database credentials.

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

## API Documentation

Refer to the API documentation for details on available endpoints and their usage.

## Observability

The backend is designed with observability in mind, utilizing logging and monitoring tools to track performance and errors.

## Scalability

The application is built to scale horizontally, allowing for multiple instances to handle increased load.

## Optimization

Performance optimizations have been implemented, including database indexing and efficient query handling.

## Deployment

The backend can be deployed using Docker and Kubernetes. Refer to the deployment documentation for detailed instructions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.