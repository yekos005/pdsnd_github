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
        city = input('would you like to see data for Chicago, New York City, or Washington?: ')
        city = (city.lower())
        if city not in ('chicago', 'new york city', 'washington'):
            print('unacceptable input, pls try again')
            continue
        else:
            break
    print('Thanks for choosing {}'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('would you like to filter the data by first six month or all to apply no month filter: ')
        month = (month.lower())
        if month not in ('all','january', 'february', 'march', 'april', 'may', 'june'):
            print('unacceptable month input, pls try again.')
            continue
        else:
            break     
    print('Thanks for choosing {}'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day of week or all to apply no day filter: ')
        day = (day.lower())
        if day not in ('all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print('unacceptable day input, pls try again.')
            continue
        else:
            break
    print('Thanks for choosing {}'.format(day))

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
    df['week_day'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['week_day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month: ', most_common_month)


    # TO DO: display the most common day of week
    most_common_day = df['week_day'].mode()[0]
    print("The most common day of week: "+ most_common_day)


    # TO DO: display the most common start hour
    common_start_hour = df['start_hour'].mode()[0]
    print("The most common start hour: ", common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common used start station: ", common_start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most common used end station: ", end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['station_start_end'] = df['Start Station'] + "-" + df['End Station']
    start_end = df['station_start_end'].mode()[0]
    print("The most commonly used start and end station: ", start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total travel time: ", travel_time)


    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()
    print("Mean travel time: ", average_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df.groupby(['User Type'])['User Type'].count()
    print("User type count: ", user_type)


    # TO DO: Display counts of gender
    try:
        gender_count = df.groupby(['Gender'])['Gender'].count()
        print("Gender count: ", gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth
        year_birth = int(df['Birth Year'].min())
        print("Earliest birth year: ", year_birth)

        most_recent_year = int(df['Birth Year'].max())
        print("Most recent birth year: ", most_recent_year)

        most_common = int(df['Birth Year'].mode()[0])
        print("Most common year of birth: ", most_common)
    except KeyError:
        print("Birth Year and Gender is not found in the city washington")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    i = 0
    raw = input("Would you like to see the raw data? Type Yes or No: ").lower()
    pd.set_option('display.max_columns', 200)
    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+6])
            raw = input("Would you like to see six(6) more rows of raw data? Type Yes or No: ").lower()
            i = i+6
        else:
            raw = input("\n Your input is invalid. please enter only yes or no \n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
