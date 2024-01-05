# Subway Yelp Reviews Analysis
![](/images/Subway_fig12.png)
## Summary
* Created a set of analyses and data visualizations that support or disprove the following statements made by Subway Restaurant leadership:
  * Head of Customer Service: “Our ratings are gradually improving, and we will soon reach 4.5/5.”
  * Head of Store Operations: “Sandwiches are a tricky business. All sandwich chains suffer from poor customer ratings.”
  * Head of Social Media: “The goal of 4.5/5 is unreasonable for national chains like us. Only small, local, and boutique restaurants can achieve such high ratings.”
  * Chief Data Scientist: “It is well known that customers make the effort to give a rating only when they are either extremely angry or absolutely delighted with the service. So online ratings are not reliable.”
* Used matplotlib, seaborn, and pandas to generate line charts, bar charts, scatterplots, group by dataframes, and linear regression analyses

## Procedure
* Loaded Yelp datasets: reviews.csv and restaurants.csv 
* Extracted year from date column and merged the two tables together on business_id
* Created multiple filters and utilized groupby, mean, count, index, and arrays to find average ratings per year and total ratings received and covert them to a dataframe
* Plotted a dual line/bar chart with years on the x-axis and average ratings per year and total ratings per year on the y-axis
* Plotted Subway Stores: Average Ratings by State Through the Years
* Plotted a bar chart with error bars, comparing the mean and standard deviation of ratings for Subway and its national food chain competitors
* Plotted a bar chart with error bars, comparing the mean and standard deviation of ratings for all local vs national food chains
* Plotted a line chart highlighting average ratings by restaurant size
* Plotted an unstacked bar to analyze the number of 1-5 star ratings received from 2018-2021 
* Plotted a rating trend of randomly selected local vs national chain retaurants
* Plotted a bar chart comapring the number of reviews submitted for each star rating
* Plotted a line chart highlighting the number of unique Subway reviewers over the years
* Plotted a bar chart with error bars, comparing the mean and standard deviation of ratings for Subway in each state

## Screenshot of Data Visuals Generated
![](/images/Subway_fig2.png)
![](/images/Subway_fig12.png)
![](/images/Subway_fig3.png)
![](/images/Subway_fig4.png)
![](/images/Subway_fig6.png)
![](/images/Subway_fig11.png)
![](/images/Subway_fig5.png)
![](/images/Subway_fig7.png)
![](/images/Subway_fig8.png)
![](/images/Subway_fig9.png)
![](/images/Subway_fig1.png)

## Related Course
* Cornell University MSBA BANA 5440 Statistical Programming with Rakesh Allu, Ph.D. Student, Operations, Technology & Information Management

## Libraries Used
* [Matplotlib](https://matplotlib.org/stable/tutorials/index)
* [NumPy](https://numpy.org/doc/stable/)
* [Pandas](https://pandas.pydata.org/)
* [Seaborn](https://seaborn.pydata.org/)

