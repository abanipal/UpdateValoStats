immo3_map <- read.csv("map_data/maps_competitive_tier=26.csv")
plat3 <- read.csv("map_data/maps_competitive_tier=17.csv")
ggplot(immo3_map, aes(atkWin, numMatches))+
  geom_point(aes(color=Map))
str(plat3)
ggplot(plat3, aes(Map, defWin))+
  geom_boxplot()
#i don't think a box plot works well with map data
#we haven't finished fixing the python script that scraps data from blitz.gg, we're doing this since the data we have is old