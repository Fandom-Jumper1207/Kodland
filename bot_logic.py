import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for _ in range(pass_length):
        password += random.choice(elements)
    return password

# --- MINI-GAMES ---
def gen_coin_flip():
    return random.choice(["Heads!", "Tails!"])

def gen_roll_dice():
    return f"You rolled a {random.randint(1, 6)}!"

# --- JOKES & FUN ---
def gen_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why did the math book look sad? Because it had too many problems!",
        "Why can't your nose be 12 inches long? Because then it would be a foot!",
        "What do you call a fake noodle? An impasta!",
        "Why did the skeleton go to the party alone? He had no body to go with him!",
        "What do you call a sleeping bull? A bulldozer!",
        "What do you call a factory that makes okay products? A satisfactory!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you call a belt made of watches? A waist of time!",
        "Why couldn't the pony sing a lullaby? Because she was a little hoarse!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why do seagulls fly over the ocean? Because if they flew over the bay, they’d be bagels!"
    ]
    return random.choice(jokes)

def gen_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The best way to predict the future is to invent it. - Alan Kay",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "It always seems impossible until it's done. - Nelson Mandela",
        "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
        "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
        "Happiness depends upon ourselves. - Aristotle",
        "Turn your wounds into wisdom. - Oprah Winfrey",
        "Do what you can, with what you have, where you are. - Theodore Roosevelt",
        "Act as if what you do makes a difference. It does. - William James",
        "The mind is everything. What you think you become. - Buddha"
    ]
    return random.choice(quotes)

def gen_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts and blue blood.",
        "A day on Venus is longer than a year on Venus.",
        "Wombat poop is cube-shaped.",
        "Sea otters hold hands while sleeping so they don't float away from each other.",
        "Cows have best friends and get stressed when they are separated.",
        "A flock of flamingos is called a 'flamboyance'.",
        "The Eiffel Tower can grow up to 15 cm taller during the summer due to thermal expansion.",
        "Sharks existed before trees; sharks are over 400 million years old, while trees evolved around 350 million years ago.",
        "Butterflies taste with their feet.",
        "A single cloud can weigh over one million pounds.",
        "Sloths can hold their breath longer than dolphins can (up to 40 minutes).",
        "North Korea and Finland are separated by only one country (Russia).",
        "Polar bear skin is black, and their fur is transparent, not white."
    ]
    return random.choice(facts)

def gen_riddle():
    riddles = [
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? (Answer: An echo)",
        "I’m tall when I’m young, and I’m short when I’m old. What am I? (Answer: A candle)",
        "What has keys but can’t open locks? (Answer: A piano)",
        "What has a heart that doesn’t beat? (Answer: An artichoke)",
        "What comes once in a minute, twice in a moment, but never in a thousand years? (Answer: The letter 'M')",
        "The more of this there is, the less you see. What is it? (Answer: Darkness)",
        "What has to be broken before you can use it? (Answer: An egg)",
        "What gets wetter and wetter the more it dries? (Answer: A towel)",
        "What can travel all around the world while staying in a corner? (Answer: A stamp)",
        "What has hands, but can’t clap? (Answer: A clock)",
        "What belongs to you, but other people use it more than you do? (Answer: Your name)",
        "David’s parents have three sons: Snap, Crackle, and what’s the name of the third son? (Answer: David)",
        "What has many keys, but can't open a single door? (Answer: A piano / Computer keyboard)",
        "What has a head and a tail, but no body? (Answer: A coin)",
        "Where does today come before yesterday? (Answer: In a dictionary)"
    ]
    return random.choice(riddles)

def gen_science_pun():
    puns = [
        "I told a chemistry joke, but there was no reaction.",
        "Why did the physics teacher break up with the biology teacher? There was no chemistry.",
        "I would tell you a joke about sodium, but Na.",
        "Why can't you trust an atom? Because they make up everything!",
        "What do you call an educated tube? A graduated cylinder.",
        "Did you hear potassium and oxygen went on a date? It went OK.",
        "Why did the biologist go on a date with a microscope? He wanted to find a closer connection.",
        "Organic chemistry is difficult. Those who study it have alkynes of trouble.",
        "What is a chemist's favorite fast food side dish? Fission chips.",
        "Argon walks into a bar. The bartender says, 'We don't serve noble gases here!' Argon doesn't react.",
        "What do you do with a dead chemist? Barium!",
        "Why are parallel lines so lonely? Because they never meet.",
        "How do you organize a space party? You planet!",
        "Why did the tectonic plates split up? It wasn't their fault!",
        "Light travels faster than sound. That's why some people appear bright until you hear them speak."
    ]
    return random.choice(puns)

