from flask import Flask, jsonify, request
import requests
import threading, time, schedule, os

SECRET = os.getenv('SECRET', 'my-secret')
STOP_EVENT = threading.Event()
# Time is in Universal Time (UTC)
WAKE_UP_TIME = os.getenv('WAKE_UP_TIME', '14:30')
SLEEP_TIME = os.getenv('SLEEP_TIME', '16:30')
EMAIL = os.getenv('EMAIL', 'my@email.com')
PASSWORD = os.getenv('PASSWORD', 'password')
SERVER = os.getenv('SERVER', 'https://myserver.com')
SCHEDULE_THREAD = {
	"thread": None
}

app = Flask(__name__)

def log(message):
	print(message)

def error(status, message):
	print(status, message)
	return {
		"status": status,
		"message": message
	}

def get_token():
	try:
		r = requests.post('{}/api/auth'.format(SERVER), json = {
			"email": EMAIL,
			"password": PASSWORD
		})
		token = r.json()['token']
		return (token, None)
	except:
		return (None, error(r.status_code, "Failed to get token."))

def conduit_call(device, function, token):
	return requests.get('{}/api/send/{}/{}'.format(SERVER, device, function), headers = {
		"x-access-token": token
	})

def wake_up_protocol():
	log("Beginning wake up protocol.")
	token, err = get_token()
	if(err): return err

	log("Start massage.")
	# start massage
	for i in range(3):
		conduit_call("bedremote", "head_massage_on", token)
		time.sleep(1)
	for i in range(3):
		conduit_call("bedremote", "foot_massage_on", token)
		time.sleep(1)
	time.sleep(30)

	log("Start bed lift.")
	# lift bed
	conduit_call("bedremote", "head_on", token)
	time.sleep(30)
	conduit_call("bedremote", "head_stop", token)
	log("End bed lift.")

	log("Start leg lift.")
	# lift bed
	conduit_call("bedremote", "foot_on", token)
	time.sleep(30)
	conduit_call("bedremote", "foot_stop", token)
	log("End leg lift.")

	log("End massage lift.")
	# stop massage 
	time.sleep(300)
	for i in range(4):
		conduit_call("bedremote", "head_massage_off", token)
		time.sleep(1)
	for i in range(4):
		conduit_call("bedremote", "foot_massage_off", token)
		time.sleep(1)

	return "Completed wake up protocol."

def sleep_protocol():
	log("Beginning sleep protocol.")
	token, err = get_token()
	if(err): return err
	
	conduit_call("bedremote", "head_off", token)
	time.sleep(40)
	conduit_call("bedremote", "head_stop", token)
	
	conduit_call("bedremote", "foot_off", token)
	time.sleep(40)
	conduit_call("bedremote", "foot_stop", token)

	return "Completed sleep protocol."

def schedule_loop(stop_event, wake_time, sleep_time):
	log("Running alarm thread with wake up at: {} and sleep time at: {}!".format(wake_time, sleep_time))
	
	schedule.clear('alarm')
	schedule.every().day.at(wake_time).do(wake_up_protocol).tag('alarm')
	schedule.every().day.at(sleep_time).do(sleep_protocol).tag('alarm')

	while not stop_event.wait(1):
		schedule.run_pending()
		time.sleep(1)

	stop_event.clear()
	log("Alarm thread stopped.")

def set_loop(wake_time, sleep_time):
	thread = threading.Thread(target=schedule_loop, args=(STOP_EVENT, wake_time, sleep_time))
	thread.start()
	return thread

@app.route("/set", methods=['POST'])
def set_alarm():
	"""set_alarm will take in two times as json, one to raise the bed, and one to lower the bed.
		:int wake_hour:
		:int wake_minute:
		:int sleep_hour:
		:int sleep_minute:
		:return: Returns completed.
	"""
	content = request.get_json()
	
	if(SECRET != content['secret']):
		return jsonify(error("Forbidden", "invalid-secret")), 403

	STOP_EVENT.set()
	SCHEDULE_THREAD['thread'].join()
	
	wake_hour = content['wake_hour']
	wake_minute = content['wake_minute']
	sleep_hour = content['sleep_hour']
	sleep_minute = content['sleep_minute']
	
	SCHEDULE_THREAD['thread'] = set_loop("{}:{}".format(wake_hour, wake_minute), "{}:{}".format(
		sleep_hour, 
		sleep_minute)
	)

	return jsonify({
		"status": "Alarm updated with wake up at: {}:{} and sleep time at: {}:{}!".format(
			wake_hour, wake_minute, sleep_hour, sleep_minute
		)
	}), 200

if __name__ == "__main__":
	SCHEDULE_THREAD['thread'] = set_loop(WAKE_UP_TIME, SLEEP_TIME)
	app.run(host='0.0.0.0')
