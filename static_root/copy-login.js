document.addEventListener("DOMContentLoaded", function() {
    range = document.getElementsByClassName("small-li-login");
    console.log(range);
    for (var i = 0; i < range.length; ++i) {
        console.log("kekos");
        range[i].addEventListener("click", copy_to_clipboard);
    }
});

function copy_to_clipboard() {
    console.log("kekw");
    document.execCommand("copy");
}