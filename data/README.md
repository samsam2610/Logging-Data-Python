# Read me please!
- Methods explained:
	- Notations:
		- quat1: IMU on shank
		- quat2: IMU on thigh    
	- Method 1 (no name):
		- quat1 * quat2 * quat1.conjugate()
	- Method 2:
		- quat2 * quat1.conjugate()
	- Method 3:
		- quat1.conjugate() * quat2

- P.S: Sam's ROM is about 125 degrees.
- Method 2 - 2nd dataset: Right Leg touched left butt.
