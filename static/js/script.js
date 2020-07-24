$(document).ready(function() {
    /**
     * Function to scroll screen to message when it load
     */
    $('.feedback-message').on( "load", function(){
        $('.feedback-message').scrollIntoView();
    });

    /**
     * Function to change search button depending on text input field being empty or not
     */
    $('#searchTextInput').on( "change", function(){
        if($(this).val() == ""){
            $('#searchSubmitBtn').not('.disabled-button').addClass('disabled-button').prop("disabled", true);
        } else {
            $('#searchSubmitBtn').removeClass('disabled-button').prop("disabled", false);
        }
    });
    
    /** 
     * Function to allow user to navigate from one part of the register form to the other
     * @param current_div Currently displayed div ID - String
     * @param targetdiv_id Id of div to be loaded - String
     * @param all_inputs Array to contain all input values inside the current div - Array
     * @param field_value Value of input field currently targeted on loop proccess - String or Number
     * @param field_id Id of input field currently targeted on loop proccess - String
     */
    $('.form-trigger').click(function(){
        let current_div = $(this).attr('name');
        let targetdiv_id = $(this).attr('value');
        let all_inputs = []

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
                    return false
                }
            })

            // Searching the array to make sure that there aren't empty fields left 
            // If an empty field is found, the user gets a feedback message
            // Else, next part of form is loaded and top scrolled into view
            if( ($.inArray("", all_inputs) !== -1 ) || ($.inArray(null, all_inputs) !== -1) ) {
                $('.form-message').removeClass('d-none').html("Please fill all required fields.");
                $('.car-register-row').get(0).scrollIntoView()
            }
            else{
                $('.form-box').not('.d-none').addClass('d-none');
                $(`#${targetdiv_id}`).removeClass('d-none').get(0).scrollIntoView()
            }
        }
    });

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
});