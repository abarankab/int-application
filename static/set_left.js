document.addEventListener("DOMContentLoaded", function() {
    range = document.getElementsByClassName("small-li-login");
    for (var i = 0; i < range.length; ++i) {
        range[i].addEventListener("click", copy_to_clipboard);
    }
});

function copy_to_clipboard() {
    document.execCommand("copy");
}

function set () {
    var rect = document.querySelector("#navbar-header").getBoundingClientRect();
    document.querySelector("#results-header").style.paddingLeft = rect.left + "px";

    q = window.matchMedia("(max-width: 992px)");

    if (!q.matches) {
        document.querySelector(".ul-custom").style.marginLeft = rect.left + "px";
        document.querySelector(".ul-result").style.marginLeft = rect.left + "px";
    }
}

$(document).ready(set);

$(window).resize(set);