
const electron =require("electron");
const app = electron.app;
const url =require("url");
const path =require("path");
//javascript는 var로 변수를 선언하는데 let이라는 변수선언을 쓰는데 이유가 뭘까?

let mainWindow;

app.on('ready',function(){

  mainWindow= new electron.BrowserWindow({
    width:800, height:600
  });

  let loadUrl = url.format(
    {
      "pathname":path.join(  __dirname, "index.html"),
      "protocol":"file:"
    });
  //let loadUrl ="C:\Users\frien\Documents\node-sample\index.html"
  //let loadUrl ="http://www.naver.com";
  mainWindow.loadURL(loadUrl);
});
