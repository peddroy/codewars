# Reversed Words
# https://www.codewars.com/kata/51c8991dee245d7ddf00000e


# First attempt

sentence <- "hello world!"

solution <- function(sentence){
  split_words <- strsplit(sentence, split=' ')
  words_amount <- length(split_words[[1]])
  reverse_sentence <- split_words[[1]][words_amount:1]
  paste(reverse_sentence, collapse = ' ')
}

solution(sentence)


# Clever

solution <- function(sentence){
  paste(rev(unlist(strsplit(sentence, " "))), collapse = " ")
}

solution <- function(sentence){
  strsplit(sentence, ' ') %>% 
    unlist %>% 
    rev %>% 
    paste(collapse = ' ')
}




