# Covid-19 Tracker
A simple website to track the number of Covid-19 cases in your state. This website is currently able to display information on the 50 states in the USA

## Development 
This website was made using Flask. The usage of python for this application made it easier to scrape a credible website for the number of cases of Covid-19. 
The source that was scraped for this website can be found [here](https://www.worldometers.info/coronavirus/country/us/).\
This website has two pages: 
* The first page (index.html) displays the total number of cases in the united states, along with the total number of deaths and recoveries. 
* The second page is accessed by selecting a state from the dropdown. This page displays the number of cases in the chosen state, the number of deaths, and the number of new cases on that particular day.

Urllib3 was used to access the [website](https://www.worldometers.info/coronavirus/country/us/) and Beautiful Soup was used to parse the HTML that was retrieved by Urllib3. The necessary information was then retrieved from the html and returned by their respective functions in data.py./

App.py, which is the flask application, gets the returned data from the functions in data.py and then passes the values into the context of the HTML, which then renders them. 

---
## Get this running on a local machine
This is a very simple flask application and easy to get running on your local machine by following these steps:
* Clone this repository into your local machine.
* Make sure you have python 3.6 or higher. Python can be downloaded  [here](https://www.python.org/downloads/).

* Next, get pip, which is a package manager for python. Follow the steps [here](https://pip.pypa.io/en/stable/installing/).

* Install the required packages through pip on the command line.

**Flask:**
```python
pip install flask
```
**Urllib3:**
```python
pip install urllib3
```
**Beautiful Soup:**
```
pip install bs4
```

After these packages are successfully installed, run the app.py using python.
To run this app, make sure you change directory into the cloned repository, and run the following command:
```python
python app.py
```
The app is now running locally on port 5000.
In your browser, go to **127.0.0.1:5000** to view the app.
