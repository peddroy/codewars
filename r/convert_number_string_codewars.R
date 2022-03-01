# Convert a Number to a String!
# https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/r


# First attempt


n <- 67
class(n)

number_to_string <- function(n){
  n <- as.character(n)
  return(n)
}

number_to_string(n)
class(n)


# Clever

number_to_string <- function(n) {
  as.character(n)
}
