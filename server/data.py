
def create_users():
    from models.user import User
    users = []
    # Artist Instances
    a1 = User(
        full_name= "Leonardo da Vinci",
        username= "leo_da_vinci",
        email= "leo_da_vinci@example.com",
        bio= "I'm Leonardo da Vinci, the original Renaissance rockstar, juggling art, science, and engineering like I had a million arms – from painting masterpieces like the Mona Lisa to sketching flying machines; I was the guy who made multitasking look like a stroll through the Medici gardens.",
        location= "Vinci, Italy",
        profile_image= "https://hips.hearstapps.com/hmg-prod/images/portrait-of-leonardo-da-vinci-1452-1519-getty.jpg"
    )
    a1.password= "password123"
    users.append(a1)
    a2 = User(
        full_name= "Vincent van Gogh",
        username= "vincent_van_gogh",
        email= "vincent_van_gogh@example.com",
        bio= "I'm Vincent van Gogh, the artist who cut off his ear and painted masterpieces like it was going out of style, turning sunflowers and starry nights into my own vivid symphony of colors. because life\'s too short to paint with just one shade of melancholy.",
        location= "Zundert, Netherlands",
        profile_image= "https://hips.hearstapps.com/hmg-prod/images/vincent_van_gogh_self_portrait_painting_musee_dorsay_via_wikimedia_commons_promojpg.jpg"
    )
    a2.password= "password456"
    users.append(a2)
    a3 = User(
        full_name= "Pablo Picasso",
        username= "pablo_picasso",
        email= "pablo_picasso@example.com",
        bio= "I'm Pablo Picasso, the maestro who rocked berets, broke artistic molds, and turned Cubism into the coolest thing since sliced bread.",
        location= "Málaga, Spain",
        profile_image= "https://www.pablopicasso.org/images/picasso.jpg"
    )
    a3.password= "password111"
    users.append(a3)
    a4 = User(
        full_name= "Claude Monet",
        username= "claude_monet",
        email= "claude_monet@example.com",
        bio= "I'm Claude Monet, the French maestro who turned water lilies and haystacks into art-world rockstars, proving that my palette was as vibrant as a summer garden and my dedication to capturing light was more unwavering than a snail's journey across a water lily pond.",
        location= "Paris, France",
        profile_image= "https://www.claude-monet.com/images/claude-monet.jpg"
    )
    a4.password= "password121"
    users.append(a4)
    a5 = User(
        full_name= "Salvador Dalí",
        username= "salvador_dali",
        email= "salvador_dali@example.com",
        bio= "Surrealist artist",
        location= "Figueres, Spain",
        profile_image= "https://assets.artworkarchive.com/image/upload/t_jpg_large/v1605300238/user_43577/contact_images/dahli_x4uneu.jpg"
    )
    a5.password= "password131"
    users.append(a5)
    a6 = User(
        full_name= "Michelangelo Buonarroti",
        username= "michelangelo",
        email= "michelangelo@example.com",
        bio= "Renaissance sculptor and painter",
        location= "Caprese, Italy",
        profile_image= "https://cdn.britannica.com/46/75046-050-0973B0E8/Michelangelo.jpg"
    )
    a6.password= "password141"
    users.append(a6)
    a7 = User(
        full_name= "Frida Kahlo",
        username= "frida_kahlo",
        email= "frida_kahlo@example.com",
        bio= "Mexican painter known for her self-portraits",
        location= "Coyoacán, Mexico",
        profile_image= "https://upload.wikimedia.org/wikipedia/commons/0/06/Frida_Kahlo%2C_by_Guillermo_Kahlo.jpg"
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
        profile_image= "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Andy_Warhol_at_the_Jewish_Museum_%28by_Bernard_Gotfryd%29_%E2%80%93_LOC.jpg/640px-Andy_Warhol_at_the_Jewish_Museum_%28by_Bernard_Gotfryd%29_%E2%80%93_LOC.jpg"
    )
    a8.password= "password161"
    users.append(a8)
    a9 = User(
        full_name= "Raphael Sanzio",
        username= "raphael_sanzio",
        email= "raphael_sanzio@example.com",
        bio= "High Renaissance painter",
        location= "Urbino, Italy",
        profile_image= "https://upload.wikimedia.org/wikipedia/commons/f/f6/Raffaello_Sanzio.jpg"
    )
    a9.password= "password171"
    users.append(a9)
    a10 = User(
        full_name= "Edvard Munch",
        username= "edvard_munch",
        email= "edvard_munch@example.com",
        bio= "Expressionist painter",
        location= "Oslo, Norway",
        profile_image= "https://hips.hearstapps.com/hmg-prod/images/gettyimages-600031727jpg--.jpg"
    )
    a10.password= "password181"
    users.append(a10)
    a11 = User(
        full_name= "Rembrandt van Rijn",
        username= "rembrandt",
        email= "rembrandt@example.com",
        bio= "Dutch Golden Age painter",
        location= "Leiden, Netherlands",
        profile_image= "https://cdn.britannica.com/82/190482-050-33D2C4C5/Self-Portrait-canvas-Rembrandt-van-Rijn-Washington-DC.jpg"
    )
    a11.password= "password191"
    users.append(a11)
    a12 = User(
        full_name= "Jackson Pollock",
        username= "jackson_pollock",
        email= "jackson_pollock@example.com",
        bio= "Abstract expressionist painter",
        location= "Cody, USA",
        profile_image= "https://www.jackson-pollock.org/images/jackson-pollock.jpg"
    )
    a12.password= "password201"
    users.append(a12)
    a13 = User(
        full_name= "Willem Verbeeck",
        username= "willemverb",
        email= "willemverb@example.com",
        bio= "LA based Photographer",
        location= "Los Angeles, CA",
        profile_image= "https://pbs.twimg.com/profile_images/1232390930034053120/Gu3Ce6OX_400x400.jpg"
    )
    a13.password= "password314"
    users.append(a13)
    
    return users

