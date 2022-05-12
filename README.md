# LinkedIn-Accept-Requests

This project was borne out of an idea that hit me when I was going through my endless list of connection requests in LinkedIn, and hitting "accept".
I thought: Why not automate this stuff!?

We use the Selenium library for this. Selenium enables one to visit urls and do basic tasks like clicking on buttons and links, entering text into a field(like username and password), etc. It's a perfect tool to automate a task like visiting a url and clicking on a bunch of buttons.
Link to Selenium's documentation:- https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html

Terminal commands to install Selenium:-
sudo pip3 install selenium
sudo pip3 install webdriver_manager


This is the Url that shows the user their list of connection requests:-
https://www.linkedin.com/mynetwork/invitation-manager/

However, Selenium seems to open urls in a different browser window which asks for a login(even if you were logged in a different window).
So we first ask the user to enter their credentials(Username and Password, the latter is hidden of course).

Then, we visit the above url only to get redirected to the sign-up page. We use Selenium's "find_element_by_class_name" method to find the element that has the class "main__sign-in-link", this is the element that corresponds to the "Sign In" link. We then click it to go to it's landing page.

Here, we use the "find_element_by_id" methods to find the "username" and "password" elements. We then use the user's credentials to load these fields, before executing "Keys.RETURN" which mimics the act of pressing the Return key - this basically loads the page to login.

Since our initial url was https://www.linkedin.com/mynetwork/invitation-manager/, this is where we land up at. This url will show us the list of ALL requests including not just connection requests from people but also Event requests.

We only intend to accept all people requests, so we go to the "People" button and click it first.

Then, we use "find_elements_by_xpath"(note the plural word elements) to get a Python list of elements that correspond to the "Accept" buttons.
The exact syntax is _find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view invitation-card__action-btn']")_
Here, the "button" indicates to look for the <button> tag. Then, we need to find a variable called "class" that has the exact same value given in this above line. This corresponds to the "Accept" button. Every "Accept" button will have the same HTML tag structure.

This line of code returns a Python List. So next we iterate through the list and "click" on each.
And Voila!!, you can see the all the "accept" buttons just get destroyed!!
  
Note:- After every step in the code, I make the program sleep for a few seconds. I noticed that if we don't do this, it sometimes returns an error saying "element not found".
So I suspect, it takes a few seconds AFTER the url loads in the browser before the code can see all the HTML elements. So we need to make it wait for a few seconds before it can start looking at the HTML elements.
