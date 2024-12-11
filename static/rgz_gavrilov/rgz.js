function fillRecipesList(){
    fetch ('/rgz/rest-api/rgz_gavrilov/')
    .then(function(data){
        return data.json();
    })
    .then(function (recipes){
        let recipes = document.getElementById('recipes');
        tbody.innerHTML = '';
        for(let i=0; i<recipes.length; i++){
            let div = document.createElement('div');
            let span_name = document.createElement('span')
            let span_ingredients = document.createElement('span')
            let span_steps = document.createElement('span')
            let span_photo = document.createElement("img")

            span_name.innerText = recipes[i].name
            span_ingredients.innerText = recipes[i].ingredients
            span_steps.innerText = recipes[i].steps
            span_photo.innerText = recipes[i].photo


            div.append(span_name)
            div.append(span_photo)
            div.append(ingredients)
            div.append(steps)

            recipes.append(div)
        }
   })
}