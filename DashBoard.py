import DomainSearch
import TokenGenerator
import tkinter as tk

window = tk.Tk()
#Will Eventually be deprecated and replaced by a user-interface class

#your user id and secret can be found in your account page at snov.io
#this program requires a snov.io account to run.

# user_id= '20b2453e33887343c8c67d3d98b8f39e'
# secret= '9378dfdb3be0d1063925641187e5e8ab'
# domain = '99cave.com'

def handle_start():
    user_id = user_id_entry.get()
    secret = api_secret_entry.get()
    domain = target_domain_entry.get()
    
    token = TokenGenerator.get_access_token(user_id,secret)
    
    print(DomainSearch.get_domain_search(domain,token))
          
user_id_label = tk.Label(text='Enter your user_id')
user_id_entry = tk.Entry(width=50)
user_id_label.pack()
user_id_entry.pack()

api_secret_label = tk.Label(text='Enter your api_secret')
api_secret_entry = tk.Entry(width=50)
api_secret_label.pack()
api_secret_entry.pack()

target_domain_label = tk.Label(text='Enter the target domain')
target_domain_entry = tk.Entry(width=50)
target_domain_label.pack()
target_domain_entry.pack()

start_search_button = tk.Button(text='Start Search', command=handle_start)
start_search_button.pack()

output = tk.Text()
output.pack()

domain = 'jogger.com'

