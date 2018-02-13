# K-means-Clustering-for-SP500-Companies
## Objective
Clustering the S&P500 companies based on thier daily stock prices movement for a period of time. See if the stocks of companies operating in the same GICS sectors happen to be grouped together.

## Data
- S&P500 sectors
  - Health Care
  - Financials
  - Information Technology 
  - Industrials
  - Utilities
  - Materials
  - Consumer Staples
  - Consumer Discretionary 
  - Energy
  - Telecommunications Services
- Closing prices
  - create an indicator to indicate if the stock prices  increase compared with the previous day (1 or 0 corresponding to UP or DOWN)
  
## Method
- K-means clustering. 
  - The number of clusters is chosen to be 10 
  - Iteratively update the centroids if new points are added to the groups
  
  

