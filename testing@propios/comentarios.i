#Comentario###d#as##d##;#a=2;#asd

a = 2;#comment

#ESte caso no anda, tira error con algo del output
if(true)
	#com1		
	a = 2;
else
	#com2
	a = 2;

#Este caso ni se parseaba!! Ahora si, pero tira error con algo del output, como el otro
if(true){
	a++;	
}
else
	#comentario
	a++;



#otro comentario

while(true)#asd a++;

while(false){
#comentarioLoco
#otro
;
}
do{
	#coment
	a++;

}while(true);#asds

#Este tampoco se parseaba, ahora si. El problema es con el out, como los otros
do
a++;
#comentario
while(true)




