# TrackPackageBot
Bot that let you track your packages 

## Idea

The idea of this project is to create a simple application that, starting from the tracking/delivery number/code, let you track the packages.

Our objective is to get around the use of different technologies like:

- Docker
- CI/CD through GitLab Actions
- Automate testing

## What the bot should do

### Input

The user will be able to input the tracking identifier in many ways:

- By sending a message to a Telegram bot

At this point, the application will save the user_id and the tracking_id into a database.

### Processing

Continuously, the steps that the bot will do are:

- Get the job waiting to be processed (a queue has to be implemented)
- Obtain all information about the tracking-identifier (tracking_id, tracking_website, ecc)
- Lookup the status of the delivery 
- If new changes have arrived then add a row to the db with the new status and the timestamp of the update

The application will automatically create new jobs based on the last update time of tracking.
If a package has been delivered, all the updates of that delivery will be sent to the user through an email, and a flag on the database tables will be updated to remove from the search queries these records.

### Output

Every new notification about a delivery, a new email or telegram message has to be sent to the user.
At the end of a delivery, all the tracking updates will be sent to the user.

## Project architecture

The project architecture can be structured as follows:

- A docker application that contains:
  - Python environment to execute the input script
  - Python environment to execute the update scripts
  - Python environment to send the notifications to the user
  - SQL environment to store the data
  
The application should be run on a Raspberry PI (2 or higher), so the Docker images have to be ARM based.

TBD: the use of a single Python environment instead of 3 different ones. I prefer the 3 different environment to better separate the components of the application.

## Notes

This a personal project developed with the help of a friend.
All the code in here can be referenced for other projects (we would love to hear for what you have used our code).

## Requirements

- Docker installed on your computer

To launch the app run from the root of the project the following command:
> docker-compose up --force-recreate --build