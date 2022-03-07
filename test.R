# Setup
setwd("/home/alois/Bureau/Demarche_Scientifique/La-patate-ideale")

#Creation des dataframe
data <- read.table("Data.txt", sep = "\t", header = TRUE)
data2 <- matrix(data = 0.0, nrow = nrow(data) / 100) + 1, ncol = 2)

dim(data)
data[c(15:19, 1010:1012), 2]

# Ecriture du fichier de sortie
write("", "resultats", append = FALSE)
write("Nombre de lignes de DATA", "resultats", sep = "\t", append = TRUE)
write(nrow(data), "resultats", sep = "\t", append = TRUE)
write("Taux GC pour certaines lignes avec write.table", "resultats", sep = "\t", append = TRUE) # nolint
write.table(data[500:515, 1:2], "resultats", sep = "\t", append = TRUE)
write("Taux GC pour certaines lignes avec write", "resultats", sep = "\t", append = TRUE) # nolint
write(data[500:515, 2], "resultats", sep = "\t", append = TRUE)

# Calculs statistiques
summary(data)
table(data[, 2])
which.max(table(data[, 2]))
which.min(table(data[, 2]))

# Creation d'histogrammes
hist(data[,2], breaks = seq(from = 39, to = 60, by = 1), xlab = "Taux de GC", ylab = "Nb de regions", main = "Nb de regions par taux de GC") # nolint
abline(h = 1300, col = "red", lwd=2)
arrows(40, 3400, 49, 3400, col = "blue", code = 2)

# Utilisation de plot
plot(data[, 1], data[, 2])