# --- NINJAGO ---
def gen_ninjago_quote():
    quotes = [
        "The greatest power is the power of knowledge. - Sensei Wu",
        "A true ninja is not measured by the number of enemies defeated, but by the strength of their character. - Lloyd",
        "Courage is not the absence of fear, but the triumph over it. - Kai",
        "The path to greatness is paved with perseverance and determination. - Nya",
        "A ninja's strength lies not in their weapons, but in their heart. - Cole",
        "Ninja never give up, even when the odds are against them. - Zane",
        "Ninja never quit! - Sensei Wu",
        "Ninja GO! - Lloyd",
        "I demand all the candy in town!!! - Lloyd",
        "I am a ninja, and you are wearing makeup! - Lloyd",
        "Iron sharpens iron, and brothers sharpen each other. - Sensei Wu",
        "A ninja's greatest weapon is their mind. - Lloyd",
        "The greatest victory is the one that requires no battle. - Sensei Wu",
        "The best way to defeat your enemies is to make them your friends. - Sensei Wu",
        "Never put off until tomorrow what you can do today. - Sensei Wu"
    ]
    return random.choice(quotes)

def gen_ninjago_fact():
    facts = [
        "Ninjago is a fictional world created by LEGO, featuring a group of ninja heroes who protect their land from evil forces.",
        "The main characters in Ninjago are Lloyd, Kai, Jay, Zane, Cole, and Nya.",
        "Ninjago has been adapted into a popular animated TV series called 'LEGO Ninjago: Masters of Spinjitzu'.",
        "The Ninjago series has been running since 2011 and has multiple seasons and spin-offs.",
        "Ninjago has a rich lore that includes ancient prophecies, powerful artifacts, and legendary battles.",
        "Zane was the very first character designed for the theme before the show even started!",
        "Jay's full name is Jay Walker (formerly Jay Gordon).",
        "The Green Ninja prophecy was originally meant to reveal Kai as the Green Ninja in early concept stages.",
        "Lord Garmadon was originally created as the First Spinjitzu Master's eldest son who got corrupted by Great Devourer venom.",
        "The Four Elemental Weapons of Spinjitzu are the Sword of Fire, Scythe of Quakes, Nunchucks of Lightning, and Shurikens of Ice.",
        "Nya was originally the Samurai X before unlocking her elemental power over Water.",
        "Sensei Wu's favorite beverage is tea, and he even owned a tea shop called 'Steeper Wisdom'.",
        "Cole's favorite food is cake, a recurring joke throughout the entire series.",
        "Pixal's name stands for 'Primary Interactive X-ternal Assistant Life-form'.",
        "The realm of Ninjago is actually just one of Sixteen Realms in the Ninjago multiverse."
    ]
    return random.choice(facts)

def gen_ninjago_riddle():
    riddles = [
        "I am a ninja's best friend, but I am not alive. What am I? (Answer: A weapon)",
        "I can be found in the shadows, but I am not a ghost. What am I? (Answer: A ninja)",
        "I can be fast and silent, but I am not a cat. What am I? (Answer: A ninja)",
        "I can be strong and brave, but I am not a soldier. What am I? (Answer: A ninja)",
        "I can be skilled and wise, but I am not a teacher. What am I? (Answer: A ninja)",
        "I control the flames and wear red, who am I? (Answer: Kai)",
        "I spin through the air and wield the power of lightning in blue, who am I? (Answer: Jay)",
        "I am made of metal, ice flows through my heart, yet I am the kindest brother. Who am I? (Answer: Zane)",
        "I love cake and wield the strength of the earth in black, who am I? (Answer: Cole)",
        "I am the Master of Water and built Samurai X, who am I? (Answer: Nya)",
        "I was once the Dark Lord's son, but became the legendary Green Ninja, who am I? (Answer: Lloyd)",
        "I drink tea and teach the ninja how to spin, who am I? (Answer: Sensei Wu)",
        "I am four-armed, dark, and once ruled the Underworld, who am I? (Answer: Lord Garmadon)",
        "What technique lets a ninja spin so fast they create a tornado of elemental energy? (Answer: Spinjitzu)",
        "What golden ancient weapons were forged in the Temple of Light to create Ninjago? (Answer: The Golden Weapons of Spinjitzu)"
    ]
    return random.choice(riddles)

