// vars
"use strict";
var testim = document.getElementById("testim"),
  testimDots = Array.prototype.slice.call(
    document.getElementById("testim-dots").children
  ),
  testimContent = Array.prototype.slice.call(
    document.getElementById("testim-content").children
  ),
  testimLeftArrow = document.getElementById("left-arrow"),
  testimRightArrow = document.getElementById("right-arrow"),
  testimSpeed = 4500,
  currentSlide = 0,
  currentActive = 0,
  testimTimer,
  touchStartPos,
  touchEndPos,
  touchPosDiff,
  ignoreTouch = 30;
window.onload = function() {
  // Testim Script
  function playSlide(slide) {
    for (var k = 0; k < testimDots.length; k++) {
      testimContent[k].classList.remove("active");
      testimContent[k].classList.remove("inactive");
      testimDots[k].classList.remove("active");
    }

    if (slide < 0) {
      slide = currentSlide = testimContent.length - 1;
    }

    if (slide > testimContent.length - 1) {
      slide = currentSlide = 0;
    }

    if (currentActive != currentSlide) {
      testimContent[currentActive].classList.add("inactive");
    }
    testimContent[slide].classList.add("active");
    testimDots[slide].classList.add("active");

    currentActive = currentSlide;

    clearTimeout(testimTimer);
    testimTimer = setTimeout(function() {
      playSlide((currentSlide += 1));
    }, testimSpeed);
  }

  testimLeftArrow.addEventListener("click", function() {
    playSlide((currentSlide -= 1));
  });

  testimRightArrow.addEventListener("click", function() {
    playSlide((currentSlide += 1));
  });

  for (var l = 0; l < testimDots.length; l++) {
    testimDots[l].addEventListener("click", function() {
      playSlide((currentSlide = testimDots.indexOf(this)));
    });
  }

  playSlide(currentSlide);

  // keyboard shortcuts
  document.addEventListener("keyup", function(e) {
    switch (e.keyCode) {
      case 37:
        testimLeftArrow.click();
        break;

      case 39:
        testimRightArrow.click();
        break;

      case 39:
        testimRightArrow.click();
        break;

      default:
        break;
    }
  });

  testim.addEventListener("touchstart", function(e) {
    touchStartPos = e.changedTouches[0].clientX;
  });

  testim.addEventListener("touchend", function(e) {
    touchEndPos = e.changedTouches[0].clientX;

    touchPosDiff = touchStartPos - touchEndPos;

    console.log(touchPosDiff);
    console.log(touchStartPos);
    console.log(touchEndPos);

    if (touchPosDiff > 0 + ignoreTouch) {
      testimLeftArrow.click();
    } else if (touchPosDiff < 0 - ignoreTouch) {
      testimRightArrow.click();
    } else {
      return;
    }
  });
};
const hamMenu = document.querySelector('.hamburger-menu');
const ham1 = document.querySelector('.hamburger1');
const ham2 = document.querySelector('.hamburger2');
function displayHamMenu1(ham) {
  hamMenu.style.display = 'flex';
  ham.style.display = 'none';
  ham2.style.display = 'block';
}
function displayHamMenu2(ham) {
  hamMenu.style.display = 'none';
  ham.style.display = 'none';
  ham1.style.display = 'block';
}

// const packageInfoCard = document.querySelector('.info-container');
// function cancelInfoCard(){
//   packageInfoCard.style.display = 'none';
// }

const navBar = document.querySelector('.nav-bar');
document.addEventListener('scroll', (event) => {
  console.log(window.scrollY);
  if (window.scrollY != 0) {
    navBar.classList.add('fix-top');
  } else {
    navBar.classList.remove('fix-top');
  }
  
})

const trackDots = document.querySelectorAll('.package-status-track-container .package-track-card .package-track-dot:not(.active-track ~ .package-track-card .package-track-dot)');
trackDots.forEach((dot) => {
  dot.innerText = '&#10003;';
  console.log(dot);
  console.log('hi');
})

const CurrentDot = document.querySelector('.active-track .package-track-dot');

CurrentDot.innerText= '&#8702;';
