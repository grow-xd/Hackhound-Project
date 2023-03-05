function sendsms() {
    var message = document.getElementById("message").value;
    var accountSid = 'AC0add35446a2feb5668442c1407c2295f';
    var authToken = '941bd34a66e9a4b7fef10c7dab00be02';

    // Require the Twilio module and create a REST client
    require(['twilio'], function (twilio) {
        var client = twilio(accountSid, authToken);

        client.messages.create({
            to: "+919928198552",
            from: "+15676777669",
            body: message

        }, function (err, message) {
            console.log(message.sid);
        });
    });
}

// Twilio Credentials
