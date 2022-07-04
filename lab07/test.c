#include <stdio.h>
int main(){
int addOK(int x, int y){
    int suma = x + y;
    int negativo_over = (x < 0 && y < 0 && suma >= 0);
    int positivo_over = (x >= 0 && y >= 0 && suma <= 0);
    return !negativo_over && !positivo_over;
    
    }
}