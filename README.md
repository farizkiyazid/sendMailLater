# sendMailLater
Flask app that sends POST request of an email and sends it on the specified time we want.

# The apps installation
- to run the app
flask run

- to make database
flask db init

- to create database migration
flask db migrate

- to update the migration to the database
flask db upgrade

- after that you'll need to fix the config with your own email

# The app endpoints
- for homepage : / or /index

- for POST form : /email

- for the POST endpoint : /save_emails

- you can also use /save_emails directly with POST
