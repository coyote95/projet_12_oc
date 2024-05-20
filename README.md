# Projet 12 OpenClassrooms: Develop a secure back-end architecture with Python and SQL

Creation of a Python application "Epic Events" to manage contracts and events for clients. The application uses a relational database secured by authentication and authorization management. Error logging is also ensured by Sentry.

## Installation with pip

Install project with powershell windows:

```bash
    git clone https://github.com/coyote95/projet_12_oc.git
    cd projet_12_oc
    python -m venv ENV
    source ENV/Scripts/activate
    pip install -r requirements.txt
```

## Configuration file

You need to create an .env file with your environment variable:

SECRET_KEY="your_sercret_key"  
DATABASE="path_database"  
SENTRY="url_sentry"
    
