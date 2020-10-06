/*Problema d intercambio de monedas: Dada una cantidad solicitada, calcular el número de monedas (o billetes) a entregar. 
Nota: la cantidad puede variar, pero las denominaciones de las monedas (o billetes) siempre serán: 100, 50, 20, 10, 5, 2, 1*/
#include<iostream>
using namespace std;

int main()
{
    int num=0, l=0, bil;
    int monedas[] = {100,50,20,10,5,2,1};
    l = sizeof(monedas)/sizeof(monedas[0]);

    cout<<"Ingrese la cantidad de dinero: "; cin>>num;
    for(int i=0;i<l;i++)
    {
       bil = num/monedas[i];
       num = num%monedas[i];
       cout<<"La cantidad de billetes o monedas de "<<(monedas[i])<<" es: "<<bil<<endl;
    }
    return 0;
}