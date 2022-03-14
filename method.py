# Course: CSE163
# Author: Frank Iris
# Project Title: Covid-19 World Vccination/Caese Analysis

# import the library we need to use
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import scipy.stats


def vac_world_map(country_df):
    """
    Parameter:
        country_df: a data file that contains the vaccination records
        in the world.
    Argument:
        The vac_world_map method will shows the
        number and distribution of total vaccinations in different countries
        which indicates the global total vacinnation pattern.
        The pattern I generated from the map is the total vaccination number
        seems much more higher in China,India, United State and Brazil.
    Returns:
        An interactive Choropleth map of the total vaccinations
    """
    # data pre-procssing for map data
    # sicne the total vaccination data is cumulative, we just need to sort
    # and find the max number
    total_vac_df = country_df.groupby('country').max()
    interactive_total_vac_world_map = go.Figure(data=go.Choropleth(
        locations=total_vac_df['iso_code'],
        z=total_vac_df['total_vaccinations'],
        text=total_vac_df.index,
        # set the color scale
        colorscale='Viridis',
        # determine whether the color scale is defult
        autocolorscale=False,
        # countries with higher total vaccinations would in dark
        # color and vice versa
        reversescale=True,
        colorbar_title='total_vaccinations',
    ))
    # add titles and set the format/size of the map
    interactive_total_vac_world_map.update_layout(
        width=1200,
        height=550,
        geo=dict(
            showframe=True,
            showcoastlines=True,
        ),
        title={
           'text': 'Total vaccination by country',
           'x': 0.5,
           'xanchor': 'center'
        }
    )
    interactive_total_vac_world_map.show()


def covid_death_map(new_merged):
    """
    Parameter:
        new_merged: a data file that combined the vaccination records
        and COVID case information based on date and country.
    Argument:
        The covid_death_map method will shows the
        number and distribution of cumulative total deathes. The reson I want
        to include this map is not only tracing the distribution of total
        deathes around the world but also with the map to comapre with the
        total vacinations map.
        The assumption we address is when there is a higher
        immunization(vaccination),the cumulative cases would be lower.
    Returns:
        An interactive Choropleth map of the total deaths
    """
    death_max_df = new_merged.groupby('country').max()
    death_map = go.Figure(data=go.Choropleth(
                          locations=death_max_df['iso_code'],
                          z=death_max_df['cumulative_total_deaths'],
                          text=death_max_df.index,
                          # set the color scale
                          colorscale='Viridis',
                          # determine whether the color scale is defult
                          autocolorscale=False,
                          # countries with higher total vaccinations
                          # would in dark color and vice versa
                          reversescale=True,
                          colorbar_title='death map'))
    # add titles and set the format/size of the map
    death_map.update_layout(
        width=1200,
        height=550,
        geo=dict(
            showframe=True,
            showcoastlines=True,
        ),
        title={
               'text': 'Total deathes Map',
               'x': 0.5,
               'xanchor': 'center'
        }
    )

    death_map.show()


def scatter_death_vac(new_merged):
    """
    Parameter:
        new_merged: a data file that combined the vaccination records
        and COVID case information based on date and country.
    Argument:
        The scatter_death_vac method will generates two scatter plots, and it
        will show that whether there are elationship between the
        the vaccination and new deathes, by comparing the daily_vaccinations,
        people_fully_vaccinated and daily_new deaths.
         According to the scatter plot, there is no
        obvious relationship between fully vaccinated status/daily vaccination
        and the increase new death.
    Returns:
        Two scatter plots that saved in the (Relationship between death cases
        and vaccines png.)
    """
    fig = plt.figure()
    # put the plot together
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    # set the figure size
    fig.set_figheight(6)
    fig.set_figwidth(15)
    new_merged = new_merged.dropna()
    fully_vac = new_merged['people_fully_vaccinated']
    daily_vac = new_merged['daily_vaccinations']
    daily_death = new_merged['daily_new_deaths']
    # draw the scatter plots to find relationship
    ax1.scatter(fully_vac, daily_death)
    ax2.scatter(daily_vac, daily_death)
    # add titles and lables
    ax1.set_title('The relationship between people fully vaccinated and daily'
                  'new deaths')
    ax1.set_xlabel('people_fully_vaccinated')
    ax1.set_ylabel('daily_new_deaths')
    ax2.set_title('The relationship between daily vaccinations and daily new'
                  'deaths')
    ax2.set_xlabel('daily_vaccinations')
    ax2.set_ylabel('daily_new_deaths')
    # test r-suqared
    x1 = fully_vac
    x2 = daily_vac
    y = daily_death
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x1, y)
    print("p-value and r-squared for graph fully vaccinated and daily deaths"
          "are: ", p_value, ",", r_value**2)
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x2, y)
    print("p-value and r-squared for graph daily vaccinations and daily deaths"
          "are: ", p_value, ",", r_value**2)
    plt.savefig('Relationship between death cases and vaccines')


