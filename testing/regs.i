usuario = {nombre:"Al", edad:50};
print(capitalizar(usuario.nombre));
nacimiento = 2016;
nacimiento -= usuario.edad;
usuarios = [{nombre:"Mr.X", edad:10}, usuario];

suma = 0;
for (i = 0; i < length(usuarios); i++) {
	print(usuarios[i].nombre);
	suma += usuarios[i].edad;
	suma = usuarios[0].edad;
}

j = [[1],[2],[1, 2, 3]];
k = {list:["A", "B", "c"], doublelist:j};
a = 0;
#Ojo, esta linea no anda
a = j[1][2];
a += k.doublelist[0][1];
