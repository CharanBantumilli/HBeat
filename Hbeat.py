from joblib import load
import pandas as pd
import argparse
import warnings

def Main():
    parses = argparse.ArgumentParser(
        prog= "Hbeat",
        description= "Heart Stroke Risk Analyzer - Supply patient data as arguments.",
        epilog= "Example:\n  Hbeat 56 1 1 120 236 0 124 --inherited 1 --oxygenlevels 2 --aw 79.825 --model \"./models/alt_Hbeat.joblib\"",
        formatter_class= argparse.RawTextHelpFormatter
    )
    parses.add_argument("Age",type=int, help="Age of the patient")
    parses.add_argument("Sex",type=int ,help="0 = Female 1 = Male")
    parses.add_argument("Chestpain",type=int, help="Chest pain type (0-3)")
    parses.add_argument("BP",type=int, help="Resting blood pressure (mm Hg)")
    parses.add_argument("Cholestrol",type=int, help="Serum cholestrol (mg/dl)")
    parses.add_argument("Sugar",type=int ,help="Fasting blood sugar >120mg/dl (1=True, 0=False)")
    parses.add_argument("HeartRate",type=int, help="Maximum heart rate achieved")
    parses.add_argument("--inherited",type=int,default=0, help="Family history of heart disease (1=True, 0=False, Default=0)")
    parses.add_argument("--oxygenlevels",type=int, default=1, help="Oxygen level indicator (Default: 1)")
    parses.add_argument("--aw",type=float,default=0.0, help="Artery width value (Default: 0.0)")
    parses.add_argument("--model", default="Hbeat.joblib",help="Path to model file")

    args = parses.parse_args()
    warnings.filterwarnings('ignore')

    model = load(args.model)

    data = pd.DataFrame([{
        'Age': args.Age, 'Sex': args.Sex, 'Chestpain': args.Chestpain, 'BP': args.BP, 'Cholestrol': args.Cholestrol, 'Sugar': args.Sugar,     
        'HeartRate': args.HeartRate, 'Inherited': args.inherited, 'Oxygenlevels': args.oxygenlevels, 'AW': args.aw
    }])

    prediction = model.predict(data)
    if prediction[0]==1:
        print(f'Prediction: risk of heart disease detected. Please consult a doctor.\n Data:\n {data}')
    elif prediction[0]==0:
        print("Prediction: No significant heart risk detected. Stay healthy!")
    else:
        print(f"Unexpected prediction value: {prediction}")

if __name__ == "__main__":
    Main()
