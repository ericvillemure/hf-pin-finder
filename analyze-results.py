import re
import json

# The printed output of this script should be retried since they were all misunderstood by HFL.
# Since HFL will not spell out the recognized password on the 3rd attempt we are not outputting them
# in this script. Therefore if the password is not found after trying all possible combinations every 
# 2nd retries should be retried because it's possible one of the 3rd attempts was misunderstood but
# was also the right password.  The current rate for misunderstood passwords are about 8.5%

results_file = "data/results.json"
results = json.load(open(results_file))
misunderstood_passwords = list()
count_by_retries = {"0":0,"1":0,"2":0}
for key in results:
    #  results[row[0]] = {
    #         "PIN": row[0],
    #         "popularity": row[1],
    #         "retries": retries,
    #         "response": text,
    #         "audio": audio_file,
    #         "date": f'{datetime.datetime.now()}'
    #     }
    numeric_response = re.sub(r'[^0-9]', '', results[key]["response"])
    count_by_retries[str(results[key]["retries"])] += 1
    if (results[key]["retries"]!=2 and key != numeric_response):
        audio = results[key]["audio"] if "audio" in results[key] else "?"
        misunderstood_passwords.append(f'{results[key]["retries"]+1}/3 {key}!={results[key]["response"]} {audio}')

print(f'Number of tried PINS: {len(results)}')
print(f'Number of 2nd retries: {count_by_retries["2"]}')
print(f'Number of misunderstood PINS: {len(misunderstood_passwords)}')
print(count_by_retries)
print(*misunderstood_passwords,sep='\n')