

import cgi
import cgitb
import athletemodel
import yate

cgitb.enable()

athletes = athletemodel.get_from_store()

from_data=cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.header("Athlete:" + athlete_name + ", DOB" +
                    athletes[athlete_name].dob + "."))

print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3()))
print(yate.start_form("generate_list.py"))
print(yate.para("Select an athlete from the list to work with:"))

for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))

print(yate.end_form("select"))
print(yate.include_footer({"Home": "/index.html"}))