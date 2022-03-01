# Well of Ideas - Easy Version
# https://www.codewars.com/kata/57f222ce69e09c3630000212/train/r


# First attempt

x <- c('bad', 'good', 'good')

well <- function(x) {
  count_good <- 0
  for (i in x) {
    if (i == 'good') {
      count_good <- count_good + 1
    }
  }
  if (count_good == 0) {
    paste('Fail!')
  } else if (count_good == 1 | count_good == 2) {
    paste('Publish!')
  } else {
    paste('I smell a series!')
  }
}

well(x)

# Clever

well <- function(x){
  if (sum(x == "good") > 2) {
    "I smell a series!"
  } else if (sum(x == "good") > 0) {
    "Publish!"
  } else {
    "Fail!"
  }
}


