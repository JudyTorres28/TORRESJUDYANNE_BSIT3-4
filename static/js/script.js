$(document).ready(function() {
    // Smooth scrolling when clicking on links with .scroll-link class
    $('a.scroll-link').click(function(event){
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 500);
    });
});