#imports
import matplotlib.pyplot as plt
from time import sleep
import math

#Gen Params
isolation  = 155
time = 0
heat_cap = 1000
earth_energy = 0
earth_temp = 0
dt = 60
#albedo = 0.29


#Surface Params
surface_heat_cap = 1000
surface_temp = 250
surface_emissivity = 0.99

#albedo profile
Ocean = 0.07
Snow_ice = 0.65
Tundra = 0.17
Desert = 0.36
Forest = 0.15
Grassland = 0.20

albedo_comp = [Ocean,Snow_ice,Tundra,Desert,Forest,Grassland]

Ocean_percentage = 0.70  #0.70
Snow_ice_percentage = 0.04 #0.04
Tundra_percentage = 0.06 #0.06
Desert_percentage = 0.1 #0.1
Forest_percentage = 0.04 #0.04
Grassland_percentage = 0.06 #0.06

surface_comp = [Ocean_percentage,Snow_ice_percentage,Tundra_percentage,Desert_percentage,Forest_percentage,Grassland_percentage]

def albedo_complier(surface_comp,albedo_comp):
    albedo = 0.0
    
    for i in range(len(surface_comp)):
        albedo+=surface_comp[i]*albedo_comp[i]
    return (albedo)

albedo = albedo_complier(surface_comp,albedo_comp)


# Atmosphere Params
atm_heat_cap = 5000
atm_temp = 250 #
atm_emissivity = 0.99
atm_abs = 0.20

#layer2
atm_heat_cap_2 = 2500
atm_temp_2 = 200 #

atm_abs_2 = 0.10

#layer3
atm_heat_cap_3 = 1500
atm_temp_3 = 150 #

atm_abs_3 = 0.05

#layer4
atm_heat_cap_4 = 1500
atm_temp_4 = 100 #

atm_abs_4 = 0.01

#plot init
plt.figure()
plt.xlabel("Time")
plt.ylabel("Temp")
plt.ion()

def black_body(temp):
    sigma = 5.67E-8
    return sigma*temp**4

def day_night(time_now):
    return 1 + (math.sin(time_now*math.pi/86400))/4   #the *24 is to speed up the cycle 

    


print("Albedo: " + str(albedo))
a=0
while True:
    
    albedo = (day_night(time))*(albedo_complier(surface_comp,albedo_comp))
    
    surface_temp += ((isolation*(1-albedo-atm_abs-atm_abs_2)) + (atm_emissivity*black_body(atm_temp)) - black_body(surface_temp))*dt/surface_heat_cap
    atm_temp += ((atm_abs*isolation)+(atm_emissivity*black_body(atm_temp_2))+(surface_emissivity*black_body(surface_temp))-(2*(black_body(atm_temp))))*dt/atm_heat_cap
    atm_temp_2 += ((atm_abs_2*isolation)+(atm_emissivity*black_body(atm_temp))+(atm_emissivity*black_body(atm_temp_3))-(2*(black_body(atm_temp_2))))*dt/atm_heat_cap_2
    atm_temp_3 += ((atm_abs_3*isolation)+(atm_emissivity*black_body(atm_temp_2))-(2*(black_body(atm_temp_3))))*dt/atm_heat_cap_3
    time += dt 
    #print("Time:"+str(time)+" S | Earth Temp:"+str(surface_temp)+" K"+" | Atmosphere Temp:"+str(atm_temp)+" K")
    if a==100:
        plt.scatter(time, surface_temp, color="blue")
        plt.scatter(time, atm_temp, color="yellow")
        plt.scatter(time, atm_temp_2, color="red")
        plt.scatter(time, atm_temp_3, color="black")
        #plt.scatter(time, atm_temp_3, color="red")
        print(surface_temp-atm_temp,atm_temp-atm_temp_2)
        plt.pause(0.00001)
        #sleep(0.00005)
        a=0
    a+=1
    
