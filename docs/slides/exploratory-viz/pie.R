# Libraries
library(tidyverse)
library(hrbrthemes)
library(viridis)
library(patchwork)

# create 3 data frame:
data1 <- data.frame( name=letters[1:5], value=c(17,18,20,22,24) )
data2 <- data.frame( name=letters[1:5], value=c(20,18,21,20,20) )
data3 <- data.frame( name=letters[1:5], value=c(24,23,21,19,18) )

# Plot
plot_pie <- function(data, vec){
  
  ggplot(data, aes(x="name", y=value, fill=name)) +
    geom_bar(width = 1, stat = "identity") +
    coord_polar("y", start=0, direction = -1) +
    scale_fill_viridis(discrete = TRUE,  direction=-1) + 
    geom_text(aes(y = vec, label = rev(name), size=4, color=c( "white", rep("black", 4)))) +
    scale_color_manual(values=c("black", "white")) +
    theme_void() +
    theme(legend.position = "none") + 
    xlab("") +
    ylab("")
  
}

plot_pie(data1, c(10,35,55,75,93))

a <- plot_pie(data1, c(10,35,55,75,93))
b <- plot_pie(data2, c(10,35,53,75,93))
c <- plot_pie(data3, c(10,29,50,75,93))
p1 <- a + b + c

plot_bar <- function(data){
  ggplot(data, aes(x=name, y=value, fill=name)) +
    geom_bar( stat = "identity") +
    scale_fill_viridis(discrete = TRUE, direction=-1) + 
    scale_color_manual(values=c("black", "white")) +
    theme_ipsum() +
    theme(
      legend.position="none",
      plot.title = element_text(size=14),
      panel.grid = element_blank(),
    ) +
    ylim(0,25) +
    xlab("") +
    ylab("")
}

# Make 3 barplots
a <- plot_bar(data1)
b <- plot_bar(data2)
c <- plot_bar(data3)

# Put them together with patchwork
p2 <- a + b + c

p1 / p2
