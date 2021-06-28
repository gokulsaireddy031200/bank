 


function searchTable(){  
	var key =document.vinform.name.value;  
	
  key=key.toUpperCase()
  /*var url = 'cache'+'/'+key; */
  var url='cache/'+key
  console.log(url);
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
       
        if (this.readyState == 4 && this.status == 200) {

                myObj = this.response;
               

                
                  console.log(typeof myObj)
                
                  
                document.getElementById("tablelocation").innerHTML = myObj; 
              }
         document.getElementById('tablelocation').innerHTML = this.responseText; 
      
      else{
      	document.getElementById('tablelocation').innerHTML = "No record found";
      }

    };
    
    if(key=="" || key==null){
      
    }
  else{
    xhttp.open('GET', url, true);
    xhttp.send();
  }
  document.getElementById('tablelocation').innerHTML = "Enter valid key to search";

}
  function searchList(){
  // body...
  var choice = document.getElementById("choice").value;
  choice=choice.toUpperCase();
  var url = 'cache'+'/'+choice;
  var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        myObj = JSON.parse(this.responseText);
                var txt = "<table border='1' style='width:75%'>  <tr> <th> ifsc </th><th> bank_id </th><th> branch </th><th> address </th> <th> city </th><th> district </th> <th> state </th> <th> bank_name </th> </tr> " ;


                for (x in myObj) {
                  
                  txt += "<tr> <td>" + myObj[x].ifsc + "</td>";
                  txt += "<td>" + myObj[x].bank_id + "</td>";
                  txt += "<td>" + myObj[x].branch + "</td>";
                  txt += "<td>" + myObj[x].address + "</td>";
                  txt += "<td>" + myObj[x].city + "</td>";
                  txt += "<td>" + myObj[x].district + "</td>";
                  txt += "<td>" + myObj[x].state + "</td>";
                  txt += "<td>" + myObj[x].bank_name + "</td></tr>";
                }
                txt += "</table>"    
                document.getElementById("tablelocation").innerHTML = txt;
      }
      else{
        document.getElementById('tablelocation').innerHTML = "No record found";
      }
    };
    
    if(choice=="" || choice==null){
      
    }
  else{
    xhttp.open('GET', url, true);
    xhttp.send();
}
}


