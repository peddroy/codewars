# Exclamation marks series #2: Remove all exclamation marks from the end of sentence
# https://www.codewars.com/kata/57faece99610ced690000165

# First attempt

string <- "Hi!"

remove <- function(string) {
  string <- gsub('!', '', string)
  return(string)
}

remove(string)

#Second attempt

rm(remove)
rm(string)

string <- "Hi! Hi!"

remove <- function(string) {
  string <- strsplit(string, '')[[1]]
  a <- ''
  
  for (i in string){
    if (i == '!') {
      a <- append(a, '')
    } else {
      a <- append(a, i)
    }
  }
  a <- paste(a, collapse = '')
  return(a)
}

remove(string)



