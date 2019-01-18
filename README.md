# WEC 2019 Competition

Mitch Adam, Kyle Hennig, Nayan Prakash, and Ryan Shukla.
Team Osborne Village.

## Getting started
Backend code can be found in the server folder.<br>
Frontend code can be found in the client folder.

## Dependencies
We used PixiJS for 2D rendering.<br>
http://www.pixijs.com/<br>
Tornado web server.<br>
`pip install tornado`

## Running our code
Begin by running `python run_server.py`. Python version 3.7 is recommended.<br>
Next, to start our web client, execute `./run_client.sh`.<br>
Open Google Chrome to the webpage http://localhost:8000/ to view the user interface.<br>
Click "Start Game" to begin playing. Click on a basin, and you lose. Find all the basins without clicking one, and you win.<br>

## Running our bot
Begin by running `python run_botserver.py`.
Next, to start our web client, execute `./run_client.sh`.<br>
Open Google Chrome to the webpage http://localhost:8000/ to view the user interface.<br>
Click "Start Bot" to open the grid.<br>
Finally, to run the bot, execute `python run_bot.py`.<br>
