create table etudiant (
	idetudiant int(4) not null auto_increment, 
	nom varchar (50), 
	prenom varchar (50), 
	age int(3), 
	montant float, 
	dateinscription date, 
	primary key (idetudiant) 
	);
	
	insert into etudiant values (null, "dupond", "olivier", 22, 4000, "2018-01-19") ;