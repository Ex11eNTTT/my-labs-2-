function fillRecipes(){
    fetch ('/rgz/rest-api/rgz_gavrilov/')
    .then(function(data){
        return data.json()
    })
    .then(function(recipes){
        let tbody = document.getElementById('recipes');
        tbody.innerHTML = '';
        for(let i=0; i<recipes.length; i++){
            let tr = document.createElement('tr');
            let tr_photo = document.createElement('tr');
            let tr_bt1 = document.createElement('tr');
            let bt_look = document.createElement('button');
            let photo_td = document.createElement('td');
            let name = document.createElement('td');
            let photo = document.createElement('img');

            let bt_redact = document.createElement('button');
            bt_redact.innerText = 'Редактировать';
            bt_redact.onclick = function(){
                redact_recipe(recipes[i].id)
            };


            bt_look.innerText = 'Приготовить!';
            bt_look.onclick = function() {
                look_recipes(recipes[i].id);
            };

            name.innerText = recipes[i].name;
            photo.src = recipes[i].photo
            photo.style.width = '300px'
            tr.append(name)
            photo_td.appendChild(photo);
            tr_photo.appendChild(photo_td)
            tr_bt1.appendChild(bt_look)
            tr_bt1.appendChild(bt_redact)
            tbody.append(tr)
            tbody.append(tr_photo)
            tbody.append(tr_bt1)
        }

    })
}


