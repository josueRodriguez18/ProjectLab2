#include<cmath>
class Object{
    public:
        double pos[2], orientation, toBall, g_pos[];

        void point();
};

class Field {
    public:
        double corners[4];
        double center[2] = { abs(corners[0] - corners[1])/2, abs(corners[2] - corners[3])/2 };
        Object Blue[3], Red[3], Ball;

        double* grid(Object a);
        bool isOriented(Object a, Object Ball); 
};

double* Field::grid(Object a){
    double pos[2];
    pos[0] = a.pos[0] - center[0];
    pos[1] = a.pos[1] - center[1];

    return pos;    
}

bool Field::isOriented(Object a, Object Ball){
    double orient, x_diff = Ball.g_pos[0] - a.g_pos[0], y_diff = Ball.g_pos[1] - a.g_pos[1];
    orient = tan(y_diff/x_diff);

}