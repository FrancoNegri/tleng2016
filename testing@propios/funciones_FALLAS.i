vec1 = ["asd","adada"];
vec = [1,2,3];
#MultiEscalar:
#Lineas que deberian fallar:
multiplicacionEscalar(vec1,2);
#multiplicacionEscalar(["asd"],2);
#multiplicacionEscalar([1,2],"sad");
#multiplicacionEscalar([1,2],2,3);
#multiplicacionEscalar();

#vec2 = multiplicacionEscalar(vec,1);
#vec2[0] = "asd";

#Capitalizar:
#a  = 2 + capitalizar("asd");
#capitalizar([1]);
#capitalizar();
#capitalizar(capitalizar("asd") + 2);


#Colineales:
#a = colineales(multiplicacionEscalar([1,2],2),2);
#a = colineales(1,[1,2]);
#colineales(vec1,vec1);

#Length:
#vec1[1] = length("asd");
#length(2);
#length();
