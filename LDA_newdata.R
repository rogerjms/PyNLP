library(topicmodels)
data(AssociatedPress)

train <- AssociatedPress[1:100,]
test <- AssociatedPress[101:150,]

train.lda <- LDA(train,5)
terms(train.lda)
(train.topics <- topics(train.lda))


test.topics <- posterior(train.lda,test)
(test.topics <- apply(test.topics$topics, 1, which.max))
