$(document).ready(function() {
    $('.feedback-message').on( "load", function(){
        $('.feedback-message').scrollIntoView();
    });
    /**
     * Function to activate search button depending on text input field being empty or not
     */
    $('#searchTextInput').on( "change", function(){
        if($(this).val() == ""){
            $('#searchSubmitBtn').not('.disabled-button').addClass('disabled-button').prop("disabled", true);
        } else {
            $('#searchSubmitBtn').removeClass('disabled-button').prop("disabled", false);
        };
    });
    /**
     * Function to activate add to cart button depending on number input field being empty or not
     */
    $('.addon-input').on( "change", function(){
        if($(this).val() == ""){
            $('.addon-submit').not('.disabled-button').addClass('disabled-button').prop("disabled", true);
        } else {
            $('.addon-submit').removeClass('disabled-button').prop("disabled", false);
        }
    });
    
    /** 
     * Function to allow user to navigate from one part of the register form to the other
     * while validating the current part of the form.
     * current_div Currently displayed div ID - String
     * targetdiv_id Id of div to be loaded - String
     * all_inputs Array to contain all input values inside the current div - Array
     * field_value Value of input field currently targeted on loop proccess - String or Number
     * field_id Id of input field currently targeted on loop proccess - String
     */
    $('.form-trigger').click(function(){
        let current_div = $(this).attr('name');
        let targetdiv_id = $(this).attr('value');
        let all_inputs = [];

        if($(this).hasClass("back-button")){
            $('.form-box').not('.d-none').addClass('d-none');
            $(`#${targetdiv_id}`).removeClass('d-none');
        } 
        else{
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

    /** 
     * Function to generate form action url dinamically following user choices 
     * item_id Id of selected item - String
     * addon_type Type of addon chosen - String
     */
    $(".addon-radio").click(function(){
        item_id = $(this).attr('id');
        addon_type = $(this).attr('value');
        $(`#${addon_type}`).attr('action', `/cart/add/${addon_type}/${item_id}`);
    });
});