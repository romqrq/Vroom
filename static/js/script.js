$(document).ready(function() {
    $('.form-trigger').click(function(){
        // filled_form = $(this).attr('name');
        targetdiv_id = $(this).attr('value');
        $('.form-box').not('.d-none').addClass('d-none');
        $(`#${targetdiv_id}`).removeClass('d-none');
        // $(`#${filled_form}`).submit('d-none');
    });
    // $( "#carRegForm").submit(function( event ) {
    //     alert( "Handler for .submit() called." );
    //     event.preventDefault();
    // });
    // $('#crfSubmitButton').click(function(){
    //     $("#carRegForm").submit() 
    // })
});