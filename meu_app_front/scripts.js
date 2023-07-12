// Url variable
const url_brands = "http://127.0.0.1:5000/brands"
const url_models = "http://127.0.0.1:5000/models"
const url_fuels = "http://127.0.0.1:5000/fuels"
const url_cars = 'http://127.0.0.1:5000/cars'
const url_car = 'http://127.0.0.1:5000/car';

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


function onchangeModel() {
    labelModelId.textContent = models.value
}

const onclickBrands = async () => {
    // Removes all options from the list.
    while (models.options.length > 0) {
        models.remove(0);
    }

    labelBrandId.textContent = brands.value;
    await displayOptionModels();
}

function onclickFuels() {
    labelFuellId.textContent = fuels.value
}

brands.onclick = onclickBrands;
models.onchange = onchangeModel;
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
    let response = await fetch(url_cars);

    if (response.status !== 200) {
        console.warn('Verifique a url de carros, ela retornou o código: ',
            response.status);
        return [];
    }
    let data = await response.json();
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
    let options = await dados["Models"].filter(dados => dados.Brand === brands.options[brands.selectedIndex].text);

    // First record is always the field name and title, by default
    const newOption = document.createElement("option");
    newOption.text = "Modelo";
    models.appendChild(newOption);

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
    };
};

// Function that populates year manufacturing and year model
const displayOptionYears = async () => {

    const options = [
        2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
        2020, 2021, 2022, 2023
    ];

    for (let option of options) {
        // Year manufacturing
        const newOption = document.createElement("option");
        newOption.text = option;
        dtYearManufacture.appendChild(newOption);

        // Year model
        const newOption1 = document.createElement("option");
        newOption1.text = option;
        dtYearModel.appendChild(newOption1);
    };
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
    };
};

// Function that populates select cars
const displayOptionCars = async () => {
    let table = document.getElementById('tabCars');

    // Calls the function that gets the data from the cars
    const options = await getPostCars();
    const item = options["cars"];

    for (let index = 0; index < item.length; index++) {
        let newRow = table.insertRow(1);

        let cellBrand = newRow.insertCell();
        let cellModel = newRow.insertCell();
        let cellFuel = newRow.insertCell();
        let cellYear_manufacture = newRow.insertCell();
        let cellYear_model = newRow.insertCell();
        let cellColor = newRow.insertCell();
        let cellValue = newRow.insertCell();
        let cellIdCar = newRow.insertCell();
        insertButtonDelete(newRow.insertCell())
        insertButtonUpdate(newRow.insertCell())

        cellBrand.innerHTML = item[index].Brand;
        cellModel.innerHTML = item[index].Model;
        cellFuel.innerHTML = item[index].Fuel;
        cellYear_manufacture.innerHTML = item[index].Year_manufacture;
        cellYear_model.innerHTML = item[index].Year_model;
        cellColor.innerHTML = item[index].Color;
        cellValue.innerHTML = item[index].Value;
        cellIdCar.innerHTML = item[index].Id;
    }
    deleteCar();
    BuscaCar();
};

//  Function to create a close button for each list item
const insertButtonDelete = (parent) => {
    let btnDelete = document.createElement("delete");
    let txtDelete = document.createTextNode("\u00D7");
    btnDelete.className = "delete";
    btnDelete.appendChild(txtDelete);
    parent.appendChild(btnDelete);
};

// Function to create a update button for each list item
const insertButtonUpdate = (parent) => {
    let btnUpdate = document.createElement("update");
    let txtUpdte = document.createTextNode("\u03BD");
    btnUpdate.className = "update";
    btnUpdate.appendChild(txtUpdte);
    parent.appendChild(btnUpdate);
};

// Click button
const btnClickAdicionar = async () => {
    let selYearManufacture = document.getElementById("selectYearManufacture").value;
    let selYearModel = document.getElementById("selectYearModel").value;
    let selColor = document.getElementById("selectColor").value;
    let selValue = document.getElementById("inpValue").value;

    if (isNaN(labelBrandId.textContent)) {
        alert("Selecione uma marca na lista!");
    } else if (isNaN(labelModelId.textContent)) {
        alert("Selecione um modelo na lista!");
    } else if (isNaN(labelFuellId.textContent)) {
        alert("Selecione o tipo de combustivel na lista!");
    } else if (isNaN(selYearManufacture)) {
        alert("Selecione o ano de fabricação na lista!");
    } else if (isNaN(selYearModel)) {
        alert("Selecione o ano do modelo na lista!");
    } else if (selColor == "Cor") {
        alert("Selecione a cor na lista!");
    } else if (isNaN(selValue)) {
        alert("Valor informado não e valido!");
    } else {
        if (Number(labelIdCar.textContent) === 0) {
            await postCar(0, selColor, labelFuellId.textContent, labelModelId.textContent, selValue, selYearManufacture, selYearModel, labelBrandId.textContent)
            window.location.reload(true);
            alert("Item adicionado com sucesso!")
        } else {
            if (confirm("Deseja realmente alterar o carro?")) {
                await postCar(labelIdCar.textContent, selColor, labelFuellId.textContent, labelModelId.textContent, selValue, selYearManufacture, selYearModel, labelBrandId.textContent)
                window.location.reload(true);
                alert("Item alterado com sucesso!")
            };
            window.location.reload(true);
        };
    }
}

