## Search imdb using python and command line
This afternoon someone told me about a movie they watched called "Kite".

The movie rang a bell but I couldn't remember if I had seen it or anything else about it so I decided I would look it up. It was at this moment that I thought "hang on! there should be an api for imdb so that I can integrate it into my bot and do a search write within discord.

Enter this repo :) 

The project uses [IMDbPY](https://github.com/alberanid/imdbpy)

### To get started:
- Install module using:
    ```pip install git+https://github.com/alberanid/imdbpy ```
or
    ``` pip install imdbpy ```
- Once installed, you can use the [Quick-Start](https://imdbpy.readthedocs.io/en/latest/usage/quickstart.html#searching) to get started.

### Usage:
To use my script as it stands at time of writing.

``` python search.py -m movie [-p people | -k keyword ] ```
