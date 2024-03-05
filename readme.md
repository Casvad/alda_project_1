# About this repo

Project to generate random data about cars in colombia.

# Attributes 

1. VehicleID (Primary Key): Unique identifier for each vehicle.
2. LicensePlate: The license plate number of the vehicle.
3. Brand: The brand or manufacturer of the vehicle. 
4. Model: The model of the vehicle. 
5. Year: The manufacturing year of the vehicle. 
6. Color: The color of the vehicle. 
7. FuelType: The type of fuel the vehicle uses (e.g., gasoline, diesel, electric). 
8. TransmissionType: The type of transmission (e.g., automatic, manual). 
9. OdometerReading: The current odometer reading of the vehicle. 
10. RegistrationDate: The date when the vehicle was registered. 
11. InsuranceProvider: The insurance provider for the vehicle. 
12. InsuranceExpirationDate: The expiration date of the vehicle insurance. 
13. OwnerName: The name of the vehicle owner. 
14. OwnerID: Identification number of the vehicle owner. 
15. OwnerAddress: The address of the vehicle owner. 
16. City: The city where the vehicle is registered. 
17. Department: The department (administrative region) where the vehicle is registered. 
18. VehicleType: The type of vehicle (e.g., sedan, SUV, truck). 
19. EngineSize: The size of the vehicle engine.  
20. WheelDrive: The type of wheel drive (e.g., 2WD, 4WD).
21. LastMaintenanceDate: The date of the vehicle's last maintenance. 
22. NumberOfSeats: The number of seats in the vehicle. 
23. NumberOfDoors: The number of doors in the vehicle. 
24. GPSInstalled: Indicates whether the vehicle has a GPS system installed. 
25. EmissionStandard: The emission standard the vehicle complies with. 
26. SafetyRating: Safety rating of the vehicle. 
27. InsuranceCoverageType: Type of coverage in the vehicle insurance. 
28. EstimatedMarketValue: Estimated market value
29. VehicleStatus: IN_USE,SELLING,MAINTENANCE
30. AccidentHistory: 

Taken from ChatGPT

# Sources

1. Car Color https://www.elcarrocolombiano.com/industria/colores-de-autos-mas-populares-2021/
2. Brand https://www.eltiempo.com/economia/finanzas-personales/estas-son-las-marcas-de-carros-mas-vendidas-en-colombia-en-2023-801990
3. fuel_type https://www.semana.com/economia/actualidad/vida-ejecutiva/automoviles/articulo/en-colombia-de-los-vehiculos-a-gas-natural-el-77-por-ciento-son-buses-y-el-16-camiones/202218/
4. transmission_type https://noticias.autocosmos.com.co/2020/04/21/los-autos-con-caja-mecanica-tienden-a-desaparecer
5. insurance_provider https://aliarseguros.com/blog-mejores-aseguradoras-autos-colombia
6. city https://noticias.autocosmos.com.co/2019/10/03/en-que-lugares-de-colombia-se-matriculan-mas-vehiculos
7. vehicle_type https://www.motor.com.co/industria/En-2023-se-vendieron-186.222-vehiculos-nuevos-en-Colombia.-Cayo--29-el-mercado.-20240102-0006.html

---

# Python version
Python 3.11.0

# Running locally and testing

```
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

# Check coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. 
Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```shell

```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.