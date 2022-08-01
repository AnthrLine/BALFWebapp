//import Swup from 'swup';
//const swup = new Swup();

let details = navigator.userAgent;
let regexp = /android|iphone|kindle|ipad/i;
let isMobileDevice = regexp.test(details);
if (isMobileDevice) {
} else {
    alert('Aquesta web és només per a mòbils, sentim les molèsties.')
	window.location.replace("https://google.com");
}


if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
        navigator.serviceWorker.register("/sw.js");
    });
}
