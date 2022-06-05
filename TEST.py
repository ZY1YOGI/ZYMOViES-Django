from tmdbv3api import TMDb, Search

tmdb = TMDb()

tmdb.api_key = "b3b2cba3f60060d27295ae00e67c7f6e"

search = Search()

results = search.movies({"query": "Matrix", "year": 1999})

for result in results:
    print(result.title)
    print(result.overview)


import requests

url = "https://online-movie-database.p.rapidapi.com/auto-complete"

querystring = {"q":"game of thr"}

headers = {
	"X-RapidAPI-Host": "online-movie-database.p.rapidapi.com",
	"X-RapidAPI-Key": "295bfb0596mshd546d882c29ec69p1721c0jsnb9bd36e62935"
}




from django import View,render, messages,redirect,CreateUserForm, Login_Form,authenticate,login

class SignUp_SignUp(View):
    template_name = 'SignIn_SignUp.html'

    def get(self, request, *args, **kwargs):
        context = {  
            'LoginUser':Login_Form,
            'CreateUser':CreateUserForm
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'LoginUser' in request.POST:

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request , username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'USERNAME OR PASSWORD ERROR')

        if 'CreateUser' in request.POST:
 
            form_CreateUser = CreateUserForm(request.POST)

            if form_CreateUser.is_valid():
                form_CreateUser.save()
                return redirect('SignUp-SignIn')
            else:
                messages.error(request, form_CreateUser.errors)