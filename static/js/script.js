$(document).ready(function() {
    $('.form-trigger').click(function(){
        // filled_form = $(this).attr('name');
        targetdiv_id = $(this).attr('value');
        $('.form-box').not('.d-none').addClass('d-none');
        $(`#${targetdiv_id}`).removeClass('d-none');
        // $(`#${filled_form}`).submit('d-none');
    });
    $(".addon-radio").click(function(){
        item_id = $(this).attr('id');
        addon_type = $(this).attr('value');
        $(`#${addon_type}`).attr('action', `/cart/add/${addon_type}/${item_id}`);
    });
    // $( "#carRegForm").submit(function( event ) {
    //     alert( "Handler for .submit() called." );
    //     event.preventDefault();
    // });
    // $('#crfSubmitButton').click(function(){
    //     $("#carRegForm").submit() 
    // })
});