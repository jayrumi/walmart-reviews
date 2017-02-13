from random import randint
import requests
from lxml import html
import datetime
import time

def reviews(in_product_id, *arg):

    product_id = str(in_product_id)

    try:
        if str(arg[0]).lower() == 'log':
            log = 1
        else:
            log = 0
    except:
        log = 0


    gen_headers = str(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/' + str(
            randint(1, 42)) + '.0.' + str(randint(1, 2311)) + '.' + str(randint(1, 90)) + ' Safari/' + str(
            randint(100, 537)) + '.' + str(randint(1, 36)))
    in_headers = {'User-Agent': gen_headers}

    walmart_url = str('https://www.walmart.com/reviews/product/' + product_id)
    page = requests.get(walmart_url, headers=in_headers).text

    if log == 1:
        print("Product link:", walmart_url)

    parser = html.fromstring(page)

    XPATH_PRODUCT_NAME = '//div[@class="Grid review-product-header hide-content display-inline-block-m"]/div/div/div/h2/a/text()'
    product_name = parser.xpath(XPATH_PRODUCT_NAME)[0]

    countPagesList = []
    for cnt in parser.xpath('//div[@class="js-review-pagination-bottom"]/div[@class ="review-pagination js-review-pagination hide-content display-inline-block-m"]/div/ul/li/a/text()'):
        countPagesList.append(cnt)

    try:
        pageCounter = int(countPagesList[-1])
    except:
        pageCounter = 1

    if log == 1:
        print("Count of page(s) with review(s)", str(pageCounter))

    reviews_list = []

    for pg_counter in range(pageCounter):

        walmart_url = str('https://www.walmart.com/reviews/product/' + product_id + '?limit=20&page=' + str(pg_counter + 1) + '&sort=relevancy')
        page = requests.get(walmart_url, headers=in_headers).text
        parser = html.fromstring(page)

        XPATH_REVIEW_LIST = '//div[@class="js-review-list"]/div'
        page_review_list = parser.xpath(XPATH_REVIEW_LIST)

        for review in page_review_list:

            try:
                review_title = review.xpath(
                    './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="Grid"]/div/text()')[0]
            except:
                review_title = 'None'
            #print('review_title:', review_title)

            try:
                review_date = review.xpath(
                    './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="Grid"]/span/text()')[0]
            except:
                review_date = 'None'
            #print('review_date:', review_date)

            try:
                review_rating = str(review.xpath(
                    './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="stars customer-stars"]/span[@class="visuallyhidden"]/text()')[0]).replace(' stars', '')
            except:
                review_rating = 'None'
            #print('review_rating:', review_rating)

            try:
                reviewer_name = review.xpath(
                    './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="stars customer-stars"]/span[@class="customer-name hide-content display-inline-block-m"]/span/text()')[0]
            except:
                reviewer_name = 'None'
            #print('reviewer_name:', reviewer_name)

            try:
                review_text = review.xpath(
                    './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="customer-review-text"]/p/text()')[0]
            except:
                review_text = 'None'
            #print('review_text:', review_text)

            try:
                review_helpful_yes = review.xpath(
                    './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="btn-vote-group js-btn-vote-group customer-review-voting hide-content display-inline-block-m"]/span/span[@class="js-vote-positive-count"]/text()')[0]
            except:
                review_helpful_yes = 'None'
            #print('review_helpful_yes:', review_helpful_yes)

            try:
                review_helpful_no = review.xpath(
                    './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="btn-vote-group js-btn-vote-group customer-review-voting hide-content display-inline-block-m"]/span/span[@class="js-vote-negative-count"]/text()')[0]
            except:
                review_helpful_no = 'None'
            #print('review_helpful_no:', review_helpful_no)

            try:
                reviewer_location = review.xpath(
                    './/div[@class="Grid-col u-size-3-12-m customer-info hide-content display-inline-block-m"]/div[@class="customer-location"]/text()')[0]
            except:
                reviewer_location = 'None'
            #print('reviewer_location:', reviewer_location)

            reviewer_attributes = []
            for attr in review.xpath(
                    './/div[@class="Grid-col u-size-3-12-m customer-info hide-content display-inline-block-m"]/div[@class="customer-attributes"]/div'):
                #print(attr.xpath('text()'), attr.xpath('span/text()'))
                attr_dict = {}
                attr_dict[str(attr.xpath('text()')[0]).replace('Would recommend to a friend?\n              ', 'Recommend').replace(':', '')] = attr.xpath('span/text()')[0]
                reviewer_attributes.append(attr_dict)
            #print(reviewer_attributes)

            if len(review.xpath(
                './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="hide-content-m"]/div/div/div/a/text()')) > 0:
                is_reviewer_verified = 'Yes'
            else:
                is_reviewer_verified = 'No'
            #print('is_reviewer_verified:', is_reviewer_verified)

            reviewer_top_list = []

            reviewer_top_list_raw = review.xpath(
                './/div[@class="Grid-col u-size-8-12-m js-customer-review-body customer-review-body"]/div[@class="hide-content-m"]/div/div/div/text()')
            try:
                for i in reviewer_top_list_raw:
                    if i.find('        ') > 0:
                        None
                    else:
                        reviewer_top_list.append(i)
            except:
                None

            #print(is_reviewer_verified, reviewer_top_list)

            review_dictionary = {
                'review_title': review_title,
                'review_date': review_date,
                'review_rating': review_rating,
                'review_text': review_text,
                'review_helpful_yes': review_helpful_yes,
                'review_helpful_no': review_helpful_no,
                'reviewer_name': reviewer_name,
                'reviewer_location': reviewer_location,
                'reviewer_attributes': reviewer_attributes,
                'is_reviewer_verified': is_reviewer_verified,
                'reviewer_top_list': reviewer_top_list
            }

            reviews_list.append(review_dictionary)
        if log == 1:
            print("Page #" + str(pg_counter + 1) + ". Count of parsed reviews in overall:", str(len(reviews_list)))
    #print(reviews_list)

    product_dictionary = {
        'product_id': product_id,
        'product_name': product_name,
        'product_reviews_list': reviews_list
    }

    ts = time.time()
    if log == 1:
        print("System date: ", str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')), "\n")

    return(product_dictionary)
