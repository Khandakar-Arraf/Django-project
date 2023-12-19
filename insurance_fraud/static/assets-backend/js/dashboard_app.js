document.getElementById("print-button").addEventListener("click", function() {
    // Apply the "no-print" class to elements you want to hide during printing
    var hideheader = document.querySelector(".app-header");
    var hide_button = document.querySelector(".app-layout-builder-toggle");
        hideheader.style.display = "none";
        hide_button.style.display = "none";
        document.body.style.overflowY = "hidden";
    

    // Trigger the browser's print functionality
    window.print();

    // Restore the visibility of hidden elements after printing
    
        hideheader.style.display = "inherit";
        hide_button .style.display = "inherit";
});
