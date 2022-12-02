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
Create an e-commerce application for The Guilty Grape wine shop that is useful for clients and staff members as well.

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
* Create a design that matches the requirements of an e-commerce website.

**Relevant content**<br>
* Add a representative cover image;
* Add the website title and details about its purpose;
* Add a section that includes information about the shop's name, description, location and contact data;
* Make a clear and beautiful designed presentation of the menu elements;

**Features for upgraded experience**<br>
* Create a list with all the products and group them by category;
* Create a Bag feature that allows the user to add, update and remove products from the shopping bag;
* Create a Wishlist feature that gives the user the possibility to add and remove items from the wishlist;
* Create a Review feature that displays all the reviews added for a product and allows the user to add and edit his review;
* Create a Checkout feature for giving the user the possibility to complete an order on the website;
* Create a Profile page for the user to add/update his delivery details and see his orders' history;
* Create a Newsletter feature that allows the user to subscribe with his email;
* Create a Voucher feature that offers the user a dicount code on account registration;
* Create a page for the staff members to manage all the orders for all the users;
* Create a feature for the staff members to add/edit products on the website;


**Different client and staff member Accounts**<br>
* Allow the clients to add/edit reviews and the staff members only the option to read them;
* Give the client permission to add/remove products from wishlist and remove the feature for staff members;
* Only guest and client users to access the shopping bag and its features;
* Only guest and client users can make an order on the website;
* Give permission only for staff members to add/edit products; 
* Allow access to Profile page only for clients users;
* Allow access to Wishlist page only for clients users;
* Allow access to Orders page only for staff member users;

**Responsiveness**<br>
* Create a responsive design for desktop, tablet and mobile devices.<br><br>
