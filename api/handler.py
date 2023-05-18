import pickle
import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance

#loading model
path = 'C:/Users/edils/repos/pa004_health_insurance/'
model = pickle.load(open(path + 'src/models/model_lgb.pkl','rb'))

#Initiate API
app = Flask(__name__)

@app.route('/healthinsurance/predict', methods=['POST'])

def healthinsurance_predict():
    
    test_json = request.get_json() #Load json for production
    
    if test_json: #there is data
        if isinstance(test_json, dict ): #only one row
            test_raw = pd.DataFrame(test_json, index=[0]) #keys for dict transform in columns
        
        else: #has multiple rows
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        #Instatiate Class
        pipeline = HealthInsurance()

        #Data Description
        df1 = pipeline.rename_columns(test_raw)

        #Data Transformation
        df2 = pipeline.rename_categorical(df1)

        #Data Encoding
        df3 = pipeline.data_encoding(df2)
        
        #Data Rescalling
        df4 = pipeline.data_rescalling(df3)

        #prediction
        df_response = pipeline.get_prediction(model, test_raw, df4)
        
        print(df4)

        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)