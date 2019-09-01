const { _: [sqlFileName], e = "local", env = e } = require("simple-argv")

console.log(`Eseguo ${sqlFileName}.sql in ambiente ${env}`)

const mysql = require("mysql")
const config = require(`./db-config.json`)
const { readFileSync } = require("fs")
const { join } = require("path")

const sql = readFileSync(join(__dirname, `${sqlFileName}`), "utf8")

const pool = mysql.createPool({
  connectionLimit: 10,
  multipleStatements: true,
  ...config
})
const insert ='INSERT INTO user VALUES (default,"andrea","breaglia");'
const select = "SELECT * FROM user"

pool.query(sql,(err, data) => {
  if (err) {
    console.log(err)
  } else {
    console.log(data)
  }
})