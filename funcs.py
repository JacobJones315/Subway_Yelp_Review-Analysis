import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
reviews = pd.read_csv('reviews.csv')
reviews.head()

restaurants = pd.read_csv('restaurants.csv')
restaurants.head()

# merging excel sheets 
merge = reviews.merge(restaurants, how = 'left', on = ['business_id']) 
merge.head()

# creates new df, . loclooks in merge df and then whats in [] and if true pulls out entire row, only subway restaurants
sub_business = merge.loc[merge['name'] == 'Subway']
sub_business.head()

rating_ = pd.DataFrame(merge.groupby(["name"], as_index = False).stars.mean())


# Q1: create a new column for year and month, so we can make our comparisons via graphic

# Creates year column, using date column
sub_business['year'] = pd.to_datetime(sub_business['date']).dt.year

# Creates month column, using date column
sub_business['month'] = pd.to_datetime(sub_business['date']).dt.month

#creates a month_year column with mm/year
sub_business['month_year'] = sub_business['month'].astype(str) + '/' + sub_business['year'].astype(str)

# creates month/year column and column with mean stars 
rating_trend2 = pd.DataFrame(sub_business.groupby(["month_year"], as_index = False).stars.mean())
# creates year column and column with mean stars 
rating_trend = pd.DataFrame(sub_business.groupby(["year"], as_index = False).stars.mean())
# creates year column and unique reviewID column
rating_count = pd.DataFrame(sub_business.groupby(["year"], as_index = False).review_id.nunique())

###############################################################################################################

#Q1)

#how to plot
#take pandas columns and convert into arrays and plot, easier to manage


std_dev_reviews1 = pd.DataFrame(sub_business.groupby(["year"], as_index =False).stars.std())

#performs same thing as above
astd_dev_reviews10 = sub_business.groupby('year')['stars'].std().reset_index()

Std_dev1 = np.array(std_dev_reviews1['stars'])
#our second y axix 2y's


#seaborn figure
fig_bb = plt.figure(figsize=(10,6))
bb= sns.barplot(data = sub_business, x = 'year', y ='stars')
bb.set_xlabel('Year')
bb.set_ylabel("Average Rating")
bb.set_title("Rating Trend by Year Subway")


#groups by year, state, and avg stars for that year/state
rating_count01 = sub_business.groupby(['year', 'state'])['stars'].mean().reset_index()
# Using pivot_table to rearrange the DataFrame
pivot_df = rating_count01.pivot_table(values='stars', index='state', columns='year')

rating_count02 = sub_business.groupby(['year', 'state'])['review_id'].count().reset_index()
pivot_df2 = rating_count02.pivot_table(values='review_id', index='state', columns='year')

#creates new column in df of total reviews by state, by summing along entire row
pivot_df2['Total'] = pivot_df2.sum(axis=1)

#nlargest selects the largest values in the total column, i selected the top 5 
top_5_states = pivot_df2.nlargest(5, 'Total')

# lookis in pivot_df for the states in top 5 by index which is the corresponding state, so we can see the average raating for each state by year
HVR_states= pivot_df.loc[top_5_states.index]


#.T is the transpose function, turns columns into rows and rows into columns, turns the years into the index
#default python uses the index as the x axis and the values as the y_axix
#allows us to graph average reviews for each state by year
fig, qr = plt.subplots(dpi =100)
qr =HVR_states.T.plot()

qr.set_xlabel('Year')
qr.set_ylabel('Average Rating')
qr.set_title('Rating Trends Across States')
qr.legend(title='State')



#different graph version Q1, used in Q2
v = np.array(rating_trend['year'])
w = np.array(rating_trend['stars'])
y_count= np.array(rating_count['review_id'])
# saying create this object and use this DPI configuration, standard 100 DPI
fig,ab= plt.subplots(dpi = 100)
ab.plot(v,w, 'r--o')

ab.set_xlabel('Year')
ab.set_ylabel('Average Rating')
ab.set_title('Rating Trend by Year Subway')

ab2 = ab.twinx()
ab2.bar(v, y_count, alpha =0.5)
ab2.set_ylabel('Number of Ratings')
#########################################################################################################
#Q2, graph 1 

jersey_mikes = merge.loc[merge['name'] == "Jersey Mike's Subs"] # pull out all rows with jmikes
jersey_mikes.head()