function showModal(){
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal(){
    document.querySelector('div.modal').style.display = 'none';
}

function showModal2(){
    document.querySelector('div.modal2').style.display = 'block';
}

function hideModal2(){
    document.querySelector('div.modal2').style.display = 'none';
}

function showModal3(){
    document.querySelector('div.modal3').style.display = 'block';
}

function hideModal3(){
    document.querySelector('div.modal3').style.display = 'none';
}

function showModal4(){
    document.querySelector('div.modal4').style.display = 'block';
}

function hideModal4(){
    const ingredientList = document.getElementById('ingredientList');
    ingredientList.innerHTML = '';
    document.querySelector('div.modal4').style.display = 'none';
}

function showModal5(){
    document.querySelector('div.modal5').style.display = 'block';
}

function hideModal5(){
    const ingredientList = document.getElementById('ingredientList');
    ingredientList.innerHTML = '';
    document.querySelector('div.modal5').style.display = 'none';
}






function look_recipes(id){
    fetch(`/rgz/rest-api/rgz_gavrilov/not/${id}`)
    .then(function(data){
        return data.json();
    })
    .then(function(recipes){
        document.getElementById('name_modal').innerHTML = recipes.name
        document.getElementById('photo_modal').src = recipes.photo
        document.getElementById('photo_modal').style.width = '150px'
        document.getElementById('ingredients_modal').innerHTML = recipes.ingredients
        document.getElementById('steps_modal').innerHTML = recipes.steps
        showModal();
    })
}

function redact_recipe(id){
    fetch(`/rgz/rest-api/rgz_gavrilov/${id}`)
    .then(function(data){
        if(data.ok){
            return data.json();
        }
        if(data.status === 401){
            return(alert('Вы не авторизованы!'))
        }
    })
    .then(function(recipes){
        document.getElementById('id_modal2').value = recipes.id
        document.getElementById('name_modal2').value = recipes.name
        document.getElementById('photo_modal2').value = recipes.photo
        document.getElementById('ingredients_modal2').value = recipes.ingredients
        document.getElementById('steps_modal2').value = recipes.steps
        showModal2();
    })
}




function redact(){
    const recipe={
        id: document.getElementById('id_modal2').value,
        name: document.getElementById('name_modal2').value,
        photo: document.getElementById('photo_modal2').value,
        ingredients: document.getElementById('ingredients_modal2').value,
        steps: document.getElementById('steps_modal2').value,
    }
    fetch('/rgz/rest-api/rgz_gavrilov/',{
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(recipe)
    })
    .then(function(resp){
        if(resp.ok){
            fillRecipes();
            hideModal2();
            return {};
        }})
}


function delete_recipe(){
    const id = document.getElementById('id_modal2').value
    fetch(`/rgz/rest-api/rgz_gavrilov/${id}`,{method: 'DELETE'})
    .then(function(resp){
        if(resp.ok){
            fillRecipes();
            hideModal2();
            return {};
        }})
}

function search_name(){
    showModal3()
}


function search_name2(){
    const name = document.getElementById('search_name').value
    fetch(`/rgz/rest-api/rgz_gavrilov/search/${name}`)
    .then(function(resp){
        if(resp.ok){
            fillRecipes_search_name(resp);
            hideModal3();
        }
        if(resp.status === 400){
            return(alert('По вашему запросу ничего не найдено'))
        }})
}



function fillRecipes_search_name(resp) {
resp.json().then(function(resp) {
    let tbody = document.getElementById('recipes');
    tbody.innerHTML = '';
    for (let i = 0; i < resp.length; i++) {
        let tr = document.createElement('tr');
        let tr_photo = document.createElement('tr');
        let tr_bt1 = document.createElement('tr');
        let bt_look = document.createElement('button');
        let photo_td = document.createElement('td');
        let name = document.createElement('td');
        let photo = document.createElement('img');

        let bt_redact = document.createElement('button');
        bt_redact.innerText = 'Редактировать';
        bt_redact.onclick = function() {
            redact_recipe(resp[i].id);
        };

        bt_look.innerText = 'Приготовить!';
        bt_look.onclick = function() {
            look_recipes(resp[i].id);
        };

        name.innerText = resp[i].name;
        photo.src = resp[i].photo;
        photo.style.width = '300px';
        tr.append(name);
        photo_td.appendChild(photo);
        tr_photo.appendChild(photo_td);
        tr_bt1.appendChild(bt_look);
        tr_bt1.appendChild(bt_redact);
        tbody.append(tr);
        tbody.append(tr_photo);
        tbody.append(tr_bt1);
    }
    let bt_reset = document.createElement('button');
    bt_reset.innerText='Сбросить';
    bt_reset.onclick = function(){
        fillRecipes()
    }
    tbody.appendChild(bt_reset)
});
}
function add_ingredient(){
        const input = document.createElement('input');
        input.type = 'text';
        document.getElementById('ingredientList').appendChild(input);
    }

function search_or() {
    const ingredients = Array.from(document.querySelectorAll('#ingredientList input')).map(input => input.value);
    fetch('/rgz/rest-api/rgz_gavrilov/search/or', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredients })
    })
    .then(function(resp){
        if(resp.ok){
            fillRecipes_search_name(resp);
            hideModal4();
        }
        if(resp.status === 400){
            return(alert("По вашему запросу ничего не найдено"))
        }})
}

function search_and() {
    const ingredients = Array.from(document.querySelectorAll('#ingredientList input')).map(input => input.value);
    fetch('/rgz/rest-api/rgz_gavrilov/search/and', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredients })
    })
    .then(function(resp){
        if(resp.ok){
            fillRecipes_search_name(resp);
            hideModal4();
        }
        if(resp.status === 400){
            return alert('По вашему запросу ничего не найдено!');
        }
        if(resp.status === 500){
            return alert('По вашему запросу ничего не найдено!');
        }})
}


function add_recipe(){
    const recipe={
        name: document.getElementById('name_modal5').value,
        photo: document.getElementById('photo_modal5').value,
        ingredients: document.getElementById('ingredients_modal5').value,
        steps: document.getElementById('steps_modal5').value,
    }
    fetch('/rgz/rest-api/rgz_gavrilov/add',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(recipe)
    })
    .then(function(resp){
        if(resp.ok){
            fillRecipes(resp);
            hideModal5();
        }
})
}