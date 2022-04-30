###########################################
#---------------Taux de GC ---------------#
###########################################


setwd("sortie")
# Load data
data <- read.table("tauxGC.txt", sep = "\t", header = TRUE) # nolint
data2 <- read.table("gcSkew.txt", sep = "\t", header = TRUE) # nolint

# Plot
plot(data[, 1], data[, 2], type = "l", xlab = "Position en kilobases", ylab = "Taux GC", main = "Graphique representant le taux de GC en fonction des kilobases", ylim = c(20, 40)) # nolint
print("Plot done")


############################################
#------------------GC Skew-----------------#
############################################


# Plot
plot(data2[, 1], data2[, 2], type = "l", xlab = "Position en kilobases", ylab = "GC Skew", main = "Graphique representant le GC Skew en fonction des kilobases", ylim = c(-40, 40)) # nolint
abline(h = 0, col = "blue", lwd = 2)
print("Second plot done")