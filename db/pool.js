const mysql= require('mysql')
const config = require('./db-config.json')

const pool = mysql.createPool({
  connectionLimit: 10,
  multipleStatements: true,
  ...config
})


module.exports = pool
 