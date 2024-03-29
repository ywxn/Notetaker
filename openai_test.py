# this is how the openai api call needs to be structured apparently lol
from openai import OpenAI

# read the OPENAI_API_KEY file to get the api_key
with open("OPENAI_API_KEY", "r") as file:
    api_key = file.read().strip()

prompt = """
I was a collector as a child. Growing up in Portland, Oregon, we would frequent the Oregon coast, and I would gather agates in the sand with my brother. My mother liked road trips short and long, and I gathered metal pins at theme parks and antique stores. I was a Teenage Mutant Ninja Turtles fan, and had every action figure, including every variant of April O’Neil. I would stop in my local comic shops to add the latest Flash, Spawn, Ghost Rider, and Savage Dragon, and the occasional manga. And my collection of Nintendo, Game Boy, and Super Nintendo games was the envy of my small group of friends and a magnet for our sleepovers.

On paper, I was media-obsessed hoarder, but the reality was that most of my compulsion to was about my father. He was a true collector, finding the rarest baseball and basketball cards, dragging us to trading card shows to hunt and barter, assembling pristine collections of duck stamps that he proudly displayed all across his small apartment. I say his because I had no real home: joint custody and divorce meant that my home was my backpack, always nomadic. Collecting was my way of trying to be closer to my father, who only really ever seemed interested in completing his collections. My brother and I collected so that he might be interested in us.

I was more like my mother. She was a compulsive organizer, always making sure everything was in its place. Part of that was purging, ruthlessly editing down photo albums and mementos to the sparest of reminders of the past and aggressively selling and donating the objects in our home the moment they had no purpose. Her home was a snapshot of our practical needs and a selective memory of key moments she wanted to remember. This was the way I wanted to live; object-free, memory free. My collections were a burden to be discarded.

And so when I left home for college, I abandoned nearly everything. My father sold my action figures, my comic books, my games. I reduced every captured moment of my childhood into a small 5 gallon storage bin of paper and trinkets. That separation from the objects of my adolescence was a claim to freedom and a severing of memories. I wanted to look forward, and that meant erasing my past.

The purge became a habit, particularly as I tried to keep my gender identity secret, especially from myself. I would carefully orchestrate separate devices and profiles of web browsing and digital documents representing the thinnest trace of my exploration into the underworld of trans experiences online. And then I would delete it a few weeks later, pretending that it had never happened. I curated the smallest possible set of gender affirming clothing that I carefully hid from myself and others, and then in fleeting moments of privacy as a young married parent, wear them, cry, and then toss them in a distant public trash can. As I made new memories with my daughter and ex, I would surgically edit down hundreds of hours of video to a short one hour DVD, always silent behind the camera, trying to erase the fact that I was ever there.

Coming out as trans was the biggest purge of all. Across months, I deleted hundreds of internet accounts, erased my name everywhere I could on the internet, hid away an archive of thousands of digital photos with my triggering old face, trying desperately to remove any evidence of my old self ever existing. The purge of the old me was so thorough, I lost my credit history for a year, unable to take out a car loan; I was mistaken by my colleagues at conferences as the wife of my former self. Liberating myself from my gender prison was an act of creation, but also destruction.

Purging, however, has become harder. As a young adult, it was an act of burning, recycling, composting, or trashing paper, because most of the traces of me were material. These were acts of total agency, as they were paper I had in my position, and that no one else could find, see, or recover if I destroyed them thoroughly enough. But as the internet took hold as our primary store, purging became an act of begging. Some websites would gladly oblige. Others asked for proof that I was me. Others refused. Some said “happily”, and yet continue to dead name me to do this day, or eagerly recommend images from my past that I thought I’d deleted. And even if I did delete them, my friends and family carry with them their own collections, traces of former me intricately woven through their digital archives. Mail will forever arrive with my deadname, my wife crossing it out with a sharpie every evening before I sift through it for bills.

There’s a concept I learned early in my research called data dependency. It’s the simple idea of a causal relationship between two statements in a computer program. Say, for example, a program has these three lines of code:

let price = 5;
let quantity = 10
let charge = price * quantity

Here, charge has a data dependency on two variables, price and quantity. This notion is helpful for reasoning about how the behavior of a program is shaped by data and other computation that computes data, and a central part of reasoning about whether programs are correct, why they behave the way they do, and what they’ll do in response to new data. Data dependencies in computer programs are massive networks of connections between logic, connected by data values.

But the internet, essentially a massive network of traces of the distant and recent past, introduces a new kind of data dependency that reaches far beyond the logic of code. Our algorithms, whether symbolic recommendation algorithms or probabilistic prediction engines, are hungry for our history, and data dependent on it. As products and services have tried to extract value out of our pasts, our digital lives are predominantly shaped not by what might be, but what has been. I get music that past me might like based on what I’ve listened to for the past 20 years, but not something that would suprise or change me. I get search results that are what others have found useful, but not the unexamined fringes of the web that might make me see the world anew. I get restaurants that history has rewarded with algorithmic recommendations, not unknown, offline hidden gems. Being on today’s internet means living in a facsimile of our individual and collective pasts, forever trapped in a lagging silhouette of past cultures. Deep learning, and its derivative of the moment, large language models, promise that we’ll never have to leave the past, and never create a new future.

Being a new person in this digital world, means leaving it. The spaces I’ve found where I feel freest from my past are the strictly organic ones, where I am just a person with a body and a mind, only carrying with me my thoughts, knowledge, and personality, and only encountering others and their thoughts, knowledge, and personalities. We encounter each other as complex bundles of endless surprise, accessed only through fuzzy, unreliable wetware of recall and the ambiguous beauty of language. In these untethered spaces, I see myself independent from my past and instead through the rich lens of others’ minds.

Creating new things also means leaving the digital world. The art I’ve loved most over the past several years has been that derived from separation. Adrianne Lenker recorded songs, for example, in a one-room cabin in the Massachusetts mountains during lockdowns, and captured something pure, human, and singular. It felt truly new, and deeply grounded in her own internal data dependencies of memory and experience, but unencumbered by the internet’s heavy weight of algorithmic, data-driven cultural extrusions. Bo Burnham’s Inside, for all its pop culture whiteness, felt like seeing his mind from the inside out, and only felt possible because it recursed on itself and a room, not a billion traces of the past.

I think about my purging, and this art, and the web’s recent obsession with generative AI, and feel the weight of a billion parameters modeling the past of the public web. I know those models have every word I’ve shared on the web, a million copies of my deadname, my old face a thousand times over, and my old ideas and beliefs, forever enshrined for the connected subset of humanity to slowly dismantle their own humanity. And yet, here I am, sharing these words, only accelerating that tragic future, nudging tomorrow’s corporate memo toward solemnity.

When I talk to youth about these things, they have trouble seeing our current world as inhuman, because they have not seen a world that is human. I tell them stories where severance from the past was their choice and they were free to become something new without being surveilled. But they hear my stories as a kind of fantasy or science fiction, something that might have existed in another distant world, or might only exist int the distant future. For now, they accept, and sometimes celebrate, that their humanity is the grist for tomorrow’s TikTok recommendation and B- essay. And just like the corporate strategy would have them believe, they come to believe that’s all they’re worth.
"""

client = OpenAI(api_key=api_key)

completion = client.completions.create(
    model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=200
)
print(completion.choices[0].text)
print(dict(completion).get("usage"))
print(completion.model_dump_json(indent=2))
