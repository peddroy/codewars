# Sum of Multiples
# https://www.codewars.com/kata/57241e0f440cd279b5000829


# First attempt

sum_mul <- function(n, m){
  mul_vec <- 0
  for (i in n:(m-1)) {
    if(n == 0 | m == 0 | n < 0 | m < 0){
      return('INVALID')
    }
    if (n > m | n == m) {
      return(0)
    }
    if((i %% n) == 0) {
      mul_vec <- append(mul_vec, i)
    }
    i <- i + 1
  }
  return(sum(mul_vec))
}

sum_mul(2, 9)


# Clever
sum_mul <- function(n, m){
  if(m <= 0 | n <= 0) {
    "INVALID"
  }
  else if(n >= m) {
    0
  } else {
    result <- c(n:(m-1))
    sum(result[result %% n == 0])
  }
}

sum_mul(2,9)
