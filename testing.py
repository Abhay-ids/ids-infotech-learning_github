import re

text = '''

SAINT LUCIA GOVERNMENT GAZETTE
1404
Issue 42 | Monday October 16,  2023
File No (210): TM/2023/ 000168
Mark Name:  KGM
Applicant (730): KG Mobility Corp. of 455-12, Dongsak-
ro, Pyeongtaek-si, Gyeonggi-do, Republic of Korea
Filing date (220): 26/06/2023
Priorities (330): March 23, 2023  South Korea  40-
2023-0051860
Agent (740): Leslie Prospere of GORDON, GORDON 
& CO. of P. O. Box 161, 10, Manoel Street, Castries, 
St. Lucia
Class (511): 12 Automobiles; parts and fi ttings for 
automobiles; land vehicles; air pumps for automobiles; 
automobile engines; steering wheels for automobiles; 
automobile tires; parts and fi ttings for motorcycles; 
traction control systems for automobiles; electric 
cars; doors for automobiles; suspension systems for 
automobiles; bicycles; motorcycles; lane departure 
warning systems for automobiles; seat covers for 
automobiles; self-driving cars; vehicles for locomotion 
by land, air, water or rail; automobile sunroofs; 
bumpers for automobiles.
BETADINE
File No (210): TM/2017/ 000182
Mark Name: BETADINE
Applicant (730): Mundipharma AG of St. Alban-
Rheinweg 74, CH-4020 Basel, Switzerland
Filing date (220): 09/08/2017
Agent (740): LEONNE THEODORE-JOHN of 
NICHOLAS JOHN & CO., Hewanorra House, 
TrouGarnier Financial Centre, Pointe Seraphine, 
Castries, Saint Lucia
Class (511): 05 Pharmaceutical preparations and 
substances; 
Pharmaceutical 
and 
veterinary 
preparations; sanitary preparations for medical 
purposes; dietetic food and substances adapted for 
medical or veterinary use; dietary supplements for 
humans and animals; dietetic substances adapted for 
medical use; dietary supplements; plasters, materials 
for dressings; disinfectants; antiseptics; pharmaceutical 
preparations and substances, including, acids and 
chemical preparations for pharmaceutical purposes; 
pharmaceutical creams; gels for dermatological use; 
medicinal oils; skin creams, gels, oils, lotions and 
ointments for pharmaceutical purposes; medicinal 
ointments; homeopathic pharmaceutical preparations; 
pharmaceutical preparations being comprised of 
plant extracts; extracts of medicinal plants; nail care 
preparations for medical use; medicated hair care 
preparations; pharmaceutical preparations for skin 
care; pharmaceutical preparations for use on the scalp, 
nails, hair, and skin and pharmaceutical sunscreen 
and sun care preparations; sunburn preparations for 
pharmaceutical purposes; antiseptic and antibacterial 
preparations; wipes for medical use; medical 
dressings; wipes, dressings, cloths, and materials for 
use in dressing wounds, including those impregnated 
with pharmaceutical preparations; cleaning cloths 
impregnated with disinfectant for hygiene purposes; 
wound dressings; Antitussive lozenges; Lozenges 
for pharmaceutical purposes; Breath freshening 
preparations, containing medicines; eye drops; Gargle 
for medical purposes; Sore throat lozenges.
BZ5C
File No (210): TM/2023/ 000218
Mark Name: BZ5C
Applicant (730): TOYOTA JIDOSHA KABUSHIKI 
KAISHA (also trading as TOYOTA MOTOR 
CORPORATION) of 1, Toyota-cho, Toyota-shi, 
Aichi-ken, Japan
Filing date (220): 20/07/2023
Agent (740): Tyrone D. Chong of P O Box 81, Castries, 
St. Lucia
Class (511): 12 Automobiles and structural parts thereof.
File No (210): TM/2023/ 000225
Mark Name: Chee Zees
Applicant (730): Associated Brands Industries Limited 
of No. 2 Bhagowite Traces, San Juan, Trinidad and 
Tobago
Filing date (220): 03/08/2023
Agent (740): Tyrone D. Chong of 27 Micoud Street, 
Castries, St. Lucia
Class (511): 29 Snack food made from potato or based 
products; potato-based snack foods
30 Cheese fl avored corn-based snack;
TRADEMARK APPLICATIONS
1405
Issue 42 | Monday October 16,  2023
SAINT LUCIA GOVERNMENT GAZETTE
File No (210): TM/2023/ 000226
Mark Name: Zoomers
Applicant (730): Associated Brands Industries Limited 
of No. 2 Bhagowite Traces, San Juan, Trinidad and 
Tobago
Filing date (220): 03/08/2023
Agent (740): Tyrone D. Chong of 27 Micoud Street, 
Castries, St. Lucia
Class (511): 30 Cheese fl avored corn snack;
File No (210): TM/2023/ 000092
Mark Name: ORIENT O.E. EXPRESS
Applicant (730): ORIENT EXPRESS of 82 rue Henri 
Farman, 92130 Issy-Lex-Moulineaux, France
Filing date (220): 04/04/2023
Priorities (330): March 9, 2023  EU  018846604
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 7, Mongiraud 
Street, Castries, St. Lucia
Class (511): 12 Vehicles; apparatus for land, sea and air 
locomotion; motor vehicles; cars; bus; trucks; railway 
vehicles; rail vehicles; trains; locomotives; engines; 
wagons; railway car compartments; sleeping cars; 
dining cars; bar cars; lounge cars; water and sea 
vehicles; boats; boat; cruising sailboats; ships; ocean 
liners; cruise liners; canoes; yachts; freighters; ferries; 
barges; houseboats; ferries; underwater vehicles; 
aerial vehicles; airplanes; helicopters; aircraft; dirigible 
balloons; seaplanes; hot air balloons; handling trolleys; 
trolleys for luggage and parcels; bicycles; scooters; 
motorcycles.
39 Cruise services; arranging, arranging and booking 
of cruises; transportation services on a cruise 
ship; provision of cruise ship for travel; issuance of 
travel tickets; issuance of transport tickets; travel 
reservation 
services; 
reservation 
of 
transport 
tickets; reservation and rental, including online, of 
seats for travel and transport, in particular in trains, 
boats, airplanes; transport; freight (transportation of 
goods); passenger transport; transport of luggage; 
transport of packages; rail transport; motor transport 
of passengers; air transport of passengers; maritime 
transport of passengers; transportation of passengers 
by car, bus boat, sailboat, ship, liner, dinghy, yacht, 
ferry, 
freighter, 
barge, 
barge, 
ferry, 
airplane, 
helicopter; intermodal transport of passengers by 
land, rail, sea, air; limousine services; collection, 
removal, storage, routing and delivery of goods, 
luggage and parcels; loading and unloading; rental of 
parking places and areas, of garages; loan and rental 
of vehicles, railway cars, wagons, trucks, vans, cars, 
motorcycles, bicycles; freight forwarding services; 
transit services; packaging, wrapping and packaging of 
goods; products, parcels; garage (parking) of vehicles; 
travel agency services; arranging of transport and 
travel, including by train, boat, plane; organization 
of excursions; organization of tours and tourist visits; 
accompaniment of travelers; chauffeur services; 
transportation by taxi; information, including online, 
relating to transport and travel, in particular by train, 
boat, plane; information, including online, concerning 
transport fares and timetables, in particular trains, 
buses, planes, boats.
43 Providing of food and drink (food, meals, snacks, 
appetizers, dishes or meals), for eat-in or take-away 
consumption, including on board trains, buses, boats, 
planes; services of bars and snack bars, fi xed or 
mobile, including on board trains, buses, boats, planes; 
snack bar services; self-service restaurant services; 
catering services; organization of catering services for 
banquets and receptions; temporary accommodation; 
hotel services; hotel services provided on board 
trains; hotel services provided on board boats, 
ships, sailboats; hotel services rendered on board air 
vehicles; reservation of temporary accommodation; 
hotel reservations; reservation of boarding houses; 
reservation of restaurant tables; information relating 
to temporary accommodation and catering; none of 
the aforementioned services being intended for use in 
connection with discos and/or disco clubs.
TUDOR T-FIT
File No (210): TM/2023/ 000174
Mark Name: TUDOR T-FIT
Applicant (730): Montres Tudor SA of Rue François-
Dussaud 3, Geneva, Switzerland
Filing date (220): 28/06/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
SAINT LUCIA GOVERNMENT GAZETTE
1406
Issue 42 | Monday October 16,  2023
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), boxes and presentation 
cases for clock and watchmaking and jewellery, watch 
movements and parts thereof; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings.
TUDORWATCH
File No (210): TM/2023/ 000176
Mark Name: TUDORWATCH
Applicant (730): Montres Tudor SA of Rue François-
Dussaud 3, Geneva, Switzerland
Filing date (220): 28/06/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), boxes and presentation 
cases for clock and watchmaking and jewellery, watch 
movements and parts thereof; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings.
PERPETUAL 1908
File No (210): TM/2023/ 000179
Mark Name: PERPETUAL 1908
Applicant (730): ROLEX SA OF Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 29/06/2023
Priorities (330): March 13, 2023  Switzerland 
03240/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), boxes and presentation 
cases for clock and watchmaking and jewellery, watch 
movements and parts thereof; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery).
Unilumin
File No (210): TM/2023/ 000186
Mark Name: Unilumin
Applicant (730): Unilumin Group Co., Ltd. of Building 
A, 112 Yongfu Road, Qiaotou Community, Fuyong 
Town, Baoan District, Shenzhen, China
Filing date (220): 07/07/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 09 Data processing apparatus; Downloadable 
computer software for controlling the operation 
of audio and video devices; Computer software 
platforms, downloadable, for operating internet-
enabled and connected lighting apparatus and home 
security alarms; Light emitting diode (LED) displays; 
Video monitors; Luminous pointers; digital signs; 
Neon signs; virtual reality headsets; Combination 
video players and recorders; Transparency projection 
apparatus; Teaching robots; Video screens; LED 
drivers; Flat panel display screens; LCD large-screen 
displays; Playing devices for sound and image carriers; 
Electronic LCD advertisement display unit with multi-
networking (TCP/IP) capabilities; Touch screens; 
Organic light-emitting diodes (OLED).
11 Lamps; Germicidal lamps for purifying air; Light-
emitting diode lighting apparatus; Air sterilizers; 
Disinfectant apparatus; LED lamps; LED landscape 
lights; Arc lamps [lighting fi xtures]; LED lights 
for automobiles; Stage lighting apparatus; Lights 
for vehicles; Lighting apparatus, namely, lighting 
installations; Luminous tubes for lighting; Luminous 
house numbers; LED safety lamps; Light-emitting 
diode lighting installations; Lighting installations; 
Wet-cleaning drying machines; Air heating apparatus; 
Heating installations.
MICROSTELLA
File No (210): TM/2023/ 000209
Mark Name: MICROSTELLA
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
1407
Issue 42 | Monday October 16,  2023
SAINT LUCIA GOVERNMENT GAZETTE
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 06 Metal nuts.
08 Hand tools and instruments, hand-operated; spanner.
14 Components for clock and watchmaking articles and 
accessories for clock and watchmaking articles not 
included in other classes.
SYLOXI
File No (210): TM/2023/ 000210
Mark Name: SYLOXI
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), watch movements and 
parts thereof, boxes and presentation cases for clock 
and watchmaking and jewellery,; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings.
PARACHROM
File No (210): TM/2023/ 000211
Mark Name: PARACHROM
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), watch movements and 
parts thereof, boxes and presentation cases for clock 
and watchmaking and jewellery,; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings.
PARAFLEX
File No (210): TM/2023/ 000212
Mark Name: PARAFLEX
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), watch movements and 
parts thereof, boxes and presentation cases for clock 
and watchmaking and jewellery,; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings.
TRINERGY
File No (210): TM/2023/ 000213
Mark Name: TRINERGY
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), watch movements and 
parts thereof, boxes and presentation cases for clock 
and watchmaking and jewellery,; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings. 
SAINT LUCIA GOVERNMENT GAZETTE
1408
Issue 42 | Monday October 16,  2023
OYSTERCLASP
File No (210): TM/2023/ 000214
Mark Name: OYSTERCLASP
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), watch movements and 
parts thereof, boxes and presentation cases for clock 
and watchmaking and jewellery,; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings.
EASYLINK
File No (210): TM/2023/ 000215
Mark Name: EASYLINK
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), watch movements and 
parts thereof, boxes and presentation cases for clock 
and watchmaking and jewellery,; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings.
DYNACHROM
File No (210): TM/2023/ 000216
Mark Name: DYNACHROM
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking), watch movements and 
parts thereof, boxes and presentation cases for clock 
and watchmaking and jewellery,; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery); cuffl inks; key rings.
OYSTERMATIC
File No (210): TM/2023/ 000219
Mark Name: OYSTERMATIC
Applicant (730): ROLEX SA of Rue François-Dussaud 
3-5-7, Geneva, Switzerland
Filing date (220): 13/07/2023
Priorities (330): March 21, 2023  Switzerland  
03749/2023
Agent (740): Michael B. G. Gordon of GORDON, 
GORDON & CO. of P.O. Box 161, 10, Manoel Street, 
Castries, St. Lucia
Class (511): 14 Clock and watchmaking articles, 
namely watches, wristwatches, components for 
clock and watchmaking articles and accessories 
for clock and watchmaking articles not included 
in other classes, clocks and other chronometric 
instruments, chronometers, chronographs (clock and 
watchmaking), watch bracelets, watch straps, dials 
(clock and watchmaking),  boxes and presentation 
cases for clock and watchmaking and jewellery, watch 
movements and parts thereof; jewellery; precious 
stones and semi-precious stones; precious metals and 
their alloys; pins (jewellery).
'''
list1=[]
pattern = r'Priorities\s*\(330\):\s*(\w+\s*\d+,\s*\d{4})\s*(\D*)(.*?\d*\n\d*\D\d*)'  # Adjusted pattern
matches = re.finditer(pattern, text)

for match in matches:
    value = match.group(3).replace('A','')
    print(value)

# pattern_1 = re.compile(r"\d+", re.MULTILINE)
# matches_1 = pattern_1.findall(matches[0])
# for match in matches_1:
#     print(match)
