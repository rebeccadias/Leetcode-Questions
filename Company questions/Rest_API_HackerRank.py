"""
Question: Use the HTTP GET method to retrieve information from a database of patient medical records. Query https://jsonmock.hackerrank.com/api/medical_recordsto find all the records. The query result is paginated and can be further accessed by appending to the query string ?page=num where num is the page number.
The query response from the API is a JSON object with the following five fields:
﻿﻿page: the current page
﻿﻿per_page: the maximum number of results per page
﻿﻿total. the total number of records in the search result
﻿﻿total pages. the total number of pages to query in order to get all the results
﻿﻿data: an array of JSON objects containing medical records
The data field in the response contains a list of medical records with the following schema:
田
﻿﻿id. the unique ID of the record
﻿﻿timestamp: the timestamp when the record was generated (In UTC as milliseconds)

userld: the id of the user for whom the transaction has been recorded
• userName: the name of the patient for whom the transaction has been recorded
• userDob: the date of birth of user in format DD-MM-YYYY
• vitals. object, the vitals of the user
• vitals.bloodPressureDiastole: the diastolic pressure reading of the user, mmHg
• vitals.bloodPressure Systole: the systolic pressure reading of the user, mmHg
• vitals.pulse: the pulse rate of the user, beats per minute
• vitals.breathingRate: the breathing rate of the user, breaths per minute
• vitals. bodyTemperature: the body temperature of the user, degrees Fahrenheit
• diagnosis. object, the diagnosis for the user N
• diagnosis.id. the id of the condition diagnosed
• diagnosis.name: the name of the condition diagnosed
• diagnosis.severity. the severity of the condition diagnosed
• doctor. object, the doctor who diagnosed the condition
• doctor.id. the id of the doctor who diagnosed the condition
• doctor.name: the name of the doctor who diagnosed the condition
• meta: object, the meta information of the user
• meta.height. The current height of the user, centimeters
• meta. weight. The current weight of the user, pounds


Given the diagnosis name and doctor id, filter the records over all the pages.
Calculate the average pulse rate for these patients and return the value truncated to an integer. For example, 1.99 truncates to 1.
Function Description
Complete the function pulseRate in the editor below.
pulseRate has the following parameter(s):
string diagnosisName: name of the disease to be searched for int doctorld: Id of the doctor
Returns
int: the average pulse rate of the selected patients truncated to an integer

Sample Input For Custom Testing
Common Cold
2
Sample Output
101
Explanation
The diagnosis name and doctor id are searched in the records on pages 1 - 10.
The integer value of the average pulse rate is returned.

"""


#Solution

import requests
import math

def pulseRate(diagnosisName, doctorId):
    totalPulseRate = 0
    count = 0
    currentPage = 1
    totalPages = 1  # Placeholder, updated after first response

    while currentPage <= totalPages:
        response = requests.get(f"https://jsonmock.hackerrank.com/api/medical_records?page={currentPage}")
        json = response.json()

        if currentPage == 1:
            totalPages = json['total_pages']

        for record in json['data']:
            if record['diagnosis']['name'] == diagnosisName and record['doctor']['id'] == doctorId:
                totalPulseRate += record['vitals']['pulse']
                count += 1

        currentPage += 1

    if count > 0:
        averagePulseRate = totalPulseRate / count
        return truncateToInt(averagePulseRate)
    else:
        return 0  # No matching records found

def truncateToInt(number):
    return math.floor(number)



