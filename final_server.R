# import the library we used
library(ggplot2)
library(plotly)
library(bslib)
library(dplyr)
library(ggplot2)
library(tidyverse)
library(mapproj)
library(maps)
library(scales)

# load the data
vac_data <- read.csv("https://raw.githubusercontent.com/info-201b-wi22/final-project-IrisDin/main/country_vaccinations.csv?token=GHSAT0AAAAAABRSLIK3YEJGA3WQGF2Q4LS6YR2H3CA")
vac_type_data <- read.csv("https://raw.githubusercontent.com/info-201b-wi22/final-project-IrisDin/main/country_vaccinations_by_manufacturer.csv?token=GHSAT0AAAAAABRSLIK2HHCUSLMYD6G2WNIOYR2H36Q")
# change the numbers into scientific notation
options(scipen=999)

server <- function(input, output) {
    # creating interactive bar plot
    output$vacplot <- renderPlotly({
    vac_type_data$date <- as.Date(vac_type_data$date)
    vac_type_data <- vac_type_data %>% filter(vaccine == input$vac_type)
    vac_plot <- ggplot(data = vac_type_data) +
      aes(x = date, fill = vaccine, group = vaccine, weight = total_vaccinations) +
      geom_bar() +
      coord_flip() +
      scale_fill_brewer("Vaccine", palette = "Dark2")+
      scale_y_continuous(labels = scales::label_number_si()) +
      labs(x = "Date", y = "Total Vaccination", title = "Vaccine types used in the world") +
      theme_minimal() +
      facet_wrap(~vaccine, scales="free")
    # change the style of the civilization
    vac_plot <- vac_plot + theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
    # Make interactive plot
    # change hover text
    my_plotly_plot <- ggplotly(vac_plot, tooltip = c("vaccine"))
    return(my_plotly_plot)
  })
  
  # line_daily was the interactive line chart we are creating
  output$line_daily <- renderPlotly({
    vac_data$date <- as.Date(vac_data$date)
    my_plot <- vac_data %>% filter(country == input$user_category) %>% filter(date >= input$date[1] & date <= input$date[2])
    plots <- ggplot(data = my_plot) + geom_line(mapping = aes(x = date, y = daily_vaccinations, color = country)) +
      scale_y_continuous(labels = scales::label_number_si())+
      labs(x = "Date", y = "daily Vaccination", title = "Daily vaccination trend")
    my_plotly_plot <- ggplotly(plots)
    return(plots)
  })
  
  # creating the interactive the map
  processed <- vac_data %>%  select(country, date, total_vaccinations, people_fully_vaccinated, daily_vaccinations) %>% group_by(country) %>% filter(date == max(date)) 
  processed <- rename(processed, region = country)
  processed[processed == 'United States'] <- 'USA'
  world_shape <- map_data("world")
  world_shape <- left_join(world_shape, processed, by="region")
  
    chart1 <- ggplot(world_shape) +
      geom_polygon(mapping = aes(x = long, y = lat, group = group, fill = daily_vaccinations)) + 
      scale_fill_continuous(low = 'yellow', high ='red', labels = scales::label_number_si()) +
      coord_map() +
      labs(title = 'Daily Vaccinations world map', fill = 'Daily vaccinations')
    
    
    chart2 <- ggplot(world_shape) +
      geom_polygon(mapping = aes(x = long, y = lat, group = group, fill = people_fully_vaccinated)) + 
      scale_fill_continuous(low = 'yellow', high ='green', labels = scales::label_number_si()) +
      coord_map() +
      labs(title = 'People fully vaccinated world map', fill = 'people_fully_vaccinated')
    
    chart3 <- ggplot(world_shape) +
      geom_polygon(mapping = aes(x = long, y = lat, group = group, fill = total_vaccinations)) + 
      scale_fill_continuous(low = 'blue', high ='green', labels = scales::label_number_si()) +
      coord_map() +
      labs(title = 'Total Vaccinations world map', fill = 'total_vaccinations')

    # manually set the graph
    output$map <- renderPlotly({
      if (input$choice == 'daily_vaccinations') {
        result1 <- ggplotly(chart1)
        return (result1)
      }
      else if (input$choice == 'total_vaccinations') {
        result2 <- ggplotly(chart2)
        return (result2)
      }
      else if (input$choice == 'people_fully_vaccinated') {
        result3 <- ggplotly(chart3)
        return (result3)
      }
    })
  }