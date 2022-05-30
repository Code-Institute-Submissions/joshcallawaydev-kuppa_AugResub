# KUPPA overview

KUPPA is a ecommerce store built with Django.

This is for demonstation purposes only and will be used for my final Code Institute module. This is a public repo so forking and cloning is accepted. Alternatively if you have any suggestions for features and or bug fixes please contact me.

## Additional notes

1) Debug currently set to TRUE
2) add social media login to installed apps via `https://django-allauth.readthedocs.io/en/latest/installation.html`
3) Issue binding port - Authentication and Authorisation functionality - test once deployed
4) do i need a csrf_token for my remove_item function in basket.html

## Table Of Contents

- [User Experiance](#UX)
- [Design](#Design)
- [Technology / Features](#Technology)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credit](#Credit)
- [Future Features](#Features)

## UX

### 1. First time user - as a first time user i would like to

- Understand what the site sells
- Easily navigate to products
- Easily see details for a specific product
- See clear calls to action
- See products for sale
- See some visuals to intise me in
- Easily searh for products

### 2. Returning user - as a returning user i would like to

- Sign up / Register for easy purchasing
- Easily log in
- Have access to my account page
- See the brand contact details
- See the brands socials
- Sort products by price
- Sort products by Name
- Sort products by Category
- See a visual aid that my payment is in process

### 3. Frequent user - as a frequent user i would like to

- See my previous orders
- Delete my account
- Update my profile imformation
- Have my order info pre-populated
- IF ADMIN, have access to add products
- IF ADMIN, have access to edit products
- IF ADMIN, have access to remove products
- IF ADMIN, have access to all orders
- IF ADMIN, have access to an admin panel

## Design

### Strategy

- The site stratigy was to build a product that was free of clutter, leaving customers with an easy to access and easy to understand ecommerce platform for buying coffee and coffee related accessories.

### Scope

- The scope (apps) of the project where as follows

1) Home
2) Products
3) Basket
4) Checkout
5) Accounts

### Structure

- The structure of the ecommerce platform allows customer to easily navigate the site from products to understanding more about the business and its goals. Customers can also easily sign up and save their details making the process as easy and seamless as possible

### Skeleton

- All site functionality is linked around a user and their profile. Customers can buy without signing up but have more functionality and information once they are signed up. All products are grouped by category making it easy for customers to understand their options.

### Surface

- The live site keeps to a minimalistic ethos and colour scheme allowing cusotmers to feel connected to the brand, keeping confusion and complexity away. All functionality leads to products and then to basket and checkout, always allowing customers the option to sign up or sign in to drive more business to KUPPA.

### Color scheme

The color scheme was chosen to match that of the ecommerce platforms main seller - coffee.

1) Main colour - #804102
2) Secondary colour - #fff
3) Tersery colour - #000

### Typography

My primary font was taken from Google fonts (https://fonts.google.com/).

1) Primary font - Poppins
2) Secondary font - Helvetica
3) Tersery font - sans-serif

### Sizing

I chose REM as the primary unit due to its flexability with responsive design. I have also used PX where necessary for absolute sizing.

### Imagery

PLEASE NOTE I DO NOT OWN THE RIGHTS TO THESE IMAGES AND THEY ARE USED FOR DEMONSTRATION PURPOSES ONLY.

Original images were taken from the internet and all links can be found below.

Some images were updated in canva to show the KUPPA logo. Again this is for demo purposes only and would not be used in a real site.

With more time i would add further images to differentiate the products.

[Main KUPPA product image](https://ae01.alicdn.com/kf/HTB16FJ9KFXXXXX6XFXXq6xXFXXXy/20X30cm-Wholesale-StandUp-Blank-brown-Zipper-Kraft-bag-Candy-Coffee-Tea-gift-Kraft-paper-bag-with.jpg)
[Reuable cup image](https://cdn.shopify.com/s/files/1/0196/2708/1828/products/Nought_bamboo_reusable_coffee_cup_with_lid_900x.jpg?v=1566416632)
[Glass image](https://cdn.shopify.com/s/files/1/0051/0417/3144/products/12oz_KeepCup_brew_glass_1500x.jpg?v=1643387103)
[SAge Barista Touch image](https://www.sageappliances.com/content/dam/sage/uk/assets/espresso/finished-goods/bes880/ses880bss2guk1/images/pdp0.jpg.transform/breville-lrg/image.jpg)

### UI / Mockups

See readme > images for detailed list of design / Mockups

[README Images](https://github.com/joshcallawaydev/kuppa/tree/main/README/images)

## Technology

### Languages

- HTML5
- CSS3
- JavaScript (jQuery)
- Python / (Django)
- SQLite

### Frameworks / Features

- Bootstrap
- Google Fonts
- Django
- Jinja
- Balsamiq
- Responsive Design
- Mobile First
- Font Awesome
- Stripe

### Imports / Extras

- asgiref==3.5.0
- black==22.3.0
- click==8.1.3
- Django==3.2
- django-allauth==0.41.0
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- oauthlib==3.2.0
- pathspec==0.9.0
- Pillow==9.1.0
- python-dotenv==0.20.0
- python3-openid==3.2.0
- pytz==2022.1
- requests-oauthlib==1.3.1
- sqlparse==0.4.2
- stripe==3.1.0

- render
- get_object_or_404
- login_required
- messages
- path
- AppConfig
- forms (crispy)
- models
- User
- post_save
- receiver
- session
- CountryField
- path
- HttpResponse
- redirect
- Decimal
- os
- json
- reverse
- require_POST
- Sum
- render_to_string
- csrf_exempt
- Q
- Lower

See requirements.txt for imports and versions

## Testing

Stripe testing was performed in trst dev mode. For card detials please see the documentation using the link below

[Stripe Docs](https://stripe.com/docs/testing)

## Deployment

[Deployment folder](https://github.com/joshcallawaydev/kuppa/tree/main/README/images)

## Credit

## Features

1) add option for changing coffee bag sizes
2) update the inbuilt django widgets to more customizable look and feel
