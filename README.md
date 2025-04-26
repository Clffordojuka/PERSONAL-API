# Personal API

Personal API is a RESTful API built with FastAPI, SQLAlchemy, and MySQL to manage customer data. This API allows for creating, retrieving, updating, and deleting customer records.

## Features

- **Create Customers**: Adds new customer records.
- **Read Customers**: Fetch customer details by ID or list all customers.
- **Database Integration**: Uses MySQL for persistent storage.
- **Validation**: Email validation and prevention of duplicate email entries.
- **Swagger UI**: Interactive API documentation with Swagger UI for easy testing and exploring.

## Tech Stack

- **FastAPI**: Web framework for building APIs quickly and efficiently.
- **SQLAlchemy**: ORM (Object Relational Mapper) to interact with the MySQL database.
- **MySQL**: Relational database for storing customer data.
- **Pydantic**: Data validation and parsing.
- **Uvicorn**: ASGI server for running the FastAPI app.

## Installation

Follow these steps to get the Personal API running on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/Clffordojuka/PERSONAL-API.git
cd PERSONAL-API
```

### 2. Set up a virtual environment

It's recommended to use a virtual environment to isolate your dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- For **Windows**:

  ```bash
  \venv\Scripts\activate
  ```

### 3. Install dependencies

Install all the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set up the `.env` file

Create a `.env` file in the root directory to store your database credentials.

Example of `.env` file:

```dotenv
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=personal_api_db
```

Replace `yourpassword` with the actual MySQL password.

### 5. Create the database

Ensure your MySQL server is running and create the database:

```sql
CREATE DATABASE personal_api_db;
```

### 6. Run the app

Run the FastAPI app with Uvicorn:

```bash
uvicorn personal_api.main:app --reload
```

The app will be available at `http://127.0.0.1:8000`.

### 7. Access the Swagger UI

Once the application is running, you can visit the Swagger UI for interactive documentation:

```
http://127.0.0.1:8000/docs
```

Here you can test the endpoints by creating and retrieving customers.

## API Endpoints

### POST /customers

Create a new customer.

**Request Body**:
```json
{
  "customerName": "John Doe",
  "email": "john.doe@example.com",
  "phoneNumber": "123-456-7890",
  "customerAddress": "123 Main St, City, Country"
}
```

**Response**:
```json
{
  "customerID": 1,
  "customerName": "John Doe",
  "email": "john.doe@example.com",
  "phoneNumber": "123-456-7890",
  "customerAddress": "123 Main St, City, Country",
  "dateCreated": "2025-04-25T00:00:00"
}
```

### GET /customers/{customer_id}

Get a customer by their ID.

**Response**:
```json
{
  "customerID": 1,
  "customerName": "John Doe",
  "email": "john.doe@example.com",
  "phoneNumber": "123-456-7890",
  "customerAddress": "123 Main St, City, Country",
  "dateCreated": "2025-04-25T00:00:00"
}
```

### GET /customers

Get a list of all customers.

**Response**:
```json
[
  {
    "customerID": 1,
    "customerName": "John Doe",
    "email": "john.doe@example.com",
    "phoneNumber": "123-456-7890",
    "customerAddress": "123 Main St, City, Country",
    "dateCreated": "2025-04-25T00:00:00"
  },
  {
    "customerID": 2,
    "customerName": "Jane Doe",
    "email": "jane.doe@example.com",
    "phoneNumber": "987-654-3210",
    "customerAddress": "456 Another St, City, Country",
    "dateCreated": "2025-04-26T00:00:00"
  }
]
```

### Error Handling

- **400 Bad Request**: Returned if a customer email already exists when trying to create a new customer.
- **404 Not Found**: Returned when trying to retrieve a customer by ID that doesn’t exist.

## Deployment

This project can be deployed on **Render** for a seamless cloud deployment.

### Steps for Deployment on Render

1. **Create an account**: Go to [Render](https://render.com) and create an account if you don't have one already.
2. **Create a new Web Service**:
   - Click on **New Web Service**.
   - Connect your GitHub repository to Render.
   - Select the `PERSONAL-API` repository and choose **FastAPI** as the service type.
3. **Set up environment variables**:
   - On Render, set the following environment variables:
     - `MYSQL_HOST`: The host for your MySQL database.
     - `MYSQL_PORT`: The port for your MySQL database (usually `3306`).
     - `MYSQL_USER`: The MySQL username.
     - `MYSQL_PASSWORD`: The MySQL password.
     - `MYSQL_DB`: The name of your MySQL database.
4. **Deploy the Service**: Click **Deploy**. Render will automatically build and deploy your FastAPI app.

Once deployed, you can access your API endpoint on the Render URL provided.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature-name'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.