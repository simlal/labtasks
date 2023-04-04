// Go to selected labspace based on checkbox selection

var button = document.querySelector('#selected-labspace');

button.addEventListener('click', function() {
    // Select all checked checkboxes
    var checkboxes = document.querySelectorAll('input[name="check"]:checked');

    // Check if exactly one checkbox is checked
    if (checkboxes.length === 1) {
        // Get the URL of the selected Labspace object from the data-url attribute of the checkbox
        let url = checkboxes[0].getAttribute('data-url');
        console.log("selectedurl:", url)

        // Navigate to the URL of the selected Labspace object
        window.location.href = url;

    } else if (checkboxes.length === 0) {
        swal({
            title: "Error!",
            text: "You must select a labspace",
            icon: "error",
            button: "OK"
        })
    } else {
        // Display an alert message if no checkboxes or more than one checkbox is checked
        swal({
            title: "Error!",
            text: "Please select exactly one labspace",
            icon: "error",
            button: "OK"
        });
    }
});