def fully_vac_compare(country_df):
    """
    Parameter:
        country_df: a data file that contains the vaccination records
        in the world.
    Argument:
        The fully_vac_compare method will create a bar chat, and it will show
        the fully vaccination progress throughout different countries.
        For better visulization, the bar chart only contains the top 10 country
        with the most people being fully vaccinated.
    Returns:
        A bar chat of the people fully vaccinated in the world.
        The plot is being save in the Top10_country_people_fully_vaccinated.png
    """
    fully = country_df.groupby('country').max()
    # since there are so many countries in the dataset, I just pick the top 10
    # for better visulization
    fully_progress_total = fully.sort_values('people_fully_vaccinated'
                                             )[-10:]
    fig, ax = plt.subplots(1)
    # make the graph huaman readable
    plt.ticklabel_format(style='plain')
    fig.set_size_inches(8, 6)
    ax.barh(y=fully_progress_total.index,
            width=fully_progress_total.people_fully_vaccinated)
    # add title and labels
    ax.set_title('Top 10 country with the number of people fully vaccinated')
    ax.set_xlabel('The number of people fully vaccianted')
    ax.set_ylabel('Country')
    plt.savefig('Top10_country_people_fully_vaccinated')


def full_vac_per_hun(country_df):
    """
    Parameter:
        country_df: a data file that contains the vaccination records
        in the world.
    Argument:
        The fully_vac_per_hun method will construct a bar chat, and it will
        show the people_fully_vaccinated_per_hundre throughout different
        countries. Considering the readability of the graph, we only include
        top 10 countries.

        Since from the top10_country_people_fully_vaccinated, we found the
        number of people of fully vaccinated might hugely related to country
        oopulation. Thus,we continue to explore the
        people_fully_vaccinated_per_hundred to find the ratio between
        population fully immunized and total population up to the date.
        The top10 country showed up hugely changed.
    Returns:
        A bar chat of the people_fully_vaccinated_per_hundred in the world.
        The plot is being save in the
        Top10_country_people_fully_vaccinated_per_hundred.png
    """
    # find the highest ratio
    fully_hundred = country_df.groupby('country').max()
    # since there are so many countries in the dataset, I just pick the top
    # 10 for better visulization
    fully_progress_total = fully_hundred.sort_values('people_fully_'
                                                     'vaccinated_per_'
                                                     'hundred')[-10:]
    fig, ax = plt.subplots()
    ax.barh(y=fully_progress_total.index, width=fully_progress_total.
            people_fully_vaccinated_per_hundred)
    # add title and labels
    fig.set_size_inches(8, 6)
    ax.set_title("Top 10 country with its ratio of total number of"
                 'people fullyvaccinated per hundred')
    ax.set_xlabel('The ratio of number of people fully vaccianted per hundred')
    ax.set_ylabel('Country')
    plt.savefig('Top10_country_people_fully_vaccinated_per_hundred')


def world_vac_distri(type_df):
    """
    Parameter:
       type_df: a data file that contains the usage of differnet tyeps
       of the vaccine in the world.
    Argument:
        The world_vac_distri method will create a pie chat, and it will show
        the percentage of different vaccination brand are being used in the
        world. The interactive pie chart can clearly
        show the fraction and oberserve the highest/lowest use of vaccination
        brand.
         The pattern I generated is pifzer and Moderna was the two popular
        vaccinations that are being used in the world. Pifzer even
        composed 66% percent of the overall vaccination being used which we
        can see its dominant role.
    Returns:
        A interactibe pie chart shows the use of differnt brands of vaccines.
    """
    # data preprocessing, find the total number of vaccination being used by
    # different manufacture
    df_manu_type = type_df.groupby('vaccine').sum()
    # implemnt the interactive pie chart since that can make the plot
    # more organized and human readable
    manu_type_pie = go.Figure(data=[go.Pie(labels=df_manu_type.index,
                              values=df_manu_type.total_vaccinations)])
    # add titels and change features/styles
    manu_type_pie.update_layout(
        title_text="World vaccinations use of different manufactures",
        title_x=0.5
    )
    manu_type_pie.update_traces(textposition='outside',
                                textinfo='label+percent')
    manu_type_pie.show()


