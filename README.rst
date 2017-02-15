Goal and Prehistory
===================

How you can know Walmart API provides to get only 5 reviews. I needed to get all reviews was related to specific item. And I wrote a little parser.

How to install
==============
It's easy:
::
    pip install walmart-reviews

Structure
=========

Function reviews returns a dictionary which can be transform in json. The structure is next:
::
        'product_id': product_id,               # Product ID
        'product_name': product_name,           # Product name
        'product_reviews_list': reviews_list    # List with reviews: [{...}, {...}, ..., {...}]

Every review is presented like dictionary:
::
        'review_title': review_title,                   # Review title
        'review_date': review_date,                     # Review posted date
        'review_rating': review_rating,                 # Product's rating was evaluated by the reviewer
        'review_text': review_text,                     # Review text
        'review_helpful_yes': review_helpful_yes,       # Amount of positive voices about review's usefulness
        'review_helpful_no': review_helpful_no,         # Amount of negative voices about review's usefulness
        'reviewer_name': reviewer_name,                 # Reviewer's name
        'reviewer_location': reviewer_location,         # Reviewer's location
        'reviewer_attributes': reviewer_attributes,     # List with reviewer's attributes such as ages, gender and etc. (if it is pointed)
        'is_reviewer_verified': is_reviewer_verified,   # When the reviewer is verified it returns "Yes", else - "No"
        'reviewer_top_list': reviewer_top_list          # Returns list with all reviewer's TOPs (if reviewer is TOP's participant)

How to use
==========

Example:
::
    from wlmrt.review import reviews
    rws = reviews(10811473)
    for i in rws['product_reviews_list']:
        print(i)

You will get
::
    {'review_title': 'Great product', 'review_date': '1/26/2017', 'review_rating': '5.0', 'review_text': "Ordered item online and received it a day later. \nI ordered this size as many of the other reviews mentioned that they could not purchase the liners in store for the other sizes.\n\nAfter receiving the litter pan I went to Walmart to purchase the liners and also found that the store I went too also had all the other sizes of liners too so those reviews were not helpful...\n\nOverall my two over weight cats like the box and so far so good. I took the door off so they would get used to going in and out. Smell seems to be controlled too. I may buy another for the price you can't beat it.", 'review_helpful_yes': 'None', 'review_helpful_no': 'None', 'reviewer_name': 'Bakes14', 'reviewer_location': 'Clarington, Ontario, Canada', 'reviewer_attributes': [{'Recommend': 'Yes'}], 'is_reviewer_verified': 'Yes', 'reviewer_top_list': []}
    {'review_title': 'Extreme Upgrade!', 'review_date': '1/2/2017', ...
    ...

In brackets you need to paste the product's id. Product's id is a number in the link.
For https://www.walmart.com/ip/Large-Enclosed-Cat-Pan-Colors-May-Vary-Cats/10811473 the id is 10811473

You can use package in 2 mode: with log and without log.
Calling with log:
::
    from wlmrt.review import reviews
    rws = reviews(10811473, 'log')
    for i in rws['product_reviews_list']:
        print(i)
When mode 'log' is turned on you can see the log of parsing process:
::
    Product link: https://www.walmart.com/reviews/product/10811473
    Count of page(s) with review(s) 15
    Page #1. Count of parsed reviews in overall: 20
    Page #2. Count of parsed reviews in overall: 40
    ...
    Page #15. Count of parsed reviews in overall: 289
    System date:  2017-02-15 12:40:10

P.S.
====

Thank you for reading and using the package. I wait your suggestions how to improve the package.