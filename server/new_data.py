from faker import Faker
fake = Faker()

def create_users():
    from models.user import User
    users = []
    a1 = User(
        full_name="Tyler Smith",
        username="ty_smith",
        email="ty_smith@example.com",
        bio="Passionate about capturing moments through the lens. I specialize in both film and digital photography, seeking the extraordinary in the ordinary. Join me on a visual journey!",
        location="Seattle, WA",
        profile_image="https://images.unsplash.com/photo-1603415526960-f7e0328c63b1?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    )
    a1.password = "password123"
    users.append(a1)
    a2 = User(
        full_name="Emma Johnson",
        username="emma_j",
        email="emma_j@example.com",
        bio="Digital artist and creator, transforming ideas into visual masterpieces. By day, I code; by night, I paint. Let's explore the intersection of technology and art together!",
        location="San Francisco, CA",
        profile_image="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    )
    a2.password = "coding123"
    users.append(a2)
    a3 = User(
        full_name="Jordan Taylor",
        username="jtaylor",
        email="jtaylor@example.com",
        bio="Visual storyteller through the lens of a camera. I find beauty in every frame, capturing emotions and stories. Join me in exploring the artistry of photography!",
        location="Denver, CO",
        profile_image="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    )
    a3.password = "hiker123"
    users.append(a3)
    a4 = User(
        full_name="Sophie Davis",
        username="soph_d",
        email="soph_d@example.com",
        bio="Diving into the world of art, I explore various mediums to express my creativity. From paintings to sculptures, let's embark on an artistic journey together!",
        location="New York, NY",
        profile_image="https://images.unsplash.com/photo-1606914707708-5180546f153d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjN8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
    )
    a4.password = "booklover123"
    users.append(a4)
    a5 = User(
        full_name="Chris Mitchell",
        username="chris_m",
        email="chris_m@example.com",
        bio="Every pixel tells a story in my digital art. Aspiring animator on a quest to bring imagination to life. Let's discuss the magic of animation and create our own visual tales!",
        location="Los Angeles, CA",
        profile_image="https://images.unsplash.com/photo-1624561172888-ac93c696e10c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjJ8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
    )
    a5.password = "artlover123"
    users.append(a5)
    a6 = User(
        full_name="Olivia Martinez",
        username="olivia_m",
        email="olivia_m@example.com",
        bio="Exploring the world through the lens of art, I find inspiration in culinary creations. Join me on a journey of food photography and discover the visual delights of gastronomy!",
        location="Chicago, IL",
        profile_image="https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
    )
    a6.password = "foodie123"
    users.append(a6)
    a7 = User(
        full_name="Ryan Williams",
        username="ryan_w",
        email="ryan_w@example.com",
        bio="Composing melodies and creating harmonies, I'm on a musical journey. Let's explore the art of sound together, from classic compositions to modern beats!",
        location="Nashville, TN",
        profile_image="https://images.unsplash.com/photo-1463453091185-61582044d556?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8cHJvZmlsZSUyMHBpY3R1cmV8ZW58MHx8MHx8fDI%3D"
        )
    a7.password = "musiclover123"
    users.append(a7)
    a8 = User(
        full_name="Aiden Turner",
        username="aiden_t",
        email="aiden_t@example.com",
        bio="From coding to creating, I'm a tech enthusiast exploring the artistry of innovation. Join me in blending technology and creativity to build something extraordinary!",
        location="Austin, TX",
        profile_image="https://images.unsplash.com/photo-1544723795-3fb6469f5b39?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
    )
    a8.password = "techlover123"
    users.append(a8)
    a9 = User(
        full_name="Mia Thompson",
        username="mia_t",
        email="mia_t@example.com",
        bio="Expressing my love for fitness through the art of yoga. Join me on a journey of mindfulness and movement, discovering the artistry of a balanced and healthy lifestyle!",
        location="Miami, FL",
        profile_image="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cHJvZmlsZSUyMHBpY3R1cmV8ZW58MHx8MHx8fDI%3D"
    )
    a9.password = "fitlife123"
    users.append(a9)
    a10 = User(
        full_name="Elijah Carter",
        username="elijah_c",
        email="elijah_c@example.com",
        bio="In the world of cinema, every frame is a piece of art. Aspiring filmmaker on a quest to tell stories that resonate. Let's discuss our favorite films and create cinematic wonders!",
        location="Los Angeles, CA",
        profile_image="https://images.unsplash.com/photo-1544435253-f0ead49638fa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
    )
    a10.password = "filmlover123"
    users.append(a10)
    a11 = User(
        full_name="Grace Miller",
        username="grace_m",
        email="grace_m@example.com",
        bio="Advocating for the environment through the art of sustainable living. Join me in creating a greener world, one eco-friendly choice at a time!",
        location="Portland, OR",
        profile_image="https://images.unsplash.com/photo-1521856729154-7118f7181af9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjl8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
    )
    a11.password = "greenplanet123"
    users.append(a11)
    a12 = User(
        full_name="Liam Foster",
        username="liam_f",
        email="liam_f@example.com",
        bio="Sports through the lens of art and athleticism. Join me in celebrating the beauty of sports photography and the physical artistry of the human body!",
        location="Chicago, IL",
        profile_image="https://images.unsplash.com/photo-1534308143481-c55f00be8bd7?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDR8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
        )
    a12.password = "sportsfan123"
    users.append(a12)
    a13 = User(
        full_name="Ava Simmons",
        username="ava_s",
        email="ava_s@example.com",
        bio="Immersed in the world of visual arts, I express my creativity through painting. Join me on a journey of colors and brushstrokes, where every canvas tells a unique story!",
        location="New York, NY",
        profile_image="https://images.unsplash.com/photo-1524154217857-45f012d0f167?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzR8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
        )
    a13.password = "artist123"
    users.append(a13)
    a14 = User(
        full_name="Owen Roberts",
        username="owen_r",
        email="owen_r@example.com",
        bio="Traveling through the world, I capture moments of beauty in photography. Join me in exploring the artistry of diverse cultures and landscapes!",
        location="Denver, CO",
        profile_image="https://images.unsplash.com/photo-1586962358070-16a0f05b8e67?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTZ8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
    )
    a14.password = "traveler123"
    users.append(a14)
    a15 = User(
        full_name="Eva White",
        username="eva_w",
        email="eva_w@example.com",
        bio="Fashion is my canvas, and style is my art. Join me in exploring the world of fashion, where every outfit is an expression of creativity!",
        location="Miami, FL",
        profile_image="https://images.unsplash.com/photo-1489424731084-a5d8b219a5bb?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDB8fHByb2ZpbGUlMjBwaWN0dXJlfGVufDB8fDB8fHwy"
    )
    a15.password = "fashionista123"
    users.append(a15)
    
    return users
    
def create_artworks():
    from models.artwork import Artwork
    artworks = []

    artworks.append(Artwork(user_id=1, title="Wavelength", description="A tranquil seascape with shades of blue and calming waves.", image="https://images.unsplash.com/photo-1671288152072-f6f8eb4ef210?q=80&w=1928&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=True))
    artworks.append(Artwork(user_id=1, title="Winter Wonderland", description="One man's wasteland is another man's wonderland.", image="https://images.unsplash.com/photo-1697802212357-1e6c81a58d61?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=85.00, preview=False))
    artworks.append(Artwork(user_id=1, title="Urban Exploration", description="My apartment's daily view.", image="https://images.unsplash.com/photo-1634391352293-3753e5188fe0?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=200.00, preview=True))
    artworks.append(Artwork(user_id=1, title="Night Shift", description="Working that late night.", image="https://images.unsplash.com/photo-1612038928056-e2b831b5bb22?q=80&w=2350&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=150.00, preview=False))
    artworks.append(Artwork(user_id=1, title="Crosswalk", description="Look both ways before crossing.", image="https://images.unsplash.com/photo-1652002667524-650f3f32ddac?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fDM1JTIwbW0lMjBmaWxtfGVufDB8fDB8fHwy", price=95.00, preview=True))

    artworks.append(Artwork(user_id=2, title="Splash of Color", description="The vibrant lights of the city in a dynamic and energetic composition.", image="https://images.unsplash.com/photo-1543857778-c4a1a3e0b2eb?q=80&w=1910&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=130.00, preview=True))
    artworks.append(Artwork(user_id=2, title="Complementary", description="Elegance expressed through abstract forms and delicate lines.", image="https://images.unsplash.com/photo-1531489956451-20957fab52f2?q=80&w=1760&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=75.00, preview=False))
    artworks.append(Artwork(user_id=2, title="Colours", description="A serene landscape illuminated by the soft glow of the moon.", image="https://images.unsplash.com/flagged/photo-1567934150921-7632371abb32?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=180.00, preview=True))
    artworks.append(Artwork(user_id=2, title="Therapy Session", description="Dreamy cityscape with a mix of reality and imagination.", image="https://images.unsplash.com/photo-1605721911519-3dfeb3be25e7?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=110.00, preview=False))
    artworks.append(Artwork(user_id=2, title="Dull Mood", description="Fusion of abstract elements creating a visually dynamic piece.", image="https://images.unsplash.com/photo-1618331835717-801e976710b2?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=True))

    artworks.append(Artwork(user_id=3, title="Soul Nebula", description="The Soul Nebula caught on a astrophotography camping trip.", image="https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?q=80&w=1871&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=140.00, preview=True))
    artworks.append(Artwork(user_id=3, title="Snow Mountain Under Stars", description="Overnight hiking trip and I caught this gem on our trip!", image="https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=95.00, preview=False))
    artworks.append(Artwork(user_id=3, title="Lost In It All", description="A moment of zen combining a long exposure of the Milky Way and a candid.", image="https://images.unsplash.com/photo-1527492662722-dbaf97270863?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=220.00, preview=True))
    artworks.append(Artwork(user_id=3, title="The Blood Moon", description="After 1 hour of hiking, we set up our cameras at 2500m.", image="https://images.unsplash.com/photo-1533206482744-b9766a45e98a?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=160.00, preview=False))
    artworks.append(Artwork(user_id=3, title="Milky Way", description="A long exposure taken on my Sony A7000.", image="https://images.unsplash.com/photo-1467685790346-20bfe73a81f0?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=130.00, preview=True))

    artworks.append(Artwork(user_id=4, title="Mean Mug", description="I wish I could say this is my creation but my friend outdid me on the artwork of pottery.", image="https://images.unsplash.com/photo-1472517990513-4f22ae253bd3?q=80&w=1748&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=180.00, preview=True))
    artworks.append(Artwork(user_id=4, title="Ghost", description="In the moments to feel like Patrick Swayze.", image="https://images.unsplash.com/photo-1468322638156-074863f9362e?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=False))
    artworks.append(Artwork(user_id=4, title="Focus", description="Sculptor and his work.", image="https://images.unsplash.com/photo-1447758902204-48010b87c24d?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=90.00, preview=True))
    artworks.append(Artwork(user_id=4, title="Holding Hands", description="My mom always told me to not point fingers, never to hold sculptures to point.", image="https://images.unsplash.com/photo-1514504576470-3e9195509469?q=80&w=1745&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=200.00, preview=False))
    artworks.append(Artwork(user_id=4, title="Busts", description="We went salvage hunting.", image="https://images.unsplash.com/photo-1541618016834-667715db6e8d?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=110.00, preview=True))

    artworks.append(Artwork(user_id=5, title="David the Bust", description="Reflecting emotions through abstract brushstrokes and colors.", image="https://images.unsplash.com/photo-1634986666676-ec8fd927c23d?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=130.00, preview=True))
    artworks.append(Artwork(user_id=5, title="Where the Buck Are We?", description="Dreamlike dreamscape painted in warm hues of a setting sun.", image="https://images.unsplash.com/photo-1635322966219-b75ed372eb01?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=95.00, preview=False))
    artworks.append(Artwork(user_id=5, title="Filling in the Cracks", description="Fantasy exploration of vibrant florals in a surreal setting.", image="https://images.unsplash.com/photo-1637666505754-7416ebd70cbf?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGRpZ2l0YWwlMjBhcnR8ZW58MHx8MHx8fDI%3D", price=200.00, preview=True))
    artworks.append(Artwork(user_id=5, title="Think Pink", description="Elegance of a cityscape captured in detailed brushwork.", image="https://images.unsplash.com/photo-1630857453903-0386bfb0d990?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=150.00, preview=False))
    artworks.append(Artwork(user_id=5, title="Can You Lend a Hand?", description="Illusions of reality portrayed through abstract forms and colors.", image="https://images.unsplash.com/photo-1637140945341-f28ada987326?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=95.00, preview=True))

    artworks.append(Artwork(user_id=6, title="Blueberry Cheesecake", description="If blueberries aren't on your cheesecake, did you really enjoy it?", image="https://images.unsplash.com/photo-1695088957322-e253097aa640?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=True))
    artworks.append(Artwork(user_id=6, title="Spring Rolls", description="Crispy Vietnamese Spring rolls!", image="https://images.unsplash.com/photo-1577859584099-38d38a4aacb5?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=80.00, preview=False))
    artworks.append(Artwork(user_id=6, title="As American as Apple Pie", description="Can you think of anything better??.", image="https://images.unsplash.com/photo-1616953882439-4765aafc8ef1?q=80&w=1827&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=180.00, preview=True))
    artworks.append(Artwork(user_id=6, title="Upscaled", description="Upscale bar food plates.", image="https://images.unsplash.com/photo-1695606453151-e58a72d04d28?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=140.00, preview=False))
    artworks.append(Artwork(user_id=6, title="VSB", description="Vegetable Side Bowl", image="https://images.unsplash.com/photo-1695606452846-b71f5936dcf7?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=100.00, preview=True))

    artworks.append(Artwork(user_id=7, title="Harmony", description="The beauty of a piano.", image="https://images.unsplash.com/photo-1680023477795-6c672e79545c?q=80&w=1925&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=160.00, preview=True))
    artworks.append(Artwork(user_id=7, title="Jam Session", description="For those sessions you just want to jam with friends.", image="https://images.unsplash.com/photo-1527632122372-d846578e23c3?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=70.00, preview=False))
    artworks.append(Artwork(user_id=7, title="Concertscape", description="The dreamscape found in concerts.", image="https://images.unsplash.com/photo-1577648884063-1d3d1477b8a7?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=190.00, preview=True))
    artworks.append(Artwork(user_id=7, title="The Chosen One", description="A moment of zen found before the chaos.", image="https://images.unsplash.com/photo-1578559117711-f80f34af785f?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=False))
    artworks.append(Artwork(user_id=7, title="Lights, Camera, Rave!", description="Do you guys think these artists just press play and make up the rest?", image="https://images.unsplash.com/photo-1574154945982-0c7aff5adaef?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=85.00, preview=True))

    artworks.append(Artwork(user_id=8, title="Motherboard", description="i was cleaning my laptop and i found it wonderful. see ya.", image="https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=110.00, preview=True))
    artworks.append(Artwork(user_id=8, title="Coding Nightmares", description="Do you guys ever have nightmares but in code? Yeah me either...", image="https://images.unsplash.com/photo-1516259762381-22954d7d3ad2?q=80&w=1778&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=80.00, preview=False))
    artworks.append(Artwork(user_id=8, title="Obsolete", description="A blast from the past but still relevant?.", image="https://images.unsplash.com/photo-1663770114127-4f61cb62b56d?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=170.00, preview=True))
    artworks.append(Artwork(user_id=8, title="Sleep Coding", description="When you want to get mad at the cause of the bugs but the cause is you.", image="https://images.unsplash.com/photo-1456406644174-8ddd4cd52a06?q=80&w=1736&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=130.00, preview=False))
    artworks.append(Artwork(user_id=8, title="IRL Zoom Session", description="Which came first? Social interaction in person or Zoom?", image="https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=90.00, preview=True))

    artworks.append(Artwork(user_id=9, title="Between a Rock and a Peaceful Place", description="It's all about perspective.", image="https://images.unsplash.com/photo-1677741447831-fb66b7294a40?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=140.00, preview=True))
    artworks.append(Artwork(user_id=9, title="Head of the Class", description="When you have to decide whether you should be taking photos or doing the poses.", image="https://images.unsplash.com/photo-1677741447985-da1d90c00742?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=75.00, preview=False))
    artworks.append(Artwork(user_id=9, title="A Moment of Zen", description="Just take a deep breath and keep going.", image="https://images.unsplash.com/photo-1677741447312-cc3211e9253e?q=80&w=1915&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=200.00, preview=True))
    artworks.append(Artwork(user_id=9, title="Healthy Eats", description="You are what you eat and this looks beautiful.", image="https://images.unsplash.com/photo-1478145046317-39f10e56b5e9?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=150.00, preview=False))
    artworks.append(Artwork(user_id=9, title="Running Photographers Club", description="In all reality, the only thing coming out of this club is blur.", image="https://images.unsplash.com/photo-1634085398114-5091e0d9ed9e?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=True))

    artworks.append(Artwork(user_id=10, title="Clapper", description="Nine takes later and we're still improving.", image="https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=1718&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=160.00, preview=True))
    artworks.append(Artwork(user_id=10, title="Catch Me If You Can", description="With this amount of gear, who couldn't?", image="https://images.unsplash.com/photo-1614270248176-3fdd040ac6e7?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=90.00, preview=False))
    artworks.append(Artwork(user_id=10, title="Personal Confession", description="Working on a music video about personal confessions.", image="https://images.unsplash.com/photo-1619286463995-8a38630a5efd?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=190.00, preview=True))
    artworks.append(Artwork(user_id=10, title="Electronic Clapper", description="If it ain't broke, make an electronic version of it.", image="https://images.unsplash.com/photo-1515634928627-2a4e0dae3ddf?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=130.00, preview=False))
    artworks.append(Artwork(user_id=10, title="Red Dragon", description="I'm pretty sure this camera costs more than everything I own combined.", image="https://images.unsplash.com/photo-1518929773866-ffd0b4500ff1?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=125.00, preview=True))
   
    artworks.append(Artwork(user_id=11, title="Nutrients of Life", image="https://images.unsplash.com/photo-1492496913980-501348b61469?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=True))
    artworks.append(Artwork(user_id=11, title="One World", image="https://images.unsplash.com/photo-1570358934836-6802981e481e?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=85.00, preview=False))
    artworks.append(Artwork(user_id=11, title="Power of Life in the Palm of Our Hands", image="https://images.unsplash.com/photo-1523810192022-5a0fb9aa7ff8?q=80&w=1734&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=200.00, preview=True))
    artworks.append(Artwork(user_id=11, title="Life in the Smallest Places", image="https://images.unsplash.com/photo-1627213373335-26c0417ac50d?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=150.00, preview=False))
    artworks.append(Artwork(user_id=11, title="Love & Protect", image="https://images.unsplash.com/photo-1555435434-d2b5fa602793?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=95.00, preview=True))

    artworks.append(Artwork(user_id=12, title="Before the Cross", description="A few moments before this young gentlemen assisted in the game-winning goal.", image="https://images.unsplash.com/photo-1631495635307-e9ec1e58d8df?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=130.00, preview=True))
    artworks.append(Artwork(user_id=12, title="Two Minute Drill", description="Two minutes left to win the game.", image="https://images.unsplash.com/photo-1623196152574-340255cb1c89?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=75.00, preview=False))
    artworks.append(Artwork(user_id=12, title="Take the Jump", description="The most intimidating jump on the track.", image="https://images.unsplash.com/photo-1558807769-d642ad6af1a0?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=180.00, preview=True))
    artworks.append(Artwork(user_id=12, title="Two For One", description="Met these two snowboarding and couldn't pass up the chance for a photoshoot.", image="https://images.unsplash.com/photo-1617939533073-6c94c709370c?q=80&w=1744&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=110.00, preview=False))
    artworks.append(Artwork(user_id=12, title="Buckshot", description="The beauty of the Rome SDS.", image="https://images.unsplash.com/photo-1617939533087-b7f5567105bf?q=80&w=1886&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=True))

    artworks.append(Artwork(user_id=13, title="The Old Road", description="The old familiar winter road, painted with oil paint.", image="https://images.unsplash.com/photo-1586536672467-686dd4fabacb?q=80&w=1900&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=140.00, preview=True))
    artworks.append(Artwork(user_id=13, title="Counting Sheep", description="Herding sheep through town, painted with oil paint.", image="https://images.unsplash.com/photo-1578301978693-85fa9c0320b9?q=80&w=1919&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=95.00, preview=False))
    artworks.append(Artwork(user_id=13, title="Arming the Cannons", description="Painted with oil paint.", image="https://images.unsplash.com/photo-1582561424760-0321d75e81fa?q=80&w=1989&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=220.00, preview=True))
    artworks.append(Artwork(user_id=13, title="Up the Creek Without a Paddle", description="I love drawing water scenes, painted with oil paint.", image="https://images.unsplash.com/photo-1578926375605-eaf7559b1458?q=80&w=1963&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=160.00, preview=False))
    artworks.append(Artwork(user_id=13, title="Life on the Prairie", description="This is my favorite I've done, painted with oil paint.", image="https://images.unsplash.com/photo-1586537049236-b212dc756931?q=80&w=1919&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=130.00, preview=True))

    artworks.append(Artwork(user_id=14, title="Hong Kong", description="hong Kong Island, Taken on Canon 8D10", image="https://images.unsplash.com/photo-1525856331869-3d345509b9fb?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=180.00, preview=True))
    artworks.append(Artwork(user_id=14, title="Ninh Binh, Vietnam", description="This is one of the most spectacular views.", image="https://images.unsplash.com/photo-1489258205848-4b9651de165b?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=120.00, preview=False))
    artworks.append(Artwork(user_id=14, title="Fiji", description="Taken on Nikon D3400", image="https://images.unsplash.com/photo-1593078875274-446ed98bae67?q=80&w=1886&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=90.00, preview=True))
    artworks.append(Artwork(user_id=14, title="Rome", description="An iconic image of the beauty of Rome streets. Nikon D3400", image="https://images.unsplash.com/photo-1598258500419-5d7895465a20?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=200.00, preview=False))
    artworks.append(Artwork(user_id=14, title="Kyoto", description="Taken in Kyoto, Japan. Canon 8D10", image="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=110.00, preview=True))

    artworks.append(Artwork(user_id=15, title="The Power of Three", image="https://images.unsplash.com/photo-1615222443417-6d76586644a9?q=80&w=1905&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=130.00, preview=True))
    artworks.append(Artwork(user_id=15, title="No Photos Please", image="https://images.unsplash.com/photo-1523398002811-999ca8dec234?q=80&w=1905&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=95.00, preview=False))
    artworks.append(Artwork(user_id=15, title="Flower Bride", image="https://images.unsplash.com/photo-1625798368112-b31baa814de7?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=200.00, preview=True))
    artworks.append(Artwork(user_id=15, title="Hair", description="Hair by Carolyn Jayun Gahan model @george__bones Makeup @rebeccarichards", image="https://images.unsplash.com/photo-1601597565151-70c4020dc0e1?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=150.00, preview=False))
    artworks.append(Artwork(user_id=15, title="White on Pink", image="https://plus.unsplash.com/premium_photo-1664453546973-0fff543557bd?q=80&w=1886&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", price=95.00, preview=True))
    
    return artworks