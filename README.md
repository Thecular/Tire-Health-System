▶ Project Title: Tire-Wear Model Evaluation.



▶ Overview: This project evaluates an earlier tire-wear prediction model developed as part of my initial machine-learning work. The objective is to critically assess the model's data preparation, validation methodology, predictive performance, and engineering relevance using a structured model-evaluation framework.



Rather than treating model performance as a single metric, this evaluation examines whether the model generalizes appropriately, whether the evaluation methodology is reliable, and whether its predictions are meaningful from an engineering perspective.



▶ Problem Statement: Predict tire wear based on available operating-condition variables.

Input Features:

1. Time(seconds)
2. Speed(kmh)
3. Load(N)
4. Tire Temperature(Celsius)
5. Pressure(kPa)
6. Slip Angle(Degree)



Target:

Tire Wear-Rate(mm/km)



▶ Engineering Context: Tire wear is the degradation of tire due to use, its mostly influenced but not limited to time(duration), speed, load, tire temperature and pressure, slip angle. Tire wear prediction aid in reduction of automobile accident and offers a glimpse of the state of the tire. The evaluation considers not only predictive performance but also whether model behavior is consistent with expected engineering relationship.



▶ Dataset:

1. Source: The dataset is a synthetic dataset created for initial model development and training.

2. Dataset Size:

   * Number of observations: 200
   * Number of features: 6
   * Target variable: 1



3. Features:



|Feature|Description|Data Type|
|-|-|-|
|Time|Operating time interval|Numerical|
|Speed| Operating speed|Numerical|
|Load|Load on the tire|Numerical|
|Tire Temperature|Operating temperature|Numerical|
|Tire Pressure|Tire pressure |Numerical|
|Slip Angle|Tire slip angle|Numerical|
|Tire Wear-Rate|Target variable|Numerical|



▶ Original Model: The original implementation used linear regression to predict tire wear-rate.



* Algorithm: Linear Regression and Random Forest Regression
* Features: Time, Speed, Load, Tire temperature, Tire pressure, Slip angle
* Target: Tire wear-rate
* Preprocessing: Nil
* Original train/test split: 80% Training, 20 Test
* Original evaluation metrics: Root Mean-Squared Error(RMSE), Mean Absolut Error(MAE), R-Squared(R²)
* Original results: The linear regression out-performed random forest regression across the evaluation metrics.

