import requests
import json


# headers = {
# 	"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# 	"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61",
# 	"bx-ajax" : "true"
# 	# "group" : "ИВТ-33"
# }


# def get_page(url):
# 	s = requests.Session()
# 	response = s.get(url=url, headers=headers)

# 	with open("index.html", "w") as file:
# 		file.write(response.text)

# def get_json(url):
# 	s = requests.Session()
# 	response = s.post(url=url, data={'group': 'БТС-11'})

# 	if (response):
# 		with open("result.json", "w") as file:
# 			json.dump(response.json(), file, indent=4, ensure_ascii=False)



# with open("pysch.json") as file:
# 	data = json.load(file)

# ######################################################################################################################################## #

def get_groups(url): # GET request ; JSON response
	s = requests.Session()
	response = s.get(url=url)

	return response.json()

def get_schedule(url, group): # POST request ; JSON response
	s = requests.Session()
	response = s.post(url=url, data={'group': group})

	return response.json()

def get_all_schedules(): # All schedules for all groups in one file pysch.json
	groups = get_groups(url="https://miet.ru/schedule/groups")
	if (groups):
		print(len(groups))

	allData = []

	for group in groups :
		schedule = get_schedule(url="https://miet.ru/schedule/data", group=group)

		if (schedule):
			allData.append(schedule)
			print(group + " parsed")
	
	print("THAT ALL!")
	print(len(allData))
	with open("pysch.json", "w") as file:
		json.dump(allData, file, indent=4, ensure_ascii=False)


# ----- ### ----- MAIN FUNCTION ----- ### ----- #
def main(): 
	
	get_all_schedules()

if __name__ == "__main__":
	main()