def holiday_vac_case_death_compare(new_merged):
    '''
    Parameter:
        new_merged: a data file that combined the vaccination records
        and COVID case information based on date and country.
    Argument:
        The holiday_vac_case_death_compare method will creates three separate
        graphs each correspond to the change of daily_vaccinations,
        daily_new_cases, and daily_new_deaths between Oct 1st and Jan 1st, the
        period with lots of holidays in US.
        Also we are able to identify through the graph whether there is a
        turning point occured especially during the holidays.
    Return:
        Three interactive line charts:
        1. plot about the daily vaccinations
        2. plot about the daily_new_cases
        3. plot about the daily_new_deaths
    '''
    us = new_merged[new_merged['country'] == 'United States']
    us['date_new'] = pd.to_datetime(us['date'])

    # set conditions to only select specific period ot fime
    condition1 = us['date_new'] >= '2021-10-01'
    condition2 = us['date_new'] <= '2022-01-01'
    merged = us[condition1 & condition2]

    # create the graph by using the plotly to make it interactive

    fig = px.line(merged, x='date_new', y='daily_vaccinations', width=800,
                  height=500)
    fig2 = px.line(merged, x='date_new', y='daily_new_cases', width=800,
                   height=500)
    fig1 = px.line(merged, x='date_new', y='daily_new_deaths', width=800,
                   height=500)

    fig.update_layout(title="Daily Vaccinations from 10/1/2021 to 1/1/2022",
                      xaxis_title="date", yaxis_title="Number of people "
                      "vaccinated", title_x=0.5)
    fig1.update_layout(title="Daily New Cases from 10/1/2021 to 1/1/2022",
                       xaxis_title="date", yaxis_title="Number of "
                       "people has COVID", title_x=0.5)
    fig2.update_layout(title="Daily New Deaths from 10/1/2021 to 1/1/2022",
                       xaxis_title="date", yaxis_title="Number of "
                       "people died due to COVID", title_x=0.5)

    fig.show()
    fig1.show()
    fig2.show()


def normal_vac_case_death_compare(vac_data, case_data):
    '''
    Parameter:
        vac_data: a data file that contains the vaccination record only in US
        case_data: a data file that contains the COVID case information in US
    Argument:
        The normal_vac_case_death_compare method will creates three separate
        graphs each correspond to the change of daily_vaccinations,
        daily_new_cases, and daily_new_deaths between May 1st and Sep 1st, the
        regular time period in US.
        In this case,it is feasible for us to catch the pattern
        variation of the people getting vaccinated. What's more, by viewing the
        changes of the number of people getting vaccinated in two periods of
        time.
        It is alo possible for us to draw insightes whether the trends of death
        cases and COVID cases shows the consistent alternation overtime.
    Return:
        Three interactive line charts:
        1. plot about the daily vaccinations
        2. plot about the daily_new_cases
        3. plot about the daily_new_deaths
    '''
    # the reason why we use two dataset in this case rather than merged data
    # set is because since we use the left join, thus it will use the
    # vaccination record data as base to match.
    # I tried to use the outer merged but it will shows the iso_code error,
    # which it can't match the country correspondingly therefore I choose to
    # extract data from each file, the line chart as I generated by using two
    # method is the totally the same.
    vac_data['new_date'] = pd.to_datetime(vac_data['date'])
    c1 = vac_data['new_date'] >= '2021-05-01'
    c2 = vac_data['new_date'] <= '2021-09-01'
    us_vac = vac_data[c1 & c2]

    case_data['new_date'] = pd.to_datetime(case_data['date'])
    c3 = case_data['new_date'] >= '2021-05-01'
    c4 = case_data['new_date'] <= '2021-09-01'
    us_case = case_data[c3 & c4]

    # create the interactive graph
    fig3 = px.line(us_vac, x='new_date', y='daily_vaccinations', width=800,
                   height=500)
    fig4 = px.line(us_case, x='new_date', y='daily_new_cases', width=800,
                   height=500)
    fig5 = px.line(us_case, x='new_date', y='daily_new_deaths', width=800,
                   height=500)
    # add lables to the graph constructed previously
    fig3.update_layout(title="Daily Vaccinations from 5/1/2021 to 9/1/2021",
                       xaxis_title="date", yaxis_title="Number of "
                       "people vaccinated", title_x=0.5)
    fig4.update_layout(title="Daily New Cases from 5/1/2021 to 9/1/2021",
                       xaxis_title="date", yaxis_title="Number of "
                       "people has COVID", title_x=0.5)
    fig5.update_layout(title="Daily New Deaths from 5/1/2021 to 9/1/2021",
                       xaxis_title="date", yaxis_title="Number of "
                       "people died due to COVID", title_x=0.5)

    fig3.show()
    fig4.show()
    fig5.show()


def main():
    # the dataset we will use
    df_country = pd.read_csv('country_vaccinations.csv')
    df_manu = pd.read_csv('country_vaccinations_by_manufacturer.csv')
    df_case_record = pd.read_csv('worldometer_coronavirus_daily_data.csv')
    # replace the different naming style to uniform the country names.
    df_case_record['country'] = \
        df_case_record['country'].str.replace('USA', 'United States')
    df_case_record['country'] = \
        df_case_record['country'].str.replace('UK', 'United Kingdom')
    # combined the vac data with case data whole world
    merged_world = df_country.merge(df_case_record,
                                    left_on=('date', 'country'),
                                    right_on=('date', 'country'))
    # us death and case data frame
    clip1 = df_case_record[df_case_record['country'] == 'United States']
    # us vaccination dataframe
    clip2 = df_country[df_country['country'] == 'United States']

    # call the function we defined previously
    vac_world_map(df_country)
    covid_death_map(merged_world)
    scatter_death_vac(merged_world)
    fully_vac_compare(df_country)
    full_vac_per_hun(df_country)
    world_vac_distri(df_manu)
    holiday_vac_case_death_compare(merged_world)
    normal_vac_case_death_compare(clip2, clip1)


if __name__ == '__main__':
    main()
