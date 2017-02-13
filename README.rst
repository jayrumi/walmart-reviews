Goal and Prehistory
===================

How you can know Walmart API provides to get only 5 reviews. I needed to get all reviews was related to specific item. And I wrote a little parser.

How to install
==============


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
