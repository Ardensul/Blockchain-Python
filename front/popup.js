function pop(msg)
{
	/* Get viewport dimensions */
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
	
	/* Check if we already have a message div */
	if (document.getElementById("pop"))
	{
		/* Re-purpose it */
		var div = document.getElementById("pop");
		div.style.display= "block";
		div.getElementsByTagName("p")[0].innerHTML = msg;
		div.style.top = "-" + 2 * parseInt(div.style.height) + "px;";
	}
	else
	{
		/* Create message div if it does not exist */
		var div = document.createElement("div");
		div.setAttribute("id", "pop");
		div.style.cssText = "display: block; background: white; border: 1px solid white; border-radius: 15px; text-align: center; padding: 15px; position: absolute; z-index: 102;";
		div.style.cssText += "box-shadow: 5px 10px 10px #000000";
		div.style.cssText += "width: " + (viewPortWidth * 20)/100 + "px;";
		div.style.cssText += "height: " + (viewPortHeight * 10)/100 + "px;";
		div.style.cssText += "left: " + (viewPortWidth/2 - parseInt(div.style.width)/2) + "px;";
		div.style.cssText += "top: -" + 2 * parseInt(div.style.height) + "px;";
		
		var p = document.createElement("p");
		p.innerHTML = msg;
		div.appendChild(p);
		
		var b = document.createElement("button");
		b.onclick = function(){ slideIn(); };
		b.innerHTML = "Close";
		div.appendChild(b);
		
		document.getElementsByTagName("body")[0].appendChild(div);
	}
	
	slideOut();
	setTimeout(slideIn, 5000);
}

function slideOut()
{
	var div = document.getElementById("pop");
	
	while (parseInt(div.style.top) < 0)
	{
		//setInterval( function(){ div.style.top = parseInt(div.style.top) + 1 + "px"; }, 50 );
		div.style.top = parseInt(div.style.top) + 1 + "px";
	}
}

function slideIn()
{
	var div = document.getElementById("pop");
	
	while (parseInt(div.style.top) > -2 * parseInt(div.style.height))
	{
		//setInterval( function(){ div.style.top = parseInt(div.style.top) - 1 + "px"; }, 50 );
		div.style.top = parseInt(div.style.top) - 1 + "px";
	}
	div.style.display = "none";
}