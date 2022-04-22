###########################################
#-------------Premier graphique-----------#
###########################################

# Load data
data <- read.table("sortie/tauxGC.txt", sep = "\t", header = TRUE) # nolint

# Set up the plot
setwd("sortie")

# Plot
plot(data[,1], data[,2], type = "l", xlab = "Position en kilobases", ylab = "Taux GC", main = "ORI", ylim = c(20,50)) #nolint
print("Plot done")