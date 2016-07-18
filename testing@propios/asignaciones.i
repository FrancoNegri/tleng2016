a = 5.4;
b = 3;
c = 2.3;
a = "asd";
a = 2;

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

g = [1,2,3];
f = [4,5,6];

g[0] = 2;
b = g[0]++;

#Las variables pueden cambiar "dinamicante" su tipo
a = "sd";
#Los vectores no
g[0] += 1;
g[0] *= 2;

t = ["a","b","c"];
t[0] += t[0] + t[1];

