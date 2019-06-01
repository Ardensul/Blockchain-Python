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
		document.getElementById("pop").style.display = "block";
		div.style.top = div.style.height * (-1);
	}
	else
	{
		/* Create message div if it does not exist */
		var div = document.createElement("div");
		div.setAttribute("id", "pop");
		div.style.cssText = "display: block; background: white; border: 15px solid white; text-align: center; position: absolute; top: 0; left: 0; z-index: 102;";
		div.style.cssText += "width: " + (viewPortWidth * 20)/100 + "px;";
		div.style.cssText += "height: " + (viewPortHeight * 10)/100 + "px;";
		div.style.left = viewPortWidth/2 - div.style.width/2;
		div.style.top = div.style.height * (-1);
		
		var p = document.createElement("p");
		p.innerHTML = msg;
		div.appendChild(p);
		
		var b = document.createElement("button");
		b.onclick = function(){ b.parentNode.style.display = "none"; };
		b.innerHTML = "Close";
		div.appendChild(b);
		
		document.getElementsByTagName("body")[0].appendChild(div);
	}
}