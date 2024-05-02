import numpy as np  # Import NumPy library

def predict_handover(device_position, access_points):
    closest_ap = min(access_points, key=lambda ap: np.linalg.norm(np.array(device_position) - np.array(ap.position)))
    return closest_ap

class AccessPoint:
    def __init__(self, position):
        self.position = position

device_position = (10, 20)
ap1 = AccessPoint((5, 15))
ap2 = AccessPoint((15, 25))
ap3 = AccessPoint((20, 10))
access_points = [ap1, ap2, ap3]
predicted_ap = predict_handover(device_position, access_points)

print("Predicted Handover to AP:", predicted_ap.position)
