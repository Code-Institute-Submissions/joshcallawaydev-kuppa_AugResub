# Testing

All testing was performed to ensure a robust and reliable product and is crucial to a project delivery.

Below is the testing performed on this project. Testing was compiled throughout the project in effort to minimise bugs and styling issues.

# Table of contents

* [User stories](#User-stories)
* [Dev Tools Testing](#Dev-Tools-Testing)
* [Validators](#Validators)
* [Other testing](#Other)

# User stories

### 1. First time user - as a first time user i would like to

Understand what the site sells
![Understand what the site sells](./images/test_images/image_1.png)

Easily navigate to products
![Navigation](./images/test_images/image_4.png)

Easily see details for a specific product
![Product Details](./images/test_images/image_3.png)

See clear calls to action
![Call to action](./images/test_images/image_2.png)

See products for sale
![All products page](./images/test_images/image_5.png)

See some visuals
![Home page images](./images/test_images/image_6.png)

Easily search for products
![Search Bar](./images/test_images/image_8.png)

### 2. Returning user - as a returning user i would like to

Sign up / Register for easy purchasing
![Links to sign up](./images/test_images/image_9.png)

Easily log in to accounts
![Link to login](./images/test_images/image_9.png)

Have access to my account page
![Account page](./images/test_images/image_10.png)

See the brand contact details
![Footer](./images/test_images/image_11.png)

See the brands socials
![Footer](./images/test_images/image_11.png)

Sort products by price
![Sort by price](./images/test_images/image_12.png)

Sort products by Name
![Sort by Name](./images/test_images/image_12.png)

Sort products by Category
![Sort by category](./images/test_images/image_12.png)

Sort products by Rating
![Sort by rating](./images/test_images/image_12.png)

See a visual aid that my payment is in process
![Processing screen](./images/test_images/image_13.png)

### 3. Frequent user - as a frequent user i would like to

See my previous orders
![My account](./images/test_images/image_14.png)

Update my profile imformation
![Account page](./images/test_images/image_14.png)

Have my order info pre-populated
![Checkour form](./images/test_images/image_15.png)

IF ADMIN, have access to add products
![Add products](./images/test_images/image_16.png)

IF ADMIN, have access to edit products
![Edit products](./images/test_images/image_16.png)

IF ADMIN, have access to remove products
![Delete products](./images/test_images/image_16.png)

IF ADMIN, have access to all orders
![Admin panel](./images/test_images/image_17.png)

IF ADMIN, have access to an admin panel
![Admin panel](./images/test_images/image_17.png)

# Dev Tools Testing

Lighthouse
![Chrome lighthouse](./images/test_images/image_21.png)
Cross browser
Firefox
![Firefox](./images/test_images/firefox.png)
Responsiveness
![Responsive testing](./images/test_images/responsive.png)
![Responsive testing](./images/test_images/responsive2.png)
Some issues at small screen sizes on the add product page however this i am happy with as these features, including admin dashboard would be mainly desktop use i believe. - I have sliced text to fix this issue partially.

# Validators

HTML

All pages tested and only jinja templating returning bad values.

![account.html](./images/test_images/accounthtml.png)
![basket.html](./images/test_images/baskethtml.png)
![checkout.html](./images/test_images/checkouthtml.png)
![checkout_complete.html](./images/test_images/checkout_completehtml.png)
![checkout_complete.html](./images/test_images/checkout_completehtml.png)
![index.html](./images/test_images/indexhtml.png)
It states to use H2-H6 tags however i have a good use of H1, H3 and H4 tags in this document. It is also worth noting that its an extention of the base template which too has its own headers which this validator will not be factoring.
![privacy html](./images/test_images/privacyhtml.png)
Please note this pages is not finished but were added to imporve the sites validity.
![terms html](./images/test_images/termshtml.png)
Please note this pages is not finished but were added to imporve the sites validity.
![add products pagehtml](./images/test_images/add_productshtml.png)
![all products html](./images/test_images/all_productshtml.png)
Warning all related to jinja templating as per all other pages
![edit products html](./images/test_images/edit_productshtml.png)
![products details html](./images/test_images/product_deetshtml.png)
![main nav html](./images/test_images/mainnav.png)
![mobile top html](./images/test_images/mobiletop.png)
![base html](./images/test_images/base.png)

CSS

![Checkout css](./images/test_images/checkoutcss.png)
![base css](./images/test_images/basecss.png)

JS - beautifytools

![JS testing](./images/test_images/jstest.png)

Python

All python has been fomratted with Black, Autopep8 and Pylance to ensure PEP8 standard where possible.

### Navigation

All navigation was tested, both mobile and large viewports
![Nav testing](./images/test_images/image_22.png)

### Products

All links and images tested on products
![Products testing](./images/test_images/image_23.png)

### Basket

All basket functionality and sums tested
![Basket testing](./images/test_images/image_24.png)

### Checkout / Payments

All checkout links functionality and payment tested
![Checkout and form testing](./images/test_images/image_25.png)
![Payment testing](./images/test_images/image_26.png)

### Account

All account functionality and links tested
![Account](./images/test_images/image_27.png)
![Past purchases](./images/test_images/image_28.png)

### Product Management

All product management tested
![Delete product](./images/test_images/image_29.png)
![Edit / Add product](./images/test_images/image_30.png)

### Other Images

Favicon wouldnt load
![No Favicon](./images/test_images/favicon.png)
Images Wouldnt Render
![No Images Rendering](./images/test_images/norender.png)
Search bar issue
![Search issues](./images/test_images/image_7.png)
Testing the buttons
![Button and network tab](./images/test_images/image_18.png)
Testing the links
![Links and network tab](./images/test_images/image_19.png)
Testing the links
![Testing basket as anonamous user and logged in user](./images/test_images/image_20.png)
Form name field
![Form name field](./images/test_images/formname.png)
Leaving name field blank on populated form to add level of checking to customer
Securuty / Authentication
![Securuty / Authentication](./images/test_images/security.png)

With more time i would like to have used automated testing more. The testing was thorough but more automated testing would be better for robustness.
