neuron <- function(x, state, weights)
{
  maxact <- 0
  for(e in matrix[x,]){
    if (e > 0) maxact <- maxact + e
  }
  
  activation <- state %*% weights[x,] # dot product
  
  if (activation > 0){
    activation <- activation / maxact
    return(activation ** 4)
  }
  
  return(0.0)
}
  
tick <- function(state, weights)
{
  new_state <- c(NA)
  
  for (i in 1:length(state)){
    new_state[i] <- neuron(i, state, weights)
  }
  
  return(new_state)
}

init_weights <- function(n_neurons, deviation)
{
  return(matrix(rnorm(n_neurons ** 2, sd=deviation), n_neurons, n_neurons))
}

# reads a string of bits as an unsigned integer and interprets it as a fraction of maximum possible activation
# for that string of bits, i.e. 0101 -> 5/(2^4 - 1) = 0.33..
readin <- function(bits)
{
  n <- 0
  for (i in 1:length(bits)){
    n <- (2 ** (i-1)) * bits[i]
  }
  
  return(n / ((2 ** length(bits)) - 1))
}
  
writeout <- function(activation, n_bits)
{
  intact = floor(activation * ((n_bits ** 2) - 1))
  bits = c(NA)
  
  for (i in 1:n_bits){
    bits[i] <- intact %% 2
    intact = intact / 2
  }
  
  return(bits)
}

