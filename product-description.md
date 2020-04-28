# COVID-19 Apple Mobility Trends Reports

The source code outlining how this product gathers, transforms, revises and publishes its datasets is avaiable at [https://github.com/rearc-data/apple-maps-mobility-trends-covid-19](https://github.com/rearc-data/apple-maps-mobility-trends-covid-19).

## Product Description
This dataset contains COVID‑19 mobility trends in countries/regions and cities from Apple. The CSV file show a relative volume of directions requests per country/region or city compared to a baseline volume on January 13th, 2020.

Cities represent usage in greater metropolitan areas and are stably defined during this period. In many countries/regions and cities, relative volume has increased since January 13th, consistent with normal, seasonal usage of Apple Maps. Day of week effects are important to normalize as you use this data.

Data that is sent from users’ devices to the Maps service is associated with random, rotating identifiers so Apple doesn’t have a profile of your movements and searches. Apple Maps has no demographic information about the users, so we can’t make any statements about the representativeness of usage against the overall population.

#### Data Source
This resource is provided in CSV format. The dataset includes to following columns:

`geo_type, region, transportation_type, alternative_name` followed by a column for each day since January 13, 2020.

## More Information
- Source: [Apple Mobility Trends Reports](https://www.apple.com/covid19/mobility)         
- [Terms of Use](https://www.apple.com/covid19/mobility)  
- Frequency: Daily
- Format: CSV

## Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub [issue](https://github.com/rearc-data/apple-maps-mobility-trends-covid-19/issues) and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you are looking for specific open datasets currently not available on ADX, please submit a request on our project board [here](https://github.com/rearc-data/covid-datasets-aws-data-exchange/projects/1).
- If you have questions about the source data, please contact Apple.
- If you have any other questions or feedback, send us an email at data@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.
