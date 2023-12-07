
def create_users():
    from models.user import User
    users = []
    # Artist Instances
    a1 = User(
        full_name= "Leonardo da Vinci",
        username= "leo_da_vinci",
        email= "leo_da_vinci@example.com",
        bio= "Italian Renaissance polymath",
        location= "Vinci, Italy",
        profile_image= "leonardo.jpg"
    )
    a1.password= "password123"
    users.append(a1)
    a2 = User(
        full_name= "Vincent van Gogh",
        username= "vincent_van_gogh",
        email= "vincent_van_gogh@example.com",
        bio= "Post-Impressionist painter",
        location= "Zundert, Netherlands",
        profile_image= "van_gogh.jpg"
    )
    a2.password= "password456"
    users.append(a2)
    a3 = User(
        full_name= "Pablo Picasso",
        username= "pablo_picasso",
        email= "pablo_picasso@example.com",
        bio= "Cubist artist and sculptor",
        location= "Málaga, Spain",
        profile_image= "picasso.jpg"
    )
    a3.password= "password111"
    users.append(a3)
    a4 = User(
        full_name= "Claude Monet",
        username= "claude_monet",
        email= "claude_monet@example.com",
        bio= "Impressionist painter",
        location= "Paris, France",
        profile_image= "monet.jpg"
    )
    a4.password= "password121"
    users.append(a4)
    a5 = User(
        full_name= "Salvador Dalí",
        username= "salvador_dali",
        email= "salvador_dali@example.com",
        bio= "Surrealist artist",
        location= "Figueres, Spain",
        profile_image= "dali.jpg"
    )
    a5.password= "password131"
    users.append(a5)
    a6 = User(
        full_name= "Michelangelo Buonarroti",
        username= "michelangelo",
        email= "michelangelo@example.com",
        bio= "Renaissance sculptor and painter",
        location= "Caprese, Italy",
        profile_image= "michelangelo.jpg"
    )
    a6.password= "password141"
    users.append(a6)
    a7 = User(
        full_name= "Frida Kahlo",
        username= "frida_kahlo",
        email= "frida_kahlo@example.com",
        bio= "Mexican painter known for her self-portraits",
        location= "Coyoacán, Mexico",
        profile_image= "frida_kahlo.jpg"
    )
    a7.password= "password151"
    users.append(a7)
    a8 = User(
        full_name= "Andy Warhol",
        username= "andy_warhol",
        email= "andy_warhol@example.com",
        _password= "password161",
        bio= "Pop art pioneer",
        location= "Pittsburgh, USA",
        profile_image= "warhol.jpg"
    )
    a8.password= "password161"
    users.append(a8)
    a9 = User(
        full_name= "Raphael Sanzio",
        username= "raphael_sanzio",
        email= "raphael_sanzio@example.com",
        bio= "High Renaissance painter",
        location= "Urbino, Italy",
        profile_image= "raphael.jpg"
    )
    a9.password= "password171"
    users.append(a9)
    a10 = User(
        full_name= "Edvard Munch",
        username= "edvard_munch",
        email= "edvard_munch@example.com",
        bio= "Expressionist painter",
        location= "Oslo, Norway",
        profile_image= "munch.jpg"
    )
    a10.password= "password181"
    users.append(a10)
    a11 = User(
        full_name= "Rembrandt van Rijn",
        username= "rembrandt",
        email= "rembrandt@example.com",
        bio= "Dutch Golden Age painter",
        location= "Leiden, Netherlands",
        profile_image= "rembrandt.jpg"
    )
    a11.password= "password191"
    users.append(a11)
    a12 = User(
        full_name= "Jackson Pollock",
        username= "jackson_pollock",
        email= "jackson_pollock@example.com",
        bio= "Abstract expressionist painter",
        location= "Cody, USA",
        profile_image= "pollock.jpg"
    )
    a12.password= "password201"
    users.append(a12)
    
    return users

