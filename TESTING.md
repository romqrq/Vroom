# Vroom - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://vroom-heroku.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation services](#validation-services)
    - [Jasmine](#jasmine)
    - [Python Testing](#python-testing)
    - [Coverage](#coverage)
    - [Travis](#travis)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)

## Automated Testing

### Validation Services

The following validation services and linter were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

- [JSHint](https://jshint.com/) was used to validate JavaScript.

- [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

**IMPORTANT**

If you wish to run any of these tests for yourself, you can 
1- Clone the [Vroom GitHub repository](https://github.com/romqrq/Vroom)
2- Follow the steps in the [README.md](readme.md#how-to-run-this-project-locally) under "How to run this project locally"
3- Make sure that you have the entire project running on your own IDE.

### Python Testing

#### How to run Python tests

To run the existing Python tests:

1. Activate your virtual environment.

2. In the terminal enter the following command:

```
python manage.py test
```

3. If you wish to run the tests within a specific app only you can specify with:

```
python manage.py test <app name here>
```

4. The test results will be shown within the terminal.

_NOTE: The `python` part of these commands assumes you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

### A note about TDD

This project did not utilize Test Driven Development. The reason for this was that I was learning how Django works and functions and found it impossible to write tests for methods and classes that I did not understand well as I went along.

The automated tests for this project were created after the vast majority of the project was already complete, once I had a firmer grasp of how my code was working and what its expected output was. Now that I have a better understanding of how automated tests work, I intend to attempt TDD with my next projects.

### Coverage

We used [Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/) to provide feedback during testing to check that enough of my code had been tested.

When running coverage, it generated an immense number of files that weren't supposed to be tested and it was showing a coverage of only 38%.
The work around was checking individually the coverage on the files meant to be tested.

#### How to run coverage

1. Activate your virtual environment.
2. In the terminal enter the following command:
```
coverage html
```
3. Open the newly created `htmlcov` directory in the root of your project folder. 
4. Open the `index.html` file inside it.
5. Run the file in the browser to see the output.

### Travis

- [Travis](https://travis-ci.org/) was used throughout the unit testing of this project to provide continuous integration with the deployed site.
- The [Travis Documentation](https://docs.travis-ci.com/) provides all the information needed to set it up.
- I set the heroku deployment settings for this project to only allow deployment when the travis had passed the latest push to the master branch on GitHub.

## User Stories Testing

The following section goes through the user stories identified in the [Ux section of README.md](README.md#UX) to check that the site meets those needs.

**As a visitor of Vroom I expect/want/need:**

1. **To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.**
    - Arrangement of site elements such as navbar, footer, icons, carousels, products lists, search, contact, FAQs and forms conform to expected placement.
    - The key pages of the site can be accessed from the navigation bar, which can be found always visible at the top of all pages of the site.

2. **The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.**
    - The information follows the **progressive disclosure** method, where the surface pages have basic information and as the user drill into the site, more information is made available.
    - On the search results page, the user will find cards with a **carousel of images** so they can have a peek on the product before deciding have a better look at it.
    - A combination of **font sizes, icons and images** are used to favour a 'at a glance' read and understanding of the content.
    - Users can also visit the **frequently asked questions page**, where some common questions are displayed and the user can also send an email in case the question is still unanswered.

3. **The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.**
    - Some points for this already covered in previous user story details.
    - Once the user moves to a car detail page the user can access more detailed information.
    - In many areas, the user is offered the option to do pre-setup searches by car category.
    - The search page allows the user to run a text search through all car brands, models, year and location to find what they are looking for.

4. **To be able to use the website in any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.**
    - The project used a mobile first approach, developing the full content with mobile in mind and later on adapting to medium and large screens.
    - All pertinent elements are responsive, avoiding overflow, content being squeezed or hard to read on any screen size a user might be using.
    - The use of the site has been extensively tested on desktop, tablet and phone size screens as well as all screen sizes available to simulate in Chrome Developer Tools.

5. **To be able to read reviews of the business and other users written by previous customers, to build trust in my decision of engaging the platform.** 
    - Many of the pages contain carousel elements displaying feedback from other users for that specific product.
    - The about page contains part of the history of the company and opens the opportunity for a personal connection with the user.

6. **For all information and images to be laid out in a clear and easy to understand way, on whatever size screen I am viewing the website on.**
    - Special attention was dispensed towards images being of good quality and to be displayed without distortions.
    - Text is never too large or too small.
    - Buttons are always large enough to be used on touch screen devices.

7. **Plenty of high quality images of the cars and products for sale, so I have a clear idea of what I am renting/buying.**
    - Each of the listings has capacity to display 5 images.

8. **To be able to easily find out all the information I need to make an informed purchase. I expect detailed information about car (model, year, engine, transmission, doors, seats, fuel...), insurance coverage, accessories such as GPS or car seats and pick up/delivery options to be available on every listing page.**
    - The car detail page displays all specific details for that listing including a link to the owner's profile.

9. **To be informed if I try to order more items than are available in stock.**
    - Whenever a user adds an item to their cart or adjusts the quantity in their cart the current stock level for that item is checked from its database entry. A modal will alert the user if they attempt to add more to their cart than is available in stock, and their cart will be updated to reflect the maximum number available.

10. **A text search function so that I can quickly narrow down my search when looking for something specific.**
    - A text search is available on the search page. It searches through the products brands, models, year and locations.

11. **There to be a frequently asked questions page for any further questions I might have about how to deal with some situations.**
    - A FAQs page is provided and linked to in the navigation bar.

12. **That once I am logged in I can access my account details and update them if I need to.**
    - The profile page gives the logged in user the ability to visualise their personal information.
    - the edit profile page allows the logged in user to update their username, email address, first name, last name and password.

13. **To be able to find information on my bookings and how to cancel or change them.**
    - This feature is to be added on a future release.

14. **To be able to connect to the businesses social media channels to keep up to date with new listings on the site.**
    - The footer contains links to all social media where Vroom is present.
    - For this project, the links redirect the user to the main page of the respective social media channel.

15. **To be able to easily get in contact with the customer service via a contact form**
    - The contact page is easily located from the navigation bar.
    - The contact page is also linked to in the Frequent Asked Questions page to encourage the user to get in contact.
    - At this point, the contact form doesn't send emails.

16. **Feedback from the website I am using when I interact with it, I expect to see messages to inform me when my forms have been completed and sent correctly. Or to let me know when an error has ocurred and what to do next.**
    - HTTP responses provide feedback to the user if there is a problem with their input values in forms.
    - The standard django messages were used to display feedback to users.
    - JavaScript was used to make sure the images are always within the user's screen.
    - Where possible, individual and more specific messages are displayed in areas such as form fields.

## Manual Testing

Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected.

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different screen sizes (40" TV and 15" notebook).

#### Elements on every page

1. Navbar
    - Clicked each link in the navbar to confirm that it leads to the correct page.
    - Confirm that when logged out the options "Register" and "Log in" are visible and that "Profile" and "Log out" are not.
    - Log into the site, confirm that options "Profile" and "Log out" are visible and that "Register" and "Log in" are not.
    - Click the "Find a Car" link in the navbar, confirm that all categories are listed in the dropdown menu.
    - Add an item to the users cart, confirm that the counter appears over the shopping cart icon with the correct number of items displays.
    - Delete all items from the users cart, confirm that the counter is no longer visible in the navbar.

2. Footer
    - Click on all social media buttons and confirm that they bring the user to the respective social media main page.

#### Home Page

1. Carousel
    - Confirm that images are displayed correctly and text is clearly readable.

2. What are users using vroom for
    - Confirm that image, icons and text are displayed correctly and clearly readable.

3. Find the car of your dreams
    - Clicked on all buttons and confirm they bring the user to the correct page.
    - Upon change on screen, content remains well displayed with no distortions or overflow.

4. Vroom my car
    - Clicked vroom my car button and confirm it brings the user to the correct page.
    - Upon change on screen, content remains well displayed with no distortions or overflow.

5. Great experience and convenience
    - Clicked on all buttons and confirm they bring the user to the correct page.
    - Upon change on screen, content remains well displayed with no distortions or overflow.

6. Testimonials carousel
    - Confirm that images are displayed correctly and text is clearly readable.

#### Find a Car Page

1. Search section
    - Select input field displays the correct categories.
    - Text input field is displayed correctly with placeholder.
    - Search button remains deactivated while the text input field is empty and is activated when user types something on the input field.

2. Search results section
    - Cards with cars are displayed correctly.

3. Car cards
    - Carousel with the images of the car only changes images upon user action.
    - Car information are displayed correctly with pertinent icons.
    - Input field is displayed correctly with placeholder.
    - Vroom! button adds the product to cart correctly and redirects the user to the addons page.
    - View button brings the user to the car details page.

#### Car Detail Page

1. Images carousel
    - Check that arrows move between the images going forward and backwards.
    - Images are displayed correctly with black background where image dimensions differ from div area.

2. Car details
    - Confirm that all details are displayed correctly.
    - Values and keys are paired correctly.

3. Rent this car now
    - Input field is displayed correctly with placeholder.
    - Vroom! button adds car to cart and redirects the user to the add ons page..

4. Meet the owner
    - Confirm that all details are displayed correctly.
    - Values and keys are paired correctly.
    - View profile button brings the user as a visitor to car owner profile.

#### Edit Car Page

1. Update car form
    - Form is displayed correctly.
    - Fields load the values from the correct car object.
    - Choose File buttons allow user to upload new image files.
    - Update button correctly updates car register, redirects user to index page and displays feedback message confirming that the entry has been updated.

2. Delete car form
    - Form is displayed correctly.
    - Delete button removes the car from the database, redirects user to index page and displays feedback message confirming that the entry has been updated.

#### Rent my Car Page

1. Rent my car
    - Text is displayed correctly.
    - Link to FAQs brings the user to the Frequently asked questions page.
    - Link to Contact us brings the user to the Contact page.

2. Main details form
    - Form is displayed correctly.
    - Fields display the correct labels and placeholders.
    - Select options display the correct items.
    - Validation is triggered on submission of empty fields.
    - Next step button loads the next form correctly.

3. Technical specifications form
    - Form is displayed correctly.
    - Fields display the correct labels and placeholders.
    - Select options display the correct items.
    - Validation is triggered on submission of empty fields.
    - Previous button loads the previous form correctly without triggering validation.
    - Next step button loads the next form correctly.

4. Location form
    - Form is displayed correctly.
    - Fields display the correct labels and placeholders.
    - Select options display the correct items.
    - Validation is triggered on submission of empty fields.
    - Previous button loads the previous form correctly without triggering validation.
    - Next step button loads the next form correctly.

5. Location form
    - Form is displayed correctly.
    - Fields display the correct labels and placeholders.
    - Choose file buttons allow user to upload images.
    - Validation is triggered on submission of empty fields.
    - Previous button loads the previous form correctly without triggering validation.
    - Vroom my car submits the form correctly and redirects user to index page and displays feedback message confirming that the car is ready to vroom.

#### About Page

- All text is displayed correctly.
- Confirm that images adjust correctly to screen size.

#### FAQs Page

1. Frequently asked questions section
    - Buttons containing questions are displayed correctly.
    - Confirm that buttons trigget the corresponding answers.

2. Can't find what you're looking for section
    - Text and buttons are displayed correctly.
    - Click the Contact us button and it brings the user to the Contact page as expected.

#### Contact Page

- Text is displayed correctly.
- Confirm that form fields are displayed correctly with correct spacing, labels and placeholders.
- Submit button clears the form simulating the action of sending the data.

#### Register Page

- Try to go to the register url when already logged in, confirm that the user is redirected to the home page and feedback message is displayed.
- Log out then go to the register page again. Confirm that the register form is displayed as expected.
- Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
- Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
- Go into devtools, change the `type` attribute on the email form to `text`, attempt to send the form. confirm that the Django validation catches the error and tells the user to enter an email address.
- Fill in the form with two different passwords, confirm the error is caught again and the user is informed of their mistake.
- Fill in the registration form correctly, confirm that the user is automatically logs in the user, redirects to the index page and feedback message is displayed confirming successful registration.

#### Login Page

- Form and text is loaded correctly.
- Attempt to log in with a username not in the database, confirm the relevant error message is shown.
- Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
- Log in with a correct username and password, confirm that the user is logged in and that they are redirected to the index page and feedback message is displayed.
- Try to go to the login url when already logged in, confirm that the user is redirected to the home page and feedback message is displayed.

#### Reset Password Page

- Form and text is loaded correctly.
- Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
- Reset Password button correctly sends the email to the user, redirects to index page and feedback message is displayed confirming the email has been sent.
- For some reason this feature doesn't work when running the project locally but works from Heroku.

#### Profile Page

- Go to the profile page of a newly created user. Confirm that the profile is populated with correct **username**, **first** and **last names**, **email address**, **member since** and **cars owned**.
- Edit Profile button is displayed correctly and redirects user to correct page.
- Confirm that the cards containing the cars informations load correctly with no distortions or overflows.

#### Edit Profile Page

- Confirm that forms and text are loaded correctly.
- Submit blank form fields and it doesn't wipe the existing values.
- Fill in the form with a non-email address, confirm that the applicable error is shown to the user
- Fill in the form correctly, confirm that the user is redirected to profile page and feedback message is displayed.
- Confirm that the information on the profile has been updated.

#### Cart Page

- Try to access the cart when empty, confirm that user sees the 'empty cart' page.
- Click the **Find a car** button and confirm it takes the user to the all cars page.
- Add items to the cart and return to the cart page, confirm that all items in the cart are displayed correctly, with the correct amounts requested by the user.
- Go to the cart page when not logged in to the site, confirm that the user can visualise the items.
- Adjust the quantity field, confirm that the shopping cart subtotal is updated to reflect the change.
- Click the delete button on an item, confirm that the cart page is reloaded with that item removed from the cart and feedback message is displayed.
- Delete all items from the cart, confirm that the cart page is reloaded to reflect the empty cart and 'empty cart' page is displayed.

#### Checkout Page

- Navigate to the checkout page urls without anything in the cart. Confirm that the user is redirected to index page.

##### Order Summary

- Confirm that text loads correctly.
- Values loaded from cart items are displayed in correct order and on the right place.

##### Payment Details

- Confirm that form and text are displayed correctly.
- Fields adjust correctly to screen size/
- Form validation working for all required fields.
- Submit payment button correctly submits the payment and returns correct feedback messages for card validation.

### Testing undertaken on tablet and phone devices

All steps below were repeated to test mobile and tablet specific elements on my Samsung phone and tablet, in both the firefox browser and samsung internet browser.

Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar
    - Open the website on mobile, confirm that the navbar is collapsed into a burger icon
    - click the burger icon, confirm that the navbar list appears are expected.
    - Click the "Find a car" dropdown menu, confirm that the correct categories are displayed.
    - Add something to the cart, confirm that the user shopping cart icon counter appears and displays correctly.

2. Footer
    - Scroll to the bottom of the page, confirm that the footer contents is displayed as expected with the bootstrap grid.
    - No content squashed or squeezed or disproportionate in size.
    - Confirm that all links and buttons in footer are easy to click with a finger on the smallest screen sizes.

3. Find a car page
    - Confirm that the products are displayed one on top of each other on mobile, and 2 to a row on tablet.
    - Confirm that all clicks and swipes operate as expected on touch screen.

4. Checkout page
    - Check that the display of elements matches the expected layout for mobile and tablet devices.

5. All pages
    - Navigate to all pages on the site, check that the layout is as expected for the screen size.
    - Check that all buttons, menus, forms and other elements are the correct proportions and easily clickable with a finger.

### Bugs discovered

#### Solved bugs

1. **When trying to run tests, python threw error saying it couldn't create test database**
    - As I was using the Postgres database from AWS bucket, python was unable to create the test database.
    - Bug fixed by explicitly using local sqlite3 database.

2. **Form validation problem on vroom my car as form was displayed as 4 parts**
    - Because the form is so long, we decided to break it down into 4 sections that are displayed one at a time.
    - That created a validation problem as the "next step" button didn't trigger the validation for that part of the form.
    - The solution was to use JavaScript to look for required fields and make sure they weren't empty before the next step.

    ```JavaScript
    /**
     * Function to allow user to navigate from one part of the register form to the other
     * while validating the current part of the form.
     * @param current_div Currently displayed div ID - String
     * @param targetdiv_id Id of div to be loaded - String
     * @param all_inputs Array to contain all input values inside the current div - Array
     * @param field_value Value of input field currently targeted on loop proccess - String or Number
     * @param field_id Id of input field currently targeted on loop proccess - String
     */
    $('.form-trigger').click(function(){
        let current_div = $(this).attr('name');
        let targetdiv_id = $(this).attr('value');
        let all_inputs = [];

        //The button to go back to the previous part of the form won't trigger the field check
        if($(this).hasClass("back-button")){
            $('.form-box').not('.d-none').addClass('d-none');
            $(`#${targetdiv_id}`).removeClass('d-none');
        }
        else{
            // Creating an array with the value of every input element inside the current div
            // If field is required, it is added to the array
            // else the function returns false and moves on to the next iteration
            $(`#${current_div} :input`).each(function(){
                field_value = $(this).val();
                field_id = $(this).attr('id');
                if($(`[for=${field_id}]`).hasClass('requiredField')){
                    all_inputs.push(field_value);
                }
                else{
                    return false;
                }
            });

            // Searching the array to make sure that there aren't empty fields left
            // If an empty field is found, the user gets a feedback message
            // Else, next part of form is loaded and top scrolled into view
            if( ($.inArray("", all_inputs) !== -1 ) || ($.inArray(null, all_inputs) !== -1) ) {
                $('.form-message').removeClass('d-none').html("Please fill all required fields.");
                $('.car-register-row').get(0).scrollIntoView();
            }
            else{
                $('.form-box').not('.d-none').addClass('d-none');
                $(`#${targetdiv_id}`).removeClass('d-none').get(0).scrollIntoView();
            }
        }
    });
    ```

3. **Submission of empty search field**
    - User was able to submit an empty field for search.
    - To solve that, we used JavaScript to watch the text input field and on change event, activate the submit search button.

    ```JavaScript
    /**
     * Function to activate search button depending on text input field being empty or not
     */
    $('#searchTextInput').on( "change", function(){
        if($(this).val() == ""){
            $('#searchSubmitBtn').not('.disabled-button').addClass('disabled-button').prop("disabled", true);
        } else {
            $('#searchSubmitBtn').removeClass('disabled-button').prop("disabled", false);
        }
    });
    ```

4. **Django Feedback message comming up out of the user's screen**
    - When filling a form, if any error message came up, it would come up at the top of the page and many times outside the user's screen. That would leave the user not knowing what was happening.
    - To fix this we used JavaScript to scroll into view the message whenever it comes up.

    ```JavaScript
    /**
     * Function to scroll screen to message when it load
     */
    $('.feedback-message').on( "load", function(){
        $('.feedback-message').scrollIntoView();
    });
    ```  

5. **On Addons pages, each item had to have its own 'add to cart' form**
    - For each addon, there is a specific parameter to be passed to the view in order to add that item correctly to the cart.
    - The solution we came up with was to use JavaScript to dynamically generate the url according to the radio button selected by the user.
    - This way only one 'add to cart' form is used avoiding repetition.

    ```JavaScript
    /**
     * Function to generate form action url dinamically following user choices
     * @param item_id Id of selected item - String
     * @param addon_type Type of addon chosen - String
     */
    $(".addon-radio").click(function(){
        item_id = $(this).attr('id');
        addon_type = $(this).attr('value');
        $(`#${addon_type}`).attr('action', `/cart/add/${addon_type}/${item_id}`);
    });
    ```

#### Unsolved bugs

1. **Error When the user submits image files that are jpg!d or other less common extensions**
    - This error has not been dealt with due to time constraints.
    - The idea of solution is:
        1. To use JavaScript to check the field and isolate the file extension.
        2. Use messages feedback to tell user the expected file extensions.

2. **Error when trying to delete order items**
    - When trying to delete an order through the admin panel on heroku, it raises a server error even though it works locally.
    - We couldn't look in depth into this problem due to time constraints.

    ```python
    class OrderLineItem(models.Model):
        """Model for each line in the order representing a product"""

        order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
        car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True)
        track_day = models.ForeignKey(TrackDayAddon,
                                    on_delete=models.PROTECT, null=True)
        insurance = models.ForeignKey(InsuranceAddon,
                                    on_delete=models.PROTECT, null=True)
        private_driver = models.ForeignKey(PrivateDriverAddon,
                                        on_delete=models.PROTECT, null=True)
        rental_days = models.IntegerField(blank=False)

        if car:
            def __str__(self):
                return "{0} {1} {2} @ {3} per day".format(
                    self.rental_days, self.car,
                    self.car.model, self.car.price
                )

        elif track_day:
            def __str__(self):
                return "{0} {1} {2} @ {3} per day".format(
                    self.rental_days, self.track_day.title,
                    self.track_day.coverage, self.track_day.price
                )
        elif insurance:
            def __str__(self):
                return "{0} {1} {2} @ {3} per day".format(
                    self.rental_days, self.insurance.title,
                    self.insurance.coverage, self.insurance.price
                )
        elif private_driver:
            def __str__(self):
                return "{0} {1} {2} @ {3} per day".format(
                    self.rental_days, self.private_driver.title,
                    self.private_driver.coverage, self.private_driver.price
                )
    ```

## Further testing

1. Sent the link to friends, family and especially focusing on people with IT and design background for more technical feedback.
