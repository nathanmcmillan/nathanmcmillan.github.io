			var scrollspeed = 0.075;
			
            var scrollx = -1;
			var targetx = -1;
			
			function scrollto(id)
			{
				var target = document.getElementById(id);
				
				scrollx = self.pageXOffset;
				targetx = target.offsetLeft;

				scroll();
			}

			function scroll()
			{
				if (self.pageXOffset > targetx)
				{
					scrollx += Math.floor((targetx -scrollx) * scrollspeed - 0.5);
					self.scrollTo(scrollx, 0);
					
					if (self.pageXOffset < targetx) self.pageXOffset = targetx;
					else setTimeout('scroll()', 20);
				}
				else if (self.pageXOffset < targetx)
				{
					scrollx += Math.ceil((targetx - scrollx) * scrollspeed + 0.5);
					self.scrollTo(scrollx, 0);
					
					if (self.pageXOffset > targetx) self.pageXOffset = targetx;
					else setTimeout('scroll()', 20);
				}
				else
				{
					// targetx = -1;
				}
			}

function load()
{
	/*window.onscroll = function()
	{
		if (targetx == -1)
		{
			window.scrollTo(scrollx, 0);
		}
	};*/
	
	window.addEventListener('resize', resize, false);
	resize();
}

function resize()
{
	var size = document.body.clientWidth < document.body.clientHeight ? document.body.clientWidth : document.body.clientHeight;
	size *= 0.14;
	
	if (size < 40) size = 40;
	
	document.body.style.fontSize = "" + size + "%";
}