import pickle
import pandas as pd
import numpy as np
import inflection

class HealthInsurance:
    def __init__(self):
        self.home_path                = 'C:/Users/edils/repos/pa004_health_insurance/'
        
        self.age_scaler                           = pickle.load(open(self.home_path + 'src/features/age_scaler.pkl', 'rb'))
        self.annual_premium_scaler                = pickle.load(open(self.home_path + 'src/features/annual_premium_scaler.pkl', 'rb'))        
        self.fe_policy_sales_channel_scaler       = pickle.load(open(self.home_path + 'src/features/fe_policy_sales_channel_scaler.pkl', 'rb'))        
        self.fe_region_code_scaler                = pickle.load(open(self.home_path + 'src/features/fe_region_code_scaler.pkl', 'rb'))        
        self.vintage_scaler                       = pickle.load(open(self.home_path + 'src/features/vintage_scaler.pkl', 'rb'))        
        
    def rename_columns(self, df1):
        cols_old = df1.columns

        cols_new = []
        cols_new = cols_old.map(lambda x: inflection.underscore(x))

        df1.columns = cols_new

        return df1
    
    def rename_categorical(self, df2):

        #Renaming vehicle_age lines
        #< 1 Year = new || 1-2 Years = used || >2 Years = old
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'old' if x == '> 2 Years' else 'used' if x == '1-2 Year' else 'new')

        #Renaming vehicle_damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 1 if x=='Yes' else 0)

        #Renaming gender #Male = 1, Female = 0
        df2['gender'] = df2['gender'].apply(lambda x: 1 if x=='Male' else 0)

        return df2

    def data_encoding(self, df5):

        #vehicle_age - Label Encoder
        df5['vehicle_age'] = df5['vehicle_age'].apply(lambda x: 0 if x == 'new' else 1 if x == 'used' else 2)

        #region_code - Frequency Encoding
        df5['region_code'] = df5['region_code'].map(self.fe_region_code_scaler)

        #policy_sales_channel
        df5['policy_sales_channel'] = df5['policy_sales_channel'].map(self.fe_policy_sales_channel_scaler)    
    
        return df5

    def data_rescalling(self, df5):

        #age 
        df5['age'] = self.age_scaler.transform(df5['age'].values.reshape(-1,1))


        #annual_premium
        df5['annual_premium'] = self.annual_premium_scaler.transform(df5['annual_premium'].values.reshape(-1,1))


        #vintage
        df5['vintage'] = self.vintage_scaler.transform(df5['vintage'].values.reshape(-1,1))
        
        cols_selected = {'vintage',
                         'annual_premium',
                         'age',
                         'region_code',
                         'vehicle_damage',
                         'policy_sales_channel',
                         'previously_insured',
                         'vehicle_age',
                         'gender'}

        return df5[cols_selected]
                  

    def get_prediction(self, model, original_data, test_data):
        
        yhat = model.predict_proba(test_data)
        
        original_data['Prediction'] = yhat[:,1]
        
        return original_data.to_json(orient='records', date_format='iso')