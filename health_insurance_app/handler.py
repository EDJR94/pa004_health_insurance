import pickle
import pandas as pd
import os
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance

#loading model
model = pickle.load(open('models/model_lgb.pkl','rb'))

# initialize API
app = Flask( __name__ )

@app.route( '/healthinsurance/predict', methods=['POST'] )
def healthinsurance_predict():
    test_json = request.get_json()
   
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            
        # Instantiate Rossmann class
        pipeline = HealthInsurance()
        
        # data cleaning
        df1 = pipeline.rename_columns( test_raw )
        
        # feature engineering
        df2 = pipeline.rename_categorical( df1 )
        
        # data preparation
        df3 = pipeline.data_encoding( df2 )
        
        df4 = pipeline.data_rescalling(df3)
        
        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df4 )
        
        return df_response
        
        
    else:
        return Response( '{}', status=200, mimetype='application/json' )
    
#Usar isso para testar na maquina
#if __name__ == '__main__':
    #app.run('0.0.0.0', debug=True)

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)