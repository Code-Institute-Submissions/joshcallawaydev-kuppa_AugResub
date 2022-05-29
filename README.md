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

- understand what the site sells
- easily navigate the site
- See products for sale
- See some visuals to intise me in
- Easily searh for products

### 2. Returning user - as a returning user i would like to

- Sign up / Register for easy purchasing
- Have access to my account page
- See the brand contact details
- See the brands socials

### 3. Frequent user - as a frequent user i would like to

- See my previous orders
- Delete my account
- Update my profile imformation
- IF ADMIN, have access to add / remove products
- IF ADMIN, have access to all orders and admin panel

## Design

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

TBA

### UI / Mockups

TBA - ![text](./link)

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

## Testing

## Deployment

## Credit

## Features

1) add option for changing coffee bag sizes
2) update the inbuilt django widgets to more customizable look and feel
