$(document).ready(function() {
    
    $('.feedback-message').on( "load", function(){
        $('.feedback-message').scrollIntoView();
    });

    // Function to allow user to navigate from one part of the register form to the other
    // current_div => Currently displayed div ID - String
    // targetdiv_id => Id of div to be loaded - String
    // all_inputs => Array to contain all input values inside the current div - Array
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

    // Function to generate form action url dinamically following user choices
    // item_id => Id of the chosen/clicked item - String
    // addon_type => Type of add on chosen - String
    $(".addon-radio").click(function(){
        item_id = $(this).attr('id');
        addon_type = $(this).attr('value');
        $(`#${addon_type}`).attr('action', `/cart/add/${addon_type}/${item_id}`);
    });
});