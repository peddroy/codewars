# Fake Binary
# https://www.codewars.com/kata/57eae65a4321032ce000002d/train/r

# First attempt

x <- '45385593107843568'

prefake_bin <- function(x){
    
    x <- strsplit(x, '')[[1]]
    a <-''
    
    for (i in x) {
      if (as.numeric(i) < 5) {
        a <- append(a, '0')
      } else {
        a <- append(a, '1')
      }
    }
    a <- paste(a, collapse = '')
    return(a)
}

prefake_bin(x)


# Clever

rm(x)
rm(a)
rm(prefake_bin)

x <- '45385593107843568'

prefake_bin <- function(x) {
  x <- gsub('[0-4]', 0, x)
  x <- gsub('[5-9]', 1, x)
  return(x)
}

prefake_bin(x)
