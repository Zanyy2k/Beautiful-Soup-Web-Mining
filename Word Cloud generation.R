library("tm")
library("plyr")
library("class")
library("RTextTools")

# Load in the required files 
setwd("C:/Users/zyu/Desktop/SocialMedia_Analysis")
JML_Yelp <- read.csv("C:/Users/zyu/Desktop/SocialMedia_Analysis/JML_Yelp.csv")

# collapse the rows into text
Yelp_Reviews = paste(JML_Yelp$Reviews, collapse="")

# Text Cleaning
# Remove punctuation
df = data.frame(Yelp_Reviews, stringsAsFactors = FALSE)
myCorpus = Corpus(VectorSource(df))

myCorpus = tm_map(myCorpus, content_transformer(tolower))
myCorpus = tm_map(myCorpus, removePunctuation)
myCorpus = tm_map(myCorpus, removeNumbers)
myCorpus = tm_map(myCorpus, removeWords, stopwords("english"))
myCorpus = tm_map(myCorpus, removeWords, c("p","lang","Malone","malon","Jo","plaza"))
myCorpus = tm_map(myCorpus, stemDocument)

# Start of Analysis
tdm = TermDocumentMatrix(myCorpus, control = list(wordLengths = c(1,Inf)))

library(wordcloud)
m = as.matrix(tdm)
#calculate the frenquency of words and sort it by frequency
word.freq = sort(rowSums(m),decreasing=T)
wordcloud(words = names(word.freq),
          freq = word.freq,
          random.order = F,
          ordered.colors = T)
