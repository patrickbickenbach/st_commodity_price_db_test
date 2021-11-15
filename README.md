# Commodity Price Database
Using web scraping to gather data and create my own commodity price database for personal use only.\
Implemented Streamlit to create an simple website for easy visualisation of gathered data.

### Packages you need to install to run the website and web scraper:
1) WINDOWS:
```
pip install streamlit
pip install beautifulsoup4
pip install matplotlib
```
2) LINUX:
```
pip install streamlit
pip install beautifulsoup4
pip install matplotlib
pip install lxml
pip install pandas
pip install requests
sudo apt-get install libatlas-base-dev
```
### Automate linux device with Crontab:
```
0 8 * * * python /home/pi/Desktop/commodity_price_db/linux/webscrape.py
1 8 * * * sh /home/pi/Desktop/commodity_price_db//linux/automate_git.sh
```
\
![Skjermbilde](https://user-images.githubusercontent.com/67826084/140814979-0076ba33-b874-4167-8e46-71c3ba7fe1de.PNG)
