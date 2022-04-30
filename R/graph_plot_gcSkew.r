############################################
#------------------GC Skew-----------------#
############################################


setwd("sortie")

# Load data
data <- read.table("gcSkew.txt", sep = "\t", header = TRUE) # nolint

# Plot
plot(data[, 1], data[, 2], type = "l", xlab = "Position en kilobases", ylab = "GC Skew", main = "Graphique representant le GC Skew en fonction des kilobases", ylim = c(-40, 40)) # nolint
abline(h = 0, col = "blue", lwd = 2)
print("Plot done")