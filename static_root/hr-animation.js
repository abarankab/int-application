function add() {
    q = window.matchMedia("(max-width: 992px)");
    var hr = document.getElementById("hr-custom");

    if (!q.matches) {
        hr.style.backgroundColor = "#ffd05d";
        hr.animate(
            {
                height: ["1px", "2px"],
                marginBottom: ["1px", "0px"]
            }, {
                duration: 40
            }
        );
        hr.style.height = "2px";
        hr.style.marginBottom = "0px";
    }
    else {
        hr.style.backgroundColor = "#ffd05d";
        hr.animate(
            {
                height: ["4px", "6px"],
                marginBottom: ["100px", "98px"]
            }, {
                duration: 40
            }
        );
        hr.style.height = "6px";
        hr.style.marginBottom = "98px";
    }
}

function remove() {
    q = window.matchMedia("(max-width: 992px)");
    var hr = document.getElementById("hr-custom");

    if (!q.matches) {
        hr.animate(
            {
                height: ["2px", "1px"],
                marginBottom: ["0px", "1px"]
            }, {
                duration: 40
            }
        );
        hr.style.height = "1px";
        hr.style.marginBottom = "1px";
        hr.style.backgroundColor = "#e6e6e6";
    }
    else {
        hr.animate(
            {
                height: ["6px", "4px"],
                marginBottom: ["98px", "100px"]
            }, {
                duration: 40
            }
        );
        hr.style.height = "4px";
        hr.style.marginBottom = "100px";
        hr.style.backgroundColor = "#e6e6e6";
    }
}