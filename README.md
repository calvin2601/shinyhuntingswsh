# shinyhuntingswsh

## Context

### Background Info
As you may already know, Pokemon is about collecting a variety of creatures and battling them. But there is a subsection of players who play the game around Shiny POkemon

### What is a shiny Pokemon?

Pokemon generally come in a particular colour, such as Pikachu's being yellow and only yellow...for the most part, but there is a very small chance that a Pokemon can be a different colour as so:


<img src="https://archives.bulbagarden.net/media/upload/thumb/5/56/Spr_7p_006.png/600px-Spr_7p_006.png" alt="Shiny Charizard" width ="400" height=auto title="Shiny Charizard"> 
Normal Charizard (orange)



<img src="https://archives.bulbagarden.net/media/upload/thumb/6/63/Spr_7p_006_s.png/400px-Spr_7p_006_s.png" alt="Shiny Charizard" width ="400" height=auto title="Shiny Charizard">
Shiny Charizard (black)

For some Pokemon, the alternative colour scheme may look better. If you combine that with the rarity of encountering a Shiny Pokemon, they can become highly sought after. There is even a subreddit with over 200k subscribers. ([r/ShinyPokemon](https://www.reddit.com/r/ShinyPokemon/))

As I mentioned before, they are rare. The probability is 1/4096 in current (Gen6+) games (used to be 1/8192) but there are methods to increase your odds. It is therefore very unlikely to run into one during a normal playthrough of the game and so people who want a Shiny Pokemon will typically have to Shiny Hunt, ie keep on encountering Pokemon until they get a Shiny Pokemon and this can take a very long time, where spending weeks or even years in some cases is not unheard of.

[One Man's Five-Year Quest To Find A Shiny Pokémon](https://kotaku.com/one-mans-five-year-quest-to-find-a-shiny-pokemon-1603763304)

Considering the monotonous nature of Shiny Hunting, you may have lapses in concentration and run away from a Shiny Pokemon by accident as you may be distracted by something else, eg I would personally Shiny Hunt when watching something to help deal with the tedium. These fails are very well-documented on the internet such as:

https://youtu.be/dcUUbGb77tY?t=471 (watch from 7:50 if the timestamp doesn't work)

You can easily find other examples on youtube.

Also sometimes the colour may not differ greatly as well and so it may be hard to tell depending on which generation of game that you are playing and some visual effects may mask the difference even more. Those with eyesight problems such as colourblindness may also have trouble distinguishing the two forms.

[11 Shiny Pokemon That Look Nearly Identical To Their Original Form](https://www.thegamer.com/shiny-pokemon-original-design/)

And this is where my Python Script comes in.

## How my Python Script Works on a Basic Level

The aim of this script is to provide a safety net so that you won't miss a Shiny Pokemon.

![](https://github.com/calvin2601/shinyhuntingswsh/blob/main/normalshinycomparison.gif)


As shown in the above gif, the added sparkles (the shiny animation) on the right hand side means that the time between the two text boxes is substantially longer. This Python script will monitor this transition time and if it is longer than usual, it will alert you via sound that a Shiny Pokemon has appeared as well as printing a message in the console.

## How my Python Script Works in More Detail



## Some things to note with this script

1. These scripts in particular only work in Pokemon Sword and Shield using the random encounter method, max raids or soft resetting.
2. These scripts can be modified for Pokemon Brilliant Diamond and Shining Pearl but you will need to redo images and make sure that the region of interest is appropriate for those games as I have [here](place github repo here).
3. While these scripts can be modified for games where the overworld sprites can be shiny, the scripts lose their usefulness by a fair amount as when you see a shiny in the overworld then you would force an encounter by walking up to it. The only way I can see these scripts being useful is if you walk up to a Pokemon and didn't know that it was shiny and you looked away so you would miss the sparkles etc.
4. The max raid script may produce false positives (ie it thinks there is a Shiny Pokemon when there isn't) as some certain Pokemon animations when encountering can last longer than the usual time needed for the sparkles to appear. I did not account for this for now as it should not happen often enough to fix. If it does produce a shiny sound alert, I would probably do visual check if the pokemon is shiny and if you are not sure, just capture it and check its shiny status in the summary screen. Better to be safe than sorry!
5. Because opencv relies upon comparing the feed appearing on your PC screen to screenshots captured in the past, any changes to how your display works like gpu drivers, display calibration etc may affect if the script works or not. An extreme example would be for whatever reason, your captured screenshots were in black and white as your gpu can only show in black and white but new gpu drivers now allow colour to be displayed and so your video feed is in colour now. Now the region of interest of both your screenshots and video feed can never match and can never satisfy conditions in the code. I would redo the captured images first if the script does not work.
6. You can force a false positive to see if the alerts etc work by clicking and holding the window in the gap between the two boxes indicating when you have encountered a wild pokemon and when you have sent out your own Pokemon so that the feed freezes but the Python code is still keeping time. You let go after enough time has to satisfy the time condition (in this case over 1 second) and a sound alert should be produced.




