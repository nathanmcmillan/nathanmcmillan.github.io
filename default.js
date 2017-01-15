window.onload = function()
{
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