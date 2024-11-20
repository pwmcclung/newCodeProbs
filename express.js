const solution = () => {
    var express = require('express');
    var app = express();
    var port = process.env.PORT;
    var host = process.env.HOST;
    var server = app.listen(port, host, () =>{
      console.log(`Server listening on http://${host}:${port}`);
    });
    return server;
  };