# Blog Post Storage Service

## Overview

This microservice enables the storage of user-submitted blog posts into a MongoDB database. It leverages Flask for the backend, offering a RESTful API endpoint for blog post submissions. The service is designed with simplicity and scalability in mind, ensuring easy integration into broader applications requiring blog content management.

## Features

- RESTful API endpoint for blog post submissions.
- MongoDB for robust data storage and retrieval.
- Cross-origin request handling for frontend-backend integration.
- Environment variable management for secure configuration.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- pymongo
- dotenv
- A MongoDB database

### Installation and Setup

1. Clone the repository to your local machine.
2. Install the required Python packages:

```bash
pip install Flask pymongo python-dotenv flask-cors
```
Configure your MongoDB connection string in a .env file:
```makefile
LOGININFO=your_mongodb_connection_string
```
### Running the Service
Execute the Flask application:

```bash
python blog_post.py
```
The service will start, listening for blog post submissions on /blog_post.

### Usage
To submit a blog post, send a POST request to /blog_post with a JSON payload containing the username and post data.
