###########################################
#-------------Premier graphique-----------#
###########################################
# Setup
directory <- getwd()

# Load data
data <- read.table("sortie/tauxGC.txt", sep = "\t", header = TRUE) # nolint

# Set up the plot
setwd("sortie")
# Plot
plot(data[, 1], data[, 2], type = "l", xlab = "Position en kilobases", ylab = "Taux GC", main = "ORI", ylim = c(20, 50)) # nolint
print("Plot done")
############################################
#-------------Deuxième graphique-----------#
############################################
# Setup
setwd(directory)

# Load data
data <- read.table("sortie/calcGC.txt", sep = "\t", header = TRUE) # nolint

# Set up the plot
setwd("sortie")
# Plot
plot(data[, 1], data[, 2], type = "l", xlab = "Position en kilobases", ylab = "G-C/G+C", main = "ORI", ylim = c(-40, 40)) # nolint
abline(h = 0, col = "blue", lwd = 2)
print("Second plot done")