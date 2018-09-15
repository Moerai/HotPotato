
const express = require("express");
const app = express();

app.get('/', function(request, response){
  let now = Date.now();
  response.send('<h1>Hello World'+now+'</h1>');

});
app.get('/page1',(req,res)=>{
  res.send('<p>page1</p>');
});
app.listen(89,function(){
  console.log("OK!!!");
});
app.get('/user',(req,res)=>{
  var user = {
    "name":"PARKSUNGSOO",
    "age":20,
    "id":"friendnt"
  }
});
