import paho.mqtt.client as mqtt
import threading
import time
from queue import Queue
import csv


q1 = Queue() #process queue for sensor 1
log_list1 = [] #log list for sensor 1
q2 = Queue()
log_list2 = []
q3 = Queue()
log_list3 = []
q4 = Queue()
log_list4 = []

nclients = 4
process_queues = [q1, q2, q3, q4]
log_lists = [log_list1, log_list2, log_list3, log_list4]
client_threads = []


def on_connect(client, userdata, flags, rc):
	print(f"Connected with result code {rc}")
def on_log(client, userdata, level, buf):
	print("log: " + buf)

def on_message(client, userdata, msg):
    message = str(msg.payload.decode("utf-8"))
    topics = msg.topic.split('/')
    # print(topics)
    subtopic = topics[1]
    match subtopic:
        case 'data':
            client.proq.put(message)
            client.logL.append([message])
            with open(f'{client.logfile}.csv', 'w', newline='') as f:
                csvwriter = csv.writer(f)
                csvwriter.writerows(client.logL)
                f.close()
        case 'calib':
            print(f'{topics[0]}: {message}')
        case 'calib_status':
            if message == 'a':
                print('imu is not calibrated')
            else:
                print('imu is calibrated')

def Sub(client, topic):
    client.subscribe(f'{topic}/#')
    client.loop_forever()

# def process(s1, s2):
#     log_process =[]
#     while True:
#         if not (s1.empty() or s2.empty()):
#             a = s2.get()
#             b = s1.get()
#             c = int(a.split(' ')[2]) - int(b.split(' ')[2])
#             log_process.append([c])
#             with open(f'log_process.csv', 'w', newline='') as f:
#                 csvwriter = csv.writer(f)
#                 csvwriter.writerows(log_process)
#                 f.close()


for i in range(nclients):
    cname="client"+str(i)
    t=int(time.time())
    client_id =cname+str(t) #create unique client_id
    client = mqtt.Client(client_id) #create new instance
    client.proq = process_queues[i]
    client.logL = log_lists[i]
    client.logfile = f'log_list{i+1}'
    client.on_connect = on_connect
    #client.on_publish = on_publish
    client.on_message = on_message
    client.username_pw_set("user" + str(i+1),"1234")
# Create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
    client.connect("192.168.50.10", 1883, 3600)
    client_threads.append(threading.Thread(target=Sub, args=(client,f'mqtt{i+1}',)))


for thread in client_threads:
    thread.start()

# process_thread = threading.Thread(target=process, args=(q1, q2,))
# process_thread.start()
