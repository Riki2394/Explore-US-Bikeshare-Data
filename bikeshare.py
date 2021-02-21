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
    print('Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city do you want to know the data of? Chicago, New York City or Washington?\n").lower()
        if city not in ["chicago", "new york city", "washington"]:
            print("Sorry, i can't access this data. Please try again".title())
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nSelect a month between January, February, March, April, May, June or all if you don't want to apply any filters\n").lower()
        if month not in ["january", "february", "march", "april", "may", "june", "all"]:
            print("Sorry, i can't find any matches".title())
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich day would you like to filter by? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all\n").lower()
        if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            print("Sorry, i can't find any matches".title())
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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]

    if day != "all":
        df[df["day_of_week"] == day.title()]


    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("Most common month : {}".format(most_common_month).title())


    # TO DO: display the most common day of week
    most_common_dow = df["day_of_week"].mode()[0]
    print("Most common day of week : {}".format(most_common_dow).title())


    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    start_hour = df["hour"].mode()[0]
    print("Most common sart hour : {}".format(start_hour).title())


    latest_start_hour = df["hour"].max()
    print("Latest start hour : {}".format(latest_start_hour).title())


    earliest_start_hour = df["hour"].min()
    print("Earliest start hour : {}".format(earliest_start_hour).title())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    time.sleep(2)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].value_counts().idxmax()
    print("Most commonly used start station : {}".format(popular_start_station).title())


    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].value_counts().idxmax()
    print("Most commonly used end station : {}".format(popular_end_station).title())


    # TO DO: display most frequent combination of start station and end station trip
    combined_station = df.groupby(["Start Station", "End Station"]).size().nlargest(1)
    print("Most frequent combination of start station and end station trip : {}".format(combined_station).title())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    time.sleep(2)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time : {}".format(total_travel_time/86400).title(), "Days")


    # TO DO: display mean travel time
    avg_travel_time = df["Trip Duration"].mean()
    print("Mean travel time : {}".format(avg_travel_time/60).title(), "Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    time.sleep(2)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df["User Type"].value_counts()
    print("Count of user types : {}".format(counts_user_types).title())


    # TO DO: Display counts of gender
    if "Gender" in df.columns :
        gender_counts = df["Gender"].value_counts()
        print("Count of gender : {}".format(gender_counts).title())

    else:
        print("Count of gender : No data available".title())


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df["Birth Year"].min()
        print("Earliest year of birth : {}".format(earliest_yob).title())

    except KeyError:
        print("Earliest year of birth : Sorry, no information available".title())


    try:
        most_recent_yob = df["Birth Year"].max()
        print("Most recent year of birth : {}".format(most_recent_yob).title())

    except KeyError:
        print("Most recent year of birth : Sorry, no information available".title())


    try:
        most_common_yob = df["Birth Year"].mode()[0]
        print("Most common year of birth : {}".format(most_common_yob).title())

    except KeyError:
        print("Most common year of birth : Sorry, no information available".title())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    pd.set_option('display.max_columns',200)
    view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n")
    if view_data.lower() == "yes":
        start_loc = 0
        while True:
            print(df.iloc[start_loc : start_loc +5])
            start_loc += 5
            view_display = input("Do you wish to continue? Enter yes or no : ")
            if view_display.lower() != "yes":
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            int(input("Please help us to improve, rate our service with a score from 1 to 5(only int) :"))
            print("Thanks for your time, we hope to see you soon!")
            break


if __name__ == "__main__":
    main()
