Assessment brief: 
 
My project aims to generate a personalized 20-song playlist from a random selection of songs by using machine learning algorithms to model a user's preferences. I began my project by trying to understand how the Spotify API works what features it has and how it can be used. This initial first step was very difficult and took me a long time to retrieve data as there were problems with the API’s limits to how many calls I could make and how much data I was able to extract. In the end, I was able to navigate this problem by making multiple CSV files and merging them using pandas. I decided that I was going to use two machine learning algorithms in my project and two greedy algorithms to help me choose the best songs. 

Algorithm One: For the user top songs dataset I want to apply a greedy algorithm to select the top songs by popularity that would go into a sub playlist without exceeding a duration limit. I decided to do this because, for my later algorithms, I wanted a small number of songs.

Algorithm Two: To train my model I decided to use a random forest classifier. I began by creating a data frame with both user songs and random songs labeled with a dummy variable (0 and 1) in a label column. I then trained my random forest classifier on the available features to select the user songs from the random songs. The results of this model were 85% accurate which I thought was good. I then used this model on an unseen dataset with just the random songs and selected the top 50 songs that were most likely to be in the user's library. 

Algorithm Three: For the third algorithm I wanted to select the top 20 most acoustic songs from the list. The first algorithm I tried to do this was a divide and conquer algorithm, however, when I ran this it came up with the error that the maximum recursion depth had been reached so I knew that this wasn't an appropriate algorithm to use. I then decided to run a greedy algorithm that simply lists the songs in descending order for acousticness and then selects the top tracks, this is a much simpler algorithm.

Algorithm Four: This last algorithm uses a Markov chain algorithm to order the songs in the playlist in regards to both tempo and energy.

The first thing it does is calculate the difference in tempo and energy between consecutive songs in the playlist. It then uses a function to calculate the transition probabilities. It selects a random song from the list as the initial song then it uses the transitional probabilities to select the next song.

My algorithm then exports the selected 20 songs into a Spotify playlist in the chosen order. 

