# Analysis of Weather Data for Ice Cream Shop

### Overview

In hopes of opening an ice cream shop on the Hawaiin island of Oahu, weather data was analyzed to better inform decision making for the investor. The data from several weather stations on the island was extracted from a sqllite database to make for quicker analysis.

### Results
The summary statistics for temperatures during the month of June and December were asked for by the potential investor. The following images are screen shots of the tables that were created.
<br><br>
<img width="148" alt="Screen Shot 2022-09-07 at 10 15 12 AM" src="https://user-images.githubusercontent.com/106560606/189249954-e4b263d2-c374-4d6d-9fca-d95855534d4a.png">

<br><br>
![Screen Shot 2022-09-08 at 6 37 36 PM](https://user-images.githubusercontent.com/106560606/189249965-aa55f06f-4463-4885-b881-b6afce151d6d.png)

<br><br>
From these summary statistics there are three differences between June and December temperatures:
- June has a warmer average at 74.9 degrees compared to 71.0 degrees for December. 
- December has the lower minimum at 56.0 degrees compared to 64.0 degrees for June. 
- December has a larger range for minimum and maximum temperatures at 27 degrees while June only has a range of 21 degrees.

### Summary
With the summary provided by the query of the sqllite database it is clear that temperatures for both December and June would be considered enjoyable for most people. However, while the temperatures would be enjoyable this query is lacking information about precipitation. Two additional queries that could provide additional insight for the investor should include information about precipitation. The first could be the summary statistics for number of days that did not have any precipitation occur (or "sunny days"). The second potential query could be the amount of precipitation that occured. This information paired with temperature information would be very useful in determining how much business an ice cream shop could potentially bring in. For example, going solely based on temperature data could mean warm days would be viewed as good for business however if most of these days have high amounts of precipitation it would not be good for business.    
