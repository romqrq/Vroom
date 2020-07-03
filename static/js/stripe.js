$(function() {
    // linking the payment form by id, so when we submit the payment,
    // this is how the data will be transferred to Stripe
    // most of the IDs are from STRIPE and we can use them within our code
    // We MUST stick to those IDs to get Stripe to work
    $("#payment-form").submit(function() {
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            // stripe refers to cvv as cvc
            cvc: $("#id_cvv").val()
        };
    // Creating a token
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

            // Prevent the credit card details from being submitted
            // to our server
            // If we don't do this and there has been some kind of error, just an
            // HTLM error, the you would even be able to read the data straight
            // out of the console
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
            // if we don't get a 200 status, we need to post something:
        } else {
            // error message comes from stripe API
            $("#stripe-error-message").text(response.error.message);
            // changes the status of that div in checkout.html to display the error
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});