# new column for year
jersey_mikes['year'] = pd.to_datetime(jersey_mikes['date']).dt.year

# rating trend 
rating_trend3 = pd.DataFrame(jersey_mikes.groupby(["year"], as_index = False).stars.mean()) #mean stars by year

# unique ratings
rating_count2 = pd.DataFrame(jersey_mikes.groupby(["year"], as_index = False).review_id.nunique()) #unique reviews by year

#std_dev of stars
std_dev_reviews = pd.DataFrame(jersey_mikes.groupby(["year"], as_index =False).stars.std())
Std_dev = np.array(std_dev_reviews['stars'])


# bar graph
c = np.array(rating_trend3['year'])
d = np.array(rating_trend3['stars'])

fig,cd= plt.subplots(dpi = 100, figsize = (15,11))
#bar plot with errorbars using yerr , error_kw error bar paramaters
jersey_bars = cd.bar(c,d, yerr=Std_dev, color = 'black', error_kw=dict(lw=1, capsize=5, capthick=2, ecolor='black'))


cd.set_xlabel('Year')
cd.set_ylabel("Average Ratings")
cd.set_title("Rating Trend by Year Jersey Mike's vs Subway")

# create an overlay of subways avg rating on same graph as jersey mikes
ax2 = cd.twinx()
#subway_bars is handle for legend
subway_bars = ax2.bar(c, w, yerr=Std_dev1, color ='red', alpha =0.5, error_kw=dict(lw=1, capsize=5, capthick=2, ecolor='red')) #alpha makes it transparent


# Display legends for both sets of bars, have to create seperate legens to do twin 
ax2.legend(labels=['Subway'], loc='upper right')
cd.legend(labels=["Jersey Mike's"], loc='upper left')

#Q2 graph 2 

# finding mean, std for each restaurant
subwaystarsarray = np.array(sub_business['stars'])
subwaymeanstars = subwaystarsarray.mean()
subwaystarstdev= subwaystarsarray.std()

JMikesstarsarray = np.array(jersey_mikes['stars'])
Jmikesmeanstars = JMikesstarsarray.mean()
Jmikesstarstdev= JMikesstarsarray.std()

McDonalds = merge.loc[merge['name'] == "McDonald's"]
McMeanarray = np.array(McDonalds['stars'])
McMean = McMeanarray.mean()
Mcstdev = McMeanarray.std()

McDonalds = merge.loc[merge['name'] == "McDonald's"]
McMeanarray = np.array(McDonalds['stars'])
McMean = McMeanarray.mean()

#graphing avg mean rating and stdev for each on one graph
Restaurants = ['Subway', 'McDonalds', 'Jersey Mikes']
means = [subwaymeanstars, McMean, Jmikesmeanstars]
stdevs =[subwaystarstdev, Mcstdev, Jmikesstarstdev]
x =np.arange(len(Restaurants))
bar_colors = ['red', 'blue', 'green']

fig,lz = plt.subplots(dpi = 100)
meanbar = lz.bar(x,means, width = 0.5, yerr =stdevs, capsize = 5, color = bar_colors)

lz.set_xlabel('Restaurants')
lz.set_ylabel("Average Ratings")
lz.set_title("Comparing Restaurants Mean Ratings and Stdev")
lz.set_xticks(x)
lz.set_xticklabels(Restaurants)

####################################################################################################################

#Q3

#finds number of unique citys for each restaurant name, creates two columns, reset_index removes name from index and resets it to default
locations= merge.groupby('name')['city'].nunique().reset_index()

#another way to code above locations for unique citys
locationsexample2= merge.groupby(['name'], as_index = False).city.nunique()

#renames column names approptiatley
locations.columns = ['name', 'unique_city_count']

#filters all restaurants in < 50 citys from locations df
AllLocal= locations.loc[locations['unique_city_count'] <50]
#filters all restaurnats in > 50 citys from locations df
AllNational= locations.loc[locations['unique_city_count'] >=50]

#keeps only All local/national rows and populates all other columns from merge df including star ratings which I wanted
All_local_merged_data = AllLocal.merge(merge, how = 'left', on = 'name') 
All_National_merged_data = AllNational.merge(merge, how = 'left', on = 'name') 

