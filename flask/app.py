from flask import Flask, render_template,request
import pickle
app=Flask(__name__)

model=pickle.load(open("salary.pkl","rb"))
@app.route('/')
@app.route('/home',methods=['GET','POST'])
def homepage():
                return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
                return render_template('prediction.html')


@app.route('/result', methods =['GET','POST'])
def result():
 if request.method=="POST":
        Specialty =(request.form['Specialty'])
        Female =(request.form['Female'])
        Feel_Fairly_Compensated = (request.form['Feel_Fairly_Compensated'])
        Difference_in_Earnings_between_Physicians_who_Feels_Fairly_vs_Unfairly_Paid = (request.form['Difference_in_Earnings_between_Physicians_who_Feels_Fairly_vs_Unfairly_Paid'])
        overall_career_satisfaction = (request.form['overall_career_satisfaction'])
        satisfied_w_income = (request.form['satisfied_w_income'])
        would_choose_medicine_again = (request.form['would_choose_medicine_again'])
        would_choose_the_same_specialty = (request.form['would_choose_the_same_specialty'])
        survey_respondents_by_specialty = (request.form['survey_respondents_by_specialty'])
        labels_below_are_correct_only_when_annual_income_is_in_descending_order =(request.form['labels_below_are_correct_only_when_annual_income_is_in_descending_order'])


        pred =[[float(Specialty), float(Female) ,float(Feel_Fairly_Compensated), float(Difference_in_Earnings_between_Physicians_who_Feels_Fairly_vs_Unfairly_Paid),float(overall_career_satisfaction), float(satisfied_w_income), float(would_choose_medicine_again), float(would_choose_the_same_specialty), float(survey_respondents_by_specialty),float(labels_below_are_correct_only_when_annual_income_is_in_descending_order)]]
        print(pred)
        output = model.predict(pred)
        print(output)
        return render_template('result.html',output=output)


if __name__=='__main__':
        app.run(debug=True)
