#Datapane will be used create a personal report for this code. Sign up on Datapane to get the token and sign in.

from IPython.display import Javascript

def window_open(url):
    display(Javascript('window.open("{url}");'.format(url=url)))


window_open('https://datapane.com/home')

token = input('Insert your token after signing in Datapane ')
print('Your token is', token)

!datapane login --server=https://datapane.com/ --token=$token