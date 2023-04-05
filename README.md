# Django Web Scraper
This is a Django web scraping application. Users can scrape web pages, view a list of all the pages they have scraped, and see details of the links found on each page.

## Features
User authentication: Users can register, login, and logout to access the web scraping features.
Add Pages: Users can add web pages for scraping by providing the URL of the page.
Scraping in the Background: The scraping process is handled asynchronously using celery and redis cloud, allowing users to continue using the application while pages are being scraped.
Page List: Users can view a list of all the pages they have scraped, along with the number of links found on each page.
Page Details: Users can view the details of each page, including the links found on the page with their URLs and names.
Pagination: Both the page list and page details views are paginated to handle large numbers of pages and links.

## Technologies Used
Django framework.
Celery.
Redis Cloud.
Bootstrap.

## Setup and Installation
NOTE: You need to edit create a .env file and add:
CELERY_BROKER_URL=redis://:<your-password-here>N@<your-redis-hiost>:<port>
CELERY_RESULT_BACKEND=redis://:<your-password-here>N@<your-redis-hiost>:<port>
EXAMPLE:
CELERY_BROKER_URL=redis://:sdfsdffdsffgN@redis-14512.c266.us-east-1-3.ec2.cloud.redislabs.com:14512
CELERY_RESULT_BACKEND=redis://:sdfsdffdsffgN@redis-14512.c266.us-east-1-3.ec2.cloud.redislabs.com:14512
or directly edit the following line at settings.py file:
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

Create a new directory for the project.
Go to your new directory.
Clone the repository.
Create a virtual environment and activate it.
Install the dependencies using pipenv.
Create a .env file.
Edit the .env file.
  
Open a new terminal.
Got to the project direcotry.
Run Celery.
  
Go to the project directory.
Start the dev server.

```bash
mkdir koombea
git clone git@github.com:juliobarbagallo/koombea.git
pipenv shell
pipenv install
cd koombea
touch .env
```
### In the .env file you must to add the env variables for celery:
CELERY_BROKER_URL and CELERY_RESULT_BACKEND as mentioned above.



## Open a new terminal
```bash
cd koombea/py_scraper
celery -A py_scraper worker -l info -E
```

## Go back to the original terminal
```bash
python manage.py runserver
```
  
## Open the browser and navigate to: http://127.0.0.1:8000/ or http://127.0.0.1:8000/accounts/login/
  
Usage
Register or login to access the web scraping features.
Click on "Add Page" to add a web page for scraping by providing the URL of the page.
Once the page is added, the scraping process will start asynchronously in the background.
Users can view the list of all the pages they have scraped on the "Pages" page, including the number of links found on each page.
Users can click on the page name to view the details of the links found on that page, including the URLs and names of the links.
