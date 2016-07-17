a = 5.4;
b = 3;
c = 2.3;
a = "asd";

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

g[0] = 2;

b = g[0]++;
