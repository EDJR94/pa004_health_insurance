# Health Insurance Cross Sell Project
![image](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/3e1559a5-7153-457f-a092-cac66c713a11)

## 01. Business Problem

Our client is an insurance company that has provided health insurance to its customers and now needs help building a model to predict whether its insured customers from the previous year would also be interested in a vehicle insurance provided by the company.

Building a model to predict whether a customer would be interested in vehicle insurance would be extremely useful for the company, as it can plan its communication strategy accordingly to target these more interested customers, thereby optimizing its business and reducing costs.

## 02. Assumptions

- The original variables/attributes (and their meanings) of the dataset are:

| Column | Description |
| ------ | ----------- |
| id | Unique ID for each customer |
| gender | Customer's gender |
| age | Customer's age |
| region_code | Region code where the customer lives |
| policy_sales_channel | Code of the contact channel chosen by the customer |
| driving_license | Does the customer have a driver's license? |
| vehicle_age | Age of the customer's vehicle |
| vehicle_damage | Has the vehicle been damaged before? |
| previously_insured | Has the customer been insured before? |
| annual_premium | Annual premium amount (for health insurance) |
| vintage | Number of days the customer has had health insurance |
| response | Would the customer be interested in vehicle insurance? |

## 03. Solution Strategy

The strategy used was the CRISP method, divided into 10 parts:

![CRISP Method](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/67b3ae4f-ea88-42e9-9cb4-43eee51cec4a)

1. Business question presented.
2. Understanding the Insurance Company's Business.
3. Data Collection.
4. Data Cleaning.
5. Data Exploration.
6. Data Modeling.
7. Use of Machine Learning Models.
8. Evaluation of Machine Learning Algorithm.
9. Model Deployment in Production.
10. Send the prediction and rank it using Google Sheets.

## 04. Key Business Insights

The following business hypotheses were raised based on how the company's business worked:

1. People who already have health insurance may be more inclined to purchase vehicle insurance, as they already have experience with insurance.
2. Customers with a history of car accidents may be more interested in vehicle insurance.
3. Customers with newer vehicles are more likely to purchase insurance.
4. Customer age may be an important factor, with younger customers being less likely to acquire vehicle insurance.
5. The geographic location of customers may be important, with people living in areas with high vehicle theft rates being more likely to acquire vehicle insurance.
6. Customer gender may be a factor, with men being more likely to acquire vehicle insurance.
7. The price of vehicle insurance may be an important factor, with customers more likely to acquire vehicle insurance if the prices are competitive.
8. Customers with driver's licenses are more likely to acquire insurance.
9. People who have had insurance before are more likely to want insurance, as they already have experience.
10. People notified through a specific means (e.g., phone) may tend to want insurance.

Among all the hypotheses, the **most relevant insights** in my opinion were the following:

1. **Customers with newer vehicles are more likely to purchase insurance.**

   We can see from the graph that most customers who would be interested are customers with used cars (1 to 2 years old) rather than new cars (less than 1 year old).

   ![Car Age Graph](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/cf866d2a-d9cd-41be-b05b-c22459c7404e)

2. **Younger people generally do not want to acquire insurance.**

   This hypothesis is true, but I would like to highlight that the ages with much higher demand than others are between 40-50 years, as shown in the graph below:

   ![Age vs Interest Graph](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/ad861d37-b944-4391-8a2c-4957a73ac806)

## 05. Machine Learning

The following Machine Learning models were used to analyze sales prediction:

- *LogisticRegression*
- *Dummy Classifier*
- *RandomForestClassifier*
- *XGB Classifier*
- *Light GBM Classifier*

After analyzing the metrics (Precision, Recall, F1 Score, Accuracy, ROC AUC Curve), I chose to proceed with the *Light GBM Classifier* as it had the best overall metrics:

| Model Name | Precision at K | Recall at K | F1 at K | Accuracy at K | ROC AUC at K |
| --- | --- | --- | --- | --- | --- |
| Light GBM | 0.44225 | 0.185761 | 0.261628 | 0.875312 | 0.861079 |

## 06. Translating the Model to Business

From the predictions made by the model, we can draw some conclusions.

Assuming that for each customer the company can sell vehicle insurance to, it has a Gross Profit of $540. Let's also consider that the company intends to call these potential customers, and each call has a total cost of $40.

Looking at the graph below, the initial customers are those with the highest probability of accepting vehicle insurance. However, there comes a point where the company starts calling customers who do not have a very high chance of purchasing insurance, and the cost starts to stand out, reducing the profit.

![Profit Curve Graph](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/f9e0c2bd-b3e9-48eb-aa9a-c4d4602311d6)

In other words, the company needs to call 46% of the customer base (those with the highest probability of accepting insurance) to maximize profit:

→ Profit by calling up to customer 35103: $3,429,452.90

→ Profit by calling the entire customer base: $1,962,802.77

This is a profit 1.74 times higher using the model.

## 06. Google Sheets Spreadsheet

After deploying the model to production, I created a Google Sheets spreadsheet that, given customer information, accesses my cloud-based model, makes predictions, and returns a ranked list of the best customers to call at the top of the list, as shown in the example below:

![Google Sheets Spreadsheet GIF](https://github.com/EDJR94/pa004_health_insurance/assets/128603807/ccd6c55c-b610-43aa-9d82-cc5bca362591)

## 07. Final Product and Conclusion

The final product was a Google Sheets spreadsheet that predicts and ranks customers who are most likely to acquire vehicle insurance, allowing the insurance company to contact only potential customers. This spreadsheet can be accessed from any device with internet access that has the Google Sheets application.

## 08. Next Steps

Continue with additional CRISP cycles, focusing on:

- Testing other Machine Learning models / Fine-tuning parameters to further refine the model.
- Creating additional features for the model from existing data.
- Exploring alternative strategies for defining model hyperparameters.
- Optimizing the model to make predictions and rank customers in Excel.

## References

Dataset: [https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction)
