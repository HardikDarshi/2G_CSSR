from flask import Flask, request,make_response, render_template
import pandas as pd
import pickle
import Preprocessing

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            object = request.files['file11']
            df1 = pd.read_excel(object)
            #df1.columns = df1.columns.str.replace(' ', '')
            main_column1 = ['NSN_BSS_la_id_LAC_Segment', 'NSN_BSS_Cell_ID_Segment',
                           'traffic_area_trf_1', 'amr_full_rate', 'amr_half_rate',
                           'SDCCH Completion Rate',
                           'NSN_BSS_TCH_Assignment_Success_Rate_BBH_NRD_newPR03',
                            'sdcch_assignment_nom',
                           'Band_900_traffic_trf_1_BH', 'Band_1800_traffic_trf_1_BH',
                           'Band_900_Total_TRX', 'Band_1800_Total_TRX',
                        'NSN_BSS_TCH_REQ_REJ_DUE_TO_TX_POWER_BH' ]

            main_column2 = ['traffic_area_trf_1', 'amr_full_rate', 'amr_half_rate',
                            'SDCCH Completion Rate',
                            'NSN_BSS_TCH_Assignment_Success_Rate_BBH_NRD_newPR03',
                            'sdcch_assignment_nom',
                            'Band_900_traffic_trf_1_BH', 'Band_1800_traffic_trf_1_BH',
                            'Band_900_Total_TRX', 'Band_1800_Total_TRX',
                            'NSN_BSS_TCH_REQ_REJ_DUE_TO_TX_POWER_BH']
            df2 = df1.drop(columns=[col for col in df1 if col not in main_column1])
            df3 = df2.dropna()
            df4 = df3.drop(columns=[col for col in df3 if col not in main_column2])
            a1 = Preprocessing.Preprocessor()
            model = 'rfc_cv_v7.sav'
            loaded_model = pickle.load(open(model, 'rb'))
            print('rfc_cv model loaded for 2G CSSR')
            prediction = loaded_model.predict(df4)
            print('Prediction is ready')
            result = pd.DataFrame(prediction)
            result.columns = ['Model_Remarks']
            result = a1.int_to_categorical(result)
            print('int to categorical conversion done')
            final_sheet = pd.merge(df3, result, left_index=True, right_index=True)
            print('Final Merged sheet is prepared')
            resp = make_response(final_sheet.to_csv())
            resp.headers["Content-Disposition"] = "attachment; filename=2G_CSSR_Remarks.csv"
            resp.headers["Content-Type"] = "text/csv"
            print('Please check Download folder for 2G CSSR Remarks sheet')
            return resp

        except Exception as e:
            print('The Exception  message is:', e)
            return 'Something is Wrong'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    #app.run(debug = True)
    #app.run(host='127.0.0.1', port=5001, debug=True)
    app.run(host='0.0.0.0', port=8001, debug=True)








