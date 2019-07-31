# Twitter data analytics 
The World's largest democracy India has a lot of buzz on Twitter and other social media platforms this year. I collected tweets related to specific and main party 'BJP,' using the keywords, which were mainly practiced by the party. Keywords such as #chowkidaar, #Mainbhichowkidaar, etc., were intentionally posted by the party under its social media campaign. Thus I decided to gather for those and other keywords used by that specific party. I collected data for the entire month of April, and after that, I performed data visualization techniques to extract insights.
* Tweepy is used to stream the tweets.
* I ran the script on a Linux server as a background process for 1 month. 
* SQLite had been used to store the tweets. 
* Textblob library is used to calculate subjectivity and polarity of tweets at the time of streaming. 
* After one month I got enough data to play with. 
* I exported SQLITE file to CSV and imported in python. 
* Plotly is used for data visualization. 
# Results
* There are three main text fields about user location, description, and text of the tweet. I plotted word cloud of each to assess the 
  Frequent words and overall inclination of the data. Surprisingly I found that there are lot of people who have their location mentioned as Pakistan and Lahore. 
   ----------pic of location 
   
* Further I extracted the year of user sign and days of the tweet twitted from user_created and created fields respectively. These 
  two new variables provide us a lot of insights such as which users are more active in this data , users who signed up in 2008 or who signed up in 2018. Moreover, we extracted which days people tweeted most and Monday and Tuesday are on lead and which devices were mostly used to tweet. We observed the polarity and subjectivity distribution of tweets
  
  --------- pic of days 
  
 * After observing all possible and potential continuos, categorical and text variables of data it was time to observe relations between differnet variables such as how polarity is affected by the user's followers, how polarity of tweets is distributed for the people who signed up in different years and tweets which are twitted on differnet days. There are more observations made between polarity, subjectivity and user followers count for different years etc. 
 
 -------polarity vs user followers 
 ------- scatter matrix 
# Notes
* I have provided the python tweet scraper code file, python data analysis code file of jupyter notebook, each cell contains specific 
  code related to different graphs, doc string is provided of each cell, to understand what is acheived by that code. 
* You can download full data from https://drive.google.com/file/d/1ksxYt6vS2kbq7uA9XztOTBa6XBwDkxhX/view?usp=sharing
# Important 
* Data size is too big to compute on cpu, thus most of the observations I made is based on sample data set extracted from main data, 
 I have provided the sample data set in directory, but you can also download full data set from the link I provided. 

:copyright:Birender Veeer Singh
