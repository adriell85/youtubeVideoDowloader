from selenium import webdriver
import json, time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_video_results():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
    driver.get('https://www.youtube.com/results?search_query=carro')

    youtube_data = []

    # scrolling to the end of the page
    # https://stackoverflow.com/a/57076690/15164646
    while True:
        # end_result = "No more results" string at the bottom of the page
        # this will be used to break out of the while loop
        end_result = driver.findElement(By.cssSelector(('#message').is_displayed()))
        # end_result = driver.find_element_by_css_selecto('#message').is_displayed()
        driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        # time.sleep(1) # could be removed
        print(end_result)

        # once element is located, break out of the loop
        if end_result == True:
            break

    print('Extracting results. It might take a while...')

    for result in driver.find_elements_by_css_selector('.text-wrapper.style-scope.ytd-video-renderer'):
        title = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer').text
        link = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
        channel_name = result.find_element_by_css_selector('.long-byline').text
        channel_link = result.find_element_by_css_selector('#text > a').get_attribute('href')
        views = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[0]

        try:
            time_published = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[1]
        except:
            time_published = None

        try:
            snippet = result.find_element_by_css_selector('.metadata-snippet-container').text
        except:
            snippet = None

        try:
            if result.find_element_by_css_selector('#channel-name .ytd-badge-supported-renderer') is not None:
                verified_badge = True
            else:
                verified_badge = False
        except:
            verified_badge = None

        try:
            extensions = result.find_element_by_css_selector('#badges .ytd-badge-supported-renderer').text
        except:
            extensions = None
        print(verified_badge)

        youtube_data.append({
            'title': title,
            'link': link,
            'channel': {'channel_name': channel_name, 'channel_link': channel_link},
            'views': views,
            'time_published': time_published,
            'snippet': snippet,
            'verified_badge': verified_badge,
            'extensions': extensions,
        })

    print(json.dumps(youtube_data, indent=2, ensure_ascii=False))

    driver.quit()

get_video_results()


# part of the output:
'''
[
  {
    "title": "I Survived 100 Days in Ancient Greece on Minecraft.. Here's What Happened..",
    "link": "https://www.youtube.com/watch?v=hUAjdnhpTXU",
    "channel": {
      "channel_name": "Forrestbono",
      "channel_link": "https://www.youtube.com/user/ForrestboneMC"
    },
    "views": "2.6M views",
    "time_published": "5 days ago",
    "snippet": "I had to survive for 100 Days of Hardcore Minecraft in Ancient Greece and battle Poseidon, God of the Sea, and Cronos, the God ...",
    "verified_badge": true,
    "extensions": "New"
  }
]
'''