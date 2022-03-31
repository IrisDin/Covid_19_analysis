# import the library we need to use
library(ggplot2)
library(plotly)
library(bslib)
library(dplyr)
library(ggplot2)
library(tidyverse)
library(shiny)
#load the dataset
vac_data <- read.csv("https://raw.githubusercontent.com/info-201b-wi22/final-project-IrisDin/main/country_vaccinations.csv?token=GHSAT0AAAAAABRSLIK3YEJGA3WQGF2Q4LS6YR2H3CA")
vac_type_data <- read.csv("https://raw.githubusercontent.com/info-201b-wi22/final-project-IrisDin/main/country_vaccinations_by_manufacturer.csv?token=GHSAT0AAAAAABRSLIK2HHCUSLMYD6G2WNIOYR2H36Q")
# data pre-processing
vac_type_data <- rename(vac_type_data, country = location)
options(scipen=999)
vac_type_data$date <- as.Date(vac_type_data$date)
vac_data$date <- as.Date(vac_data$date)

# introduction ui page
intro_tab <- tabPanel(
  "Introduction",
  fluidPage(theme = bs_theme(bootswatch = "minty"),
            img( border="0",src = "https://publichealth.jhu.edu/sites/default/files/styles/article_feature/public/2021-07/carrying-equity-in-covid-19-vaccination-forward.png?h=f2862316&itok=C9sfEOAv", height = 400, width = 700),
            h1("Purpose/Importance:"),
            p("The COVID-19 pandemic has led to the dramatic loss of human life and presents unprecedented challenges to not only public health, but also individual health more importantly. Though, people who had Covid recovered, still Covid do have potential sequelae to the different organs. 
Thus, it is crucial and urgent to get vaccinated and make it universally accessible to ensure a safe condition for the general public. The pandemic is far from over, and vaccines are our best bet on staying safe. As more and more people get vaccinated, the community immunity, 
also individual community would both improve and further secure the invade of the virus. Our main issue is the inconvenience that covid brings to people's lives. This issue is very important because it relates to the long-term impact of covid on humans. To address this issue, 
we will conduct an in-depth analysis of people's willingness and brand of vaccination.",style = "font-size:20px;")
  ),
  br(),
  h1("Main questions🤔:"),
  p("Question 1: To see the trend of people getting vaccinated around the world by analyzing different vaccine brand being used worldwide.",style = "font-size:20px;"),
  br(),
  p("Question 2: Daily vaccination trend in different country and in different period of time.",style = "font-size:20px;"),
  br(),
  p("Question 3: To visualize the distribution of vaccinated population in a world map." ,style = "font-size:20px;",
  br(),
  h1("About the dataset:"),
  p("We found the dataset from the Kaggle site which was collected from the authoritative organization Our World in Data GitHub repository specifically for the covid-19, and it is still continuing to update. There are two files of the dataset, one contains locations, also includes vaccination sources' information. 
            The second file is information about the manufacturers like Moderna and Pfizer. From the comprehensive vaccination information in different countries, people can see the total number of people who get vaccinated in their country which might let them feel safe. Also, from the vaccination information, people can also 
            visualize which country does not access adequate medical resources(vaccinations) that further provided them with help and facilitated the progress to ending the global pandemic.", style = "font-size:20px;"),
  tags$a(href ="https://www.kaggle.com/gpreda/covid-world-vaccination-progress", "Visit kaggle Website to check our data"),
  br(),
  h1("limitations🦠:"),
  br(),
  p("After viewing the dataset, we found out several limitations and problems of the dataset. To begin with, there is a lot of missing values in the front part of the dataset. However, when we scroll down the dataset, there are only a small amount of missing values remaining. To sum up, the missing values only made up a small proportion of the whole dataset. 
            We think we can change the distribution of the missing value after filtering and sorting the dataset by using R. Also, another potential problem with the dataset is that there are over 70000 rows of the dataset which contain all different countries’ vaccination information. This is a large dataset that might be hard to process and filter the core information and pattern we want.
            The potential solution we came up with is that we need to further explore our research question and drop the information or data we do not need. We need to clean and condense our dataset in order to get better visualization. In addition, we think it is necessary for us to add more features to the dataset for better analysis. For example, merging the vaccine type feature can help 
            us better visualize the usage for different brands’ vaccination like Pfizer or Moderna in different areas.",style = "font-size:20px;")
)
)

# summary and takeaway ui page
summary_tab <- tabPanel(
  "Summary/Takeways",
  fluidPage(theme = bs_theme(bootswatch = "minty"),
            img( border="0",src = "https://www.hopkinsmedicine.org/-/media/images/health/1_-conditions/coronavirus/vaccine3.ashx?la=en&hash=E14E7B4842E409C6FC40A8659B1B68F3529C0841", height = 450, width = 700),
            h1("Specific takeaways💉："),
            p("First takeaway: There is an increasing pattern of vaccine types being used in the world and more and more people are getting vaccinated, which shows that people's self-protection awareness is increased as time goes by. Beyond this trend, it is obivious that Pfizer/BioNtech and Moderna are the top two brands that
being used most frequently. By the end of Jan, 2022, more than 600 millions of people have taken the vaccine from Pfizer/BioNtech, which is the most popular brand all over the world.", style = "font-size:20px;"),
            p("Second takeaway: The daily vaccination trend of the U.S. seems steady as time passes and has been kept under 5 millions per day. Compared with the U.S., Chinese daily vaccination rate has been constantly increased from under 5 millions per day to over 10 millions per day. This comparison proves that American people are not taking vaccination as seriously as Chinese do. Moreover, even though the daily vaccination number starts to decrease after Jan, 2022, China still has the highest daily vaccination rate than all of the other countries in the world. ", style = "font-size:20px;"),
            br(),
            p("Third takeaway: China has the most vacccinated population in the world. India is the country that covered with the higest number of daily vaccinations. Since COVID outbreak is relatively early in China, so it is easy to tell that China is the one that 
takes the pandemic most seriously. As its nearby country, India also took immediate actions to fight against the coronavirus. The spreadout of the pandemic is extremly fast throughout the world. Countries with large population density are more able to be infected and
the U.S. has also been influenced severely so it has a relative high vaccinated population as well.", style = "font-size:20px;"),
            p("Forth Takeaway: Up to the most recent data, from the overall trend for the daily vaccinations in the country China, United States, and India all shown a decreasing tendency till the February 1st. Although these are the countries with relatively high daily 
              vaccinations in general. Still, due to the gradual loose policy indifferent region, seems like the number of people getting vaccinated is decreasing. Especially in the United States, for instance, wearing a mask is become optional in some regions, and even 
              at the restaurant, no vaccination verification is needed as well. Thus, it could be a crucial factor that leads to the nowadays trend.", style = "font-size:20px;"),
            br(),
            h1("Insight💡："),
            p("In recent years, the covid-19 pandemic has swept the entire globe and caused a large number of infections and deaths. From the data visualizations we made, we are able to find that China has the highest number of daily vaccinated also has shown the highest number of people fully vaccinated. To some extent, it is the country that most actively prevents and controls the pandemic mostly due to the strict regulations and widespread of vaccinations. And the U.S. also has a relatively high number of daily vaccinations, however, with a low level of people fully vaccinated. It is mostly due to the policy being made within different states and the consciousness of being vaccinated.", style = "font-size:20px;"),
            br(),
            h1("Broader implications："),
            p("As time passes by, the number of immune is increasing and shows that all human beings can recognize the importance of self-protection. People stick together to fight against the COVID-19 and this tough period of time is a historical moment that should be memorized by all human beings. Things are getting better right now and the world is getting covered by vaccines. So there would be more people being vaccinated in future no matter the daily vaccination trend is steady, increased, or decreased. Overall, the majority chooses to be vaccinated not only for protecting themselves, but also for protecting people they care for. ", style = "font-size:20px;")
  )
)

# The bar chart ui setting
type_plot_main <- mainPanel(
  plotlyOutput(outputId = "vacplot"),
  h1("Description/Analysis of the visualization📊:"),
  br(),
  p("The reason why we construct the vaccine used in the world, to be more specific, classified by the brand of the vaccine throughout the world, is to see what's the trend of people getting vaccinated worldwide, and reveals the people's awareness of self-protection. Meanwhile, we can spot among all these different kinds of vaccines, which one is most prevalent after all. From the graphs generated, it is very obvious, considering all the countries as a whole, more and more people getting vaccinated global-wise, an increasing pattern, though there are some sag occurring. Another insight we can extract from the graph is that the most popular vaccines would be Pfizer/BioNtech, Moderna, and Pfizer is the one used most frequently.", style = "font-size:23px;")
)

plot_sidebar_type <- sidebarPanel(
  selectInput(
    inputId = "vac_type",
    label = "Select vaccine",
    choices = vac_type_data$vaccine,
    selected = "Moderna",
    multiple = TRUE
  )
)

vac_type_tab <- tabPanel(
  "Vaccine types used in the world",
  sidebarLayout(
    plot_sidebar_type,
    type_plot_main
  )
)

# The line chart ui setting

line_plot_main <- mainPanel(
  plotlyOutput(outputId = "line_daily"),
  h1("Description/Analysis of the visualization📊:"),
  br(),
  p("The reason why we produce this visualization is to provide our audiences with an overview of the world's vaccination distribution. We offer several vaccination related variables for people to select and view. It is quite obvious that China has the highest daily vaccination and the most vaccinated population in the world.", style = "font-size:23px;")
)

line_sidebar <- sidebarPanel(
  selectInput(
    inputId = "user_category",
    label = "Select country",
    choices = vac_data$country,
    selected = "China",
    multiple = TRUE,
  ),
  dateRangeInput(inputId = "date", label = "Date range",
                 start = '2021-10-01',
                 end  = '2021-12-31')
)

line_daily_vaccination_tab <-tabPanel(
  "Daily vaccination trend",
  sidebarLayout(
    line_sidebar,
    line_plot_main,
  )
)

# the ui setting for map
map_plot_sidebar <- sidebarPanel(
  selectInput(
    inputId = "choice",
    label = "Different vaccination feature distribution",
    # Fill in the correct code here
    choices = c(
      "daily_vaccinations",
      "total_vaccinations",
      "people_fully_vaccinated"
    ),
    selected = "daily_vaccinations"
  )
)

map_plot_main <- mainPanel(
  plotlyOutput(outputId = "map"),
  h1("Description/Analysis of the visualization📊:"),
  br(),
  p("The visualization shown in the figure above provides a clearer and more specific understanding of the global acceptance rate of the vaccine dose. From the figure above, it can be seen that India has the most places for daily vaccination, while China's full vacation is the highest. But it is clear that the total number of people vaccinated nationwide is still low.", style = "font-size:23px;")
)

map_plot_tab <- tabPanel(
  "Maps",
  sidebarLayout(
    map_plot_sidebar,
    map_plot_main
  )
)

# the ui setting for the whole app
ui <- navbarPage(
  "Covid-19 Vaccination Analysis",
  intro_tab,
  vac_type_tab,
  line_daily_vaccination_tab,
  map_plot_tab,
  summary_tab
)