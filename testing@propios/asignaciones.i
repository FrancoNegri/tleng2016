a = 5.4;
b = 3;
c = 2.3;

a += 0;
a += b;
b*= 0;

c /= 2;
z = b;
z = b++;
z = ++b;


d = "ab";
e = "cd";
d += e;
e = d;
e = d + e;

#Casos como if (cond) a = 2 ; else a = "asd"; no esan soportados

g = [1,2,3];
f = [4,5,6];

b = g[0]++;
b = --g[0];
z = g[0] - g[2];

g[1] = g[0] + f[1];

h = ["a","b","c"];
j = ["d","e","f"];

h[1] = j[0] + h[1];
d = j[0] + h[1]; 
d += "asd";