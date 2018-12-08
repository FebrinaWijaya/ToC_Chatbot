data = {
	'text' : '''Hi! We provide some recommendations for your vacation in Indonesia. Let me know what is the purpose of your trip.
You may just type the number.
1. Adventure (Hiking, Snorkeling)
2. Historical Buildings
3. Naturals (Beach, Mountain Views)
4. Local Food
			''',
	# 'buttons' : [
 #          	{
 #          "type": "postback",
 #          "title": "Adventure (Hiking, Snorkeling)",
 #          "payload": "adventure"
 #        	},
 #        	{
 #          "type": "postback",
 #          "title": "Historical Builings",
 #          "payload": "historical buildings"
 #        	},
 #        	{
 #          "type": "postback",
 #          "title": "Naturals",
 #          "payload": "naturals"
 #        	},
 #        	{
 #          "type": "postback",
 #          "title": "Local Food",
 #          "payload": "local food"
 #        	}
 #        ],
	'Adventure':{
		'text_to_send' : '''
			Here are some places that we recommend for adventure.
			''',
		'text_button' : '''
			Click to see details about it.
			''',
		'buttons' : [
              	{
              "type": "postback",
              "title": "Raja Ampat Islands, West Papua",
              "payload": "Raja Ampat Islands, West Papua"
            	},
            	{
              "type": "postback",
              "title": "Gili Islands, Lombok",
              "payload": "Gili Islands, Lombok"
            	},
            	{
              "type": "postback",
              "title": "Mount Bromo, East Java",
              "payload": "Mount Bromo, East Java"
              	}
            	# ,
            	# {
             #  "type": "postback",
             #  "title": "Mount Rinjani, East Java",
             #  "payload": "Mount Rinjani, East Java"
            	# }
            ],
		'Raja Ampat Islands, West Papua' : 
		{
			'text' : '''Raja Ampat Islands, West Papua

Raja Ampat, meaning Four Kings, is an archipelago comprising islands Waigeo, Misool, Salawati, and Batanta, besides 1500 minor ones. The awe-inspiring backdrop of steep, forested islands, sizzling beaches, and marshy lagoons, small atolls looking like mushrooms and shining turquoise water makes the place a perfect delight for travelers. One of the famous Indonesia tourist spots is rich in marine flora and fauna diversity including rare species of corals.

Tips: There are no ATMs on this island. Make sure you have all the cash you need to survive on the island.

Things to do: Snorkelling, underwater diving, kayaking and relishing nature.
					''',
			'image' : './img/raja_ampat.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
              	{
              "type": "postback",
              "title": "See next recommended place",
              "payload": "See next recommended place"
            	},
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},

		'Gili Islands, Lombok' : 
		{
			'text' : '''Gili Islands, Lombok

Overwater villas are so romantic, that there is no way to forget them while making a list of most beautiful places in Indonesia. Fringed by white sand beaches and blue water, the complex of three small and isolated islands namely Gili Trawangan, Gili Meno and Gili Air bears unique scenic appeal.

Tips: The best time to visit Gili Islands is between June to September as thhe crystal clear water poses perfect conditions for water activities.

Things to do: Besides adventure sports like snorkeling, surfing and diving, go island hopping, fishing and touring in glass-bottom boats. Else, just chill out in a beachside cafe or shack.
					''',
			'image' : './img/gili_island.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
              	{
              "type": "postback",
              "title": "See next recommended place",
              "payload": "See next recommended place"
            	},
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},
		'Mount Bromo, East Java' : 
		{
			'text' : '''Mount Bromo, East Java

Mount Bromo or better known as Gunung Bromo is a volcano in the active state. The top of the Bromo forms a crater which emits white smoke at regular intervals. A part of the Bromo Tengger Semeru National Park, this volcano is fringed by the sea of volcanic sand. It is one of the most visited tourist places in Indonesia.

Tips: If you are opting for a private car to reach here, make sure you make arrangement well in advance.

Things to do: Hiking and trekking
					''',
			'image' : './img/mount_bromo.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
             #  	{
             #  "type": "postback",
             #  "title": "See next recommended place",
             #  "payload": "See next recommended place"
            	# },
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},
		'Mount Rinjani, East Java' : 
		{
			'text' : '''Mount Rinjani, East Java

Locally known as Gunung Rinjani, this is an active volcano on Mount Lombok. It is the second highest volcano of Indonesia after Mount Kerinci in Sumatra. The hilly landscape is dominated by the Crater Lake called Segara Anak, which has a natural hot spring in it. It is one of the best places to visit in Indonesia.

Tips: The hiking to this mountain is not for casual travelers and novice because of its treacherous path.

Things to do: Besides enjoying the serene yet daring beauty of a volcano, Mount Rinjani is a good place to go hiking. Climbing alone is not advisable, so prefer going in a group.
					''',
			'image' : '',
			'buttons' : [
              	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		}

	},

	'Historical Buildings':{
		'text_to_send' : '''
			Here are some places that we recommend for historical buildings.
			''',
		'text_button' : '''
			Click to see details about it.
			''',
		'buttons' : [
              	{
              "type": "postback",
              "title": "Borobudur Temple, Magelang",
              "payload": "Borobudur Temple, Magelang"
            	},
            	{
              "type": "postback",
              "title": "Prambanan Temple, Yogyakarta",
              "payload": "Prambanan Temple, Yogyakarta"
            	},
            	{
              "type": "postback",
              "title": "Kota Tua (Old Town), Jakarta",
              "payload": "Kota Tua (Old Town), Jakarta"
            	}
            	# ,
            	# {
             #  "type": "postback",
             #  "title": "Monument of People, Bandung",
             #  "payload": "Monument of People, Bandung"
            	# }
            ],
		'Borobudur Temple, Magelang' : 
		{
			'text' : '''Borobudur Temple, Magelang

Borobudur is a Buddhist temple located in Magelang, Central Java. The location of the temple is approximately 86 km west of Surakarta, 100 km southwest of Semarang and 40 km northwest of Yogyakarta. This stupa-shaped temple was founded by Mahayana Buddhists around the year 800 AD during the reign of Shyilendra. Borobudur is also the largest Buddhist temple and Buddhist monument in the world. 

The unique thing of Borobudur temple is the stone used as the main building construction material made of volcanic ash of Mount Merapi which is also frozen. These blocks are then arranged to form more than 500 stupas without the use of cement at all.
					''',
			'image' : './img/borobudur.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
              	{
              "type": "postback",
              "title": "See next recommended place",
              "payload": "See next recommended place"
            	},
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},

		'Prambanan Temple, Yogyakarta' : 
		{
			'text' : '''Prambanan Temple, Yogyakarta

Loro Jonggrang Temple or Prambanan Temple is the largest Hindu temple complex in Indonesia built in the 9th century AD. This temple is dedicated to Trimurti, the three main Hindu gods namely Vishnu, Shiva and Brahma. According to the inscription of Siwagrha the original name of the temple complex is Siwagrha (Sanskrit meaning “Shiva house”), and indeed in the garbagriha (main room) this temple resides in the statue of the three-meter-long Shiva Mahadewa which shows that in this temple Shiva god takes precedence.

Also, Prambanan is the largest and most magnificent Hindu temple ever built in ancient Java, the construction of the Hindu temple of the kingdom was preceded by Rakai Pikatan as a rival of Buddhist temple Borobudur and also Sewu temple located not far from Prambanan.
					''',
			'image' : './img/prambanan.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
              	{
              "type": "postback",
              "title": "See next recommended place",
              "payload": "See next recommended place"
            	},
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},
		'Kota Tua (Old Town), Jakarta' : 
		{
			'text' : '''Kota Tua (Old Town), Jakarta

Holiday to Jakarta, it’s incomplete if you have not set foot to the Old Town area located in West and North Jakarta. The reason, this classic area store many stories of the past in every corner.

For you lovers of mobile photography, here you will find various interesting spots to be tested. Starting from the classic Dutch heritage buildings, historic collections, to portraits of diversity of Indonesian who walking in this area.
					''',
			'image' : './img/old_town.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
             #  	{
             #  "type": "postback",
             #  "title": "See next recommended place",
             #  "payload": "See next recommended place"
            	# },
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},
		'Monument of People, Bandung' : 
		{
			'text' : '''Monument of People, Bandung

Next, is going to Flower City, Bandung. One of the historic places here that is photogenic for your Instagram page is the People’s Struggle Monument of West Java or also known as Monju (Monument Perjuangan). Located right on the north side of Gedung Sate Bandung, this monument has a magnificent and modern architecture.

During the day, the dominance of white color in harmony with the blue of the sky makes your photos so beautiful. While at night, the light-colored firing lights highlight this monument to make your photos look more alive and different.
					''',
			'image' : '',
			'buttons' : [
              	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		}

	},
	'Naturals':{
		'text_to_send' : '''
			Here are some places that we recommend for naturals.
			''',
		'text_button' : '''
			Click to see details about it.
			''',
		'buttons' : [
              	{
              "type": "postback",
              "title": "Bali, the Island of Gods",
              "payload": "Bali, the Island of Gods"
            	},
            	{
              "type": "postback",
              "title": "Lake Toba, North Sumatra",
              "payload": "Lake Toba, North Sumatra"
            	},
            	{
              "type": "postback",
              "title": "Dieng Plateau",
              "payload": "Dieng Plateau"
            	}
            	# ,
            	# {
             #  "type": "postback",
             #  "title": "Komodo National Park",
             #  "payload": "Komodo National Park"
            	# }
            ],
		'Bali, the Island of Gods' : 
		{
			'text' : '''Bali, the Island of Gods

Bali is perhaps the most popular of the over 17,000 islands in Indonesia, home to about 4 million people. The climate is warm all year round, although in general the best time to visit Bali is from mid-May to mid October, as in the rest of the year rain and humidity are more frequent. In Bali English is spoken everywhere, even if the official languages ​​are Indonesian and Balinese, with various local dialects spoken all around the island.

Bali, also known as the "island of the gods", is associated with the idea of ​​tropical paradise and reality does not differ much from imagination. The island in fact offers lush tropical nature, postcard beaches and a culture characterized by a deep spirituality. In addition, its transparent waters and variously populated sea bottoms are excellent for those who love snorkeling and diving. The 80% of tourism in Indonesia is poured on Bali.
				''',
			'image' : './img/bali.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
              	{
              "type": "postback",
              "title": "See next recommended place",
              "payload": "See next recommended place"
            	},
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},

		'Lake Toba, North Sumatra' : 
		{
			'text' : '''Lake Toba, North Sumatra

Toba is not only Indonesia’s biggest lake, it is also one of its most beautiful; it is stunning from every angle. Almost twice the size of Singapore, there are many viewpoints to enjoy the sight of this volcanic lake, surrounded by hills and lush greenery. While in the nearby villages, tourists can also explore the fascinating Batak culture, with its captivating traditions and cultural objects. Tourists can also visit Samosir, the small charming island in the middle of Lake Toba.
					''',
			'image' : './img/lake_toba.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
              	{
              "type": "postback",
              "title": "See next recommended place",
              "payload": "See next recommended place"
            	},
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},
		'Dieng Plateau' : 
		{
			'text' : '''Dieng Plateau

Tectonically formed after an eruption, this plateau is a caldera situated almost 2000 metres above sea level. This marshy plateau, known as Dieng which means abode of God, is one of the best places to visit in Indonesia.

Tips: The guesthouses in this part of Java are sparse and may only have least of basic amenities. Also, it gets really cold in the highlands. Make sure you pack proper clothing.

Things to do: Trek to the multi-coloured Telaga Warna lake and explore the Arjuna temple.
					''',
			'image' : './img/dieng_plateau.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
             #  	{
             #  "type": "postback",
             #  "title": "See next recommended place",
             #  "payload": "See next recommended place"
            	# },
            	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},
		'Komodo National Park' : 
		{
			'text' : '''Komodo National Park
				
A mighty and otherworldly lizard, the Komodo is arguably one of the most fascinating creatures on earth—one you can only encounter in the wild at Indonesia’s Komodo National Park. Captivating as it is, the Komodo is hardly the only interesting thing in this string of exotic islands that constitute the Komodo National Park. The three islands—Komodo, Padar, and Rinca—have glorious hills and a beach view, along with a breathtaking coastline, lush tropical hills, and thriving underwater wildlife. The Komodo Island even has the famed pink sand beach, while Padar Island has an iconic hill with a view of three magnificent bays.
					''',
			'image' : '',
			'buttons' : [
              	{
              "type": "postback",
              "title": "Select another place",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		}

	},
	'Local Food':{
		'text_to_send' : '''
			Here are local food that we recommend.
			''',
		'text_button' : '''
			Click to see details about it.
			''',
		'buttons' : [
              	{
              "type": "postback",
              "title": "Satay",
              "payload": "Satay"
            	},
            	{
              "type": "postback",
              "title": "Rendang",
              "payload": "Rendang"
            	},
            	{
              "type": "postback",
              "title": "Fried Rice",
              "payload": "Fried Rice"
            	}
            	# ,
            	# {
             #  "type": "postback",
             #  "title": "Nasi Uduk",
             #  "payload": "Nasi Uduk"
            	# }
            ],
		'Satay' : 
		{
			'text' : '''Satay

Satay is meat skewers that are cooked over coals. These juicy skewers is usually served with rice cakes (ketupat) with peanut sauce poured all over the satay. It is a national dish conceived by street vendors and has been one of most celebrated food in Indonesia. It is practically everywhere and highly addictive.
				''',
			'image' : './img/satay.jpeg',
			'image_type' : 'jpeg',
			'buttons' : [
              	{
              "type": "postback",
              "title": "See next recommended food",
              "payload": "See next recommended place"
            	},
            	{
              "type": "postback",
              "title": "Select another food",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},

		'Rendang' : 
		{
			'text' : '''Beef Rendang

This dish originated from Padang, Sumatra. Padang food is famous for its spicyness and richness in flavor. You definitely have to try Beef Rendang. It is somehow similar to Beef Curry but without the broth. We get to appreciate this dish because it take forever to cook to get that tenderness out of the beef. Try this Padang goodness and let the world know how tasty it is!
					''',
			'image' : './img/rendang.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
              	{
              "type": "postback",
              "title": "See next recommended food",
              "payload": "See next recommended place"
            	},
            	{
              "type": "postback",
              "title": "Select another food",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},
		'Fried Rice' : 
		{
			'text' : '''Fried Rice

I think this dish doesn’t need any further introduction. Indonesian Fried Rice and its reputation has taken the world by storm. Don’t you agree? Literally everyone has tried Fried Rice at some point in their life and it is the most versatile dish out there. You can mixed it with veggies, chicken, beef, seafood, whatever it is that you can think of. What makes Indonesian Fried Rice different is the use of sweet, thick soy sauce called keycap and garnished with acar, pickled cucumber and carrots. Nasi Goreng (Fried Rice) is considered Indonesia’s national dish.
					''',
			'image' : './img/fried_rice.jpg',
			'image_type' : 'jpeg',
			'buttons' : [
             #  	{
             #  "type": "postback",
             #  "title": "See next recommended food",
             #  "payload": "See next recommended place"
            	# },
            	{
              "type": "postback",
              "title": "Select another food",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		},
		'Nasi Uduk' : 
		{
			'text' : '''Nasi Uduk

This aromatic dish is also one of Indonesia’s national dish. The meal revolves around rice cooked in coconut milk. It is quite similar to Nasi Lemak from our neighbouring country, Malaysia. The difference is that nasi uduk is usually served with fried chicken, tempe (soybean cake), shredded omelette, fried onion, anchovies and topped with sambal and emping (melinjo nut crackers). You definitely cannot leave out sambal for Nasi Uduk. This dish is popular among lunchtime crowds.
				''',
			'image' : '',
			'buttons' : [
              	{
              "type": "postback",
              "title": "Select another food",
              "payload": "Select another place"
            	},
            	{
              "type": "postback",
              "title": "Change my travel purpose",
              "payload": "Change my travel purpose"
            	}
            ]

		}

	}
}