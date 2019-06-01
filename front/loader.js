function showLoader()
{
	if (document.getElementById("dimmer"))
	{
		/* Activate dimmer */
		document.getElementById("dimmer").style.display = "block";
	}
	else
	{
		/* Create dimmer if it does not exist */
		var div = document.createElement("div");
		div.setAttribute("id", "dimmer");
		div.style.cssText = "display: block; background: black; opacity: 0.5; position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 100;";
		document.getElementsByTagName("body")[0].appendChild(div);
	}
	
	if (document.getElementById("spinner"))
	{
		/* Set up spinner */
		document.getElementById("spinner").style.display = "block";
	}
	else
	{
		/* Create loader if it does not exist*/
		var div = document.createElement("div");
		div.setAttribute("id", "spinner");
		div.style.cssText = "border: 16px solid white; border-radius: 50%; border-top: 16px solid orange; max-width: 100%; max-height: 100%;";
		div.style.cssText += "position: absolute; -webkit-animation: spin 1s linear infinite; animation: spin 1s linear infinite; z-index: 101;";
		document.getElementsByTagName("body")[0].appendChild(div);
	}
	
	resizeLoader();
	
	/* Create animation data for the spinner */
	var style = document.createElement("style");
	style.innerHTML += "@-webkit-keyframes spin	{ 0% { -webkit-transform: rotate(0deg); } 100% { -webkit-transform: rotate(360deg); }}";
	style.innerHTML +=  "@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); }}";
	document.getElementsByTagName("head")[0].appendChild(style);
}

function resizeLoader()
{
	/* Get bigger dimension */
	var viewPortWidth;
	var viewPortHeight;

	if (typeof window.innerWidth != 'undefined')
	{
		viewPortWidth = window.innerWidth;
		viewPortHeight = window.innerHeight;
	}
	else if (typeof document.documentElement != 'undefined'	&& typeof document.documentElement.clientWidth != 'undefined' && document.documentElement.clientWidth != 0)
	{
		viewPortWidth = document.documentElement.clientWidth;
		viewPortHeight = document.documentElement.clientHeight;
	}
	
	var d;
	
	if (viewPortWidth > viewPortHeight) { d = viewPortWidth; }
	else { d = viewPortHeight; }

	/* Set loader size */	
	document.getElementById("spinner").style.width = ((d * 5)/100) + "px";
	document.getElementById("spinner").style.height = ((d * 5)/100) + "px";
	
	/* Reposition loader */
	var pageRect = document.body.getBoundingClientRect();
	var loaderRect = document.getElementById("spinner").getBoundingClientRect();
	document.getElementById("spinner").style.top = ( (pageRect.bottom / 2) - ( (loaderRect.bottom - loaderRect.top) / 2 ) ) + "px";
	document.getElementById("spinner").style.left = ( (pageRect.right / 2) - ( (loaderRect.right - loaderRect.left) / 2 ) ) + "px";
}