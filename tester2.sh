rm testing@propios/*.out 2> /dev/null
rm errores.txt 2> /dev/null
echo "Escribiendo errores en errores.txt"
for f in testing@propios/*.i
do
	python parser.py $f $f.out 2>> errores.txt > /dev/null
	if [ $? -eq 0 ]
	then
		echo "Pasa: " $f
	else
  		echo "No Pasa: " $f
	fi
	#Esto es para ver cuando escribamos la salida:
	#diff $f $f.out
done