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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input('whitch city do you like to see statistics for ? ')
        if city not in ('chicago','new yourk city','washington') :
            print('sorry, we have data only from chicago, new yourk city and washington')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    
    while True :
        month = input('whitch month do you want to filter with ? , please inter the month as integer , eg: january-->1....')
        if month not in (1,2,3,4,5,6) :
            print('please inter the month as integer, eg: january-->1....')
            continue
        else:
            break
    
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input('witch day do you want to filter with ? please inter the day as integer , eg: sunday-->1.... ')
        if month not in (1,2,3,4,5,6,7) :
            print('please inter the day as integer, eg: sunday-->1....  ')
            continue
        else:
            break
    
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
    df['day of week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all' :
        df = df[df['month'] == month]
    if day != 'ALL':
        df = df[df['day of week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    print('the most common month is : ',df['month'].value_counts())

    # display the most common day of week
    print('the most common day of week is : ',df['day of week'].value_counts().max)

    # display the most common start hour
    print('the most common start hour is : ',df['hour'].value_counts().max)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most commonly used start station is : ',df['Start Station'].value_counts().max)


    # display most commonly used end station
    print('the most commonly used end station is : ',df['End Station'].value_counts().max)


    # display most frequent combination of start station and end station trip
    print('the most common combination of start and end station trip is : ',df.groupby(['Start Station', 'End Station']).count())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time is : ',sum(df['Trip Duration'])/86400,' days')

    # display mean travel time
    print('mean travel time is : ', df['Trip Duration'].mean()/60 ,'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    
    try:
      gender_types = df['Gender'].value_counts()
      print('counts of gender ',df['Gender'].value_counts())
    except KeyError:
      print("No data available for this month.")
    # Display earliest, most recent, and most common year of birth
    
    try:
      print('earliest year of birth is : ',df['Birth Year'].min())
    except KeyError:
      print("No data available for this month.")
    
    try:
      print('most recent year of birth is : ',df['Birth Year'].max())
    except KeyError:
      print("No data available for this month.")

    try:
      print('most common year of birth is : ',df['Birth Year'].mode())
    except KeyError:
      print("No data available for this month.")
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
