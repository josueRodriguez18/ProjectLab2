#include<cmath>
class Object{
    public:
        //original coordinates, original orientation, distance to ball, grid position
        double pos[2], orientation, distanceToBall, gridPos[2];
        //unsure of how to make orientation relative

        void point();
};

class Field {
    public:
        //original corners
        double corners[4];
        //x,y coordinates for center
        double center[2] = { abs(corners[0] - corners[1])/2, abs(corners[2] - corners[3])/2 };
        //blue & red robots and ball
        Object Blue[3], Red[3], Ball;

        //finds grid position of object returns double array pointer
        double* grid(Object a);
        //checks if object is pointing at ball
        bool isOriented(Object a, Object Ball); 
};


double* Field::grid(Object a){
    //grid position array
    double pos[2];
    //position relative to grid
    pos[0] = a.pos[0] - center[0];
    pos[1] = a.pos[1] - center[1];
    //return array
    return pos;    
}

bool Field::isOriented(Object a, Object Ball){
    
    double orient, x_diff = Ball.gridPos[0] - a.gridPos[0], y_diff = Ball.gridPos[1] - a.gridPos[1];
    orient = tan(y_diff/x_diff);
    if(orient = Ball.orientation){
        return 1;
    }
    else{
        return 0;
    }

}