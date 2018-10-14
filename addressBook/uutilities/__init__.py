button_save = f"""
    <button style='
        display: inline-block;                      
        zoom: 1;
        padding: 6px 20px;
        margin: 0;
        cursor: pointer;
        border: 1px solid #bbb;
        overflow: visible;
        font: bold 13px arial, helvetica, sans-serif;
        text-decoration: none;
        white-space: nowrap;
        color: #555;

        background-color: #ddd;
        background-image: -webkit-gradient(linear, left top, left bottom, from(rgba(255,255,255,1)), to(rgba(255,255,255,0)));
        background-image: -webkit-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -moz-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -ms-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -o-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));

        -webkit-transition: background-color .2s ease-out;
        -moz-transition: background-color .2s ease-out;
        -ms-transition: background-color .2s ease-out;
        -o-transition: background-color .2s ease-out;
        transition: background-color .2s ease-out;
        background-clip: padding-box; /* Fix bleeding */
        -moz-border-radius: 3px;
        -webkit-border-radius: 3px;
        border-radius: 3px;
        -moz-box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        -webkit-box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        text-shadow: 0 1px 0 rgba(255,255,255, .9);

        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;' onmouseover="this.style.backgroundColor = '#555'"; 
        onmouseout="this.style.backgroundColor = '#ddd';" 
        type="submit" name="confirmation" value="yes">Zapisz</button>                    
"""

button_confirm = f"""
    <button style='
        display: inline-block;                      
        zoom: 1;
        padding: 6px 20px;
        margin: 0;
        cursor: pointer;
        border: 1px solid #bbb;
        overflow: visible;
        font: bold 13px arial, helvetica, sans-serif;
        text-decoration: none;
        white-space: nowrap;
        color: #555;

        background-color: #ddd;
        background-image: -webkit-gradient(linear, left top, left bottom, from(rgba(255,255,255,1)), 
        to(rgba(255,255,255,0)));
        background-image: -webkit-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -moz-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -ms-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -o-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));

        -webkit-transition: background-color .2s ease-out;
        -moz-transition: background-color .2s ease-out;
        -ms-transition: background-color .2s ease-out;
        -o-transition: background-color .2s ease-out;
        transition: background-color .2s ease-out;
        background-clip: padding-box; /* Fix bleeding */
        -moz-border-radius: 3px;
        -webkit-border-radius: 3px;
        border-radius: 3px;
        -moz-box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        -webkit-box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        text-shadow: 0 1px 0 rgba(255,255,255, .9);

        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;' onmouseover="this.style.backgroundColor = '#555'"; 
        onmouseout="this.style.backgroundColor = '#ddd';" 
        type="submit" name="confirmation" value="yes">Potwierdź</button>                    
"""

button_back = f"""             
    <button style='
        display: inline-block;                      
        zoom: 1;
        padding: 6px 20px;
        margin: 0;
        cursor: pointer;
        border: 1px solid #bbb;
        overflow: visible;
        font: bold 13px arial, helvetica, sans-serif;
        text-decoration: none;
        white-space: nowrap;
        color: #555;

        background-color: #ddd;
        background-image: -webkit-gradient(linear, left top, left bottom, from(rgba(255,255,255,1)), to(rgba(255,255,255,0)));
        background-image: -webkit-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -moz-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -ms-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: -o-linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));
        background-image: linear-gradient(top, rgba(255,255,255,1), rgba(255,255,255,0));

        -webkit-transition: background-color .2s ease-out;
        -moz-transition: background-color .2s ease-out;
        -ms-transition: background-color .2s ease-out;
        -o-transition: background-color .2s ease-out;
        transition: background-color .2s ease-out;
        background-clip: padding-box; /* Fix bleeding */
        -moz-border-radius: 3px;
        -webkit-border-radius: 3px;
        border-radius: 3px;
        -moz-box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        -webkit-box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        box-shadow: 0 1px 0 rgba(0, 0, 0, .3), 0 2px 2px -1px rgba(0, 0, 0, .5), 0 1px 0 rgba(255, 255, 255, .3) inset;
        text-shadow: 0 1px 0 rgba(255,255,255, .9);

        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;' onmouseover="this.style.backgroundColor = '#555'"; 
        onmouseout="this.style.backgroundColor = '#ddd'; this.color = '#555';" 
        onclick="window.history.back();" type="button">Wróć</button>
"""
