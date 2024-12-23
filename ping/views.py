from django.shortcuts import render

# Create your views here.

from django.http import Http404

def home(request):
    # Render the home page where games are listed
    return render(request, 'ping/home.html')

def game_page(request, game_name):
    # Map game names to their data, including servers
    games = {
        'rainbow-six-siege': {
            'title': 'Rainbow Six Siege',
            'article': 'Rainbow Six Siege is a tactical shooter game by Ubisoft.',
            'servers': {
                'UAE': '20.233.42.17',
                'Singapore': '20.198.169.169',
                'Hong Kong': '13.75.41.5',
                'Japan': '52.185.166.150',
                'Europe West': '168.63.103.13',
                'US West': '13.64.199.156',
                'Eu-Central-1': '18.185.132.151',
            },
        },
        'csgo': {
            'title': 'CSGO',
            'article': 'Counter-Strike: Global Offensive is a popular first-person shooter.',
            'servers': {
                'EU Server': 'https://eu.csgo.server',
                'US Server': 'https://us.csgo.server',
            },
        },
        'browser': {
            'title': 'Browser',
            'article': 'acticle of the browser',
            'servers': {
                'Google': 'www.google.com',
                'Bing': 'www.bing.com',
            },
        },
    }

    # Check if the game exists in the dictionary
    game_data = games.get(game_name)
    if not game_data:
        raise Http404("Game not found")

    # Dynamically construct the template path based on the game name
    template_path = f'ping/{game_name}.html'

    # Render the game-specific template with the data
    return render(request, template_path, {'game': game_data,
        'games': games,  # Pass the full list of games for the dropdown
        'current_game': game_name  # Pass the current game name to the template
        })

# def home(request):
#     return render(request, 'ping/index.html')


# def get_server_groups(request):
#     # Define the server groups
#     server_groups = {
#         "game1": {
#             "UAE": "20.233.42.17",
#             "Singapore": "20.198.169.169",
#             "Hong Kong": "13.75.41.5",
#             "Japan": "52.185.166.150",
#             "Europe West": "168.63.103.13",
#             "US West": "13.64.199.156",
#             "Eu-Central-1": "18.185.132.151",
#         },
#         "game2": {
#             "US East": "https://useast.example.com",
#             "US West": "https://uswest.example.com",
#             "EU Central": "https://eucentral.example.com",
#         },
#         "game3": {
#             "South America (Brazil)": "https://brazil.example.com",
#             "China (Hong Kong)": "https://hongkong.example.com",
#             "EU West": "https://euwest.example.com",
#         },
#     }
#     return JsonResponse(server_groups)


