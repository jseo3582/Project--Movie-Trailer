import media
import fresh_tomatoes

# movie data start here
toy_story = media.Movie(
    "Toy Sotry",
    "A story of a boy and his toys that come to life",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZ"
    "WJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
    "https://youtu.be/KYz2wyBy3kc")

pianist = media.Movie(
    "Pianist",
    "A Polish Jewish musician struggles to survive the destruction"
    "of the Warsaw ghetto of World War II.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdkMzE3ND"
    "ctZGI3ZC00ZjZmLWFlMGMtZmNmZTFiYTAyNzU5XkEyXkFqcGdeQXVyNDkzNTM2OD"
    "g@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
    "https://youtu.be/u_jE7-6Uv7E")

schindlers_list = media.Movie(
    "Schindler's List",
    "In German-occupied Poland during World War II, Oskar Schindler gradually"
    "becomes concerned for his Jewish workforce after witnessing their"
    "persecution by the Nazi Germans.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00"
    "NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR"
    "0,0,666,1000_AL_.jpg",
    "https://youtu.be/gG22XNhtnoY")

pearl_harbor = media.Movie(
    "Pearl Harbor",
    "A tale of war and romance mixed in with history. The story follows two"
    "lifelong friends and a beautiful nurse who are caught up in the horror of"
    "an infamous Sunday morning in 1941.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ3MDc0MDc1NF5BMl5"
    "BanBnXkFtZTYwODI1ODY2._V1_.jpg",
    "https://youtu.be/yzK0GBEkFxc")

tears_of_the_sun = media.Movie(
    "Tears of The Sun",
    "A Special-Ops commander leads his team into the Nigerian jungle in order"
    "to rescue a doctor who will only join them if they agree to save 70 "
    "refugees too.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMmI3YjQ4NjctZTk0Z"
    "i00ZDFhLTgyZjAtYWRjZTJjMjMwNjM2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzN"
    "DI@._V1_.jpg",
    "https://youtu.be/rMuX3uGQfic")

furious_seven = media.Movie(
    "Furious 7",
    "Deckard Shaw seeks revenge against Dominic Toretto and his family for "
    "his comatose brother. RIP Paul Walker.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxOTA2NDUzOV5B"
    "Ml5BanBnXkFtZTgwNzY2MTMxMzE@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
    "https://youtu.be/Skpu5HaVkOc")

star_trek_into_darkness = media.Movie(
    "Star Trek Into Darkness ",
    "After the crew of the Enterprise find an unstoppable force of terror"
    "from within their own organization, Captain Kirk leads a manhunt to a"
    "war-zone world to capture a one-man weapon of mass destruction.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NzczOTgxNF5BM"
    "l5BanBnXkFtZTcwODQ5ODczOQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://youtu.be/QAEkuVgt6Aw")

saving_private_ryan = media.Movie(
    "Saving Private Ryan",
    "Based on a World War II drama. US soldiers try to save their comrade, "
    "paratrooper Private Ryan, who's stationed behind enemy lines.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZjhkMDM4MWItZTVjO"
    "C00ZDRhLThmYTAtM2I5NzBmNmNlMzI1XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_C"
    "R0,0,679,1000_AL_.jpg",
    "https://youtu.be/RYExstiQlLc")

black_hawk_down = media.Movie(
    "Black Hawk Down",
    "160 elite U.S. soldiers drop into Somalia to capture two top lieutenants "
    "of a renegade warlord and find themselves in a desperate battle with a "
    "large force of heavily-armed Somalis.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BYWMwMzQxZjQtODM1Y"
    "S00YmFiLTk1YjQtNzNiYWY1MDE4NTdiXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_S"
    "X675_AL_.jpg",
    "https://youtu.be/5Y1ju8QwpQM")

we_were_soldiers = media.Movie(
    "We Were Soldiers",
    "The story of the first major battle of the American phase of "
    "the Vietnam War and the soldiers on both sides that fought it, "
    "while their wives wait nervously and anxiously at home for "
    "the good news or the bad news.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmN2VmNmYtOGEx"
    "NC00MmE4LTliOTUtOGMzMzFhMTNlOTM1L2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzN"
    "DI@._V1_.jpg",
    "https://youtu.be/If-UCjzRFfk")

the_hurt_locker = media.Movie(
    "The Hurt Locker",
    "During the Iraq War, a Sergeant recently assigned to an army bomb squad "
    "is put at odds with his squad mates due to his maverick way of handling "
    "his work.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzEwNzQ1NjczM15BM"
    "l5BanBnXkFtZTcwNTk3MTE1Mg@@._V1_.jpg",
    "https://youtu.be/hqsnhopttVw")

act_of_valor = media.Movie(
    "Act Of Valor",
    "An elite team of Navy SEALs embark on a covert mission to recover "
    "a kidnapped CIA agent.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3NDQxMDAzM15BM"
    "l5BanBnXkFtZTcwNzEyNjgzNw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://youtu.be/ZnlPgo9TaGo")

# This is a list of instances. Unless you add the instance here,
# the web page will not show the movie.
movies = [
    toy_story, pianist, schindlers_list, pearl_harbor,
    tears_of_the_sun, furious_seven, star_trek_into_darkness,
    saving_private_ryan, black_hawk_down, we_were_soldiers,
    the_hurt_locker, act_of_valor]

# Excuting this code and open the webpage
fresh_tomatoes.open_movies_page(movies)
