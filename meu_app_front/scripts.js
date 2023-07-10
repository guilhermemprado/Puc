// Url variable
const url_brands = "http://127.0.0.1:5000/brands"
const url_models = "http://127.0.0.1:5000/models"
const url_fuels = "http://127.0.0.1:5000/fuels"
const url_cars = 'http://127.0.0.1:5000/cars'

// Turn on batchTrack in select
const brands = document.getElementById("selectBrands");
const labelBrandId = document.getElementById("labelBrandId");
const models = document.getElementById("selectModels");
const labelModelId = document.getElementById("labelModelId");
const fuels = document.getElementById("selectFuels");
const labelFuellId = document.getElementById("labelFuellId");
const dtYearManufacture = document.getElementById("selectYearManufacture");
const dtYearModel = document.getElementById("selectYearModel");
const color = document.getElementById("selectColor");

// Sets the size of created elements
document.getElementById("selectBrands").style.width = "12%";
document.getElementById("selectModels").style.width = "23.5%";
document.getElementById("selectFuels").style.width = "12%";
document.getElementById("selectYearManufacture").style.width = "12%";
document.getElementById("selectYearModel").style.width = "10%";
document.getElementById("selectColor").style.width = "10%";


function onchange() {
    labelModelId.textContent = models.value
}

function onclickBrands() {
    // Removes all options from the list.
    while (models.options.length > 0) {
        models.remove(0);
    }

    labelBrandId.textContent = brands.value;
    displayOptionModels();
}

function onclickFuels() {
    labelFuellId.textContent = fuels.value
}

brands.onclick = onclickBrands
models.onchange = onchange;
fuels.onclick = onclickFuels;

function removeAll(selectBox) {
    while (selectBox.options.length > 0) {
        select.remove(0);
    }
}

// Function that gets the brands data
const getPostBrands = async () => {
    const response = await fetch(url_brands);

    if (response.status !== 200) {
        console.warn('Verifique a url de brands, ela retornou o código: ',
            response.status);
        return [];
    }
    const data = await response.json();
    return data;
};

// Function that gets the models data
const getPostModels = async () => {
    const response = await fetch(url_models);

    if (response.status !== 200) {
        console.warn('Verifique a url de models, ela retornou o código: ',
            response.status);
        return [];
    }
    const data = await response.json();
    return data;
};

// Function that gets the fuels data
const getPostFuels = async () => {
    const response = await fetch(url_fuels);

    if (response.status !== 200) {
        console.warn('Verifique a url de combustível, ela retornou o código: ',
            response.status);
        return [];
    }
    const data = await response.json();
    return data;
};

// Function that gets the fuels data
const getPostCars = async () => {
    const response = await fetch(url_cars);

    if (response.status !== 200) {
        console.warn('Verifique a url de carros, ela retornou o código: ',
            response.status);
        return [];
    }
    const data = await response.json();
    return data;
};

// Function that populates select brands
const displayOptionBrands = async () => {
    // Calls the function that gets the data from the brands
    const options = await getPostBrands();

    // Load the select with the brands data
    for (let option of options["brands"]) {
        const newOption = document.createElement("option");
        newOption.text = "Selecione um item";
        newOption.value = option.Id;
        newOption.text = option.Name;
        brands.appendChild(newOption);
    }
};

// Function that populates select models
const displayOptionModels = async () => {
    // Calls the function that gets the data from the models
    let dados = await getPostModels();
    let options = dados["Models"].filter(dados => dados.Brand === brands.options[brands.selectedIndex].text);

    // If you have any records
    if (options.length == 0) {
        const newOption = document.createElement("option");
        newOption.text = "Modelo";
        models.appendChild(newOption);
    }

    // Load the select with the models data
    for (let option of options) {
        const newOption = document.createElement("option");
        newOption.value = option.Id;
        newOption.text = option.Name;
        models.appendChild(newOption);
    }

};

// Function that populates select fuels
const displayOptionFuels = async () => {
    // Calls the function that gets the data from the fuels
    const options = await getPostFuels();

    // Load the select with the fuels data
    for (let option of options["Fuels"]) {
        const newOption = document.createElement("option");
        newOption.value = option.Id;
        newOption.text = option.Type;
        fuels.appendChild(newOption);
    }
};

// Function that populates year manufacturing and year model
const displayOptionYears = async () => {

    const options = [
        2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
        2020, 2021, 2022, 2023
    ]

    for (let option of options) {
        // Year manufacturing
        const newOption = document.createElement("option");
        newOption.text = option;
        dtYearManufacture.appendChild(newOption);

        // Year model
        const newOption1 = document.createElement("option");
        newOption1.text = option;
        dtYearModel.appendChild(newOption1);
    }
};

// Function that populates year manufacturing and year model
const displayOptionColor = async () => {

    const options = [
        "Azul", "Branco", "Cinza", "Marrom/Bege", "Preto", "Prata", "Verde", "Vermelho"
    ]

    for (let option of options) {
        // Year manufacturing
        const newOption = document.createElement("option");
        newOption.text = option;
        color.appendChild(newOption);
    }
};

// Function that populates select cars
const displayOptionCars = async () => {
    let table = document.getElementById('tabCars');
    
    // Calls the function that gets the data from the cars
    const options = await getPostCars();
    const item = options["cars"]

    for (let i = 0; i < item.length; i++) {
        let row = table.insertRow(1);

        let cellBrand = row.insertCell();
        let cellModel = row.insertCell();
        let cellFuel = row.insertCell();
        let cellYear_manufacture = row.insertCell();
        let cellYear_model = row.insertCell();
        let cellColor = row.insertCell();
        let cellValue = row.insertCell();
        let cellIdCar = row.insertCell();

        cellBrand.innerHTML = item[i].Brand;
        cellModel.innerHTML = item[i].Model;
        cellFuel.innerHTML = item[i].Fuel;
        cellYear_manufacture.innerHTML = item[i].Year_manufacture;
        cellYear_model.innerHTML = item[i].Year_model;
        cellColor.innerHTML = item[i].Color;
        cellValue.innerHTML = item[i].Value;
        cellIdCar.innerHTML = item[i].Id;

        insertButtonUpdate(row.insertCell(-1))
        insertButtonDelete(row.insertCell(-1))
    }
};

//  Função para criar um botão close para cada item da lista
const insertButtonDelete = (parent) => {
    let span = document.createElement("span");
    let txtDelete = document.createTextNode("\u00D7");
    span.className = "delete";
    span.appendChild(txtDelete);
    parent.appendChild(span);
  }
  
const insertButtonUpdate = (parent) => {
    let update = document.createElement("update");
    let txtUpdte = document.createTextNode("\u00D7");
    update.className = "update";
    update.appendChild(txtUpdte);
    parent.appendChild(update);
  }

// Calls the function to fill in the initial data
displayOptionBrands();
displayOptionFuels();
displayOptionYears();
displayOptionColor();
displayOptionCars();