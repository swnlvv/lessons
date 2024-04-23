search=input()
wo_first_ampersand=search.split('=')[1]
wo_second_ampersand=wo_first_ampersand.split('&')[0]

print(wo_second_ampersand)

