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
                'West US': 'https://s9westus.blob.core.windows.net/public/latency-test.json',
                'Central US': 'https://s9centralus.blob.core.windows.net/public/latency-test.json',
                'South Central US': 'https://s9southcentralus.blob.core.windows.net/public/latency-test.json',
                'East US': 'https://s9eastus.blob.core.windows.net/public/latency-test.json',
                'Brazil South': 'https://s9brazilsouth.blob.core.windows.net/public/latency-test.json',
                'South Africa North': 'https://s9southafricanorth.blob.core.windows.net/public/latency-test.json',
                'UAE North': 'https://s9uaenorth.blob.core.windows.net/public/latency-test.json',
                'North Europe': 'https://s9northeurope.blob.core.windows.net/public/latency-test.json',
                'West Europe': 'https://s9westeurope.blob.core.windows.net/public/latency-test.json',
                'Eu-Central-1': 'https://ec2.eu-central-1.amazonaws.com/ping',
                'East Asia': 'https://s9eastasia.blob.core.windows.net/public/latency-test.json',
                'Southeast Asia': 'https://s9southeastasia.blob.core.windows.net/public/latency-test.json',
                'Japan East': 'https://s9japaneast.blob.core.windows.net/public/latency-test.json',
                'Australia East': 'https://s9australiaeast.blob.core.windows.net/public/latency-test.json',
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