#finding mean and stdev for all locales
MeanLocalRestaurantStarsarray = np.array(All_local_merged_data['stars'])
MeanLocal=MeanLocalRestaurantStarsarray.mean()
localstdev = MeanLocalRestaurantStarsarray.std()

MeanNationalRestaurantStarsarray = np.array(All_National_merged_data['stars'])
MeanNational = MeanNationalRestaurantStarsarray.mean()
Nationalstdev = MeanNationalRestaurantStarsarray.std()

#3 graph #1, graphing locla vs national mean ratings

Locales = ['Local', 'National']
means2 = [MeanLocal, MeanNational]
stdevs2 =[localstdev, Nationalstdev]
q =np.arange(len(Locales))
bar_colors = ['blue', 'red']

fig,qt = plt.subplots(dpi = 100)
qt.bar(q,means2, width = 0.5, yerr =stdevs2, capsize = 5, color = bar_colors)

qt.set_xlabel('Locales')
qt.set_ylabel("Average Ratings")
qt.set_title("Comparing All Local Vs National Chain Ratings")
qt.set_xticks(q)
qt.set_xticklabels(Locales)


#3 graph #2, line graph
local = merge.loc[merge['name'] == '1000 Figs']
local['year'] = pd.to_datetime(local['date']).dt.year

#finding mean stars for 100 figs
rating_trend4 = pd.DataFrame(local.groupby(["year"], as_index = False).stars.mean())

x1= np.array(rating_trend4['year'])
y1= np.array(rating_trend4['stars'])

#finding mean stars for 101 tai cuisine
local2 = merge.loc[merge['name'] == '101 Taiwanese Cuisine']
local2['year'] = pd.to_datetime(local2['date']).dt.year
rating_trend5 = pd.DataFrame(local2.groupby(["year"], as_index = False).stars.mean())

x2= np.array(rating_trend5['year'])  
y2= np.array(rating_trend5['stars']) 

#finding mean stars for 5 guys
National = merge.loc[merge['name'] == 'Five Guys']
National['year'] = pd.to_datetime(National['date']).dt.year
rating_trend6 = pd.DataFrame(National.groupby(["year"], as_index = False).stars.mean())

x3= np.array(rating_trend6['year'])
y3= np.array(rating_trend6['stars'])

#finding mean stars for pizza hut
National2 = merge.loc[merge['name'] == 'Pizza Hut']
National2['year'] = pd.to_datetime(National2['date']).dt.year
rating_trend7 = pd.DataFrame(National2.groupby(["year"], as_index = False).stars.mean())

x4= np.array(rating_trend7['year'])
y4= np.array(rating_trend7['stars'])

#plotting all on one graph
fig, zz = plt.subplots(dpi = 100, figsize = (10,8))

zz.plot(x1, y1, '-o', label='1000 Figs (Local)')  
zz.plot(x2, y2, '-o', label='101 Taiwanese Cuisine (Local)')  
zz.plot(x3, y3, '-o', label='Five Guys (National)')  
zz.plot(x4, y4,'-o',  label='Pizza Hut (National)')  

zz.legend(loc = 'upper left')

zz.set_xlabel('Year')
zz.set_ylabel("Average Ratings")
zz.set_title("Rating Trend by Year Local Vs National Chains")


#3 trend rating size of restaurnant
#gives me avg reviews and unique city count so i can graph
avgreviews_citys = rating_.merge(locations, how = 'left', on = ['name']) 

#using seaborn to graph
fig_zx = plt.figure(dpi= 100)
zx =sns.lineplot(data = avgreviews_citys, x = 'unique_city_count', y ='stars', ci = 99)
zx.set_xlabel('Size of Restaurnat')
zx.set_ylabel("Average Rating")
zx.set_title("Restaurant Size Rating Trend")




######################################################################################################################

#Q4-A

# finding # of each star value for subway
Countstars = sub_business['stars'].value_counts()

#creates a new df from sub_business with stars and count as column headers
#size() counts the number of total individual occurences of each star rating inlcuding null values
#.reset_index(name='count') resets index from 1,2,3,4,5 being the star ratings to normal 0,1,2,3,4 
# and creates a new colum count where the values are stored
Countstarsdf = sub_business.groupby(["stars"]).size().reset_index(name='counts')

fig, am = plt.subplots(dpi = 100)
x5= np.array(Countstarsdf['stars'])  
y5= np.array(Countstarsdf['counts'])

