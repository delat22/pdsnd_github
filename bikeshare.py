#Import build in functions

import time
import pandas as pd
import numpy as np

#Cities in US bikeshare data
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city name(chicago, new york city or washington): ")
        if city not in ('chicago', 'new york city', 'washington'):
            print('whoops: {} is not a specified city name'.format(city))
            continue
        else:
            print('You are checking through {}'.format(city))
            break
    
    # getting time filter input in month, day, both or none
    while True:
        filter_by = input('Would you like to filter by month, days or not at all?(Use "none" for no time filter)' )
        if filter_by not in ('month', 'day', 'both', 'none'):
            print('whoops: you\'ve entered a wrong input')
            continue
        else:
            print('You want to check data through {}'.format(filter_by))
            break
    
    # the time input as specified from above
    if filter_by == 'month':
        # get user input for month (all, january, february, ... , june)
        while True:
            month = input("Enter month: ")
            if month not in ('january', 'february', 'march', 'april', 'may', 'june'):
                print('input month from January to june only')
                continue
            else:
                day = 'all'
                break
            
        # get user input for day of week (all, monday, tuesday, ... sunday)
    elif filter_by == 'day':
        while True:
            day = input("Enter days of week: ")
            if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                print('input day from monday to sunday')
                continue
            else:
                month = 'all'
                break
    elif filter_by == 'both':
        while True:
            month = input("Enter month: ")
            day = input("Enter days of week: ")
            
            if month not in ('january', 'february', 'march', 'april', 'may', 'June'):
                print('input month from january to June only and day from monday to sunday')
                continue
            elif day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                print('input month from january to June only and day from monday to sunday')
                continue
            else:
                break
    #filtering none                      
    elif filter_by == 'none':
        month = 'all'
        day = 'all'


    print('-'*40)
    return city, month, day


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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
        
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    


    # display the most common month
    
    print('The most frequest month is: ', df['month'].mode()[0])
    


    # display the most common day of week
    print('The most frequest day is: ', df['day_of_week'].mode()[0])
    


    # display the most common start hour
    
    print('The most frequest hour is: ', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The commonly used start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The commonly used End station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total time of travel: ', df['Trip Duration'].sum())

    # display mean travel time
    print('Mean time of travel: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Type of users: ', df['User Type'].value_counts())

    # Display counts of gender
    try:
        print('Gender: ', df['Gender'].value_counts())
    except Exception:
        print('Washington is not classified by gender')

    # Display earliest, most recent, and most common year of birth
    try:
        print('Earliest Birth Yeaer: ', df['Birth Year'].min())
        print('Most recent Birth Yeaer: ', df['Birth Year'].max())
        print('Common Birth Yeaer: ', df['Birth Year'].mode()[0])
        print("\nThis took %s seconds." % (time.time() - start_time))
    except Exception:
        print('washington not classified by Birth year')
    finally:
        print('-'*40)
    
def prompt_data(df):
    """ Display the raw data on bikeshare"""
    N = 5
    print('Would you like to see some data')
    while True:
        raw_data = input('(yes or no) ' )
        if raw_data == 'yes':
            print(df.head(N))
            N += 5
            print('Would you like to see more data')
            continue
        else:
            break
        
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        prompt_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
