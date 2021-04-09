Main objective of this final script was to display 'x' rated books from first n pages of website http://books.toscrape.com/ where x is user defined and value can be from 1-5 and n is also user definer value can be between 1-50. 

First problem that i faced what if user give wrong input , so to resolve this issue i used try and exception keywords to check if digit is entered or not and if else block to check is input value lies in correct range. 
Another issue that i faced that how to reprompt for input if wrong input is given. by using little logic and using While loop if solved this case too. 

next thing was to select correct book titles using bs4 and css selector. For one rated books selector is star-rating.One (This we can look by inspecting element from google chrome developer tool) , similarly for two rating selector is star-rating.Two, for three star rating, star-rating.Three ; for four star rating ,star-rating.Four and lastly for five star rated books selector is star-rating.Five. So according to user input we can intialize selector variable with one of the five option above (By using if else statements)

Next task was to loop through all the pages and select the books titile according to user input. for sending http request we are using requests module and to parse the content fetch by requests module we are using bs4 module. 
In parsing , we first create BeautifulSoup object and then look for all the products by using selector-'.product_pod' and we go to each product soup object and look for rating value using selector that was defined in earlier step and save that to a result array

Final step is to print all the titles , which is easily done through looping through all result array and print element. 

For resolving problem that comes while making the script , i used resources/public forum like stackoverflow and github , analysed some webscraping code and then completed this script. 