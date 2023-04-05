// Go to selected labspace

var button = document.querySelector('#selected-labspace-btn');

button.addEventListener('click', function() {
    // Select all checked checkboxes
    var checkboxes = document.querySelectorAll('input[name="check"]:checked');

    // Check if exactly one checkbox is checked
    if (checkboxes.length === 1) {
        // Get the URL of the selected Labspace object from the labspace-url attribute of the checkbox
        let url = checkboxes[0].getAttribute('labspace-url');
        console.log("selectedurl:", url)

        // Navigate to the URL of the selected Labspace object
        window.location.href = url;

    } else if (checkboxes.length === 0) {
        swal({
            title: "Error!",
            text: "You must select the labspace to go to",
            icon: "error",
            button: "OK"
        })
    } else {
        swal({
            title: "Error!",
            text: "Please select exactly one labspace to go to",
            icon: "error",
            button: "OK"
        });
    }
});


// Edit the labspace
var editButton = document.querySelector('#edit-labspace-btn');

editButton.addEventListener('click', function(event) {
    // Prevent the default link behavior
    event.preventDefault();

    // Select all checked checkboxes
    var checkboxes = document.querySelectorAll('input[name="check"]:checked');

    // Check if exactly one checkbox is checked
    if (checkboxes.length === 1) {
        // Get the URL of the selected Labspace object
        let url = checkboxes[0].getAttribute("edit-url")

        // Navigate to the URL
        window.location.href = url;
    } else if (checkboxes.length === 0) {
        swal({
            title: "Error!",
            text: "You must select a labspace to edit",
            icon: "error",
            button: "OK"
        })
    } else {
        swal({
            title: "Error!",
            text: "Please select exactly one labspace to edit",
            icon: "error",
            button: "OK"
        });
    }
});

// Delete the labspace
var editButton = document.querySelector('#delete-labspace-btn');

editButton.addEventListener('click', function(event) {
    // Prevent the default link behavior
    event.preventDefault();

    // Select all checked checkboxes
    var checkboxes = document.querySelectorAll('input[name="check"]:checked');

    // Check if exactly one checkbox is checked
    if (checkboxes.length === 1) {
        // Get the URL of the selected Labspace object
        let url = checkboxes[0].getAttribute("delete-url")

        // Navigate to the URL 
        window.location.href = url;
    } else if (checkboxes.length === 0) {
        swal({
            title: "Error!",
            text: "You must select a labspace to delete",
            icon: "error",
            button: "OK"
        })
    } else {
        swal({
            title: "Error!",
            text: "Please select exactly one labspace to delete",
            icon: "error",
            button: "OK"
        });
    }
});