	•	Notations:
	  ⁃	quat1: IMU on shank
	  ⁃	quat2: IMU on thigh
    
	•	Method 1 (no name):
	  ⁃	quat1 * quat2 * quat1.conjugate()
    
	•	Method 2:
	  ⁃	quat2 * quat1.conjugate()
    
	•	Method 3:
	  ⁃	quat1.conjugate() * quat2
