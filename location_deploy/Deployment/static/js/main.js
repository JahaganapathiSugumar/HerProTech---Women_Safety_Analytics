$(document).ready(function () {
    // Initialize hidden elements
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('#stats-image-container').hide(); // Hide the stats image container initially

    // Upload Preview function
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')'); // Display the selected image
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650); // Smooth fade-in effect
            }
            reader.readAsDataURL(input.files[0]); // Read the file as a URL
        }
    }

    // Image upload handler
    $("#imageUpload").change(function () {
        $('.image-section').show(); // Show image section
        $('#btn-predict').show();   // Show predict button
        $('#result').text('');      // Clear previous result
        $('#result').hide();        // Hide result
        readURL(this);              // Preview the image
    });

    // Prediction button click handler
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling API /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text('Result: ' + data);
                console.log('Success!');
            },
        });
    });

    // Toggle chatbot visibility
    $('#toggle-chatbot').on('click', function() {
        const chatbotContainer = $('#chatbot-container');
        const isVisible = chatbotContainer.is(':visible');

        if (isVisible) {
            chatbotContainer.slideUp(300); // Smooth hide
            $(this).css('bottom', '20px'); // Reset button position
            $(this).text('Chat'); // Reset button text
        } else {
            chatbotContainer.slideDown(300); // Smooth show
            $(this).css('bottom', '540px'); // Adjust button position above the chatbot
            $(this).text('Close Chat'); // Change button text
        }
    });

    // Handle click event for the statistics button
    $('#btn-stats').on('click', function() {
        const imageUrl = 'C:/Users/sreep/OneDrive/Desktop/Deployment/Screenshot 2024-08-22 080644.png'; // Replace with the path to your image
        const statsImageContainer = $('#stats-image-container');
        const statsImage = $('#stats-image');

        // Set the source of the image
        statsImage.attr('src', imageUrl);

        // Show the image container with a smooth effect
        statsImageContainer.slideDown(300);
    });

    // Ensure the chatbot iframe loads properly
    const chatbotIframe = document.querySelector('#chatbot-container iframe');
    chatbotIframe.addEventListener('load', function() {
        console.log('Chatbot loaded successfully');
    });

    chatbotIframe.addEventListener('error', function() {
        console.log('Error loading the chatbot');
        alert('Failed to load the chatbot. Please try again later.');
    });
});
