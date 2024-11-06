earth_to_moon = 384_400
earth_to_sun = 149_600_000
mars_to_sun = 227_940_000
saturn_to_sun = 1_430_000_000
moon_to_mars = mars_to_sun - (earth_to_sun + earth_to_moon)
mars_to_saturn = saturn_to_sun - mars_to_sun

earth_to_moon_autonomy = 4160.149
moon_to_mars_autonomy = 1314.161
mars_to_saturn_autonomy = 2832.438

earth_to_moon_total_gas = float("{:.4f}".format(earth_to_moon/earth_to_moon_autonomy)[:-1])
moon_to_mars_total_gas = float("{:.4f}".format(moon_to_mars/moon_to_mars_autonomy)[:-1])
mars_to_saturn_total_gas = float("{:.4f}".format(mars_to_saturn/mars_to_saturn_autonomy)[:-1])

print(f"earth to moon gas: {earth_to_moon}/{earth_to_moon_autonomy} = {earth_to_moon_total_gas}")
print(f"moon to mars gas: {moon_to_mars}/{moon_to_mars_autonomy} = {moon_to_mars_total_gas}")
print(f"earth to moon gas: {mars_to_saturn}/{mars_to_saturn_autonomy} = {mars_to_saturn_total_gas}")

total_gas = earth_to_moon_total_gas + moon_to_mars_total_gas + mars_to_saturn_total_gas

print(f"Total gas: {total_gas}")
