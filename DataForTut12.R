### Making the data for Q2 ###

setwd('/Users/andrewguinness/Google Drive/ND/Fall 17/Intro to Biocomputing/Intro_Biocom_ND_319_Tutorial12')
library(stringr)

SS <- round(runif(10, 111111111, 999999999))
SS <- as.character(SS)
SS <- paste(substr(SS, 1, 3), substr(SS, 4, 5), substr(SS, 6, nchar(SS)), sep = '-')


hours <-  sample(00:23, 15)
hours <- as.character(hours)
for(i in 1:15){
  if(nchar(hours[i]) == 1){
    hours[i] = paste("0", hours[i], sep = '')
  }
}
minutes <- sample(00:59, 15)
minutes <- as.character(minutes)
for(i in 1:15){
  if(nchar(minutes[i]) == 1){
    minutes[i] = paste("0", minutes[i], sep = '')
  }
}

times <- paste(hours, minutes, sep = ':')



sp <- c("H. sapiens", "C. pipiens", "H. cecropia", "E. coli", "R. pomonella")

list <- as.list(c(times, SS, sp))

write.table(list, "pattern.txt", row.names = F, col.names = F, sep = '\n')
