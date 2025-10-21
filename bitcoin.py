import requests
import sys

def main():
    x=read_command_line_input()
    price=get_bitcoin_price()
    print(f"${x*price:,.4f}")

def read_command_line_input():
    try:
        return(float(sys.argv[1])) #reading the first argument after file name in command line
    except IndexError:
        return(sys.exit("Missing command-line argument"))
    except ValueError:
        return(sys.exit("Command-line argument is not a number"))
#Avoid errors like absence of argument and wrong argument and exits

def get_bitcoin_price(): #bitcoin price recuperation fonction
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=2d0a20dd65419a45cb179ea9c3d7cb494d1546bb92d31ec6b2fda89689bfd816")
        data=response.json()
        #data contain all data extracted (timestamp + dictionary 'data') from this URL thank to .json and we can select
        #the one we want in the 'data' dictionary :
        return(float(data['data']['priceUsd']))
        #here we want the value "priceUSD" wich is the key for the actual price of the bitcoin"
    except requests.RequestException:
        sys.exit('Request failed')

main()
