from flask import Flask, request, render_template

import sklearn
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model.pkl")



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/",methods=["POST"])
def predict():
    if request.method=="POST":
        date_dep=request.form["Departure_Date"]
        Journey_Day=pd.to_datetime(date_dep,infer_datetime_format=True).day
        Journey_Month=pd.to_datetime(date_dep,infer_datetime_format=True).month
        
        Dept_hour=pd.to_datetime(date_dep,infer_datetime_format=True).hour
        Dept_min=pd.to_datetime(date_dep,infer_datetime_format=True).minute
        Total_stops = int(request.form["Stopage"])
        Arrival_Time=request.form["Arrival_Date"]
        Arrival_hour=pd.to_datetime(Arrival_Time,infer_datetime_format=True).hour
        Arrival_min=pd.to_datetime(Arrival_Time,infer_datetime_format=True).minute
        dur_hour = abs(Arrival_hour - Dept_hour)
        dur_min = abs(Arrival_min - Dept_min)
        airline=request.form['Airline']
        if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            AirAsia=1
            

        elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            AirAsia=1
             

        elif (airline=='AirIndia'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_with_Premium_convoy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            AirAsia=1
            
            
        elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_with_Premium_convoy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
        
            
        elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_with_Premium_convoy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            AirAsia=1
            
            
        elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_with_Premium_convoy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            

        elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_with_Premium_convoy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            AirAsia=1

        elif (airline=='Multiple carriers with Premium Convoy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_with_Premium_convoy = 1
            Jet_Airways_Business = 0
            AirAsia=1
            Vistara_Premium_economy = 0
            

        elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            AirAsia=1
            

        elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            AirAsia=1
        elif (airline=='AirAsia'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            AirAsia=1
            
            

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            AirAsia=0
        
        Source = request.form["Source"]
        
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
            s_Bangalore = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            s_Bangalore = 0
        elif (Source == 'Bangalore'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore = 1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore = 0


        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0
            
        
        elif (Destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore = 0

        elif (Destination == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0
            

        elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
            d_Bangalore=0
            

        elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
            d_Bangalore=0
        elif (Destination == 'Bangalore'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=1
            


        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0
            
        prediction=model.predict([[
            Total_stops,
            Journey_Day,
            Journey_Month,
            Dept_hour,
            Dept_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            AirAsia,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Vistara,
            Vistara_Premium_economy,
            s_Bangalore,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Bangalore,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])
        output=round(prediction[0],2)
    return render_template("index.html",price=output)

if __name__ == "__main__":
    app.run(debug=True)