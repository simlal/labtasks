// Get images of slides
function getImages(divId) {
    let getDiv = document.getElementById(divId)
    let images = getDiv.getElementsByTagName("img");
    return images

}
console.log("There are %i images in carousel", getImages("slides-container").length)

// Set the slides-container width according to images
function getSlidesWith() {
    const slides = document.querySelectorAll(".slides-container img")
    // console.log(document.getElementById("slides-container").clientWidth)
    for (i = 0; i < slides.length; i++) {
        console.log("img num%i width = %i pixel",i+1 , slides[i].clientWidth)
    }
}
getSlidesWith();

function textHighlightCarousel(slideIndex, slidesText) {
    for (i = 1; i < slidesText.length + 1; i++) {
        if (slideIndex == i) {
            slidesText[i - 1].style.fontWeight = "bold";
            slidesText[i - 1].style.color = "var(--secondary-text-col)";
            slidesText[i - 1].style.background = "rgba(0, 0, 0, 0.3)";
            slidesText[i - 1].style.transition = "all 1s";
            slidesText[i - 1].style.borderRadius = "40px 10px";
        }
        else {
            slidesText[i - 1].style.fontWeight = "normal";
            slidesText[i - 1].style.color = "var(--primary-text-col)";
            slidesText[i - 1].style.background = "none";
            slidesText[i - 1].style.transition = "none";
            slidesText[i - 1].style.borderRadius = "0";
            
        }
    }
}


// get slideshow images and buttons
const slidesContainer = document.getElementById("slides-container");

const prevButton = document.getElementById("slide-arrow-prev");
const nextButton = document.getElementById("slide-arrow-next");

const slides = document.querySelectorAll(".slides-container img");
const slidesText = document.querySelectorAll("#slides-text p")

// Carousel buttons and text highlight

// Initialize carousel
let slideIndex = 1;
slidesText[slideIndex - 1].style.fontWeight = "bold";
slidesText[slideIndex - 1].style.color = "var(--secondary-text-col)";
textHighlightCarousel(slideIndex, slidesText);


// change slide and highlight text on left/right click
nextButton.addEventListener("click", () => {
    const slideContainerWidth = slidesContainer.clientWidth;
    slidesContainer.scrollLeft += slideContainerWidth;
    if (slideIndex == slides.length) {
        slidesContainer.scrollLeft -= slideContainerWidth * slides.length;
        slideIndex = 1;
    }
    else {
        slideIndex += 1;
    }
    textHighlightCarousel(slideIndex, slidesText);

  });
  
prevButton.addEventListener("click", () => {
    const slideContainerWidth = slidesContainer.clientWidth;
    slidesContainer.scrollLeft -= slideContainerWidth;
    if (slideIndex == 1) {
        slidesContainer.scrollLeft += slideContainerWidth * slides.length;
        slideIndex = 3;
    }
    else {
        slideIndex -= 1;
    }
    textHighlightCarousel(slideIndex, slidesText);

  });

 