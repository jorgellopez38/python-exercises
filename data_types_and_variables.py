# EXERCISES

99.9       # Float
"False"    # String
False      # Boolean
'0'        # Integer
True       # Bool
'True'     # String
[{}]       # List
{'a': []}  # Dictionary

### What data type would best represent:


#### A term or phrase typed into a search box?
- string
#### If a user is logged in?
- boolean
#### A discount amount to apply to a user's shopping cart?
- integer
#### Whether or not a coupon code is valid?
- boolean
#### An email address typed into a registration form
- string
#### The price of a product?
- float
#### A Matrix?
- list
#### The email addresses collected from a registration form?
- dictionary
#### Information about applicants to Codeup's data science program?
- dictionary

facebook_pay = 350*10
google_pay = 400*6
amazon_pay = 380*4
weekly_pay = facebook_pay + google_pay + amazon_pay
weekly_pay

class_is_not_full = True
schedule_does_not_conflict = True
enroll = class_is_not_full and schedule_does_not_conflict
enroll

purchase_more_than_two = True
product_is_not_expired = True
premium_membership = False
discount_eligible = product_is_not_expired and (purchase_more_than_two or premium_membership)
discount_eligible

my_username = 'batmaniscool'
my_password = 'batmasiscool123'

check_1 = len(my_password) >= 5
check_2 = len(my_username) <= 20
check_3 = my_username != my_password
check_3
no_whitespace_username = not(my_username.startswith(' ') or my_username [-1] == ' ')
no_whitespace_password = not(my_password.startswith(' ') or my_password [-1] == ' ')
user_and_pass_valid = no_whitespace_username and no_whitespace_password
user_and_pass_valid

