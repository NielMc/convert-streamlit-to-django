## Project Purpose
* In this project, you'll build a Data Web App to provide actionable insights and data driven recommendations for analyzing flowers profile and increasing productivity levels for Botanic field team

## External user’s goal
* The Data Web App stakeholders (Special Flower divsion team) are interested to understand how each flower's species differ from each other and a tool to speedup species recognition.

## Data Web App owner's goal
* The goal of this Data Web App is to help Botanic Garden to transform to a data driven organization.


## Business Requirements 
* As a Data Analyst from Botanic Garden, you are requested by Special Flower division to develop a system capable to distinguish among 3 distinct Iris species. Their next field mission at XYZ forest, which is officialy declared as contaminated area and is in the middle of nowehere. The team will harvest the flowers and store on boxes, but each box should have 1 specie type. The mission will happen in 10 days from today, and will take in total 25 days. 
  * 1 - We want to study how flowers' sepal and petal measurements differ across species.
  * 2 - We are interested to recognize the flower species based on its instant petal and sepal measurement


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* Business Requirement 1: Data Visualization
  * We create a Pairplot colored by Species; 3D scatter plot colored by Species and a Correlation Heatmap

* Business Requirement 2: Classification
  * We will build a classifier (Clf1_BR2) to predict flower species based on the sepal and petal measurement.
    * Train data - label: Species ; features: all other variables



## ML Business Case
### Clf1_BR2
* We will create ML model to predict what is the flower species based on sepal and petal measurements. 
It is a 3-class, single-label, classification model: 0 (Setosa), 1 (Versicolour) and 2 (Virginica).
* Our ideal outcome is to provide Special Flowers botanics team a intelligent solution to speed up
species diagnostic during the mission. The field operator will measure, with a ruler or something, 
the petal and sepal and will feed the App.

* The success metrics are: 95% overall accuracy, from the 30th prediction. We expect to have 
15 predictions per day. 
The ML model is considered a failure if Setosa species' Precision and Recall is not 100%. 
This species cant be mixed with other species under no circunstance.


* The output is defined as species class prediction based on flower measurements, 
it will be displayed into the App UI, the field operator will catalogue the measurement/prediction and 
will confirm that prediction belongs to that set of measurements. All measurements and predictions will be
stored locally in the App. There are not latency requirements. 
The ML model needs only inputs from field operator.

* The training data to fit the model come from Botanic Garden database. 
There are, in total, 150 records of all Iris flowers with petal and sepal measurments and 
its correspondent species. 
Botanic Garden warranties the measurments are accurate and free of any bias or error. 


* Heuristics: If we didnt use ML, an alternative option could be to take a flower DNA sample 
and analyze on the field which species that sample belong, but this may take 3h to be done.


## App User Interface
### Page 1
* Pairplot colored by species with multi-select menu listing all variables but species
* 3D scatter plot colored by species with 3 menus, where each menu has list of all variables but species
* Correlation Heatmap using all variables 

### Page 2
* Button to fit and save a ML model. Once finished, the model is evaluated on train and test set.

### Page 3
* User Interface with inputs (flower measurements) as numerical fields and prediction as statement

