$(document).ready(function () {
    $.getJSON('/api/customerlist', function (data) {
      var htm = `<table class="table table-striped table-hover">
      <thead style="text-align-last: center;">
        <tr style="background-color: black;
        color: aliceblue;">
          <th scope="col">Sno.</th>
          <th scope="col">Name</th>
          <th scope="col">Birth</th>
          <th scope="col">Contact Details</th>
          <th scope="col">Address</th>
          <th scope="col">Organization</th>
          <th scope="col">Picture</th>
          <th scope="col">Make Call</th>
          <th scope="col">Follow Up</th>
          <th scope="col">Update</th>
        </tr>
      </thead>
      <tbody>`
  
      data.map((item) => {
        htm += `<tr>
  <th th scope = "row" > ${item.id}</th> 
  <td>${item.firstname} ${item.lastname}</td>       
  <td>${item.gender} <br>${item.dob}</td>       
  <td>${item.emailid} <br>${item.mobileno1}<br>${item.mobileno2}</td>       
  <td>${item.address} <br>${item.cityname}<br>${item.statename}</td>
  <td>${item.organization}</td>              
  <td>
      <a href='/api/display_customer_picture?customerid=${item.id}&customername=${item.firstname} ${item.lastname}&picture=${item.photograph}'><img src="/${item.photograph}" width="30"></a>
  </ td>
  <td>
      <a href="tel:${item.mobileno}">
        <button style="-webkit-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); -moz-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);  box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);" type="button" class="btn btn-primary buttonstyle">
        <span class="material-symbols-outlined"> call</span>
        </button>
      </a>
  </td>
  <td>
      <a href="/api/callcustomerbyid?customerid=${item.id}">
        <button style="-webkit-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); -moz-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);  box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);" type="button" class="btn btn-primary buttonstyle">
        <b>Fill Details</b>
        </button>
      </a>
  </td>
  <td>
      <a href='/api/customerbyid?customerid=${item.id}'>
        <button style="-webkit-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); -moz-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); " type="button" class="btn btn-primary buttonstyle"><b>Update/Delete</b>
        </button>
      </a>
  </td>`
})
  
      htm += `</tbody ></table > `
      $('#CustomerData').html(htm)
  
    })
  })
  
  