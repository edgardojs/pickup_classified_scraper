# Classified Scraper

A Python script for scraping classified ads and sending a summary email.

## Prerequisites

- Python 3.x
- Redis (for Celery)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd classified-scraper

2. Install the dependencies
With pip (note it's recommended to use virtual environment)
`pip install -r requirements.txt`

With pipenv
a. Install pipenv
b. `pipenv shell` and `pipenv install` on the virtual environment

## Setup the environment variables
1. Create a .env file in the project root and add the following
`GOOGLE_PASSWORD=your_google_password ### Recommended to use 2 step authorization + app passwords ###
PERSONAL_EMAIL=your_personal_email@gmail.com
`
## Usage 
Running the scraper
`python run.py`

## Running Celery for Scheduled tasks
1. Start the Celery worker: 
`celery -A tasks worker --loglevel=info`
2. Start the Celery beat for scheduled tasks:
`celery -A tasks beat --scheduler celery.beat.PersistentScheduler`

## Project structure

classified_scraper.py: Contains the ClassifiedScraper class for scraping ads.

json_handler.py: Contains the JsonHandler class for loading and updating data in a JSON file.

mailer.py: Contains the EmailSender class for sending emails.

run.py: Main script for running the scraper and sending emails.

celery.py: Configuration file for Celery.

tasks.py: Celery task definition.

## License
This project is licensed under the MIT License - see the LICENSE file for details
