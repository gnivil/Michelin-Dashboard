#create empty lists for each star level
michelin_links = {}
url_1stars = []
url_2stars = []
url_3stars = []
#establish dynamic urls for each star level
for star in range(1, 4):
    if star == 1:
        url = f"https://guide.michelin.com/en/restaurants/1-star-michelin/"
    else:
        url = f"https://guide.michelin.com/en/restaurants/{star}-stars-michelin/"
    #get the last page number because 1 2 and 3 star distinctions have different amount of pages
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('ul', class_='pagination')
    last_page_number = int(pages.find_all('li')[-2].text)
    print(url)
    #looping through all the pages until last page number
    for page_number in range(1, last_page_number+1):
        page_url= url+'page/'+str(page_number)
        print(page_url)
        browser.visit(page_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        anchors= soup.find_all('a',class_='link')
        #append urls into lists
        for i, anchor in enumerate(soup.find_all('a',class_='link')):
            if (i == 0) and (page_number == 1):
                michelin_links[f'Michelin star: {star} links'] = ['https://guide.michelin.com/'+anchor['href']]
            else:
                michelin_links[f'Michelin star: {star} links'].append('https://guide.michelin.com/'+anchor['href'])