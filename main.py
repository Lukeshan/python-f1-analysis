import matplotlib.pyplot as plt

import fastf1.plotting

fastf1.Cache.enable_cache('cache')

# Load FastF1's dark color scheme
# fastf1.plotting.setup_mpl(mpl_timedelta_support=False, color_scheme='fastf1')

session = fastf1.get_session(2025, 20, 'Q')
session.load(telemetry=True, weather=False)
circuit_info = session.get_circuit_info()
corners_df = circuit_info.corners  # This is a pandas DataFrame
print(corners_df) 

ham_lap = session.laps.pick_drivers('HAM').pick_fastest()

ham_tel = ham_lap.get_car_data().add_distance()

plt.plot(ham_tel['Distance'], ham_tel['Speed'], label='HAM')
for corner in range(corners_df.shape[0]):
    plt.axvline(corners_df.iloc[corner]["Distance"], color='black', linestyle='--', alpha = 0.4)
    

plt.title(f"{session.session_info["Meeting"]["Name"]} Quali Hamilton Fast Lap Data")
plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.grid("minor")
plt.legend()
plt.show()

    