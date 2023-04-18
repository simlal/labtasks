const labelElements = document.querySelectorAll('.user-reg-form label');

labelElements.forEach(label => {
    label.addEventListener('mouseover', () => {
        const helptext = label.parentElement.nextElementSibling.querySelector('.helptext');
        helptext.style.display = 'inline';
    });
    label.addEventListener('mouseout', () => {
        const helptext = label.parentElement.nextElementSibling.querySelector('.helptext');
        helptext.style.display = 'none';
    });
});