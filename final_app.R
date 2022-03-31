# load the library and source
library(bslib)
library(shiny)
library(rsconnect)
source("final_ui.R")
source("final_server.R")
# Publish your Shiny App to the web
shinyApp(ui = ui, server = server)