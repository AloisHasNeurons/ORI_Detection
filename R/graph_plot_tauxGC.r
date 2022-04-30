###########################################
#---------------Taux de GC ---------------#
###########################################


setwd("sortie")
# Load data
data <- read.table("tauxGC.txt", sep = "\t", header = TRUE) # nolint


# Plot
plot(data[, 1], data[, 2], type = "l", xlab = "Position en kilobases", ylab = "Taux GC", main = "Graphique representant le taux de GC en fonction des kilobases", ylim = c(20, 50)) # nolint
print("Plot done")