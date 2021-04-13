from wsgiref import simple_server
from flask import Flask, request, render_template
import pickle
import json
import numpy as np
"""
*****************************************************************************
*
* filename:       main.py
* version:        1.0
* author:         CODESTUDIO
* creation date:  05-MAY-2020
*
* change history:
*
* who             when           version  change (include bug# if apply)
* ----------      -----------    -------  ------------------------------
* bcheekati       05-MAY-2020    1.0      initial creation
*
*
* description:    flask main file to run application
*
****************************************************************************
"""

app = Flask(__name__)

def get_predict_profit(duration,src_bytes,dst_bytes,wrong_fragment,urgent,hot,
        num_failed_logins,num_compromised,root_shell,su_attempted,num_root,num_file_creations,num_shells,
        num_access_files,num_outbound_cmds,count,srv_count,serror_rate,srv_serror_rate,rerror_rate,srv_rerror_rate,
        same_srv_rate,diff_srv_rate,srv_diff_host_rate,dst_host_count,dst_host_srv_count,dst_host_same_srv_rate,
        dst_host_diff_srv_rate,dst_host_same_src_port_rate,dst_host_srv_diff_host_rate,dst_host_serror_rate,
        dst_host_srv_serror_rate,dst_host_rerror_rate,dst_host_srv_rerror_rate,protocol_type,service,flag,land_1,
        logged_in_1,is_host_login_1,is_guest_login_1):

    """
    * method: get_predict_profit
    * description: method to predict the results
    * return: prediction result
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * bcheekati      05-MAY-2020    1.0      initial creation
    *
    * Parameters
    *   r_d_expenses: R&D spent
    *   administration_expenses: admin cost
    *   marketing_expenses: marketing expenses
    *   state: state name
    """
    with open('models/Network_analysis.pkl', 'rb') as f:
        model = pickle.load(f)

    with open("models/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']


    try:
        protocol_type_index = data_columns.index('protocol_type_'+str(protocol_type).lower())
    except:
        protocol_type_index = -1
    try:
        service_index = data_columns.index('service_'+str(service).lower())
    except:
        service_index = -1
    try:
        flag_index = data_columns.index('flag_'+str(flag).lower())
    except:
        flag_index = -1

    x = np.zeros(len(data_columns))

    x[0] =  duration
    x[1] = src_bytes
    x[2] = dst_bytes
    x[3] = wrong_fragment
    x[4] = urgent
    x[5] = hot
    x[6] = num_failed_logins
    x[7] = num_compromised
    x[8] = root_shell
    x[9] = su_attempted
    x[10] = num_root
    x[11] = num_file_creations
    x[12] = num_shells
    x[13] = num_access_files
    x[14] = num_outbound_cmds
    x[15] = count
    x[16] = srv_count
    x[17] = serror_rate
    x[18] = srv_serror_rate
    x[19] = rerror_rate
    x[20] = srv_rerror_rate
    x[21] = same_srv_rate
    x[22] = diff_srv_rate
    x[23] = srv_diff_host_rate
    x[24] = dst_host_count
    x[25] = dst_host_srv_count
    x[26] = dst_host_same_srv_rate
    x[27] = dst_host_diff_srv_rate
    x[28] = dst_host_same_src_port_rate
    x[29] = dst_host_srv_diff_host_rate
    x[30] = dst_host_serror_rate
    x[31] = dst_host_srv_serror_rate
    x[32] = dst_host_rerror_rate
    x[33] = dst_host_srv_rerror_rate
    if protocol_type_index>=0:
        x[protocol_type_index] = 1
    # x[34] = protocol_type
    if service_index>=0:
        x[service_index] = 1

    # x[35] = service
    if flag_index>=0:
        x[flag_index] = 1
    # x[36] = flag
    x[37] = land_1
    x[38] = logged_in_1
    x[39] = is_host_login_1
    x[40] = is_guest_login_1


    # x[0] = r_d_expenses
    # x[1] = administration_expenses
    # x[2] = marketing_expenses
    # if state_index >= 0:
    #     x[state_index] = 1

    return model.predict([x])

@app.route('/')
def index_page():
    """
    * method: index_page
    * description: method to call index html page
    * return: index.html
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * bcheekati      05-MAY-2020    1.0      initial creation
    *
    * Parameters
    *   None
    """
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """
    * method: predict
    * description: method to predict
    * return: index.html
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * bcheekati      05-MAY-2020    1.0      initial creation
    *
    * Parameters
    *   None
    """
    if request.method == 'POST':
        duration = request.form["duration"]
        src_bytes = request.form["src_bytes"]
        dst_bytes = request.form["dst_bytes"]
        wrong_fragment = request.form["wrong_fragment"]
        urgent = request.form["urgent"]
        hot = request.form['hot']
        num_failed_logins = request.form["num_failed_logins"]
        num_compromised = request.form["num_compromised"]
        root_shell = request.form["root_shell"]
        su_attempted = request.form["su_attempted"]
        num_root = request.form["num_root"]
        num_file_creations = request.form["num_file_creations"]
        num_shells = request.form["num_shells"]
        num_access_files = request.form["num_access_files"]
        num_outbound_cmds = request.form["num_outbound_cmds"]
        count = request.form["count"]
        srv_count = request.form["srv_count"]
        serror_rate = request.form["serror_rate"]
        srv_serror_rate = request.form["srv_serror_rate"]
        rerror_rate = request.form["rerror_rate"]
        srv_rerror_rate = request.form["srv_rerror_rate"]
        same_srv_rate = request.form["same_srv_rate"]
        diff_srv_rate = request.form["diff_srv_rate"]
        srv_diff_host_rate = request.form["srv_diff_host_rate"]
        dst_host_count = request.form["dst_host_count"]
        dst_host_srv_count = request.form["dst_host_srv_count"]
        dst_host_same_srv_rate = request.form["dst_host_same_srv_rate"]
        dst_host_diff_srv_rate = request.form["dst_host_diff_srv_rate"]
        dst_host_same_src_port_rate = request.form["dst_host_same_src_port_rate"]
        dst_host_srv_diff_host_rate = request.form["dst_host_srv_diff_host_rate"]
        dst_host_serror_rate = request.form["dst_host_serror_rate"]
        dst_host_srv_serror_rate = request.form["dst_host_srv_serror_rate"]
        dst_host_rerror_rate = request.form["dst_host_rerror_rate"]
        dst_host_srv_rerror_rate = request.form["dst_host_srv_rerror_rate"]
        protocol_type = request.form["protocol_type"]
        service = request.form['service']
        flag = request.form["flag"]
        land_1 = request.form["land_1"]
        logged_in_1 = request.form["logged_in_1"]
        is_host_login_1 = request.form["is_host_login_1"]
        is_guest_login_1 = request.form["is_guest_login_1"]


        output = get_predict_profit(duration,src_bytes,dst_bytes,wrong_fragment,urgent,hot,
        num_failed_logins,num_compromised,root_shell,su_attempted,num_root,num_file_creations,num_shells,
        num_access_files,num_outbound_cmds,count,srv_count,serror_rate,srv_serror_rate,rerror_rate,srv_rerror_rate,
        same_srv_rate,diff_srv_rate,srv_diff_host_rate,dst_host_count,dst_host_srv_count,dst_host_same_srv_rate,
        dst_host_diff_srv_rate,dst_host_same_src_port_rate,dst_host_srv_diff_host_rate,dst_host_serror_rate,
        dst_host_srv_serror_rate,dst_host_rerror_rate,dst_host_srv_rerror_rate,protocol_type,service,flag,land_1,
        logged_in_1,is_host_login_1,is_guest_login_1)

        # r_d_expenses = request.form['r_d_expenses']
        # administration_expenses = request.form["administration_expenses"]
        # marketing_expenses = request.form["marketing_expenses"]
        # state = request.form["state"]
        # output = get_predict_profit(r_d_expenses, administration_expenses, marketing_expenses, state)
        return render_template('index.html',show_hidden=True, prediction_text='Netwrok must be  {}'.format(output))


if __name__ == "__main__":
    #app.run(debug=True)
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()