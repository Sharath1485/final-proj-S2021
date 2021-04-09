Web-scraping Weather Forecast Information with Python
In this script main object was to you  scrapes the 5-day weather forecast from the National Weather Service website. The script extracts information from multiple elements listed under the same class name using the BeautifulSoup library.
Logic flow if the script is . first we will import all important modules like requests , bs4 ; requests for sending http request to National Weather Service website and bs4 module to parse the content of that https response. 
step second is to take input from user and checking wether input value is in float number or not. if not we can disply warning message and exit the script. 
Third step is to create url on basis of input provided by user in 2nd step. we concat lat and lon value to base url by first converting them into string. 
fourth step is to use requests module and send http request to url created in thrid step and parse the result using bs4 , result can be captured on basis of selector - class 'forecast-tombstone' tag - li. 
fifth step is to clean the result , by using various string manipulation methods like replace,split,strip. and lastly convert the final string to upper case by using python string method 'upper()'
last step is to show the result , although fifth and last step can be done through single step. 
only problem that i faced in this assigment is to clean the parsed result . First i checked for any pattern by analysing raw text and than manipulating the text by using strings methods and functions like replace, strip etc. 
