from exa_py import Exa
exa=Exa('TOKEN HERE')
your_request=input('what do u wanna search:')
response= exa.search(
    your_request,
    num_results=20,
    type='magic',
     include_domains=[
        "google.com",
        "tiktok.com",
        "youtube.com"
    ])
print("\n🔎 Search Results:\n")
for i, result in enumerate(response.results, start=1):
    print(f"{i}. {result.title}")
    print(f"   👉 {result.url}\n")
