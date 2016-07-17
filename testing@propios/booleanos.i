g = [true, true OR NOT false];
a = NOT g[1];
#Esto deberia andar
a = (NOT g[1]);
a = (NOT g[1]) AND false;
c = a == false;
c = (a == false) AND g[0];
c = (a == false) AND g[0] OR true; 
a = (false? true : g[0]);
z = 20;
d = (z > 5 ? (a == 3 ? 5 :  5 *4) : (g[0] != false ? 3 : 200));
A = NOT NOT NOT false;

