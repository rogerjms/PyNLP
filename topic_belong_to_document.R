library(topicmodels)
data("AssociatedPress", package = "topicmodels")

k <- 5 # set number of topics
# generate model
lda <- LDA(AssociatedPress[1:20,], control = list(alpha = 0.1), k)
# now we have a topic model with 20 docs and five topics

# make a data frame with topics as cols, docs as rows and
# cell values as posterior topic distribution for each document
gammaDF <- as.data.frame(lda@gamma) 
names(gammaDF) <- c(1:k)
# inspect...
gammaDF
# Now for each doc, find just the top-ranked topic   
toptopics <- as.data.frame(cbind(document = row.names(gammaDF), 
  topic = apply(gammaDF,1,function(x) names(gammaDF)[which(x==max(x))])))
# inspect...
toptopics   


#完全可以用到good bai