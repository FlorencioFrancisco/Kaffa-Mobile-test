# Kaffa-Mobile-test
This repository contains exercises of the Kaffa's pre-qualification test for Software Developer recruitment process.

# Instructions
For all Exercices python 3> is required. All exercises except 5 are CLI applications and can bu reun by calling {python file_path/file_name.py} in the command prompt.
For Exercice 5, 6 and 7 the pakedges Flask, pandas and requests are required, so make sure to install then with {pip install packedge_name}.

# Instructions for Exercise 5
To run this web app you will need node.js installed in your machine. After installing node a restart is required.
First extract the files from to-do-list.rar inside the Exercise 5 folder.
Run the TodoListAPI.py file to start the server, the REST API will be available in "localhost:5000".
Then inside the to-do-list folder run the command {npm start} to start the react application, the app will be available in "localhost:3000"
Make sure your browse allows CORS, for this I'm using the following Chrome extension: https://mybrowseraddon.com/access-control-allow-origin.html

# Exercise 1
To validate the CNPJ format is checked if all characters are numeric and lenth is 14 or lenth is 18 and the special non-numeric characters are the right ones in the right position.

# Exercise 2
To validate if the CNPJ exists we utlize the first 12 digits to calculate the first verification digit and then the first 13 digits to get the last digit. To make this calculus we use the inverse sequence of numbers multiplied by an infinete sequence of 2 to 9 then sum all the products and apply modulus of 11 subtract the result from 11 and get the last digit of the result number.
If the calculated verifications digits doesn't match with the given ones, the CNPJ is incorrect.

# Exercise 3
First its necessary to transform the input in the format "(x1, y1; x2, y2)" into an 2d array.
Then to verify if two retangles intersect is required to check for each vertex of one of then if it's x value is between the other retangle x1 and x2 values and the same for y.

# Exercise 4
To get the area of intersection of two retangles its required to find the retangle of intersection that is created by the vertex of retangle A that is inside retangle B and the vertex of retangle B that is inside retangle A.
After getting the intersection retangle we calculate it's side and height by subtracting the x value of the vertex with the smaller x from the the vertex with the greater x and the same for y, this part is important otherwise you may get a negative area.
Then the area is equal to side+1 * height+1 becuse the vertex have an area of 1. 

# Exercise 5
In this exercice its created an to do list react app with a todoList component that get the items of the to do list from an A Rest API and crate a todoItem for each of then. The todoItem component displays the to do item text and a botton to delete this item from the list. The todoList component also displays a add item section at the botton of the list.
All data interactions are made by get, post and delete requests in an Rest API made with python and flask. The api storages the data in an csv file using pandas to manage the datasets.

# Exercise 6
This applications uses python requests pakedge to make an get request in a clock api.

# Exercise 7
This aplications crates an Rest API with flask that returns a list of avaiables locations, and the current datetime of the desired location.

# Exercise 8
In this exercise an simple order management system model is designed. There are three entities: clients, oreders and products. The client can make an order of a product so this order is storaged in the orders table along with the client and product id, the amount of the order and the date. An order must have an client and product id. A client and a product can have several orders but a order can only have one client and one product, so it's possible to keep track of the number of products in each order without additionals tables.
