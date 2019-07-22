import threading
import logging

import time


def run_function(fruit):
	logging.info("Thread %s: starting", fruit)
	time.sleep(2)
	logging.info("Thread %s: starting", fruit)

	time.sleep(1)
	
	logging.info("Thread %s: starting", fruit)
	time.sleep(1)

	logging.info("Thread %s: starting", fruit)
	
	logging.info("Thread %s: finishing")

if __name__=="__main__":
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format , level=logging.INFO, datefmt="%H:%M:%S")

	logging.info(" Main: before creating thread")

	x = threading.Thread(target=run_function, args=(1,), daemon=True)


	x.start()
	time.sleep(3)
	logging.info("Main: Waiting for all the threads to finish")

	logging.info(" Main: All Done")
