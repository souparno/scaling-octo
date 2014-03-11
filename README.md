scalling-octo
=============

a scalable micro python-flask application to search a data-base on the categories selected by the user.
 The search supports both 'And' and 'OR' clause.


Installing and Running
======================
The database is provided with 20,000 datas.
 However if you want to import the datas from the csv file provided run the ImportData.py
 
 run the app.py for searching through the data's



Technologies 
=============
•	Flask (Python)<br/>
•	SqlLite<br/>
•	REST Architecture<br/> 


Points to Note
==============

If there are 'n' categories to filter the data's and the user uses 'm' no. of filter options
then the search filter's the datas on 'm' options provided by the user and selects all filters from 
rest of the (n-m) categories.