def create_artworks():
    from models.artwork import Artwork
    artworks = []
    a1 = Artwork(
        user_id=1,
        title = "Mona Lisa",
        description = "Portrait of Lisa Gherardini, wife of Francesco del Giocondo",
        image = "mona_lisa.jpg",
        price=1000.00,
        preview=True
    )
    a2 = Artwork(
        user_id=1,
        title = "The Last Supper",
        description = "Depiction of the last meal of Jesus with his disciples",
        image = "last_supper.jpg",
        price=500.00,
        preview=True
    )
    a3 = Artwork(
        user_id=1,
        title = "Vitruvian Man",
        description = "Study of the proportions of the human body according to Vitruvius",
        image = "vitruvian_man.jpg",
        price=225.00,
        preview=True
    )
    a4 = Artwork(
        user_id=1,
        title = "Annunciation",
        description = "Archangel Gabriel announcing to the Virgin Mary that she will conceive Jesus",
        image = "annunciation.jpg",
        price=100.00,
        preview=True
    )
    a5 = Artwork(
        user_id=1,
        title = "Lady with an Ermine",
        description = "Portrait of Cecilia Gallerani holding an ermine",
        image = "lady_with_an_ermine.jpg",
        price=199.99,
        preview=True
    )
    a6 = Artwork(
        user_id=2,
        title = "Starry Night",
        description = "A night sky filled with swirling clouds and bright stars over a tranquil village.",
        image = "starry_night.jpg",
        price = 500000.00,
        preview = True

    )
    a7 = Artwork(
        user_id=2,
        title = "Sunflowers",
        description = "A series of still life paintings depicting vibrant sunflowers in various stages of bloom.",
        image = "sunflowers.jpg",
        price = 350000.00,
        preview = False
    )
    a8 = Artwork(
        user_id=2,
        title = "The Bedroom",
        description = "A depiction of Van Gogh's bedroom in the Yellow House in Arles with bold colors and distinctive brushstrokes.",
        image = "the_bedroom.jpg",
        price = 700000.00,
        preview = True
    )
    a9 = Artwork(
        user_id=2,
        title = "Irises",
        description = "A masterpiece featuring vibrant irises set against a background of lush greenery.",
        image = "irises.jpg",
        price = 450000.00,
        preview = True
    )
    a10 = Artwork(
        user_id=2,
        title = "Café Terrace at Night",
        description = "A charming night scene of a cafe terrace illuminated by warm light under a starry sky.",
        image = "cafe_terrace.jpg",
        price = 600000.00,
        preview = False
    )
    artworks.extend([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
    a11 = Artwork(
        user_id=3,
        title = "Guernica",
        description = "A powerful anti-war mural depicting the horrors of the bombing of Guernica during the Spanish Civil War.",
        image = "guernica.jpg",
        price = 800000.00,
        preview = True
    )
    a12 = Artwork(
        user_id=3,
        title = "Les Demoiselles d'Avignon",
        description = "A groundbreaking work in modern art, portraying five nude women with influences from African art.",
        image = "demoiselles_davignon.jpg",
        price = 950000.00,
        preview = False
    )
    a13 = Artwork(
        user_id=3,
        title = "The Weeping Woman",
        description = "A powerful portrayal of grief and pain, featuring a woman with tears streaming down her face.",
        image = "weeping_woman.jpg",
        price = 700000.00,
        preview = True
    )
    a14 = Artwork(
        user_id=3,
        title = "Three Musicians",
        description = "A colorful and abstract composition depicting three musicians playing instruments.",
        image = "three_musicians.jpg",
        price = 600000.00,
        preview = False
    )
    a15 = Artwork(
        user_id=3,
        title = "The Old Guitarist",
        description = "A melancholic painting of an old blind guitarist, reflecting Picasso's Blue Period.",
        image = "old_guitarist.jpg",
        price = 500000.00,
        preview = True
    )
    a16 = Artwork(
        user_id=4,
        title = "Water Lilies",
        description = "A series of paintings depicting Monet's water garden at Giverny, featuring water lilies and reflections.",
        image = "water_lilies.jpg",
        price = 750000.00,
        preview = True
    )
    a17 = Artwork(
        user_id=4,
        title = "Impression, Sunrise",
        description = "The painting that gave rise to the term 'Impressionism,' featuring a harbor at sunrise.",
        image = "impression_sunrise.jpg",
        price = 900000.00,
        preview = False
    )
    a18 = Artwork(
        user_id=4,
        title = "Woman with a Parasol - Madame Monet and Her Son",
        description = "A lively scene of Monet's wife and son walking in a sunlit meadow with a parasol.",
        image = "woman_with_parasol.jpg",
        price = 680000.00,
        preview = True
    )
    a19 = Artwork(
        user_id=4,
        title = "Haystacks Series",
        description = "A series of paintings capturing the play of light and atmosphere on haystacks in the countryside.",
        image = "haystacks_series.jpg",
        price = 520000.00,
        preview = False
    )
    a20 = Artwork(
        user_id=4,
        title = "Rouen Cathedral Series",
        description = "Monet's exploration of the Rouen Cathedral facade in different lighting conditions and times of day.",
        image = "rouen_cathedral_series.jpg",
        price = 630000.00,
        preview = True
    )
    
    artworks.extend([a11,a12,a13,a14,a15,a16,a17,a18,a19,a20])
    return artworks