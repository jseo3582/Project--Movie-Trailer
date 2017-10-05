# Movie Trailer Website
This source code for a Movie Trailer website.

## Installation
Excuting `media.py` will automatically generate html file and open this page.

## Files
This code composed with three python files.
### 1. media.py
- `Movie` _class_ defined in this file
- Four data set was defined as following order.
```
movie_titile
movive_storyline
poster_image
trailer_youtube
```
### 2. movie.py
> movie data stored at `movie.py`

### 3. fresh_tomatoes.py
- Create Html file
- all the setting detail stored
- For example, 'trailer video size' can change by editing `trailer .modal-dialog` section

## Add a new movie on the website
- Entire data stored in `movie.py`, so you should editing this file.
- In order to adding a new movie following this instruction.
##### Step 1. add new informations
- Copy the code below and replace each element.
```
An instance of a movie = media.Movie("title of movie",
                                    "story of movie",		      
                                    "movie poster link",		      
                                    "movie trailer video link")
```
- _An example_
```
toy_story = media.Movie("Toy Sotry",
                        "A story of a boy and his toys that come to life",
                        "http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg",
                        "https://youtu.be/KYz2wyBy3kc")
```
##### Step 2. Add the instance at movie
- You must add the instance what you choose at the step 1 to `movie = [HERE]`
- `movie = [HERE]` find at end of the code in `media.py`
 

- _An example_
> if you are adding a movie *__Iron Man__*
If you give a instance as `iron_man`, the instance should inside of the list `movie = []`
```
movie = [Iron_Man]
```

## Copyright and Licensing
The 'movie.py' is a public domain work, dedicated using [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to do whatever you want with it.


