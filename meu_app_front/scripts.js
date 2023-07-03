/*
  --------------------------------------------------------------------------------------
  Função para obter a lista de carros existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/carros';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.cars.forEach(item => insertList(item.Brand, item.Model, item.Fuel, item.Year_manufacture, item.Year_model, item.Color, item.Value))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para obter a lista de carros existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getListBrands = async () => {
  let url = 'http://127.0.0.1:5000/marcas';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.brands.forEach(item => insertListBrands(item.Id, item.Name))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()
getListBrands()

/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

const insertButtonUpdate = (parent) => {
  let update = document.createElement("update");
  let txtupdte = document.createTextNode("\u00D7");
  update.className = "update";
  update.appendChild(txtupdte);
  parent.appendChild(update);
}

/*
  --------------------------------------------------------------------------------------
  Função para inserir carros na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (Brand, Model, Fuel, Year_manufacture, Year_model, Color, Value) => {
  var item = [Brand, Model, Fuel, Year_manufacture, Year_model, Color, Value]
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  insertButtonUpdate(row.insertCell(-1))
  document.getElementById("newBrand").value = "";
  document.getElementById("newModel").value = "";
  document.getElementById("newFuel").value = "";
  document.getElementById("newYearManufacture").value = "";
  document.getElementById("newYearModel").value = "";
  document.getElementById("newColor").value = "";
  document.getElementById("newValue").value = "";

}

/*
  --------------------------------------------------------------------------------------
  Função para inserir carros na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertListBrands = (Id, Name) => {
  var item = [Name]
  var options = '';

  options += '<option value=Vw />';
  options += '<option value=Fiat />';
  options += '<option value=Volvo />';

  // Adicionar a lista após popular toda a string options
  document.getElementById('newBrand').innerHTML = options;

}