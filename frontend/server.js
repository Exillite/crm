const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const port = 3000;
const baseDirectory = __dirname; // Директория сервера

const mimeTypes = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.css': 'text/css',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.ttf': 'font/ttf'
};

http.createServer((request, response) => {
  try {
    let requestUrl = url.parse(request.url);


    // let fsPath = baseDirectory + (requestUrl.pathname === '/' ? '/pages/index.html' : requestUrl.pathname);
    let fsPath = baseDirectory;

    switch (requestUrl.pathname) {
        case '/':
            fsPath += '/pages/index.html';
            break;
        case '/login':
            fsPath += '/pages/login.html';
            break;
        case '/reg':
            fsPath += '/pages/reg.html';
            break;
        case '/crm':
            fsPath += '/pages/crm.html';
            break;
        default:
            fsPath += requestUrl.pathname;
            break;
    }

    console.log(fsPath);

    let ext = path.extname(fsPath);

    fs.readFile(fsPath, (error, data) => {
      if (error) {
        response.writeHead(404, { 'Content-Type': 'text/plain' });
        response.write('404 Not Found\n');
        response.end();
        return;
      }

      response.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
      response.write(data);
      response.end();
    });
  } catch (e) {
    response.writeHead(500, { 'Content-Type': 'text/plain' });
    response.write('500 Internal Server Error\n');
    response.end();
  }
}).listen(port);

console.log(`Server running at http://localhost:${port}/`);
