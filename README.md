[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6445706&assignment_repo_type=AssignmentRepo)
# MAD Assignment Web API (for IT)

### Registration Number: 219001044

## Scenario

A culinary health supervision and rating agency needs a catalog of restaurants to help them know all available restaurants in Rwanda.
restaurants should have a name, the name of the owner(owner can be individual or a company), rating(number of stars), address or location 
(to simplify this you can just use districts and sectors only), list of dishes offered by the restaurant. 
Each dish should have a name, cooking time, a list of ingredients, price of the dish and different pictures of the dish.

## instructions
1. Create a web api reflecting the above scenario using technologies(programming language....) of your choice.
2. Your Api should provide a way to list restaurants in a specified location (district or sector), restaurants owned by a given individual or company, restuarants of a given rating etc...Think of all the possible scenarios users or other systems would consume your API and the type of information they would need to access.
3. It should also have features like Authentication and Authorization in  a way that only authorized users can add or modify some areas of the api.
4. Use Postman to document your Web API.
5. Deploy your web API to the platform of your choice (Heroku, Azure, etc...)
6. Submission will be done via this repository but you should also include a link to your postman collection and a link to the hosted webApi along with some default credentials for testing.

#### Note: Don't be limited to the features specified in instructions, feel free to add any other feature you think is necessary.

#### This project is made up three apps, where each app has its own url details, here initial urls that links to the urls in apps form more details:

1. https://restosupervisionapi.azurewebsites.net/,,, links to Locations app [for all about: Province, District, and Sector]
2. https://restosupervisionapi.azurewebsites.net/catalog/,,, links to restaur app [for all about: Owners and Restaurants]
3. https://restosupervisionapi.azurewebsites.net/kitchen/,,, links to dishes app [for all about: Cuisines, Dishes, Ingredients, and DishImages]

#### Super_User: username: Admin --> Password: 123

1. POST,LIST,RETRIEVE,PUT... For All ModelViewSets Of System
2. All Permissions on System Is Assigned on Him through custom permission [IsAdminOrReadOnly]

#### Staff_User: username: Kitchen-Manager --> Password: restoapi
#### Staff_User: username: Catalog-Manager --> Password: restoapi

1. POST,LIST,RETRIEVE,PUT... For All ModelViewSets Of System excepts [Province, District & Sector], through custom permission [IsManagersOrReadOnly]
2. These users are able to perform, [LIST, RETRIEVE] data on all ModelViewSet of System
3. InAddition, they are some special permissions applied on [Owner] serializer, where only user is capable to access only the owner that has been created by him/her

#### Link to Postman Collection : https://www.getpostman.com/collections/56338ac799412929a154
#### Link to the Hosted Web API : http://restosupervisionapi.azurewebsites.net