def create_artworks():
    from models.artwork import Artwork
    artworks = []
    a1 = Artwork(
        user_id=1,
        title = "Mona Lisa",
        description = "Portrait of Lisa Gherardini, wife of Francesco del Giocondo",
        image = "https://cdn.britannica.com/24/189624-050-F3C5BAA9/Mona-Lisa-oil-wood-panel-Leonardo-da.jpg",
        price=200.00,
        preview=True
    )
    a2 = Artwork(
        user_id=1,
        title = "The Last Supper",
        description = "Depiction of the last meal of Jesus with his disciples",
        image = "https://kottke.org/plus/misc/images/last-supper-copy-01.jpg",
        price=500.00,
        preview=True
    )
    a3 = Artwork(
        user_id=1,
        title = "Vitruvian Man",
        description = "Study of the proportions of the human body according to Vitruvius",
        image = "https://www.leonardodavinci.net/images/gallery/the-vitruvian-man.jpg",
        price=225.00,
        preview=True
    )
    a4 = Artwork(
        user_id=1,
        title = "Annunciation",
        description = "Archangel Gabriel announcing to the Virgin Mary that she will conceive Jesus",
        image = "https://ap.uffizi.it/1688661762-1503990074029518-568314.jpg?auto=format&max-w=800",
        price=100.00,
        preview=True
    )
    a5 = Artwork(
        user_id=1,
        title = "Lady with an Ermine",
        description = "Portrait of Cecilia Gallerani holding an ermine",
        image = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Lady_with_an_Ermine_-_Leonardo_da_Vinci_%28adjusted_levels%29.jpg/1200px-Lady_with_an_Ermine_-_Leonardo_da_Vinci_%28adjusted_levels%29.jpg",
        price=199.99,
        preview=True
    )
    a6 = Artwork(
        user_id=2,
        title = "Starry Night",
        description = "A night sky filled with swirling clouds and bright stars over a tranquil village.",
        image = "https://cdn.pixabay.com/photo/2015/12/15/05/43/starry-night-1093721_1280.jpg",
        price = 50.00,
        preview = True

    )
    a7 = Artwork(
        user_id=2,
        title = "Sunflowers",
        description = "A series of still life paintings depicting vibrant sunflowers in various stages of bloom.",
        image = "https://usa.masterpiecebynumbers.com/cdn/shop/products/Van_Gogh_-_Sunflowers.jpg?v=1571674640",
        price = 35.00,
        preview = False
    )
    a8 = Artwork(
        user_id=2,
        title = "The Bedroom",
        description = "A depiction of Van Gogh's bedroom in the Yellow House in Arles with bold colors and distinctive brushstrokes.",
        image = "https://iiif.micr.io/ZKSPH/full/1280,/0/default.jpg",
        price = 70.00,
        preview = True
    )
    a9 = Artwork(
        user_id=2,
        title = "Irises",
        description = "A masterpiece featuring vibrant irises set against a background of lush greenery.",
        image = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Irises-Vincent_van_Gogh.jpg/1200px-Irises-Vincent_van_Gogh.jpg",
        price = 45.00,
        preview = True
    )
    a10 = Artwork(
        user_id=2,
        title = "Café Terrace at Night",
        description = "A charming night scene of a cafe terrace illuminated by warm light under a starry sky.",
        image = "https://www.vangoghstudio.com//Files/6/102000/102147/ProductPhotos/Source/1938150426.jpg",
        price = 60.00,
        preview = False
    )
    artworks.extend([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
    a11 = Artwork(
        user_id=3,
        title = "Guernica",
        description = "A powerful anti-war mural depicting the horrors of the bombing of Guernica during the Spanish Civil War.",
        image = "https://2.bp.blogspot.com/-dlllLhl8c7s/UnrFUvtgMxI/AAAAAAAARXQ/Cv8QKBgfVD4/s1600/guernica.jpg",
        price = 80.00,
        preview = True
    )
    a12 = Artwork(
        user_id=3,
        title = "Les Demoiselles d'Avignon",
        description = "A groundbreaking work in modern art, portraying five nude women with influences from African art.",
        image = "https://upload.wikimedia.org/wikipedia/en/4/4c/Les_Demoiselles_d%27Avignon.jpg",
        price = 95.00,
        preview = False
    )
    a13 = Artwork(
        user_id=3,
        title = "The Weeping Woman",
        description = "A powerful portrayal of grief and pain, featuring a woman with tears streaming down her face.",
        image = "https://miro.medium.com/v2/resize:fit:1400/1*D1w37WAU9cZVS6_J5Q4gdw.jpeg",
        price = 70.00,
        preview = True
    )
    a14 = Artwork(
        user_id=3,
        title = "Three Musicians",
        description = "A colorful and abstract composition depicting three musicians playing instruments.",
        image = "https://www.pablopicasso.org/images/paintings/three-musicians.jpg",
        price = 60.00,
        preview = False
    )
    a15 = Artwork(
        user_id=3,
        title = "The Old Guitarist",
        description = "A melancholic painting of an old blind guitarist, reflecting Picasso's Blue Period.",
        image = "https://upload.wikimedia.org/wikipedia/en/b/bc/Old_guitarist_chicago.jpg",
        price = 50.00,
        preview = True
    )
    a16 = Artwork(
        user_id=4,
        title = "Water Lilies",
        description = "A series of paintings depicting Monet's water garden at Giverny, featuring water lilies and reflections.",
        image = "https://www.artic.edu/iiif/2/3c27b499-af56-f0d5-93b5-a7f2f1ad5813/full/843,/0/default.jpg",
        price = 75.00,
        preview = True
    )
    a17 = Artwork(
        user_id=4,
        title = "Impression, Sunrise",
        description = "The painting that gave rise to the term 'Impressionism,' featuring a harbor at sunrise.",
        image = "https://i.etsystatic.com/18641759/r/il/0982d3/3854750965/il_fullxfull.3854750965_7ag7.jpg",
        price = 90.00,
        preview = False
    )
    a18 = Artwork(
        user_id=4,
        title = "Woman with a Parasol - Madame Monet and Her Son",
        description = "A lively scene of Monet's wife and son walking in a sunlit meadow with a parasol.",
        image = "https://media.nga.gov/iiif/99758d9d-c10b-4d02-a198-7e49afb1f3a6/full/full/0/default.jpg?attachment_filename=woman_with_a_parasol_-_madame_monet_and_her_son_1983.1.29.jpg",
        price = 68.00,
        preview = True
    )
    a19 = Artwork(
        user_id=4,
        title = "Haystacks Series",
        description = "A series of paintings capturing the play of light and atmosphere on haystacks in the countryside.",
        image = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Claude_Monet_-_Stacks_of_Wheat_%28End_of_Summer%29_-_1985.1103_-_Art_Institute_of_Chicago.jpg/800px-Claude_Monet_-_Stacks_of_Wheat_%28End_of_Summer%29_-_1985.1103_-_Art_Institute_of_Chicago.jpg",
        price = 52.00,
        preview = False
    )
    a20 = Artwork(
        user_id=5,
        title="The Persistence of Memory",
        description="Dali's iconic surrealist painting featuring melting clocks in a dreamlike landscape.",
        image="https://www.artchive.com/wp-content/uploads/2023/04/The-Persistence-of-Memory-DALI-Salvador-1931-2.jpg",
        price=120.00,
        preview=True
    )
    artworks.extend([a11,a12,a13,a14,a15,a16,a17,a18,a19, a20])
    a21 = Artwork(
        user_id=5,
        title="Swans Reflecting Elephants",
        description="A mind-bending optical illusion depicting swans on a calm lake transforming into elephants in their reflection.",
        image="https://penflukyhome.files.wordpress.com/2020/06/81izy657uyl._sl1500_.jpg?w=825&h=510&crop=1",
        price=85.00,
        preview=False
    )
    a22 = Artwork(
        user_id=5,
        title="The Elephants",
        description="Dali's surreal depiction of spindly-legged elephants carrying obelisks on their backs in a barren landscape.",
        image="https://www.ladykflo.com/wp-content/uploads/2022/04/jmy-elephants-in-the-style-of-salvador-dali_2020-02-03T12-53-54.jpg",
        price=95.00,
        preview=True
    )
    a23 = Artwork(
        user_id=5,
        title="The Sacrament of the Last Supper",
        description="A religious-themed painting by Dali featuring a distorted interpretation of the traditional Last Supper.",
        image="https://www.tallengestore.com/cdn/shop/products/the_20sacrament_20of_20the_20last_20supper_32d93374-c315-4739-bd47-d6114f4e03e3.jpg?v=1479717541",
        price=110.00,
        preview=False
    )
    a24 = Artwork(
        user_id=5,
        title="Galatea of the Spheres",
        description="Dali's exploration of the concept of atomic particles and the harmony of the universe through a portrait of his wife.",
        image="https://m.media-amazon.com/images/I/719Hn8X+XtL._AC_UF894,1000_QL80_.jpg",
        price=78.00,
        preview=True
    )
    a25 = Artwork(
        user_id=6,
        title="David",
        description="Michelangelo's iconic marble statue of the biblical hero David, symbolizing the strength of the human spirit.",
        image="https://news.artnet.com/app/news-upload/2023/04/GettyImages-1395079230-1024x682.jpg",
        price=150.00,
        preview=True
    )
    a26 = Artwork(
        user_id=6,
        title="Sistine Chapel Ceiling",
        description="A masterpiece fresco in the Sistine Chapel depicting scenes from Genesis, including the creation of Adam.",
        image="https://cdn.thecollector.com/wp-content/uploads/2020/05/sistine_chapel_painted_frescoes_by_michelangelo_in_vatican_featured.jpg",
        price=200.00,
        preview=False
    )
    a27 = Artwork(
        user_id=6,
        title="Pieta",
        description="Michelangelo's sculpture of the Virgin Mary cradling the body of Jesus, showcasing profound grief and beauty.",
        image="https://upload.wikimedia.org/wikipedia/commons/6/65/Pieta_de_Michelangelo_-_Vaticano.jpg",
        price=180.00,
        preview=True
    )
    a28 = Artwork(
        user_id=6,
        title="The Creation of Adam",
        description="A central panel from the Sistine Chapel Ceiling, depicting the iconic moment of God giving life to Adam through touch.",
        image="https://cdn.thecollector.com/wp-content/uploads/2022/03/michelangelo-creation-adam-detail-featured.jpg?width=1400&quality=70",
        price=170.00,
        preview=False
    )
    a29 = Artwork(
        user_id=6,
        title="The Last Judgment",
        description="A monumental fresco on the altar wall of the Sistine Chapel, depicting the Second Coming of Christ and final judgment.",
        image="https://smarthistory.org/wp-content/uploads/2022/01/LastJudgement.jpg",
        price=220.00,
        preview=True
    )
    a30 = Artwork(
        user_id=7,
        title="The Two Fridas",
        description="A powerful and symbolic self-portrait featuring two versions of Frida Kahlo, representing her duality and inner emotions.",
        image="https://www.fridakahlo.org/images/paintings/the-two-fridas.jpg",
        price=95.00,
        preview=True
    )
    artworks.extend([a21,a22,a23,a24,a25,a26,a27,a28,a29, a30])
    a31 = Artwork(
        user_id=7,
        title="Self-Portrait with Thorn Necklace and Hummingbird",
        description="A poignant self-portrait where Frida wears a thorn necklace, reflecting her pain, and a hummingbird symbolizing hope.",
        image="https://www.arthistoryproject.com/site/assets/files/19982/frida-kahlo-self-portrait-with-thorn-necklace-and-hummingbird-1940-trivium-art-history.jpg",
        price=80.00,
        preview=False
    )
    a32 = Artwork(
        user_id=7,
        title="The Broken Column",
        description="An emotional self-portrait portraying Frida with a shattered column as her spine, revealing her physical and emotional pain.",
        image="https://www.dailyartmagazine.com/wp-content/uploads/2021/10/ddd-4.jpg",
        price=110.00,
        preview=True
    )
    a33 = Artwork(
        user_id=7,
        title="Diego and I",
        description="A representation of Frida Kahlo alongside her husband Diego Rivera, showcasing their complex and passionate relationship.",
        image="https://www.fridakahlo.org/images/paintings/frida-and-diego-rivera.jpg",
        price=90.00,
        preview=False
    )
    a34 = Artwork(
        user_id=7,
        title="The Love Embrace of the Universe",
        description="A vibrant and surreal self-portrait where Frida is embraced by the universe, symbolizing her connection to the world and life.",
        image="https://www.fridakahlo.org/images/paintings/the-love-embrace-of-the-universe-the-earth-mexico-myself-diego-and-senor-xolotl.jpg",
        price=120.00,
        preview=True
    )
    a35 = Artwork(
        user_id=8,
        title="Campbell's Soup Cans",
        description="A groundbreaking series of 32 paintings featuring different flavors of Campbell's soup cans, symbolizing consumer culture.",
        image="https://origins.osu.edu/sites/default/files/inline-images/andy-warhol-soup-cans.jpg",
        price=180.00,
        preview=True
    )
    a36 = Artwork(
        user_id=8,
        title="Marilyn Diptych",
        description="An iconic artwork featuring multiple images of Marilyn Monroe, exploring the relationship between celebrity and mass production.",
        image="https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/andy-warhols-marilyn-diptych-douglas-sacha.jpg",
        price=220.00,
        preview=False
    )
    a37 = Artwork(
        user_id=8,
        title="Brillo Boxes",
        description="A series of sculptures resembling Brillo soap pad boxes, blurring the lines between art and everyday consumer products.",
        image="https://www.artchive.com/wp-content/uploads/2023/02/Warhol_Brillo_Foundation-768x576-1.jpg",
        price=150.00,
        preview=True
    )
    a38 = Artwork(
        user_id=8,
        title="Elvis Presley",
        description="A portrait of Elvis Presley, one of Warhol's many celebrity portraits that became synonymous with his Pop art movement.",
        image="https://cdn.sanity.io/images/dqllnil6/production/f65231f34a6ac6707176013dcf64b257cff3e591-516x525.jpg?w=1920&q=60&auto=format",
        price=160.00,
        preview=False
    )
    a39 = Artwork(
        user_id=8,
        title="Gold Marilyn Monroe",
        description="A glamorous depiction of Marilyn Monroe in gold tones, emphasizing her status as a cultural icon and symbol of beauty.",
        image="https://www.moma.org/d/assets/W1siZiIsIjIwMTkvMDkvMDUvOWQ5MmNjYjJ5NF8zMTZfMTk2Ml9DUl9QcmVzc19Vc2VfXzMwMDBfcGl4ZWxfbGVuZ3RoXy5qcGciXSxbInAiLCJjb252ZXJ0IiwiLXF1YWxpdHkgOTAgLXJlc2l6ZSAyMDAweDIwMDBcdTAwM2UiXV0/316_1962_CR-Press_Use_%283000_pixel_length%29.jpg?sha=745ff28c35b4fb0d",
        price=200.00,
        preview=True
    )
    a40 = Artwork(
        user_id=9,
        title="The School of Athens",
        description="A masterpiece fresco depicting philosophers and scholars from different periods gathered in an imaginary classical setting.",
        image="https://antigonejournal.com/wp-content/uploads/2023/02/SoAR-3.png",
        price=250.00,
        preview=True
    )
    artworks.extend([a31,a32,a33,a34,a35,a36,a37,a38,a39, a40])
    a41 = Artwork(
        user_id=9,
        title="Madonna and Child with the Infant Saint John the Baptist",
        description="A tender portrayal of the Madonna and Child with the young Saint John the Baptist, showcasing Raphael's skill in depicting grace and harmony.",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Madona_del_gran_duque%2C_por_Rafael.jpg/512px-Madona_del_gran_duque%2C_por_Rafael.jpg",
        price=180.00,
        preview=False
    )
    a42 = Artwork(
        user_id=9,
        title="The Sistine Madonna",
        description="An iconic painting featuring the Madonna and Child surrounded by angels, known for its emotional depth and ethereal beauty.",
        image="https://uploads3.wikiart.org/00340/images/raphael/the-sistine-madonna-1513.jpg!Large.jpg",
        price=220.00,
        preview=True
    )
    a43 = Artwork(
        user_id=9,
        title="Portrait of Baldassare Castiglione",
        description="A celebrated portrait of the Italian diplomat and writer Baldassare Castiglione, showcasing Raphael's mastery in capturing personality.",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Baldassare_Castiglione%2C_by_Raffaello_Sanzio%2C_from_C2RMF_retouched.jpg/1200px-Baldassare_Castiglione%2C_by_Raffaello_Sanzio%2C_from_C2RMF_retouched.jpg",
        price=190.00,
        preview=False
    )
    a44 = Artwork(
        user_id=9,
        title="The Transfiguration",
        description="Raphael's final masterpiece, a large altarpiece depicting the Transfiguration of Christ, showcasing both earthly and divine scenes.",
        image="https://upload.wikimedia.org/wikipedia/commons/5/51/Transfiguration_Raphael.jpg",
        price=500.00,
        preview=True
    )
    a45 = Artwork(
        user_id=10,
        title="The Scream",
        description="One of the most iconic paintings in art history, depicting a figure in distress against a surreal, swirling backdrop.",
        image="https://smarthistory.org/wp-content/uploads/2021/12/Edvard_Munch_-_The_Scream_-_Google_Art_Project.jpeg",
        price=500.00,
        preview=True
    )
    a46 = Artwork(
        user_id=10,
        title="The Madonna",
        description="A haunting depiction of Madonna holding a child, marked by Munch's distinctive style and emotional intensity.",
        image="https://www.munchmuseet.no/globalassets/kunstverk/madonna-litografi?w=800",
        price=500.00,
        preview=False
    )
    a47 = Artwork(
        user_id=10,
        title="The Dance of Life",
        description="A symbolic painting representing the stages of life through three figures dancing under the moonlight.",
        image="https://upload.wikimedia.org/wikipedia/commons/b/b6/Edvard_Munch_-_The_dance_of_life_%281899-1900%29.jpg",
        price=500.00,
        preview=True
    )
    a48 = Artwork(
        user_id=10,
        title="Jealousy",
        description="A striking portrayal of jealousy, featuring a green-faced figure watching a couple with a sense of longing.",
        image="https://upload.wikimedia.org/wikipedia/commons/c/cb/Edvard_Munch_-_Jealousy_%281895%29.jpg",
        price=500.00,
        preview=False
    )
    a49 = Artwork(
        user_id=10,
        title="Starry Night",
        description="Munch's interpretation of the night sky, filled with swirling stars and a sense of cosmic energy.",
        image="https://www.munchmuseet.no/globalassets/kunstverk/stjernenatt.jpg",
        price=500.00,
        preview=True
    )
    a50 = Artwork(
        user_id=11,
        title="The Night Watch",
        description="Rembrandt's famous group portrait of a city militia, known for its dynamic composition and use of light and shadow.",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/The_Night_Watch_-_HD.jpg/1200px-The_Night_Watch_-_HD.jpg",
        price=500.00,
        preview=True
    )
    artworks.extend([a41,a42,a43,a44,a45,a46,a47,a48,a49, a50])
    a51 = Artwork(
        user_id=11,
        title="Self-Portrait with Two Circles",
        description="A powerful self-portrait by Rembrandt, showcasing his introspective gaze and mastery in capturing texture and expression.",
        image="https://smarthistory.org/wp-content/uploads/2019/08/Edited-Rembrandt_Self-portrait_Kenwood.jpg",
        price=500.00,
        preview=False
    )
    a52 = Artwork(
        user_id=11,
        title="The Anatomy Lesson of Dr. Nicolaes Tulp",
        description="A compelling group portrait depicting a dissection, highlighting Rembrandt's skill in portraying human anatomy and emotion.",
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Rembrandt_-_The_Anatomy_Lesson_of_Dr_Nicolaes_Tulp.jpg/1200px-Rembrandt_-_The_Anatomy_Lesson_of_Dr_Nicolaes_Tulp.jpg",
        price=500.00,
        preview=True
    )
    a53 = Artwork(
        user_id=11,
        title="The Jewish Bride",
        description="A tender and intimate portrait of a couple, often interpreted as a depiction of love and marital bliss.",
        image="https://upload.wikimedia.org/wikipedia/commons/0/0c/Rembrandt_Harmensz._van_Rijn_-_Portret_van_een_paar_als_oudtestamentische_figuren%2C_genaamd_%27Het_Joodse_bruidje%27_-_Google_Art_Project.jpg",
        price=500.00,
        preview=False
    )
    a54 = Artwork(
        user_id=11,
        title="The Storm on the Sea of Galilee",
        description="A dramatic seascape depicting a biblical scene, showcasing Rembrandt's skill in capturing tumultuous emotions and nature.",
        image="https://upload.wikimedia.org/wikipedia/commons/f/f3/Rembrandt_Christ_in_the_Storm_on_the_Lake_of_Galilee.jpg",
        price=500.00,
        preview=True
    )
    a55 = Artwork(
        user_id=12,
        title="No. 5, 1948",
        description="A groundbreaking example of Pollock's drip painting technique, characterized by energetic and chaotic splatters of paint.",
        image="https://www.jackson-pollock.org/images/paintings/number-5.jpg",
        price=500.00,
        preview=True
    )
    a56 = Artwork(
        user_id=12,
        title="Autumn Rhythm",
        description="A rhythmic and dynamic composition created through Pollock's unique drip painting style, conveying a sense of movement.",
        image="https://collectionapi.metmuseum.org/api/collection/v1/iiif/488978/preview",
        price=500.00,
        preview=False
    )
    a57 = Artwork(
        user_id=12,
        title="Blue Poles",
        description="A celebrated painting featuring tall, thin poles surrounded by energetic drips and splatters of vibrant blue paint.",
        image="https://cdn.swarezart.com/wp-content/uploads/2016/09/Blue-Poles-replica-painting-1.jpg",
        price=500.00,
        preview=True
    )
    a58 = Artwork(
        user_id=12,
        title="One: Number 31, 1950",
        description="A large-scale canvas filled with intricate and densely layered drips and swirls, showcasing Pollock's mastery of abstract expressionism.",
        image="https://i.ytimg.com/vi/2JleSka1klc/sddefault.jpg",
        price=500.00,
        preview=False
    )
    a59 = Artwork(
        user_id=12,
        title="Convergence",
        description="A vibrant and dynamic composition created through the spontaneous and gestural nature of Pollock's drip painting technique.",
        image="https://www.jackson-pollock.org/images/paintings/convergence.jpg",
        price=500.00,
        preview=True
    )
    a60 = Artwork(
        user_id=13,
        title="The House",
        description="Taken on 35mm film.",
        image="https://image.shopmoment.com/general/willem-verbeeck-gallery-01.jpg",
        price=500.00,
        preview=True
    )
    artworks.extend([a51,a52,a53,a54,a55,a56,a57,a58,a59,a60])
    a61 = Artwork(
        user_id=13,
        title="The Still of the Night",
        description="Taken on 35mm film.",
        image="https://djwp.s3.amazonaws.com/wp-content/uploads/2022/02/25112503/THUMB_HEADER-38-1024x575.jpg",
        price=500.00,
        preview=True
    )
    a62 = Artwork(
        user_id=13,
        title="The Bridge",
        description="Taken on 35mm film.",
        image="https://image.shopmoment.com/general/willem-verbeeck-gallery-02.jpg",
        price=500.00,
        preview=True
    )
    a63 = Artwork(
        user_id=13,
        title="The Courtyard",
        description="Taken on 35mm film.",
        image="https://images.squarespace-cdn.com/content/v1/634723977fd6041c2f4c7c59/19573ec5-315a-4db3-a0c0-1d024b94e0cf/Willem_Verbeeck_13.jpg",
        price=500.00,
        preview=True
    )
    a64 = Artwork(
        user_id=13,
        title="The Night Shift",
        description="Taken on 35mm film.",
        image="https://images.squarespace-cdn.com/content/v1/5ede832c2c3f923fc69dad9f/1593661122694-PLUV4H9YZHDZ1ZBKNMNT/MayXT038302.jpg",
        price=500.00,
        preview=True
    )
    artworks.extend([a61,a62,a63,a64])
    return artworks