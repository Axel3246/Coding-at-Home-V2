//Identifica si un número entero es positivo, negativo o cero.

#include <iostream>
using namespace std;

int main(){
    
    int numero;

    if (numero > 0){
        cout << "El numero es positivo" << endl;
        return 0;
    }
    else if (numero < 0){
        cout << "El numero es negativo" << endl;
        return 0;
    }
    else{
        cout << "El numero es cero" << endl;
        return 0;
    }

}