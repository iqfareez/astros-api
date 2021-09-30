const jsonServer = require('json-server');
const server = jsonServer.create();
const router = jsonServer.router('db.json');
const middlewares = jsonServer.defaults({ readOnly: true });
const port = process.env.PORT || 3000;

server.use(middlewares);
server.use(router);

server.listen(port, function () {
    console.log(`Server started on port ${port}`);
});