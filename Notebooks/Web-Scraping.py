# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
#
# # Define the function to scrap reviews of a shop from etsy.com
# def scrape_reviews(url):
#     # Define the headers
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
#     # Get the html of the page
#     html = requests.get(url, headers=headers)
#     # Parse the html
#     soup = BeautifulSoup(html.text, 'html.parser')
#     # Get the reviews
#
#
#     reviews = soup.find_all('div', {'class': 'wt-grid__item-xs-12 wt-grid__item-md-6 wt-grid__item-lg-4 wt-grid__item-xl-3 wt-mb-xs-1 wt-mb-md-2 wt-mb-lg-3 wt-mb-xl-4 wt-display-flex wt-flex-column'})
#
#     # Define the list to store the reviews
#     reviews_list = []
#     # Loop through the reviews
#     for review in reviews:
#         # Get the review
#         review = review.find('div', {'class': 'wt-grid wt-grid--block wt-grid--justify-center-xs wt-grid--justify-start-md wt-grid--justify-start-lg wt-grid--justify-start-xl'})
#         # Get the review title
#         review_title = review.find('h3', {'class': 'wt-text-body-03 wt-line-height-tight wt-break-word wt-mb-xs-0'}).text
#         # Get the review text
#         review_text = review.find('div', {'class': 'wt-text-caption wt-line-height-tight wt-break-word wt-mb-xs-0'}).text
#         # Get the review date
#         review_date = review.find('span', {'class': 'wt-text-caption wt-line-height-tight wt-break-word wt-mb-xs-0'}).text
#         # Get the review rating
#         review_rating = review.find('div', {'class': 'wt-display-flex-xs wt-display-flex-md wt-display-flex-lg wt-display-flex-xl'}).find('div', {'class': 'wt-mr-xs-1 wt-mr-md-2 wt-mr-lg-3 wt-mr-xl-4'}).find('div', {'class': 'wt}'}).find('div', {'class': 'wt-text-caption wt-line-height-tight wt-break-word wt-mb-xs-0'}).text
#         # Get the review author
#         review_author = review.find('div', {'class': 'wt-display-flex-xs wt-display-flex-md wt-display-flex-lg wt-display-flex-xl'}).find('div', {'class': 'wt-mr-xs-1 wt-mr-md-2 wt-mr-lg-3 wt-mr-xl-4'}).find('div', {'class': 'wt}'}).find('div', {'class': 'wt-text-caption wt-line-height-tight wt-break-word wt-mb-xs-0'}).text
#
#         # Append the review to the list
#         reviews_list.append([review_title, review_text, review_date, review_rating, review_author])
#     # Return the list
#     return reviews_list
#
#
# # Set the URL of the shop you want to scrape reviews from
# # url = "https://www.etsy.com/shop/MisterCrafter/reviews"
# url = "https://www.etsy.com/shop/MisterCrafter/reviews"
#
# # Scrape the reviews from the shop
# reviews = scrape_reviews(url)
#
# # Convert the reviews list to a Pandas DataFrame
# reviews_df = pd.DataFrame(reviews, columns=["Title", "Text", "Date", "Rating", "Author"])
#
# # Save the reviews to a CSV file
# reviews_df.to_csv("mistercrafter_reviews.csv", index=False)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ask user which Etsy store they want to scrape.
etsy = input('What is the shop name? ')
driver = webdriver.Chrome('chromedriver')
driver.get("https://www.etsy.com/shop/{}".format(etsy))


# code to get review and put it into a dataframe
def extract_reviews():
    reviews = driver.find_elements(By.XPATH, '//*[@id="REVIEWS"]/div[1]/div/div/div[5]/div/div[1]/div[2]/div/div')
    for review in reviews:
        m = review.find_element(By.XPATH, './/div[@class="quote"]/a')
        print(m.text)


# # get the length of reviews in an Etsy store
# def max_page():
#     # maximum_pages = driver.find_elements_by_xpath('//*[@id="reviews"]/div/div/div[2]/div[4]/nav/ul')
#     numbers = []
#     pages = []
#     for x in maximum_pages:
#         pg = x.text
#         pages.append(pg.split('\n'))
#     for i in pages[0]:
#         if i.isdigit():
#             numbers.append(int(i))
#     return max(numbers)


# clicking next
def click_next():
    element = driver.find_element_by_partial_link_text('Next page')
    element.click()
    driver.implicitly_wait(5)


# pg_length = max_page()
pg_length = 2
review_table = []

for i in range(1, pg_length):
    m = extract_reviews()
    m["page"] = i
    review_table.append(m)
    click_next()
    time.sleep(1)