// post car
async function postCar(inputIdCar, inputColor, inputFuel, inputModel, inputValue, inputYearManufacture, inputYearModel, inputBrand) {
    const formData = new FormData();
    formData.append('color', inputColor);
    formData.append('year_manufacture', inputYearManufacture);
    formData.append('year_model', inputYearModel);
    formData.append('value', inputValue);
    formData.append('model', inputModel);
    formData.append('fuel', inputFuel);
    formData.append('brand', inputBrand);

    if (Number(inputIdCar) === 0) {
        fetch(url_car, {
            method: 'post',
            body: formData
        });
    } else {
        fetch("http://127.0.0.1:5000/update_car?id=" + inputIdCar, {
            method: 'post',
            body: formData
        });
    };
};

// Function to remove a car from the list according to the click on the btnDelete button
const deleteCar = () => {
    let close = document.getElementsByClassName("delete");

    let i;
    for (i = 0; i < close.length; i++) {
        close[i].onclick = function () {
            let div = this.parentElement.parentElement;
            const nomeItem = div.getElementsByTagName('td')[7].innerHTML
            if (confirm("Você tem certeza?")) {
                div.remove()
                deleteItem(nomeItem)
                alert("Carro removido!")
            };
        };
    };
};


// Function to delete an car from the server list via DELETE request
const deleteItem = (item) => {
    fetch(url_car + '?id=' + item, {
        method: 'delete'
    });
};

// Function to update a car in the list according to the click on the btnUpdate button
const BuscaCar = async () => {
    let labelIdCar = document.getElementById("labelIdCar");
    let update = document.getElementsByClassName("update");

    let i;
    for (i = 0; i < update.length; i++) {
        update[i].onclick = async function () {
            let div = this.parentElement.parentElement;
            const idCarro = div.getElementsByTagName('td')[7].innerHTML

            labelIdCar.textContent = idCarro

            // Select the model from the list
            selectdUpdateBrand(div);

            await onclickBrands();

            // Select the model from the list
            selectdUpdateModel(div);

            // Select the fuels from the list
            selectUpdateFuel(div);

            // Select the year manufacture from the list
            selectdUpdateYearManufacture(div);

            // Select the year model from the list
            selectdUpdateYearModel(div);

            // Select the color from the list
            selectdUpdateColor(div);

            // Select the value from the input
            document.getElementById("inpValue").value = div.getElementsByTagName('td')[6].innerHTML

        };
    };
};

const selectdUpdateBrand = (objeto) => {
    // Select the brand
    let select = document.querySelector('#selectBrands');
    for (let iLine = 0; iLine < select.options.length; iLine++) {
        if (select.options[iLine].text === objeto.getElementsByTagName('td')[0].innerHTML) {
            select.selectedIndex = iLine;
            break;
        };
    };
};

const selectdUpdateModel = (objeto) => {
    // Select the models
    for (let iLine = 0; iLine < models.options.length; iLine++) {
        if (models.options[iLine].text === objeto.getElementsByTagName('td')[1].innerHTML) {
            models.options.selectedIndex = iLine;
            break;
        };
    };
    onchangeModel();
};

const selectUpdateFuel = (objeto) => {
    // Select the fuels
    let select = document.querySelector('#selectFuels');
    for (let iLine = 0; iLine < select.options.length; iLine++) {
        if (select.options[iLine].text === objeto.getElementsByTagName('td')[2].innerHTML) {
            select.selectedIndex = iLine;
            break;
        };
    };
    onclickFuels();
};

const selectdUpdateYearManufacture = (objeto) => {
    // Select the year manufacture
    let select = document.querySelector('#selectYearManufacture');
    for (let iLine = 0; iLine < select.options.length; iLine++) {
        if (select.options[iLine].text === objeto.getElementsByTagName('td')[3].innerHTML) {
            select.selectedIndex = iLine;
            break;
        };
    };
};

const selectdUpdateYearModel = (objeto) => {
    // Select the year model
    let select = document.querySelector('#selectYearModel');
    for (let iLine = 0; iLine < select.options.length; iLine++) {
        if (select.options[iLine].text === objeto.getElementsByTagName('td')[4].innerHTML) {
            select.selectedIndex = iLine;
            break;
        };
    };
};

const selectdUpdateColor = (objeto) => {
    // Select the color
    let select = document.querySelector('#selectColor');
    for (let iLine = 0; iLine < select.options.length; iLine++) {
        if (select.options[iLine].text === objeto.getElementsByTagName('td')[5].innerHTML) {
            select.selectedIndex = iLine;
            break;
        };
    };
};


// Calls the function to fill in the initial data
displayOptionBrands();
displayOptionFuels();
displayOptionYears();
displayOptionColor();
displayOptionCars();