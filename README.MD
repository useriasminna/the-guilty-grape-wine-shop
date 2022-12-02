# The Guilty Grape - Online Wine Shop
<img src="media/responsive.png" ><br>
<hr>

## Overview
The Guilty Grape is an e-commerce website created for a fictive wine shop located in Dublin, Ireland. The main purpose of the project was to implement a fully functional online store that will make the process of selecting and purchasing wine products much easier for customers.<br>
The users are given the possibility to see every product's details, create a wishlist, add items to the shopping bag, purchase with an online payment and access orders' history. Also, the staff members have permission for controlling the data using specially designed features.<br>
The website was developed using Python(Django), HTML, CSS and JavaScript. The data was stored in a PostgreSQL database using ElephantSql for manipulation.
<br><br>
The fully deployed project can be accessed at [this link](https://the-guilty-grape-wine-shop.herokuapp.com/).<br><br>

## UX
This site was created respecting the Five Planes Of Website Design:<br>
### Strategy<hr>
**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**VIEWING AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to understand the purpose of the website from the first interaction with it content |             
|                                       |1B| As a user, I want to be able to easily use the site functionalities on all viewports, so I can shop the products from any device|
|                                       |1C| As a user, I want to see a footer with relevant information and documents|
|                                       |1D| As a user, I want to be able to access a navigation menu at any time, so I can easily navigate through the website content|
|                                       |1E| As a user, I want to be able search through site products by entering a key word|
|**USER REGISTRATION/AUTENTHICATION**   |  || 
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to confirm my account with an email|
|                                       |2C| As a user/admin, I want to be able to authenticate using only email and password|
|                                       |2D| As a user, I want to be able to reset my password in case I forgot it|
|                                       |2E| As a user/admin, I want to be able to log out at any time|
|**PRODUCTS**                           |  ||
|                                       |3A| US - As a user, I want to see a catalog with all the products and also grouped by categories|
|                                       |3B| US - As a user, I want to be able to apply filters and to sort the listed products, so I can easily find the ones I am interested to buy|
|                                       |3C| US - As a user, I want to be able to see the stock availability for low stock products|
|                                       |3D| US - As a user, I want to see a page with full specifications for every product, so I can easily decide which one I would want to buy|
|                                       |3E| US - As a user, I want to be able to add any product to the shopping bag in a selected quantity|
|                                       |3F| US - As an admin, I want to be able to edit product details|
|                                       |3G|  US - As an admin, I want to be able to delete products from the catalog, so it reflect the existent stock|
|                                       |3H| US - As an admin, I want to be able to add new products to catalog, so it reflects the existent stock|
|**REVIEWS**                            |  ||
|                                       |4A| US - As a user, I want to be able to see all the reviews added for any product, so I can easily make an opinion about its quality|
|                                       |4B| US - As a logged in user, I want to be able to add a review for any product I want|
|                                       |4C| US - As a logged in user, I want to be able to see and edit my reviews added to products|
|                                       |4D| US - As a user, I want to be able to see a general review of every product|
|**WISHLIST**                           |  ||
|                                       |5A| US - As a logged-in user, I want to be able to add/remove any product from the Wishlist|
|                                       |5B| US - As a logged-in user, I want to see all the products added to Wishlist|
|                                       |5C| US - As a logged-in user, I want to be able to apply filters and to sort the products in the Wishlist|
|                                       |5D| US - As a logged-in user, I want to be able to add products to the shopping bag from the Wishlist page|
|                                       |5E| US - As a user, I want to see how many times a product has been added to Wishlist by all the users|        
|**BAG**                                |  ||
|                                       |6A| US - As a user, I want to see all the products I added to the shopping bag|
|                                       |6B| US - As a user, I want to be able to add/remove from the wishlist any product from the shopping bag|
|                                       |6C| US - As a user, I want to see all the details about the price for the order|
|                                       |6D| US - As a user, I want to be able to remove a product from the shopping bag|
|                                       |6E| US - As a user, I want to be able to edit the quantity of the products|
|                                       |6F| US - As a user, I want that all the discounts announced on the website to be applied properly|
|                                       |6G| US - As a user, I want to be able to add my vouchers to the order|
|**CHECKOUT**                           |  ||
|                                       |7A| US - As a logged-in user, I want to be able to see and edit my default delivery details for the order|
|                                       |7B| US- As a user, I want to see the order summary with all the price details|
|                                       |7C| US - As a user, I want to be able to add my delivery details for the order|
|                                       |7D| US - As a user I want to be able to introduce my card details for payment|
|**USER PROFILE**                       |  ||
|                                       |8A| US - As a logged in user, I want to be able to see and edit my delivery details|
|                                       |8B| US - As a logged-in user, I want to be able to see my orders history|
|                                       |8C| US - As a logged-in user, I want to see the full details for every order I placed on the website|
|**ADMIN MANAGE ORDERS**                |  ||
|                                       |9A| US - As an admin, I want to be able to see all the orders placed on the website grouped by date|
|                                       |9B| US -As an admin, I want to be able to filter the orders by date|
|                                       |9C| US -As an admin, I want to see full details of every order placed on the website|
|**NEWSLETTER**                         |  ||
|                                       |10A| US - As a user, I want to be able to subscribe to a newsletter, so I can always be up to date with the latest promotions|


**Project Goal:**<br>
Create a website for the Italianissimo restaurant that is useful for clients and staff members as well.

**Project Objectives:**<br> 
* To create a website with a simple and intuitive User Experience;
* To add content that is relevant and helps create a better image of the restaurant;
* To differentiate between client and staff member accounts;
* To implement fully functional features that will ease the staff members' tasks and upgrade clients' experience with the restaurant services;
* To make the website available and functional on every device.<br><br>

### Scope<hr>
**Simple and intuitive User Experience**<br>
* Ensure the navigation menu is visible and functional at every step;
* Ensure every page has a suggestive name that fits its content;
* Ensure the users will get visual feedback when navigating through pages;
* Create a design that matches the restaurant theme and does not confuse the users.

**Relevant content**<br>
* Add information about restaurant name, location and contact data;
* Make a clear and beautiful designed presentation of the menu elements;
* Create a section with the most ordered dishes;
* Create a section with customer reviews for full transparency.

**Features for upgraded experience**<br>
* Create a Booking feature that allows the users to see all the tables available for a specific date and time:
* Create a Menu feature that displays all the menu information and gives the possibility for the user to mark his favourite dishes;
* Create a Review feature that displays all the reviews added and gives the possibility for the user to add and edit his review;
* Create a Profile page for the user to see his upcoming bookings and favourite meals;
* Create a page for the staff member to manage all the bookings for all the users;

**Different client and staff member Accounts**<br>
* Permit the client to add/edit reviews and the staff member only the option to read them;
* Give the client permission to mark favourite meals and remove the option for staff members;
* Allow access to Profile page only for client type of users;
* Allow access to Manage Bookings page only for staff members type of users;

**Responsiveness**<br>
* Create a responsive design for desktop, tablet and mobile devices.<br><br>

### Structure<hr>
The structure of the website is divided into nine pages but with content depending on authentication and client/staff status <br>
-**Register/Login** pages give the user the possibility to create an account and authenticate for accessing different features.<br>
-**Logout** feature is a modal that helps user exit their current account;<br>
-The **Home** page is visible for both types of users and includes details about the restaurant, most appreciated dishes and top reviews;<br>
-The **Menu** page displays menu details and the "Add to favourite" option only for logged-in clients;<br>
-The **Booking** page is only available for logged-in users, both clients and staff members;<br>
-**Where to find us** contains information visible to all users;<br>
-The **Reviews** page displays all existent reviews and the "Add/Update review" option only for logged-in clients;<br>
-**Profile** page is only visible for the logged-in clients and displays "Upcoming bookings" and "Favourite dishes" sections;<br>
_**Manage Bookings** page gives access only to staff members and displays all the bookings registered, grouped and filtered by day.<br>

* FLOWCHARTS
The Flowchart for my program was created using <b>LucidChart</b> and it visually represents how the system works.<br>
[![N|Solid](static/italianissimo/media/flowchart.png)](static/italianissimo/media/flowchart.png)<br><br>


### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed [here](static/italianissimo/wireframes/wireframes.pdf)<br>

**Database**<br>
The project uses the PostgreSQL relational database for storing the data.<br>
There were created two diagrams to represent the relation between the tables, the initial one and the final one.
The first one was created before the actual development of the website which led to some changes to the attributes and tables for finding the most relevant and useful ones to be kept.

<details>
  <summary>Initial Schema</summary>
<img src="static/italianissimo/media/initial_db.jpeg" ><br>
</details>

<details>
  <summary>Final Schema</summary>
<img src="static/italianissimo/media/final_db.jpeg"><br>
</details><br>

### Surface<hr>
#### Color Scheme
All the colours were selected with the eyedropper plugin from the website cover, to maintain chromatic harmony. <br>
* The primary colour scheme was used for most of the text existent on the website, in either dark or bright colours for creating a good contrast.<br> 
<img src="static/italianissimo/media/clr2.png" width="30%">
<img src="static/italianissimo/media/clr3.png" width="30%">
<img src="static/italianissimo/media/clr4.png" width="30%">
<img src="static/italianissimo/media/clr1.png" width="30%"><br>

* The secondary colour scheme was used for buttons, warnings, errors or for highlighting important information.<br>
<img src="static/italianissimo/media/clr5.png" width="30%">
<img src="static/italianissimo/media/clr6.png" width="30%">
<img src="static/italianissimo/media/clr7.png" width="30%">
<img src="static/italianissimo/media/clr8.png" width="30%">

#### Fonts
* The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>
**Body:** *Tiro Devanagari Marathi, serif*<br>
**Navbar:** *Courgette, cursive*<br>
**Logo:** *Cinzel, serif*<br>
**Slogan:** *Marck Script, cursive*<br>

#### Visual Effects
* **Box shadows** <br>
Multiple box shadows were used for the cover, buttons and images. They were inspired from [css-box-shadow-examples]("https://getcssscan.com/css-box-shadow-examples")<br>
* **Animation**<br>
Some animations were used for creating a dynamic and attractive design
<details>
  <summary>View Moving arrows animation</summary>
<img src="static/italianissimo/media/arrows-capture.gif"><br>
</details>
<details>
  <summary>View Authentication links Pulse animation</summary>
<img src="static/italianissimo/media/pulse-capture.gif"><br>
</details>

* **Hover effects**<br>
<details>
  <summary>View NavBar elements hover</summary>
<img src="static/italianissimo/media/nav-capture.gif"><br>
</details>
<details>
  <summary>View Buttons hover</summary>
<img src="static/italianissimo/media/delete-capture.gif"><br>
</details>
<details>
<summary>View Footer elements hover</summary>
<img src="static/italianissimo/media/footer-capture.gif"><br>
</details><br>

## Agile Methodology
This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [Trello](https://trello.com/). As the user stories were accomplished, they were moved in the Trello board from **To Do**, to **In-Design**, **Testing** and **Done** lists. 
<details>
<summary>Sprints Details</summary>

* **Sprint 1 - SETUP**<br>
    -Setup Django<br>
    -Deploy on heroku<br><br>
* **Sprint 2 - CONTENT AND NAVIGATION**<br>
    -Create a navigation menu<br>
    -Add restaurant name, slogan and description<br>
    -Choose colors, fonts and decorative images <br><br>
    <img src="static/italianissimo/media/sprint2.png"><br><br>
* **Sprint 3 - USER REGISTRATION/AUTENTHICATION**<br>
    -Implement the *Register* page using the django-allauth module<br>
    -Implement the *Login* page using django-allauth module<br>
    -Implement *Logout* modal using django-allauth module<br><br>
    <img src="static/italianissimo/media/sprint3.png"><br><br>
* **Sprint 4 - BOOKING**<br>
    -Create *Booking* page<br>
    -Implement a feature to display available tables<br>
    -Implement booking form validation<br><br>
    <img src="static/italianissimo/media/sprint4.png"><br><br>
* **Sprint 5 - USER PROFILE**<br>
    -Create user *Profile* page<br>
    -Implement *Upcoming bookings* section<br><br>
    <img src="static/italianissimo/media/sprint5.png"><br><br>
* **Sprint 6 - STAFF MANAGE BOOKINGS**<br>
    -Create a *Manage Bookings* page to display all bookings for today<br>
    -Implement filtering by date form<br><br>
    <img src="static/italianissimo/media/sprint6.png"><br><br>
* **Sprint 7 - REVIEWS**<br>
    -Create a *Reviews* page to display all reviews<br>
    -Implement form for adding and updating review<br>
    -Complete *Home* page and add *Top Reviews* section<br><br>
    <img src="static/italianissimo/media/sprint7.png"><br><br>
* **Sprint 8 - MENU**<br>
    -Create a *Menu* page to display menu details<br>
    -Implement a feature for adding meals to favourites<br>
    -Complete the *Profile* page and add the *Favourite dishes* section<br>
    -Complete *Home* page and add *Most appreciated dishes* section<br><br>
    <img src="static/italianissimo/media/sprint8.png"><br><br>
* **Sprint 9 - CONTACT**<br>
    -Create *Where to find us* page<br>
    -Add timetable<br>
    -Add location address and map<br>
    -Add contact details<br><br>
    <img src="static/italianissimo/media/sprint9.png"><br><br>
* **Sprint 10 - TESTING**<br>
    -Create unit tests for Home App<br>
    -Create unit tests for Booking App<br>
    -Create unit tests for Menu App<br>
    -Create unit tests for Reviews App<br>
    -Create unit tests for Contact App<br>
</details><br><br>

## Features
### Existing Features<hr>
#### Create bookings
Every user that is authenticated can access the *Bookings* page for making a reservation. This feature provides a form with multiple sections that appear successively, as steps in completing the booking.
* The first section is for selecting the date and time interval of the booking<br>
    The inputs are validated after the following rules:
    * The Date value should not be less than the current day;<br>
    * For the current day the Start hour can't be less than the current hour;<br>
    * End Hour should be greater than Start hour;<br>
    * Start and End hours must be between 9:00 AM - 11:00;<br><br>
<img src="static/italianissimo/media/booking1.png" width="60%"><br><br>

* The next section appears only if the previous one is valid and it displays the tables existing in the restaurant in the colour that matches their availability status. The user can now choose a table from the dropdown, considering that it only contains the free tables. Also, there is a read-only input with a value that represents the number of seats for each selected table, as an informative element.<br> 
<img src="static/italianissimo/media/booking2.png" width="40%"><br><br>

* Another part of the form is displayed with the contact details to be filled in. A better alternative available for the users that are not staff members is to check the *Book it on my name* option. This means that the form will automatically register the authenticated user's name and email as contact details.<br>
<img src="static/italianissimo/media/booking3.png" width="40%"><br><br>

* The last section contains an overview of the booking. If the reservation is submitted, a success message will appear
<img src="static/italianissimo/media/booking4.png" width="60%"><br><br>
<img src="static/italianissimo/media/booking5.png" width="40%"><br><br>

#### Reviews
* On the *Reviews page* there is a list of all the reviews posted on the website and it is visible to all types of users. All the reviews have the same design and type of content. Important details are displayed such as *Name*, *Date and time*, *Stars rating* and the *Message* posted.<br>
<img src="static/italianissimo/media/reviews1.png" width="60%"><br><br>

* When a user is authenticated and he never posted a review, a form is provided for leaving a message and a star rating.<br>
<img src="static/italianissimo/media/reviews2.png" width="40%"><br><br>

* For authenticated users that already posted a review, the page displays the values of their review and the possibility to update it.<br>
The form for editing the review already contains the corresponding message value and the star ratings in the initial state.<br>
<img src="static/italianissimo/media/reviews3.png" width="40%"><br><br>
<img src="static/italianissimo/media/reviews4.png" width="40%"><br><br>


#### Menu 
* On the *Menu* page there is a list with all the menu elements. Every item represents a meal with details such as *Name*, *Image*, *Price*, and Ingredients. The list design is simple and attractive.<br>
<img src="static/italianissimo/media/menu1.png" width="70%"><br><br>

* An interactive feature has been added that is only available for logged-in users that are not staff members. A user has the possibility to mark his favourite meals through a form that uses a heart icon as a button. The heart shape defines the state of the meal, which can be marked or unmarked as a favourite dish.<br>
<img src="static/italianissimo/media/menu2.png" width="30%">
<img src="static/italianissimo/media/menu3.png" width="30%"><br><br>

#### Profiles
The users' accounts have been created using the **django allauth** module. This way, information about the current user can be accessed from the template and displayed for confirming that the authentication was successful.<br>
Considering that the website is created for a restaurant, the profile of the user is created to display essential information such as name and email.<br>
<img src="static/italianissimo/media/profile1.png"><br><br>
Also, the profile page contains two features that are created for giving the user a better experience with the website.<br><br>
* One of the features is called **Your upcoming bookings** and is represented by a list of the bookings created by the currently authenticated user.<br>
Every booking has a visual representation of a note with the details of the reservation written on it. <br>
<img src="static/italianissimo/media/profile2.png"><br><br>
Also, for giving the user the ability to manage his bookings, every element in the list comes with a *Delete Booking* button.<br>
The button triggers a modal for confirmation, that being a part of the defensive programming.<br>
<img src="static/italianissimo/media/profile3.png"><br><br>

* Another user-friendly feature is **Your favourite dishes**. This feature displays to the user all the meals that he has added to *Favourites* from the *Menu* page. The menu items contain the meal image and name, as it was not considered necessary to display all the details from the menu.<br>
<img src="static/italianissimo/media/profile4.png"><br><br>

#### Staff bookings management
The staff account was created as a superuser account from the terminal and also has access to the admin panel.<br>
There is a page created especially for staff members to keep a better tracking of all the reservations that are being made for the restaurant.<br>
* The bookings are displayed on a custom-designed table, grouped by day and ordered by time. The page renders by default the reservations for the current day and their number.<br>
* A form is provided for filtering the bookings by date for a better user experience.<br>
* A booking also has a delete button that triggers a confirmation modal. <br>

<img src="static/italianissimo/media/staff1.png" width="80%"><br><br>
<img src="static/italianissimo/media/staff2.png" width="50%"><br><br>

* If the bookings list is empty, a suggestive message is displayed.<br>
<img src="static/italianissimo/media/staff3.png" width="50%"><br><br>


### Future Feature Considerations<hr>
* Updating the booking feature with a more complex algorithm and design for generating the available tables. The current algorithm sets a table as *busy* even if it is registered as booked only for a small part of the interval requested by the user for the reservation. Also, the Start and End time are restricted to accept only zero hundred hours. By changing the limit to even zero-thirty hours, the tables algorithm will be more efficient.

* Another possible feature would be the implementation of a *Reward system*. Every time a client leaves a good review, a discount would appear on his profile page to use on his next visit. Also, a user should be given the status of *Loyal customer* when he registers on a system every time he eats at Italianissimo if that happens regularly. Different discounts should apply to loyal customers in order to recompensate and encourage their habit.  

## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints. For intermediate devices where the design didn't fit accordingly, custom breakpoints were used.

**Breakpoints:**

    - max-width:280px
    - max-width:768px
    - max-width:992px
    - max-width:1024px

**Tested devices:**

    - Moto G4 
    - iPhone SE 
    - iPhone XR 
    - iPhone 11 
    - iPhone 13
    - iPhone 5/SE 
    - iPhone 6/7/8 
    - Ipad
    - Ipad Air 
    - Ipad Mini
    - Ipad Pro 
    - Pixel 5 
    - Surface Duo 
    - Surface Pro 7 
    - Nest Hub 
    - Nest Hub Max
    - Samsung Galaxy S20 Ultra 
    - Samsung Galaxy S8 
    - Galaxy Note 2 
    - Galaxy Tab S4
    - Asus Vivobook

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Visual Studio](https://code.visualstudio.com/) - for writing and testing the code<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[TablePlus](https://tableplus.com/) - for managing the database entries<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[LucidChart](https://www.lucidchart.com/) - used for creating the Flowchart and Database relational schema<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Diffchecker](https://www.diffchecker.com/) - used for comparing the code<br>
[TinyPNG](https://tinypng.com/) - for compressing the images<br>
[Grammarly](https://app.grammarly.com/) - for correcting text content<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[Cloudinary](https://cloudinary.com/) - for storing static data<br>
LightHouse - for testing performance<br>

### Python packages

* django 
* gunicorn 
* dj-database-url
* psycopg2
* dj3-cloudinary-storage 
* pylint-django 
* whitenoise
* jinja2 
* django-allauth
* django-crispy-forms 
* django-braces 
* django-filter
* django-annoying 
* coverage
* pylint 
* python-dotenv 
* dateutils 
* autopep8

## Testing
The testing documentation can be found at [TESTING.MD](TESTING.MD)

## Deployment

### Deploy on Heroku
 1. Create Pipfile 
 
 In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all requirements will be created. 
 
 2. Setting up Heroku

    * Go to the Heroku website (https://www.heroku.com/) 
    * Login to Heroku and choose *Create App* 
    * Click *New* and *Create a new app*
    * Choose a name and select your location
    * Go to the *Resources* tab 
    * From the Resources list select *Heroku Postgres*
    * Navigate to the *Deploy* tab
    * Click on *Connect to Github* and search for your repository
    * Navigate to the *Settings* tab
    * Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    

3. Deployment on Heroku

    * Go to the Deploy tab.
    * Choose the main branch for deploying and enable automatic deployment 
    * Select manual deploy for building the App 
    
### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [My Repository Page](https://github.com/useriasminna/italianissimo-booking-website), press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
- On [My Repository Page](https://github.com/useriasminna/italianissimo-booking-website), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created
<hr>

## Credits
### Content
* The content of the website is fictive. 
### Media
* All .png images used on the site were taken from [pngegg](https://www.pngegg.com/)
### Code
* The code for creating a custom user model was taken and adapted from [here](https://www.codingforentrepreneurs.com/blog/
how-to-create-a-custom-django-user-model/)
* The validation for the booking form was inspired from [here](https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/)
* The method of inserting data into HTML for javascript was inspired from [here](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/)
* Django pagination was taken and adapted from [here](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)
* Pagination with a query set was inspired from [stackoverflow](https://stackoverflow.com/questions/68155106/filter-class-based-view-listview-that-has-pagination)
* Custom arrows for input type number were taken and adapted from [stackoverflow](https://stackoverflow.com/questions/63544101/customize-increment-arrows-on-input-of-type-number-using-css)

## Acknowledgements
- Code Institute for all the material and support offered<br>
- My mentor Ben Kavanagh for great tips and his willingness to help me as much as possible with the problems encountered during the development of the project<br>
- Slack community for great involvement in helping each other<br>
<hr>