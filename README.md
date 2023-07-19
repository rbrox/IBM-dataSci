📝 **Sales Forecasting Project Statement**

## Project Description
The goal of this project is to develop a sales forecasting model for Favorita stores located in Ecuador. The task is to predict the sales for thousands of product families sold at these stores. The provided dataset contains historical sales data, store and product information, promotional data, as well as supplementary information like store metadata, oil prices, and holidays/events.

## Dataset Description
The dataset includes the following files:

1. **train.csv**: This file contains time series data of sales and features such as store_nbr, family, and onpromotion. The target variable is the sales, representing the total sales for a product family at a particular store on a given date.

2. **test.csv**: Similar to the train.csv file, this file includes the same features, and the task is to predict the sales for the dates provided in this file.

3. **sample_submission.csv**: A sample submission file in the correct format.

4. **stores.csv**: This file provides metadata for the stores, including city, state, type, and cluster. The cluster variable represents a grouping of similar stores.

5. **oil.csv**: Daily oil prices are included in this file. The oil price information is available for both the train and test data timeframes. It's important to note that Ecuador's economy is highly dependent on oil prices.

6. **holidays_events.csv**: This file contains information about holidays and events, including metadata. Pay attention to the "transferred" column, as it indicates if a holiday was officially transferred to another date. Extra days added to a holiday are marked as "Bridge."

## Project Objective
The objective of this project is to build a sales forecasting model that predicts the sales of product families at Favorita stores in Ecuador. Using the historical sales data, along with the provided features such as store information, promotional data, oil prices, and holidays/events, the model should accurately forecast the sales for the given test dates.

The sales forecasting model will assist Favorita in optimizing inventory management, planning promotions, and meeting customer demand effectively. Accurate sales predictions can help in making informed business decisions, ensuring optimal stock levels, and maximizing profitability.

## Additional Considerations
There are a few additional factors to keep in mind while tackling this project:

- Wages in the public sector are paid every two weeks on the 15th and the last day of the month. This payment pattern may impact supermarket sales.
- An earthquake with a magnitude of 7.8 struck Ecuador on April 16, 2016. The earthquake and subsequent relief efforts greatly affected supermarket sales for several weeks.

By developing an accurate sales forecasting model, we aim to provide Favorita with insights and predictions that enable them to plan and optimize their operations, anticipate demand fluctuations, and improve overall business performance.

🔍 **Note**: The data-set for this project is hosted on the kaggle competition "Store Sales - Time Series Forecasting"
Link for the same is `[here](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)`