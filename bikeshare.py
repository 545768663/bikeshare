import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
   
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        enter = input("Choose a city : ")
        if enter == "chicago" or enter == "new york city" or enter == "washington":
            city = enter

    # TO DO: get user input for month (all, january, february, ... , june)
            enter2 = input("Choose a month : ")
            if enter2 == "all" or enter2 == "january" or enter2 =="february" or enter2 == "march" or enter2 == "april" or enter2 == "may" or enter2 == "june" or enter2 == "july" or enter2 == "august" or enter2 == "september" or enter2 == "october" or enter2 == "november" or enter2 == "december" :
                month = enter2

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                enter3 = input("Choose a day : ")   
                if enter3 == "all" or enter3 == "monday" or enter3 == "tuesday" or enter3 == "wednesday" or enter3 == "thursday" or enter3 == "friday" or enter3 == "saturday" or enter3 == "sunday":
                    day = enter3
                    print('-'*40)
                    break
    
    return city,month,day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      month = months.index(month) + 1
      df = df[df['month'] == month]
    if day != 'all':
      df = df[df['day_of_week'] == day.title()]
    
    print('do you want to view 5 line of raw code?')
    enter_raw = input('enter yes to see ')
    if enter_raw == "yes":
        print(df.sample(5))
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\n most common month')
    common_month = df['month'].mode()[0]
    print(common_month)
    # TO DO: display the most common day of week
    print('\n most common day of week')
    common_day = df['day_of_week'].mode()[0]
    print(common_day)
    # TO DO: display the most common start hour
   
    print('\n most common hour')
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\n the most commonly used start station')
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)
    # TO DO: display most commonly used end station
    print('\n the most commonly used end station')
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print("\nthe most frequent comniantion of start station and end station")
    common_station = df['Start Station'] + df['End Station']
    combination = common_station.mode()[0]
    print(combination)
    
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    print('total travel time is:')
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)
    # TO DO: display mean travel time
    print('mean travel time is:')
    mean_travel_time =df['Trip Duration'].mean()
    print(mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    total_type = df['User Type']
    sub_count = 0
    other = 0
    total_count = 0
    for type in total_type:
        if type == 'Subscriber':
            sub_count = sub_count + 1
        else:
            other = other + 1
        total_count = total_count + 1 
    print('the number of subscriber is :')
    print(sub_count)
    print('the number of consumer is :')
    print(other)
    print('the total number in the list is :')
    print(total_count)
    
    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender']
        male = 0
        female = 0
        total_gender = 0
        for Gender in gender_count:
            if Gender == 'Male':
                male = male + 1
            else:
                female = female + 1
            total_gender = total_gender + 1 
        print('the number of male is :')
        print(male)
        print('the number of female is :')
        print(female)
        print('the total number in the list is :')
        print(total_gender)
    else:
        print('there is no information about washington user gender')
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest = df['Birth Year'].min()
        print('the earliest birth year is: ')
        print(earliest)
        most_recent = df['Birth Year'].max()
        print('the latest birth year is')
        print(most_recent)
        most_common = df['Birth Year'].mode()[0]
        print('the most common birth year is:')
        print(most_recent)
    else:
        print('there is no information about washington in user birth year')
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
