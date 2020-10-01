
from PAJ7620U2_TCA9548A import *

TimeInit = 0.1
TimePeriod = 0.005
NBR_VALVES = 8

I2C_ch=[I2C_ch_0, I2C_ch_1, I2C_ch_2, I2C_ch_3, I2C_ch_4, I2C_ch_5, I2C_ch_6, I2C_ch_7]
obj = [0]*NBR_VALVES
obj_prev = [0]*NBR_VALVES


if __name__ == '__main__':
	
	
	#---------------------------------------------------------------------------------------------------------
	print("-------------------------------\nInitialisation I2C channels ...\n--------------------------------")
	for i in range(NBR_VALVES):
		
		try:
			I2C_setup(int(I2C_ch[i]))
			paj7620u1=PAJ7620U2()
			time.sleep(TimeInit)
			obj[i] = paj7620u1.check_gesture()
			print("I2C channel{}: {}".format(i, obj[i]))
		except Exception as e:
			print(" -> [-]Error initialisation channel{} I2C: {}".format(i,e))
			try:
				I2C_setup(int(I2C_ch[i]))
				paj7620u1=PAJ7620U2()
				time.sleep(TimeInit)
				obj[i] = paj7620u1.check_gesture()
				print("I2C channel{}: {}".format(i, obj[i]))
			except Exception as e:
				print(" -> [-]Error initialisation channel{} I2C: {}".format(i,e))
			#sys.exit()
		print(" -> [+] Channel{} I2C initialsed.".format(i))
	
	print("\nEnd of the I2C channels initialisation.")
	print("-----------------------------------------")
	time.sleep(TimeInit)
		
	#-------------------------------------------------------------------
	print("\nSensor size and brightness ...\n")
	while True:
		
		for i in range(NBR_VALVES):
		
			try:
				I2C_setup(int(I2C_ch[i]))
				obj[i] = paj7620u1.check_gesture()
				obj_prev[i] = obj[i]
			except Exception as e:
				print("Issue reading channel{}: {}".format(i, e))
				try:
					print("Retrying a read channel {}".format(i))
					I2C_setup(int(I2C_ch[i]))
					obj[i] = paj7620u1.check_gesture()
					obj_prev[i] = obj[i]
				except Exception as e:
					print("Previous value channel {}".format(i))
					obj[i] = obj1_prev[i]
			
			time.sleep(TimePeriod)
		print("Sensor1: {:10} - Sensor2: {:10} - Sensor3: {:10} - Sensor4: {:10} - Sensor5: {:10} - Sensor6: {:10} - Sensor7: {:10} - Sensor8: {:10}".format(str(obj[0]), str(obj[1]), str(obj[2]), str(obj[3]), str(obj[4]), str(obj[5]), str(obj[6]), str(obj[7])))
		
#---------------------------------------------------------------
