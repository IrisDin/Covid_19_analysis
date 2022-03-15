"""
Course: CSE163
Author: Frank Iris
Project Title: Analysis about COVID-19 Vaccination, Cases, and Deaths Worldwide
This is a test file that contain seven test functions to test the
accuracy of visualizations for question1,2,4,5,6 in the method.py file. To test
the corretness of question 3, we will use Tableau software.
"""
import math
import pandas as pd


def vac_map_test(country_df):
    """
    Test for question 1
    Argument:
        country_df: a data file that contains the vaccination records
        in the world.

        The vac_map_test will test the number being shown on the Choropleth map
        with the actual number total vaccinations that in the dataset.
        If they match, it will shown vac_map_test passed, otherwise, it will
        show the error message.
    """
    # China is the country with max number of total vaccinations
    # It is cumulative data.
    cn = country_df[country_df['country'] == 'China']
    assert cn['total_vaccinations'].max() == 3124118000
    # India is the second most country with number of total vaccinations
    india = country_df[country_df['country'] == 'India']
    actual = india['total_vaccinations'].max()
    # since from the map, it shown the scientific notation, so we pick
    # the visible digits on the map to compare with the actual number.
    visual_digit = actual // 1000
    on_map = 1776674000 // 1000
    assert visual_digit == on_map


def death_map_test(merged):
    '''
    Test for question2
    Argument:
        merged: a data file that combined the vaccination records
        and COVID case information based on date and country.

        The death_map_test method will test the number being shown on the
        Choropleth map with the actual number of daily_nwe_deaths.
        that in the dataset.
        If they match, it will shown death_map_test passed, otherwise,
        it will show the error message.
    '''
    greenland = merged[merged['country'] == 'Greenland']
    assert greenland['cumulative_total_deaths'].max() == 1
    cn = merged[merged['country'] == 'China']
    assert cn['cumulative_total_deaths'].max() == 4636
    congo = merged[merged['country'] == 'Congo']
    assert congo['cumulative_total_deaths'].max() == 369


def fully_vac_test(country_df):
    '''
    Test for question 4
    Argument:
        country_df: a data file that contains the vaccination records
        in the world.

        The fully_vac_test will test wether the top country shown on the
        fully_vaccinated bar chart is as same as in the dataset.
         If they match, it will shown fully_vac_test passed, otherwise, it will
        show the error message.
    '''
    fully = country_df.groupby('country').max()
    max_val = fully['people_fully_vaccinated'].max()

    on_chart = 'China'
    china_data = country_df[country_df['country'] == on_chart]
    assert max_val == china_data['people_fully_vaccinated'].max()


def fully_vac_per_hun_test(country_df):
    '''
    Test for question 4
    Argument:
        country_df: a data file that contains the vaccination records
        in the world.

        The fully_vac_per_hun_test will test wether the top country
        shown on the fully_vaccinated_per_hundred bar chart is as
        same as in the dataset. Since we found it is closely relate to
        the population base of a country.
        If they match, it will shown fully_vac_per_hun_test passed,
        otherwise, it will show the error message.
    '''
    fully_hun = country_df.groupby('country').max()
    max_val = fully_hun['people_fully_vaccinated_per_hundred'].max()

    on_chart = 'Gibraltar'
    gibraltar_data = country_df[country_df['country'] == on_chart]
    assert max_val == gibraltar_data['people_fully_'
                                     'vaccinated_per_hundred'].max()


def vac_dis_test(vac_type):
    '''
    Test for question5
    Argument:
       vac_type: a data file that contains the usage of differnet types
       of the vaccine in the world.

        The vac_dis_test method will test the percentage of each type used in
        the world to compare with the actual proportion calculated from the
        dataset.
        If they match, it will shown vac_dis_test passed, otherwise,
        it will show the error message.
    '''
    # calculate the total number of different brands of vaccines in the world
    vac_total_each = vac_type.groupby('vaccine').sum()
    total_vac = vac_total_each['total_vaccinations'].sum()
    # calculate the total number of single vaccine
    pfizer = vac_type[vac_type['vaccine'] == 'Pfizer/BioNTech']
    pfizer_sum = pfizer['total_vaccinations'].sum()
    # based on the data presented on pie chart, we only focus on visible digit
    pfizer_percent = round((pfizer_sum / total_vac) * 100, 1)
    on_chart = 66.2
    assert math.isclose(on_chart, pfizer_percent)

    sinovac = vac_type[vac_type['vaccine'] == 'Sinovac']
    sinovac_sum = sinovac['total_vaccinations'].sum()
    sinovac_percent = round((sinovac_sum / total_vac) * 100, 2)
    on_chart1 = 2.75
    assert math.isclose(on_chart1, sinovac_percent)


