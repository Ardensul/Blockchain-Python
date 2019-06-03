const status = {HIDDEN: 0, SHOWING: 1, SHOWN: 2, HIDING: 3};
const retCode = {NEUTRAL: 0, SUCCESS: 1, ERROR: 2};
let s = status.SHOWING;
let timer;

function setState(state) {
    s = state;

    switch (state) {
        case status.HIDDEN:
            console.log("Changed state to hidden");
            clearInterval(timer);
            break;
        case status.SHOWING:
            console.log("Changed state to showing");
            timer = setInterval(slideOut, 5);
            break;
        case status.SHOWN:
            console.log("Changed state to shown");
            clearInterval(timer);
            timer = setTimeout(transition, 6000);
            break;
        case status.HIDING:
            console.log("Changed state to hiding");
            clearTimeout(timer);
            setInterval(slideIn, 5);
            break;
    }
}

function getState() {
    return s;
}

function pop(msg, code = retCode.NEUTRAL) {

    let color;

    switch (code) {
        case retCode.NEUTRAL:
            color = "#DDDDDD";
            break;
        case retCode.SUCCESS:
            color = "#00AA00";
            break;
        case retCode.ERROR:
            color = "#AA0000";
            break;
        default:
            color = "#DDDDDD";
            break;
    }

    let div;
    /* Get viewport dimensions */
    let viewPortWidth;
    let viewPortHeight;

    if (typeof window.innerWidth != 'undefined') {
        viewPortWidth = window.innerWidth;
        viewPortHeight = window.innerHeight;
    } else if (typeof document.documentElement != 'undefined' && typeof document.documentElement.clientWidth != 'undefined' && document.documentElement.clientWidth !== 0) {
        viewPortWidth = document.documentElement.clientWidth;
        viewPortHeight = document.documentElement.clientHeight;
    }

    /* Check if we already have a message div */
    if (document.getElementById("pop")) {
        /* Re-purpose it */
        div = document.getElementById("pop");
        div.getElementsByTagName("p")[0].innerHTML = msg;
        div.style.top = "-" + 2 * parseInt(div.style.height) + "px";
        div.style.display = "block";
    } else {
        /* Create message div if it does not exist */
        div = document.createElement("div");
        div.setAttribute("id", "pop");
        div.style.cssText = "display: block; background: white; border: 1px solid white; border-radius: 15px; text-align: center; padding: 15px; position: absolute; z-index: 102;";
        div.style.cssText += "box-shadow: 5px 10px 10px #000000";
        div.style.cssText += "width: " + (viewPortWidth * 20) / 100 + "px;";
        div.style.cssText += "height: " + (viewPortHeight * 10) / 100 + "px;";
        div.style.cssText += "left: " + (viewPortWidth / 2 - parseInt(div.style.width) / 2) + "px;";
        div.style.cssText += "top: -" + 2 * parseInt(div.style.height) + "px;";

        const p = document.createElement("p");
        p.innerHTML = msg;
        div.appendChild(p);

        const d = document.createElement("div");
        d.style.cssText += "text-align: right; width: 100%";

        const b = document.createElement("button");
        b.onclick = function () {
            closePop();
        };
        b.innerHTML = "Close";
        d.appendChild(b);
        div.appendChild(d);

        document.getElementsByTagName("body")[0].appendChild(div);
    }

    setState(status.SHOWING);
}

function slideOut() {
    const div = document.getElementById("pop");

    if (getState() === status.SHOWING) {
        if (parseInt(div.style.top) > 0) {
            setState(status.SHOWN);
            return 1;
        } else {
            div.style.top = parseInt(div.style.top) + 1 + "px";
        }
    }
}

function transition() {
    setState(status.HIDING);
}

function slideIn() {
    const div = document.getElementById("pop");

    if (getState() === status.HIDING) {
        if (parseInt(div.style.top) < parseInt(div.style.height) * -2) {
            div.style.display = "none";
            setState(status.HIDDEN);
        } else {
            div.style.top = parseInt(div.style.top) - 1 + "px";
        }
    }
}

function closePop() {
    document.getElementById("pop").style.display = "none";
    setState(status.HIDDEN);
}
