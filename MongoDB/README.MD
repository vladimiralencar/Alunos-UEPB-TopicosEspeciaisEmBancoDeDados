# MONGO - COMANDOS BÁSICOS 


# Ativar o mongod
C:\"Program Files"\MongoDB\Server\3.2\bin\mongod --dbpath C:\mongodb\data\db

# importar dados para o mongo
mongoimport --stopOnError --db loja --collection clientes < clientes.json

# comandos para selecionar documentos no mongo
db.clientes.find(); <br />
db.clientes.find({}, {nome:1,_id:0}); <br />
db.clientes.findOne();    # acha um documento qualquer <br />
db.clientes.find({},{nome:1}); <br />
db.clientes.find({},{nome:1, uf:1, _id:0}); <br />
db.getCollection('clientes').find({}) <br />



MongoDB <br />

show dbs; <br />

show collections; <br />

db.v2.find({text: {$exists: ["dor de"]}},{_id:0,,text:1}).count(); <br />

db.v2.find({text: {$exists: ["dor de"]}},{_id:0, text:1}); <br />

<br />

db.v2.find({},{_id:0, text:1}); <br />
db.v2.find({},{_id:0, text:1}).count(); <br />


db.dor.find({place: {$nin: [null] } }, {'place.full_name': 1}); <br />


db.dor.find({created_at: {$exists: ["Tue Feb 09"]}}); <br />

db.dor.find({text: {$exists: ["dor de"]}}); <br /> <br />


db.dor.find({text: {$exists: ["dor de"]}, place: {$nin: [null] } }, {_id:0, 'place.full_name': 1}); <br />

db.dor.find({place: {$nin: [null] } }, {'place.full_name': 1}).count(); <br /> <br />

 db.dor.find({place: {$nin: [null] } }, {'place.full_name': 1}).sort({'place.full_name': 1}) <br />
 db.dor.find({coordinates: {$nin: [null] } }, {'coordinates': 1}) <br />

use <database>; <br />

db.dropDatabase(); <br />

db.zica_collection.drop(); <br /> <br />


# backup bd: <br />
./mongodump --out /data/dumps <br />


C:\"Program Files"\MongoDB\Server\3.2\bin\mongodump --db twitter C:\mongodb\data\dumps <br />

./mongodump --db twitter --collection zicatest2   --out /data/dumps <br />


# restaurar bd: <br />

mongorestore --db twitter path_to_bson_file <br />

para ver o tamanho dos arquivos em kbytes: <br />

ls -ilah * <br />

<br /><br />

mongodump -h localhost -d twitter -c Collection_name -o C:\mongodb\data\dumps <br />
mongodump -h localhost -d twitter -o C:\mongodb\data\dumps <br />
