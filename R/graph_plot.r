# Setup
setwd("/home/alois/Bureau/Demarche_Scientifique/La-patate-ideale")

# Load data
data <- read.table("sortie/tauxGC.txt", sep = "\t", header = TRUE)

setwd("/home/alois/Bureau/Demarche_Scientifique/La-patate-ideale/sortie")
plot(data[,1], data[,2], type = "l", xlab = "Position", ylab = "Taux GC", main = "ORI") #nolint
print("Dot plot done")
