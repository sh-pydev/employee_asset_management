# Employee asset management system
This app tracks the devices a company is giving to their employees. The functionality is as follows: First, you have to register on the web application on hehalf of a company. You have to provide your company name with no spaces, company e-mail and a password for security parpose. The company name can be resolved with dashes or underscores (ex: The_Food_Company). After sigining in, you can make a list of your available assets/gadgets/devices that you want to give to your employees. Let's say you want to provide laptops, mobile phones and tablets to your employees. So the available asset for you is Mobile phone, Tablet, and Laptop. You just have to enter the genre of your available device. It will automatically be saved to the database having a underlying link to your company. You can also delete any asset genre if you want. You can change the genre name as well.

Then you have another option to add your employees. You have to provide an unique ID for each of your employee. Along with the ID, You can store their name as well. The employee list will be saved with a link to your company and no other person can see the list of your employees. This applies for the available assets as well.

The last thing you can do is , you can assign assets to your employees. You can assign no device at all for any particular employee. Also you can assign one or more than one device for each of them. You can search employees by their ID and can see which or how many devices they have been given. You can save the issue date and return date for each  assignment. Also you can save a log of the condition of devices. In which state device is given and in which state the device is returned. You can also delete any instance if you want.

For registration, login, and logout, the knox library has been used. It is a third party library for django rest framework to solve the authentication and authorization process. It works on token based system and you have to pass your unique token along with your request on every move you make. The backend is made with django and used api framework is django rest framework. Django-filters is used to search employees in the "given asset" section. For testing purpose, sqlite database is used in this project.

#The available endpoints are:

/api/login/

/api/register/

/api/logout/

/api/asset/

/api/asset/<<int:pk>>

/api/employee/

/api/employee/<<int:pk>>

/api/given_asset/

/api/given_asset/<<int:pk>>
