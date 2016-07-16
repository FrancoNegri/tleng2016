a = 5.4;
b = 3;
c = 2.3;

a += 0;
a += b;
b = a;
b*= 0;
b /= c;
c /= 2;
c = b++;
c = ++b;

#El parser no chequea esto:
#a = 2;
#a = 4;
#Estos casitos creo que se podrian chequear...
#if (algo > 4) var = 5 else var = "asd " tiene sentido dejarlo para la compilacion


d = "ab";
e = "cd";
d += e;
e = d;
e = d + e;

g = [1,2,3];
f = [4,5,6];

a = g[0]++;
a = --g[0];
b = g[0] - g[2];
g[1] = g[0] + f[1];

h = ["a","b","c"];
j = ["d","e","f"];

h[1] = j[0] + h[1];
a = j[0] + h[1]; 
h[1] = 5;



