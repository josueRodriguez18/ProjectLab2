#include "ArduinoJson.h"
//get buffer size.

/* 

    4 arrays in document
    11 objects with 2 attributes
    2 objects with 3 attributes
    8 objects with 4 attributes
    7 objects with 6 attributes

*/

const size_t bufferSize = JSON_ARRAY_SIZE(4) + 11*JSON_OBJECT_SIZE(2) + 2*JSON_OBJECT_SIZE(3) + 8*JSON_OBJECT_SIZE(4) + 7*JSON_OBJECT_SIZE(6) + 1410;
DynamicJsonBuffer jsonBuffer(bufferSize);

const char* json = "{\"Ball\":{\"Object Center\":{\"X\":240.1168,\"Y\":149.2336},\"Bounding Box\":{\"X Left\":233,\"Y Top\":142,\"X Right\":248,\"Y Bottom\":157},\"Area\":137,\"Orientation\":153.0431,\"Aspect Ratio\":1,\"Nb Holes\":1},\"Corners\":[{\"X\":12.0495,\"Y\":210.9505},{\"X\":414.7983,\"Y\":197.7204},{\"X\":32.96965,\"Y\":39.06929},{\"X\":380.2392,\"Y\":22.04729}],\"Red Team Data\":{\"Circle\":{\"Object Center\":{\"X\":137.058,\"Y\":103.4375},\"Bounding Box\":{\"X Left\":126,\"Y Top\":93,\"X Right\":149,\"Y Bottom\":115},\"Area\":224,\"Orientation\":25.44606,\"Aspect Ratio\":1.045455,\"Nb Holes\":1},\"Square\":{\"Object Center\":{\"X\":87.07018,\"Y\":91.53947},\"Bounding Box\":{\"X Left\":76,\"Y Top\":81,\"X Right\":99,\"Y Bottom\":103},\"Area\":228,\"Orientation\":31.23487,\"Aspect Ratio\":1.045455,\"Nb Holes\":1},\"Triangle\":{\"Object Center\":{\"X\":133.7784,\"Y\":58.8125},\"Bounding Box\":{\"X Left\":126,\"Y Top\":51,\"X Right\":145,\"Y Bottom\":68},\"Area\":176,\"Orientation\":10.87619,\"Aspect Ratio\":1.117647,\"Nb Holes\":1}},\"Blue Team Data\":{\"Circle\":{\"Object Center\":{\"X\":355.0485,\"Y\":119.489},\"Bounding Box\":{\"X Left\":344,\"Y Top\":109,\"X Right\":367,\"Y Bottom\":131},\"Area\":227,\"Orientation\":149.8406,\"Aspect Ratio\":1.045455,\"Nb Holes\":1},\"Square\":{\"Object Center\":{\"X\":291.5776,\"Y\":95.96983},\"Bounding Box\":{\"X Left\":280,\"Y Top\":86,\"X Right\":304,\"Y Bottom\":107},\"Area\":232,\"Orientation\":166.9183,\"Aspect Ratio\":1.142857,\"Nb Holes\":1},\"Triangle\":{\"Object Center\":{\"X\":291.5459,\"Y\":54.35204},\"Bounding Box\":{\"X Left\":280,\"Y Top\":45,\"X Right\":301,\"Y Bottom\":64},\"Area\":196,\"Orientation\":175.8742,\"Aspect Ratio\":1.105263,\"Nb Holes\":1}}}";

JsonObject& root = jsonBuffer.parseObject(json);

JsonObject& Ball = root["Ball"];

float BallX = Ball["Object Center"]["X"]; // 240.1168
float BallY = Ball["Object Center"]["Y"]; // 149.2336

float BallO = Ball["Orientation"]; // 153.0431


JsonArray& Corners = root["Corners"];

float Corners0_X = Corners[0]["X"]; // 12.0495
float Corners0_Y = Corners[0]["Y"]; // 210.9505

float Corners1_X = Corners[1]["X"]; // 414.7983
float Corners1_Y = Corners[1]["Y"]; // 197.7204

float Corners2_X = Corners[2]["X"]; // 32.96965
float Corners2_Y = Corners[2]["Y"]; // 39.06929

float Corners3_X = Corners[3]["X"]; // 380.2392
float Corners3_Y = Corners[3]["Y"]; // 22.04729

JsonObject& Red_Team_Data = root["Red Team Data"];

JsonObject& Red_Team_Data_Circle = Red_Team_Data["Circle"];

float Red_Team_Data_Circle_Object_Center_X = Red_Team_Data_Circle["Object Center"]["X"]; // 137.058
float Red_Team_Data_Circle_Object_Center_Y = Red_Team_Data_Circle["Object Center"]["Y"]; // 103.4375


float Red_Team_Data_Circle_Orientation = Red_Team_Data_Circle["Orientation"]; // 25.44606

JsonObject& Red_Team_Data_Square = Red_Team_Data["Square"];

float Red_Team_Data_Square_Object_Center_X = Red_Team_Data_Square["Object Center"]["X"]; // 87.07018
float Red_Team_Data_Square_Object_Center_Y = Red_Team_Data_Square["Object Center"]["Y"]; // 91.53947

float Red_Team_Data_Square_Orientation = Red_Team_Data_Square["Orientation"]; // 31.23487

JsonObject& Red_Team_Data_Triangle = Red_Team_Data["Triangle"];

float Red_Team_Data_Triangle_Object_Center_X = Red_Team_Data_Triangle["Object Center"]["X"]; // 133.7784
float Red_Team_Data_Triangle_Object_Center_Y = Red_Team_Data_Triangle["Object Center"]["Y"]; // 58.8125


JsonObject& Blue_Team_Data = root["Blue Team Data"];

JsonObject& Blue_Team_Data_Circle = Blue_Team_Data["Circle"];

float Blue_Team_Data_Circle_Object_Center_X = Blue_Team_Data_Circle["Object Center"]["X"]; // 355.0485
float Blue_Team_Data_Circle_Object_Center_Y = Blue_Team_Data_Circle["Object Center"]["Y"]; // 119.489

JsonObject& Blue_Team_Data_Square = Blue_Team_Data["Square"];

float Blue_Team_Data_Square_Object_Center_X = Blue_Team_Data_Square["Object Center"]["X"]; // 291.5776
float Blue_Team_Data_Square_Object_Center_Y = Blue_Team_Data_Square["Object Center"]["Y"]; // 95.96983

JsonObject& Blue_Team_Data_Triangle = Blue_Team_Data["Triangle"];

float Blue_Team_Data_Triangle_Object_Center_X = Blue_Team_Data_Triangle["Object Center"]["X"]; // 291.5459
float Blue_Team_Data_Triangle_Object_Center_Y = Blue_Team_Data_Triangle["Object Center"]["Y"]; // 54.35204

int Blue_Team_Data_Triangle_Area = Blue_Team_Data_Triangle["Area"]; // 196
float Blue_Team_Data_Triangle_Orientation = Blue_Team_Data_Triangle["Orientation"]; // 175.8742