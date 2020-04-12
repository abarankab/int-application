function set () {
    var rect = document.querySelector("#navbar-header").getBoundingClientRect();
    document.querySelector("#results-header").style.paddingLeft = rect.left + "px";

    q = window.matchMedia("(max-width: 992px)");

    if (!q.matches) {
        document.querySelector(".form-custom").style.marginLeft = rect.left + "px";
        document.querySelector(".msg-custom").style.left = rect.left + "px";
    }
}

$(document).ready(set);

$(window).resize(set);