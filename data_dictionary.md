# Car Price Prediction Dataset - Data Dictionary

## Dataset Overview
This dataset contains information about various car models and their prices, suitable for building predictive models.

## Column Descriptions

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| car_ID | Integer | Unique identifier for each car |
| symboling | Integer | Insurance risk rating (-3 to 3, higher = riskier) |
| CarName | String | Car manufacturer and model name |
| fueltype | String | Type of fuel (gas/diesel) |
| aspiration | String | Engine aspiration (std/turbo) |
| doornumber | String | Number of doors (two/four) |
| carbody | String | Car body style (convertible, hatchback, sedan, wagon, hardtop) |
| drivewheel | String | Drive wheel configuration (fwd/rwd/4wd) |
| enginelocation | String | Engine location (front/rear) |
| wheelbase | Float | Distance between front and rear axles (inches) |
| carlength | Float | Length of the car (inches) |
| carwidth | Float | Width of the car (inches) |
| carheight | Float | Height of the car (inches) |
| curbweight | Integer | Weight of the car without passengers/cargo (lbs) |
| enginetype | String | Engine configuration (dohc, ohc, ohcf, ohcv, etc.) |
| cylindernumber | String | Number of cylinders (two, three, four, five, six, eight, twelve) |
| enginesize | Integer | Engine displacement (cubic inches) |
| fuelsystem | String | Fuel injection system type |
| boreratio | Float | Engine bore ratio |
| stroke | Float | Engine stroke length |
| compressionratio | Float | Engine compression ratio |
| horsepower | Integer | Engine horsepower |
| peakrpm | Integer | Peak RPM |
| citympg | Integer | City fuel efficiency (miles per gallon) |
| highwaympg | Integer | Highway fuel efficiency (miles per gallon) |
| price | Integer | **TARGET VARIABLE** - Car price in USD |

## Key Features for Prediction
- **Physical Dimensions**: wheelbase, carlength, carwidth, carheight
- **Weight**: curbweight
- **Engine Specs**: enginesize, horsepower, compressionratio
- **Fuel Efficiency**: citympg, highwaympg
- **Categorical Features**: CarName, fueltype, carbody, drivewheel

## Data Quality Notes
- Total Records: 207 cars
- Target Variable: price (ranges from $5,118 to $45,400)
- All numeric columns should be checked for outliers
- Categorical variables may need encoding for machine learning models

## Usage
This dataset is ideal for:
- Regression analysis to predict car prices
- Feature importance analysis
- Comparing different machine learning algorithms
- Understanding factors that influence car pricing
