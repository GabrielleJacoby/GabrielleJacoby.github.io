# Data Mining for Unconventional Oil and Gas Production in Texas

This projects uses data mining and machine learning to analyze and predict unconventional oil and gas production in the state of Texas. The project falls under the broader research topic of big data and machine learning applications in the oil and gas industry. Large sets of petroleum related data are now available and can be used for decision making. However, the overwhelming volume of data can pose a challenge to petroleum engineering analysis. The ability to clean data, identify patterns, and make future predictions can become value for financial decisions and identifying development opportunities.

This research was conducted as part of larger programs, including the Summer Undergraduate Research Internship (SURI) at the Hildebrand Department of Petroleum & Geosystems Engineering and the Scientific Computing Project at the Oden Institute for Computational Engineering & Sciences.

[Directory of oil & gas databases](https://gabriellejacoby.github.io/)

[Interactive graph of oil production from 1997-2019 per county in Texas](Texas_County_Boundaries_Detailed-shp/Pivot%20Table%20Test.ipynb)

[Creating a GIF of geographic representation of oil or gas production](Texas_County_Boundaries_Detailed-shp/Create%20Map%20-%20GIF.ipynb)

[Creating a MOV of geographic representation of oil or gas production](Texas_County_Boundaries_Detailed-shp/Create%20Map%20-%20MOV.ipynb)

[Application of the Hubbert Model to oil production trends](Texas_County_Boundaries_Detailed-shp/Hubbert%20Model%20-%20Oil.ipynb)

[Application of the Hubbert Model to gas production trends](Texas_County_Boundaries_Detailed-shp/Hubbert%20Model%20-%20GW%20Gas.ipynb)

Machine Learning to Predict Future Production:  

[Time Series Analysis - Auto-Regressive Integrated Moving Average (ARIMA) Model](Texas_County_Boundaries_Detailed-shp/Future%20Forecasting.ipynb)  
This model was able to predict production for a single county, but could be improved to train based on multiple similar counties to predict the future production of another county. 

[Time Series Forecasting using Tensor Flow](Texas_County_Boundaries_Detailed-shp/Tensor%20Flow%20Example%20-%20Production.ipynb)  
This model was able to predict production from multiple counties in one continuous data list, but could be improved to recognize that the date of the data is overlapping.  

[Time Series Decomposition - Example County](Texas_County_Boundaries_Detailed-shp/Time%20Series%20-%20Single%20County.ipynb)  
[Time Series Decomposition - Example Counties](Texas_County_Boundaries_Detailed-shp/Time%20Series%20-%20Multiple%20Counties.ipynb)  
This model was able to detect cyclical patterns in single counties, but was unable to detect patterns in multiple counties as separate data sets. This could be improved by separating data to train model.
