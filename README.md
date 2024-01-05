# Subway Yelp Reviews Analysis
![](/images/subway_fig_2.png)
## Summary
* Created a set of analyses and data visualizations that support or disprove the following statements made by Subway Restaurant leadership:
  * Head of Customer Service: “Our ratings are gradually improving, and we will soon reach 4.5/5.”
  * Head of Store Operations: “Sandwiches are a tricky business. All sandwich chains suffer from poor customer ratings.”
  * Head of Social Media: “The goal of 4.5/5 is unreasonable for national chains like us. Only small, local, and boutique restaurants can achieve such high ratings.”
  * Chief Data Scientist: “It is well known that customers make the effort to give a rating only when they are either extremely angry or absolutely delighted with the service. So online ratings are not reliable.”
* Used matplotlib, seaborn, scipy, and pandas to generate line charts, bar charts, scatterplots, groupedby dataframes, and linear regression analyses

## Procedure
* Loaded Yelp datasets: reviews.csv and restaurants.csv 
* Extracted year from date column and merged the two tables together on business_id
* Created multiple filters and utilized groupby, mean, count, index, tolist to find average ratings per year and total ratings received and covert them to a dataframe
* Plotted a dual line/bar chart with years on the x-axis and average ratings per year and total ratings per year on the y-axis
* Plotted Subway Stores: Average Ratings by State Through the Years
* Created a dataframe, bar chart with error bars, and a line chart that highlights the mean and standard deviation of ratings for Subway and its national food chain competitors
* Plotted average ratings by restaurant sizes on a bar chart and a scatter plot (linear regression, correlation, and R-squared)
* To counter the effects of overrepresentation and underrepresentation, I used random sampling and generated a new correlation and R-sqaured value
* Plotted an unstacked bar to analyze the number of 1-5 ratings received from 2018-2021 (4 years)
* Plotted a hours vs number of reviews to see time intervals that Subway receives the most reviews.

## Screenshot of Data Visuals Generated
![](/images/subway_fig_1.png)
![](/images/subway_fig_4.png)
![](/images/subway_fig_6.png)
![](/images/subway_fig_7.png)
![](/images/subway_fig_8.png)
![](/images/subway_fig_9.png)
![](/images/subway_fig_10.png)
![](/images/subway_fig_11.png)

## Related Course
* Cornell University MSBA BANA 5440 Statistical Programming with Rakesh Allu, Ph.D. Student, Operations, Technology & Information Management

## Libraries Used
* [Matplotlib](https://matplotlib.org/stable/tutorials/index)
* [NumPy](https://numpy.org/doc/stable/)
* [Pandas](https://pandas.pydata.org/)
* [SciPy](https://scipy.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