am.bar(x5,y5)

am.set_xlabel('Star Rating')
am.set_ylabel("Number Of Ratings")
am.set_title("Subway Customer Reviews By Rating ")
######################################################################################################################

#Q4-B

#filters entire subway df only keeping rows with dates 2018-2021
sub_business2018_2021= sub_business[(pd.to_datetime(sub_business['date']).dt.year >= 2018) & (pd.to_datetime(sub_business['date']).dt.year <= 2021)]
#creates new df where grouped by stars and size() counts the occurence of each value for each rating, reset_index resets index to deafult and creates a new counts column 
Countstarsdf2018_2021 = sub_business2018_2021.groupby(["stars"]).size().reset_index(name='counts')


#using seaborn to graph
fig_yx = plt.figure(dpi= 100)
yx =sns.barplot(data = Countstarsdf2018_2021, x = 'stars', y ='counts')
yx.set_xlabel('Star Rating')
yx.set_ylabel("Number Of Ratings")
yx.set_title("Subway Customer Reviews By Rating 2018-2021")


##using matplot, same graph as above
fig, an = plt.subplots(dpi = 100)
x6= np.array(Countstarsdf2018_2021['stars'])  
y6= np.array(Countstarsdf2018_2021['counts'])

an.bar(x6,y6)

an.set_xlabel('Star Rating')
an.set_ylabel("Number Of Ratings")
an.set_title("Subway Customer Reviews By Rating 2018-2021")


#4b alternate graph
#creates df of # of each rating from 2018-2021, by year
ratings2018_2021 = sub_business2018_2021.groupby('year')['stars'].value_counts().reset_index(name = 'rating_counts')


ratings_pivot_df = ratings2018_2021.pivot_table(values='rating_counts', index='stars', columns='year')

fig_qc = plt.subplots(dpi= 100)
qc =ratings_pivot_df.plot(kind='bar', width = 0.8)
qc.set_xlabel('Rating in Stars')
qc.set_ylabel("Number Of Ratings")
qc.set_title("Subway Customer Reviews By Rating 2018-2021")
qc.tick_params(axis='x', rotation=360)  # Rotate x-axis labels


# This was just collecting info for question 4
meanstarssub_business2018_2021= sub_business2018_2021.stars.mean()

jerseymike2018_2021= jersey_mikes[(pd.to_datetime(jersey_mikes['date']).dt.year >= 2018) & (pd.to_datetime(jersey_mikes['date']).dt.year <= 2021)]
meanstarjerseymike2018_2021= jerseymike2018_2021.stars.mean()
######################################################################################################################

#Bonus States vs avg reviews

city_trend = pd.DataFrame(sub_business.groupby(["state"], as_index = False).stars.mean())

y7= np.array(city_trend['stars'])  
x7= np.array(city_trend['state'])

fig, za = plt.subplots(dpi = 100)
za.bar(x7,y7)

#using seaborn to graph, 1st bonus graph, state vs avg reviews
fig_xx = plt.figure(figsize=(10,6))
xx =sns.barplot(data = sub_business, x = 'state', y ='stars')
xx.set_xlabel('States')
xx.set_ylabel("Average Rating")
xx.set_title("Average Subway Customer Reviews By State")

#2nd bonus graph, months vs avg rating 

monthlyuniquereviews = sub_business.groupby(["month"], as_index = False).review_id.nunique()

fig_cd = plt.figure(dpi = 100, figsize=(10,6))
cd =sns.barplot(data = monthlyuniquereviews, x = 'month', y ='review_id')
cd.set_xlabel('Month')
cd.set_ylabel("Number of Reviews")
cd.set_title("Unique Reviews by Month")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Aug','Sep','Oct','Nov','Dec']
cd.set_xticklabels(months)

#3rd bonus graph 
uniqueusers = sub_business2018_2021.user_id.nunique()

uniqueusersdf = sub_business.groupby(["year"], as_index = False).user_id.nunique()


fig_uu = plt.figure(dpi = 100, figsize=(10,6))
uu = sns.lineplot(data =uniqueusersdf, x = 'year' , y = 'user_id' , color = 'red', marker ='o', linestyle = '--')
uu.set_xlabel('Year')
uu.set_ylabel("Reviews")
uu.set_title("Number of Subway Unique Individual Users Reviewing")
