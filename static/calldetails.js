$(document).ready(function () {
    $.getJSON('/api/calldetailslist', function (data) {
        console.log("Data: ",data)
      var htm = `<table class="table table-striped table-hover">
      <thead style="text-align-last: center;">
        <tr style="background-color: black;
        color: aliceblue;">
          <th scope="col">Customer Id</th>
          <th scope="col">Customer Name</th>
          <th scope="col">Caller Id</th>
          <th scope="col">Caller Status</th>
          <th scope="col">Caller Name</th>
          <th scope="col">Current Date</th>
          <th scope="col">Phone Status</th>
          <th scope="col">Conversation</th>
          <th scope="col">Lead Status</th>
          <th scope="col">Mobile No.</th>
          <th scope="col">Update/Delete</th>
        </tr>
      </thead>
      <tbody>`
  
      data.map((item) => {
        htm += `<tr>
  <th th scope = "row" > ${item.customerid}</th> 
  <td>${item.customername}</td>       
  <td>${item.callerid}</td>    
  <td>${item.status}</td>    
  <td>${item.callername}</td> 
  <td>${item.currentdate}</td>       
  <td>${item.phonestatus}</td>       
  <td>${item.conversation}</td>       
  <td>${item.leadstatus}</td>    
  <td>${item.mobileno}</td>       
  <td>
      <a href='#'>
        <button style="-webkit-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);
          -moz-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); " type="button" class="btn btn-primary buttonstyle">
          <b>Update/Delete</b>
        </button>
      </a>
  </td>            
  `
})
  
      htm += `</tbody ></table > `
      $('#CustomerCallDetails').html(htm)
  
    })
  })
  
  