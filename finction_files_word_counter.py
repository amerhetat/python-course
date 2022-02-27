
def wcounter(text):
    words_list = text.split()
    # print(words_list)
    n = len(words_list)
    return n

def ccounter(text):

    # print(words_list)
    n = len(text)
    return n
def text_extractor(url, css_selector):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag = soup.select(css_selector)

    text1 = tag[0].get_text()
    return text1