def gen_ninjago_pun():
    puns = [
        "Why did the ninja go to school? To improve his 'karate' skills!",
        "What do you call a ninja who loves to garden? A 'plant'-er of stealth!",
        "Why did the ninja bring a ladder to the dojo? To reach new heights in his training!",
        "What do you call a ninja who can sing? A 'karaoke'-te master!",
        "Why did the ninja refuse to fight in the rain? He didn't want to get 'wet' behind the ears!",
        "Why is Kai always so calm under pressure? Because he knows how to keep his cool, even when he's fired up!",
        "How does Jay like his electricity? Shockingly fast!",
        "Why did Zane break down during math class? He had an error in his code!",
        "Why is Cole the strongest ninja? Because his training is rock-solid!",
        "What is Sensei Wu’s favorite kind of martial art? Tae-Kwon-Tea!",
        "Why couldn't Garmadon win at hide and seek? Because his evil plans were always spotted!",
        "What do Ninjago dragons eat for lunch? Fire-crackers!",
        "How do the ninja order food? Fast and stealthy!",
        "Why did the Snake tribe get lost? They lost their scale!",
        "What do you call a Ninja who loves winter? A Spin-jitsu-skier!"
    ]
    return random.choice(puns)

def gen_math_pun():
    puns = [
        "Why was the equal sign so humble? Because he wasn't less than or greater than anyone else.",
        "Why did the student do multiplication problems on the floor? The teacher told him not to use tables.",
        "Why was the math book sad? Because it had too many problems.",
        "Why did the two fours skip lunch? They already eight.",
        "Why was the fraction worried about marrying the decimal? Because he would have to convert.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Are monsters good at math? Not unless you Count Dracula!",
        "Why shouldn't you write math papers with a broken pencil? Because it's point-less!",
        "What did the triangle say to the circle? 'You're pointless!'",
        "Why was the obtuse triangle always upset? Because it was never right!",
        "How do you solve any equation? With a pencil and a lot of power-der!",
        "Why did the student wear glasses to math class? To improve division!",
        "What do you call dudes who love math? Alge-bros!",
        "Why did 7 eat 9? Because you're supposed to eat 3 square meals a day!",
        "Why was the math lecture so long? The professor kept going off on a tangent!"
    ]
    return random.choice(puns)

def gen_prompt():
    prompts = [
        "Write a story about a time-traveling detective.",
        "Describe a world where humans can communicate with animals.",
        "Imagine a society where everyone has a superpower, but they can only use it once a year.",
        "Write a poem about the changing seasons.",
        "Create a dialogue between two characters who are stranded on a deserted island.",
        "Imagine a world where dreams can be recorded and played back like movies.",
        "Write a story about a character who discovers they have the ability to control time.",
        "Write a story starting with the sentence: 'The lights went out, but the shadows kept moving.'",
        "Describe a cozy coffee shop owned by a friendly dragon.",
        "Write a scene where two rival spies accidentally sit at the same dinner table.",
        "Imagine a universe where gravity changes direction every hour.",
        "Write a story about an old lighthouse keeper who finds a glowing bottle on the shore.",
        "Describe a hidden city built inside a colossal hollow tree.",
        "Write about a character who receives letters mailed from 50 years in the future.",
        "Create an adventure about a group of kids who discover their school library has a secret floor."
    ]
    return random.choice(prompts)

def gen_movie_quote():
    quotes = [
        "May the Force be with you. - Star Wars",
        "I'm going to make him an offer he can't refuse. - The Godfather",
        "Here's looking at you, kid. - Casablanca",
        "You can't handle the truth! - A Few Good Men",
        "To infinity and beyond! - Toy Story",
        "I'll be back. - The Terminator",
        "There's no place like home. - The Wizard of Oz",
        "Why so serious? - The Dark Knight",
        "Houston, we have a problem. - Apollo 13",
        "E.T. phone home. - E.T. the Extra-Terrestrial",
        "You're gonna need a bigger boat. - Jaws",
        "Keep your friends close, but your enemies closer. - The Godfather Part II",
        "Fasten your seatbelts. It's going to be a bumpy night. - All About Eve",
        "Show me the money! - Jerry Maguire",
        "Carpe diem. Seize the day, boys. Make your lives extraordinary. - Dead Poets Society"
    ]
    return random.choice(quotes)

def gen_marvel_quote():
    quotes = [
        "I can do this all day. - Captain America",
        "With great power comes great responsibility. - Spider-Man",
        "I am Iron Man. - Iron Man",
        "We are Groot. - Groot",
        "I am inevitable. - Thanos",
        "I love you 3000. - Tony Stark",
        "Mr. Stark, I don't feel so good. - Peter Parker",
        "Dumbest day of my life. - Peter Parker",
        "DUDE! - Peter Parker",
        "You are spider-man. - MJ",
        "You know that really old movie.... - Peter Parker",
        "I hit it with a hammer. - Thor",
        "Puny god. - Hulk",
        "Wakanda Forever! - Black Panther",
        "Part of the journey is the end. - Tony Stark"
    ]
    return random.choice(quotes)
