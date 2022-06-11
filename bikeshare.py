import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    

    """ Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please insert a city (Chicago or New York City or Washington) to analyze: ").strip().lower()
    cities_list = ['chicago','new york city','washington']
    while city not in cities_list:
        print("that's invalid city")  
        city = input("please insert a valid city to analyze: ").strip().lower()
   

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("please insert a month (from junuary to june or all) to analyze: ").strip().capitalize()
    months_list = ["All","January", "February","March","April","May","June"]
    while month not in months_list:
             print("that's invalid month")  
             month = input("please insert a valid month (from junuary to june or all) to analyze: ").strip().capitalize()     

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please insert a day to analyze: ").strip().capitalize()
    days_list = ["All","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    while day not in days_list :
            print("that's invalid day")
            day = input("please insert a valid day to analyze: ").strip().capitalize()
            

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
    df = pd.read_csv(CITY_DATA[city], parse_dates = ["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.day_name()
    
     # filter by month if applicable
    if month != "All" :
        # use the index of the months list to get the corresponding int
        months = ["January","February","March","April","May","June"]
        month = months.index(month) + 1
        mask = df["month"] == month
        df = df[mask]
        
      # filter by day of week if applicable
    if day != "All":
        # filter by day of week to create the new dataframe
        df = df[df["day"] == day.capitalize()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    dic = {1 : "January" ,
           2 : "February",
           3 : "March",
           4 : "April",
           5 : "May",
           6 : "June"}
    df["month"] = df["Start Time"].dt.month
    popular_month =  df["month"].mode()[0]
    pop = dic.get(popular_month)
    print("the most common month for travel is {}".format(pop))

    # TO DO: display the most common day of week
    df["day"] = df["Start Time"].dt.weekday_name
    popular_day =  df["day"].mode()[0] 
    print("the most common day for travel is {}".format(popular_day))

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_hour =  df["hour"].mode()[0]
    print("the most common start hour for travel is {}" .format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_sataion = df["Start Station"].mode()[0]
    print("most commonly used start station is {}".format(start_sataion))

    # TO DO: display most commonly used end station
    end_station = df["End Station"].mode()[0]
    print("most commonly used end station is {}".format(end_station))


    # TO DO: display most frequent combination of start station and end station trip
    most_popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("most frequent combination of start station and end station trip is {}".format(most_popular_trip))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df["Trip Duration"].sum()
    day = int(total // (24 * 3600))
    total = total % (24 * 3600)
    hour = int(total // 3600)
    total = total % 3600
    minutes = int(total // 60)
    total = total % 60
    seconds = int(total)
    print("The total travel time is {} days, {} hours, {} minutes and {} seconds".format(day, hour, minutes, seconds))

    # TO DO: display mean travel time
    mean = df["Trip Duration"].mean()
    minutes = int(mean // 60)
    mean = mean % 60
    seconds = int(mean)
    print("The mean travel time is {} minutes and {} seconds".format(minutes ,seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("counts of each user type are \n{}".format(user_types))


    # TO DO: Display counts of gender
    if city != "washington" :
        user_gender = df['Gender'].value_counts()
        print("counts of each gender are \n{}".format(user_gender))
    else:
            print("sorry,there is no gender in washington")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != "washington" :
        earliest = int(df["Birth Year"].min())
        recent = int(df["Birth Year"].max())
        common = int(df["Birth Year"].mode())
        print("the earliest year of birth is {} \nthe most recent is {} \nand the most common is {}".format(earliest,recent,common))
    else:
            print("sorry, there is no Birth Year in washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    respond = input("Do you want to display a sample of data?(yes or no)").strip().capitalize()
    while respond == "Yes" :
       print(df.sample(n=5))
       respond = input("Do you want to display another sample of data?(yes or no)").strip().capitalize()
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
