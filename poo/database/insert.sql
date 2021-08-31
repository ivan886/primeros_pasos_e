INSERT INTO universes(
	 name, description, foundation)
	VALUES ('Marvel' ,
			'The Marvel Cinematic Universe is an American media franchise and shared universe centered on a series of superhero films produced by Marvel Studios. The films are based on characters that appear in American comic books published by Marvel Comics.',
		     '1939-08-20');

INSERT INTO universes(
	 name, description, foundation)
	VALUES ('DC Universe' ,
			'The DC Universe is the fictional shared universe where most stories in American comic book titles published by DC Comics take place. DC superheroes such as Superman, Batman, Wonder Woman, Martian Manhunter, The Flash, Green Lantern and Aquaman are from this universe, as well as teams such as the Justice League.',
		     '1940-08-20');


INSERT INTO public.city(
	 name, lat, lon)
	VALUES ( 'New York',  40.76118057046385, -74.00022386064575) ;

	INSERT INTO public.city(
	 name, lat, lon)
	VALUES ( 'Tunja Boyacá ',  5.549765362085938,  -73.3517548295104) ;


INSERT INTO public.characters(
	 cit_id, uni_id, name, path, description)
	VALUES ( 1, 1, '', 'Batman', 'Un año después de la aparición de Superman apareció su contrapartida oscura, Batman, un caballero de la noche, un caballero oscuro. Bruce Wayne tuvo que presenciar como sus padres eran asesinados por un ladrón de poca monta en las peligrosas calles de Gotham. Desde ese momento decidió combatir el crimen. Adoptó el disfraz de murciélago porque según él, los criminales son supersticiosos y la figura de un animal oscuro les infundiría de terror. Tiene multitud de aparatos y vehículos de alta tecnología que le ayudan en su misión de limpiar Gotham, además de haber tenido varios ayudantes: Robins y Batgirls. Su fiel mayordomo, Alfred Pennyworth, es su médico, amigo y asistente. ');



