#sentiment function
library(plyr)
library(stringr)

# Load in the required files 
setwd("C:/Users/zyu/Desktop/Web")
# Import csv file
JML_Yelp <- read.csv("C:/Users/zyu/Desktop/Web/JML_Yelp.csv")
# Select the review column
Yelp_Reviews = JML_Yelp$Reviews

# Positive and negative words
pos.words = scan('positive_words.txt', what = 'character', sep = ',')
neg.words = scan('negative_words.txt', what = 'character', sep = ',')
trimws(pos.words) #Remove white space head and tail
trimws(neg.words) #Remove white space head and tail

score.sentiment = function(sentences, pos.words, neg.words, .progress='none')
{
  require(plyr)
  require(stringr)
  
  scores = laply(sentences, function(sentence, pos.word, neg.word){
    # clean up sentences with R's regex-driven global substitute, gsub():
    sentence = gsub('<p lang="en">','',sentence)
    sentence = gsub('</p>','',sentence)
    sentence = gsub('</br','', sentence)
    # and convert to lower case: 
    sentence = tolower(sentence)
    # split into words.str_split is in the stringr package
    word.list = str_split(sentence, '\\s+')
    # sometims a list() is one level of hierarchy too much
    words = unlist(word.list)
    # compare our words to the dictionaries of positive & negative terms
    pos.matches = match(words, pos.words)
    neg.matches = match(words, neg.words)
    # match() returns the position of the matched term or NA
    # we just want a TRUE/FALSE:
    pos.matches = !is.na(pos.matches)
    neg.matches = !is.na(neg.matches)
    # and conveniently enough, True/False will be treated as 1/10 by sum():
    score = sum(pos.matches) - sum(neg.matches)
    return(score)
  }, pos.words, neg.words)
  scores.df = data.frame(score=scores, text=sentences)
  return(scores.df)
}   

#score all yelp revies 
review.scores = score.sentiment(Yelp_Reviews, pos.words, neg.words, .progress = 'text')
path = "C:/Users/zyu/Desktop/Web"
# write.csv(review.scores, file=paste(path,"reviewscore.csv", sep=""), row.names = TRUE)
