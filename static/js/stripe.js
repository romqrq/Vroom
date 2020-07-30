$(function() {
    /** 
     * Linking the payment form by id, so when we submit the payment,
     * this is how the data will be transferred to Stripe
     * most of the IDs are from STRIPE and we can use them within our code
     * We MUST stick to those IDs to get Stripe to work
     */
    $("#payment-form").submit(function() {
        let form = this;
        let card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };
    // Creating a token
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
        } else {
            // error message from stripe API
            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $('.payment-form-row').get(0).scrollIntoView();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});