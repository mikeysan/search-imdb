## Search imdb using python and command line
This afternoon someone told me about a movie they watched called "Kite".

The movie rang a bell but I couldn't remember if I had seen it or anything else about it so I decided I would look it up. It was at this moment that I thought "hang on! there should be an api for imdb so that I can integrate it into my bot and do a search right within discord.

Enter this repo :) 

The project uses [IMDbPY](https://github.com/alberanid/imdbpy)

### To get started:
- You need a terminal or Command line for Windows (Powershell)
- Python 3.8.6+
- Install module using: Note these commands work for Linux and MacOS. For Windows use `pip` instead of `pip3`

```
    pip3 install git+https://github.com/alberanid/imdbpy
    
```
or

```
pip3 install -r requirements.txt

```
or

 ```
    pip3 install imdbpy
    
```
- Once installed, you can use the [Quick-Start](https://imdbpy.readthedocs.io/en/latest/usage/quickstart.html#searching) to get started.

### Usage:
To use my script as it stands at time of writing. Open a terminal and navigate to where you saved the files

On Windows:
``` python search.py -m movie [-p people | -k keyword ] ```

On Linux:
``` python3 search.py -m movie [-p people | -k keyword ] ```
