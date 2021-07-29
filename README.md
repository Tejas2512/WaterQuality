# WaterQuality
<p align="center">
<img src="https://github.com/Tejas2512/WaterQuality/blob/fcdede47d58522842b24728bffc17f10c3dbb764/images/water.gif" >
</p>

Build web application using flask and python to predict water potability.

## Context
Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection. This is important as a health and development issue at a national, regional and local level. In some regions, it has been shown that investments in water supply and sanitation can yield a net economic benefit, since the reductions in adverse health effects and health care costs outweigh the costs of undertaking the interventions.

## Architecture
<p align="center">
<img src="https://github.com/Tejas2512/WaterQuality/blob/6785bcefb50cee80ccdb67f347772735dd63846c/images/flowchart.png">
</p>

## About Data

ppm: parts per million\
μg/L: microgram per litre\
mg/L: milligram per litre

**Column description:**

**1. ph:** pH of 1. water (0 to 14).\
**2. Hardness:** Capacity of water to precipitate soap in mg/L.\
**3. Solids:** Total dissolved solids in ppm.\
**4. Chloramines:** Amount of Chloramines in ppm.\
**5. Sulfate:** Amount of Sulfates dissolved in mg/L.\
**6. Conductivity:** Electrical conductivity of water in μS/cm.\
**7. Organic_carbon:** Amount of organic carbon in ppm.\
**8. Trihalomethanes:** Amount of Trihalomethanes in μg/L.\
**9. Turbidity:** Measure of light emiting property of water in NTU.\
**10. Potability:** Indicates if water is safe for human consumption. Potable is 1 and not potable is 0.


## Prediction

  ph | Hardness | Solids | Chloramines | Sulfate | Conductivity | Organic_carbon | Trihalomethanes | Turbidity | Potability
 --- | --- | --- |--- |--- |--- |--- |--- |--- |---
 6.8 | 181 | 500 | 3 | 30 | 350 | 2 | 70 | 4 | 1
  8.8 | 224 | 1100 | 6 | 1500 | 600 | 5 | 90 | 6 | 0


<p align="center">
<img src="https://github.com/Tejas2512/WaterQuality/blob/51fd9bc6f0dda161d4ea6e4a88857a5d8d3880fa/images/water-quality.gif" >
</p>

## App URL
https://water-potability-checker.herokuapp.com/
