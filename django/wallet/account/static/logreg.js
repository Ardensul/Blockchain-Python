window.addEventListener("resize", resizeLoader);

const sub = document.getElementById("input");
sub.onclick = function () {
    /* Activate dimmer */
    document.getElementById("dimmer").style.display = "block";

    /* Set up loader */
    document.getElementById("loader").style.display = "block";

    resizeLoader();
};

function resizeLoader() {
    /* Get bigger dimension */
    let viewPortWidth;
    let viewPortHeight;

    if (typeof window.innerWidth != 'undefined') {
        viewPortWidth = window.innerWidth;
        viewPortHeight = window.innerHeight;
    } else if (typeof document.documentElement != 'undefined' && typeof document.documentElement.clientWidth != 'undefined' && document.documentElement.clientWidth !== 0) {
        viewPortWidth = document.documentElement.clientWidth;
        viewPortHeight = document.documentElement.clientHeight;
    }

    let d;

    if (viewPortWidth > viewPortHeight) {
        d = viewPortWidth;
    } else {
        d = viewPortHeight;
    }

    /* Set loader size */
    document.getElementById("loader").style.width = ((d * 5) / 100) + "px";
    document.getElementById("loader").style.height = ((d * 5) / 100) + "px";

    document.getElementById("spinner").style.width = ((d * 5) / 100) + "px";
    document.getElementById("spinner").style.height = ((d * 5) / 100) + "px";

    /* Reposition loader */
    const pageRect = document.body.getBoundingClientRect();
    const loaderRect = document.getElementById("loader").getBoundingClientRect();
    document.getElementById("loader").style.top = ((pageRect.bottom / 2) - ((loaderRect.bottom - loaderRect.top) / 2)) + "px";
    document.getElementById("loader").style.left = ((pageRect.right / 2) - ((loaderRect.right - loaderRect.left) / 2)) + "px";
}
