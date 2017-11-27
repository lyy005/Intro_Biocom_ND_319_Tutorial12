### Making the data for Q2 ###

library(stringr)

SS <- round(runif(10, 111111111, 999999999))
SS <- as.character(SS)
paste(substr(SS, 1, 3), substr(SS, 4, 6), substr(SS, 7, nchar(SS)), sep = '-') -> SS


hours <-  sample(12:23, 10)
minutes <- sample(00:59, 10)
times <- paste(hours, minutes, sep = ':')


sp <- c("H. sapiens", "C. pipiens", "H. cecropia", "E. coli", "R. pomonella")

list <- as.list(c(times, SS, sp))

write.table(list, "pattern.txt", row.names = F, col.names = F)