def holiday_vac_case_check(country_df, case_track):
    '''
    Test for question 6.1/6.2/6.3
    Argument:
        country_df: a data file that contains the vaccination records
            in the world.
        case_track: a data file that contains the usage of differnet types
            of the vaccine in the world.

        The holiday_vac_case_check method will test whether the number being
        presented on the graph is same as the real data in the dataset from
        each file. Since the dataset being used to generate (holiday_vac_case
        _death_map is the merged version of two dataset.
         If they match, it will shown holiday_vac_case_check passed,
        otherwise, it will show the error message.
    '''
    # in this case we pick the last day of holiday period
    country_df['dates'] = pd.to_datetime(country_df['date'])
    us = country_df[country_df['country'] == 'United States']
    us = us[us['dates'] == '2021-12-31']
    assert (us['daily_vaccinations'] == 1052646).all()
    case_track['dates'] = pd.to_datetime(case_track['date'])
    us1 = case_track[case_track['country'] == 'USA']
    us1 = us1[us1['dates'] == '2021-12-31']
    assert (us1['daily_new_deaths'] == 1009).all()
    assert (us1['daily_new_cases'] == 619997).all()


def normal_vac_case_check(country_df, case_track):
    '''
    Test for question 6.4
    Argument:
        country_df: a data file that contains the vaccination records
            in the world.
        case_track: a data file that contains the usage of differnet types
            of the vaccine in the world.

        The normal_vac_case_check method will compare whether the number being
        presented on the graph is same as the real data in the dataset from
        each file. Since the dataset being used to generate normal_vac_case
        _death_map is from two separate dataset due to the left join we use.
        Thus, in this case, we will create a outer merged dataset to testify
        the accuracy of the number.
         If they match, it will shown normal_vac_case_check passed,
        otherwise, it will show the error message.
    '''
    new_merged = pd.merge(country_df, case_track, on=('date',
                          'country'), how='outer')
    new_us = new_merged[new_merged['country'] == 'United States']
    pd.to_datetime(new_us['date'])
    us = new_us[new_us['date'] == '2021-05-01']
    assert (us['daily_vaccinations'] == 2439409).all()
    assert (us['daily_new_deaths'] == 707).all()
    assert (us['daily_new_cases'] == 50803).all()


def main():
    df_country = pd.read_csv('country_vaccinations.csv')
    df_manu = pd.read_csv('country_vaccinations_by_manufacturer.csv')
    df_case_record = pd.read_csv('worldometer_coronavirus_daily_data.csv')

    df_case_record['country'] = \
        df_case_record['country'].str.replace('USA', 'United States')
    df_case_record['country'] = \
        df_case_record['country'].str.replace('UK', 'United Kingdom')
    merged_world = df_country.merge(df_case_record,
                                    left_on=('date', 'country'),
                                    right_on=('date', 'country'))
    vac_map_test(df_country)
    print("vac_map_test passed")
    death_map_test(merged_world)
    print("death_map_test passed")
    vac_dis_test(df_manu)
    print("vac_dis_test passed")
    fully_vac_test(df_country)
    print("fully_vac_test passed")
    fully_vac_per_hun_test(df_country)
    print("fully_vac_per_hun_test passed")
    holiday_vac_case_check(df_country, df_case_record)
    print("holiday_vac_case_check passed")
    normal_vac_case_check(df_country, df_case_record)
    print("normal_vac_case_check passed")
    print("All test passed")


if __name__ == "__main__":
    main()
