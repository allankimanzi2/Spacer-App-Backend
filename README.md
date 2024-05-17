Spacer-App-Backend

Spacer-App-Backend is the backend service for the Spacer platform, a marketplace that allows users to find and book unique spaces for meetings, events, and activities. This backend is built using Flask and SQLAlchemy.
Table of Contents

    Prerequisites
    Installation Guide
    Contributors
    Languages
    Suggested Workflows

Prerequisites

Before proceeding with the installation, make sure you have the following prerequisites installed on your system:

    Python 3.8.13
    pip package manager

Installation Guide
Clone the Repository

You can clone the repository using either HTTPS or SSH.

Using HTTPS:

sh

git clone https://github.com/allankimanzi2/Spacer-App-Backend.git

Using SSH:

sh

git clone git@github.com:allankimanzi2/Spacer-App-Backend.git

Navigate to the Project Directory

sh

cd Spacer-App-Backend

Create a Virtual Environment

sh

python -m venv .venv

Activate the Virtual Environment

For macOS/Linux:

sh

source .venv/bin/activate

For Windows:

sh

.venv\Scripts\activate

Install Project Dependencies

sh

pip install -r requirements.txt

Running the Application

To run the application, use the following command:

sh

flask run

Make sure your virtual environment is activated.
Database Migrations

Initialize the migrations directory:

sh

flask db init

Create a new migration:

sh

flask db migrate -m "Initial migration."

Apply the migration to the database:

sh

flask db upgrade

Contributors

    @vinnyboss90
    @Abdighafar1
    @itzkirimi
    @abdullahi-abdi-12
    @allankimanzi2

Languages

    Python 93.8%
    Mako 6.2%

Suggested Workflows

Based on your tech stack, here are some suggested workflows:
SLSA Generic Generator

Generate SLSA3 provenance for your existing release workflows.
Python Application

Create and test a Python application.
License

MIT