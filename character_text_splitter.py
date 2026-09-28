from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter

google_text = """Google began in January 1996 as a research project by Larry Page and Sergey Brin while they were both PhD students at Stanford University in California, USA.

The project initially involved an unofficial "third founder", Scott Hassan,the original lead programmer who wrote much of the code for the original Google Search engine, but he left before Google was officially founded as a company;

Hassan went on to pursue a career in robotics and founded the company Willow Garage in 2006."""


# splitter1 = CharacterTextSplitter(
#     separator=" ",  # Default separator. Other options include ["\n\n", "\n", ". ", " ", ""]
#     chunk_size=100,
#     chunk_overlap=0
# )

# chunks1 = splitter1.split_text(google_text)
# for i, chunk in enumerate(chunks1, 1):
#     print(f"Chunk {i}: ({len(chunk)} chars)")
#     print(f'"{chunk}"')
#     print()


# Example 2: RecursiveCharacterTextSplitter fixes this
print("\n" + "=" * 60)
print("2. RECURSIVE CHARACTER TEXT SPLITTER SOLUTION")
print("=" * 60)

recursive_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ". ", " ", ""],  # Multiple separators
    chunk_size=100,
    chunk_overlap=0
)

chunks2 = recursive_splitter.split_text(google_text)
print(f"Same problem text, but with RecursiveCharacterTextSplitter:")
for i, chunk in enumerate(chunks2, 1):
    print(f"Chunk {i}: ({len(chunk)} chars)")
    print(f'"{chunk}"')
    print()
